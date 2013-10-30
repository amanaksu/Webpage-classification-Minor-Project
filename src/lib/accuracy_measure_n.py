from sys import path
from sys import exit
from os import system
from construct_train_set import construct_train_set
from constants import categories
from clean import getList
from random import randint
from decimal import Decimal
def naive_bayes(freq_list,database):
	#database=pickle.load(open('database.db','rb'))
	#print(database)
	#print(type(database))
	
	v=0	
	for category in categories:
		for word in database[category]:
			v+=database[category][word]
	
	pc={}
	for category in categories:
		attributes=database[category]
		n=0
		for word in attributes:
			n+=attributes[word]
		
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
	'''n->number of train documents'''
	x=[]
	y={}
	documents={}
	accuracy={}
	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		a=open(".tmp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		documents[category]=files
		accuracy[category]=0
	
	for i in range(0,10):
		train_set={}
		test_set={}
		for category in categories:
			train_set[category]=[]
			test_set[category]=[]
			for j in range(0,n):
				t=documents[category][randint(0,len(documents[category])-1)]
				#print(type(t))
				if t not in train_set[category]:
					train_set[category].append(t)
			for d in documents[category]:
				if d not in train_set[category]:
					test_set[category].append(d)
		#train the model
		database={}
		for category in categories:
			database[category]={}
			for document in train_set[category]:
				freq=getList('./webpages/'+category+'/'+document)
				for word in freq:
					if word not in database[category]:
						database[category][word]=freq[word]
					else:
						database[category][word]+=freq[word]
		#test model
		for category in categories:
			p=0
			for document in test_set[category]:
				freq=getList('./webpages/'+category+'/'+document)
				p_cat=naive_bayes(freq,database)
				if p_cat==category:
					p+=1
			
			accuracy[category]+=p*100/len(test_set[category])
	
	print(accuracy)
	return accuracy
