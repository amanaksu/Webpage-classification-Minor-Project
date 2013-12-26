from os import system
from construct_train_set import construct_train_set
from constants import categories
from clean import getList
from math import log

def naive_bayes(freq_list,database):
	#database=pickle.load(open('database.db','rb'))
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
		
		pc[category]=0
		
		
		
		for word in freq_list:
			if word not in attributes:
				pc[category]=pc[category]+1.0/(n+v)
			else:
				pc[category]=pc[category]+(1.0+attributes[word]/(n+v))				
	'''for category in categories:
		print('Probability of ',category,' ',pc[category])
	'''
	
	Category='Unable to decide'
	p=-100000
	for category in categories:
		if p<pc[category]:
			Category=category
			p=pc[category]
	
	return Category

def k_fold_accuracy(k):
	t=int(1000/k) #number of documents in a fold
	print('number of documents in a fold=',t)
	dataset={}
	true_predicted={}
	for category in categories:
		system("ls ./dataset/"+category+">.tmp")
		a=open(".tmp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		dataset[category]=files
		true_predicted[category]=0
	for i in range(0,k):
		print('i=',i)
		train_set={}
		test_set={}
		database={}
		for category in categories:
			train_set[category]=list(dataset[category][0:i*t]+dataset[category][(i+1)*t:])
			test_set[category]=list(dataset[category][i*t:(i+1)*t])
			database[category]={}
		#print('train-set\n',train_set)
		#print('test-set\n',test_set)
		for category in categories:
			for file in train_set[category]:
				freq=getList("./dataset/"+category+"/"+file)
				for word in freq:
					if word in database[category]:
						database[category][word]+=freq[word]
					else:
						database[category][word]=freq[word]
		
		
		print('database created')
		for category in categories:
			for file in test_set[category]:
				freq=getList("./dataset/"+category+"/"+file)
				p_cat=naive_bayes(freq,database)
				if p_cat==category:
					true_predicted[category]+=1
			print('k=',k,'i=',i,'category=',category,'true_predicted\n',true_predicted)
	output={}
	for category in categories:
		output[category]=true_predicted[category]*100/1000.0
	return output
		
		
