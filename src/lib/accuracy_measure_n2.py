from os import system
from constants import *
from clean import *
from decimal import Decimal

def naive_bayes(freq_list,database):
	#database=pickle.load(open('database.db','rb'))
	
	v=0	
	for category in categories:
		for word in database[category]:
			v+=database[category][word]
	
	pc={}
	for category in categories:
		attributes={}
		n=0
		
		for word in database[category]:
			n+=database[category][word]
			if word not in attributes:
				attributes[word]=database[category][word]
			else:
				attributes[word]+=database[category][word]
			
		
		pc[category]=Decimal(10**1000)
		for word in freq_list:
			if word not in attributes:
				pc[category]=pc[category]*Decimal((1.0/(n+v)))
			else:
				pc[category]=pc[category]*Decimal(((1.0+attributes[word])/(n+v)))
				
	'''for category in categories:
		print('Probability of ',category,' ',pc[category])
	'''
	
	Category='Unable to decide'
	p=0
	for category in categories:
		if p<pc[category]:
			Category=category
			p=pc[category]
	
	return Category





def accuracy_measure_n(n):

	database={}

	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		system("tail -n "+str(n)+" .tmp > .temp")
		a=open(".temp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		database[category]={}
		t={}
		for file  in files:
			try:
				freq=getList("./webpages/"+category+"/"+file)
				for word in freq:
					if word in t:
						t[word]+=freq[word]
					else:
						t[word]=freq[word]
			except:
				print(file,"makes problem")
		for word in t:
			if t[word]>=2*n:
				database[category][word]=t[word]
			
			
		
	
	w={}
	for category in categories:
		w[category]=0
		for word in database[category]:
			w[category]+=database[category][word]
		print('Number of unique words in ',category,'=',len(database[category]))
		#print('words in ',category)
		#print(database[category])
	minval=10000
	mincat=''
	for category in categories:
		if len(database[category])<minval:
			minval=len(database[category])
			mincat=category
	
	print(mincat,'contain minimum number of words and is',minval)
	
	for category in categories:
		i=1
		while len(database[category])>minval:
			x={}
			flag=0
			for word in database[category]:
				if database[category][word]>i:
					x[word]=database[category][word]
				else:
					w[category]-=database[category][word]
					if len(database[category])<=minval:
						flag=1
						break
			database[category]=x
			if flag:
				break
			i+=1
			
			
	for category in categories:
		print('Number of words in',category,'=',len(database[category]))
		print(database[category])
	
			 
	
	
