from os import system
from clean import *
from database import *
from constants import *



def construct_train_set(n):

	database=[]



	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		system("head -n "+str(n)+" .tmp > .temp")
		a=open(".temp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		i=1
		for page in files:
			#print(page)
			#print("\rcategory : "+category+" Document number "+str(i)+" Dictionary created\r")
			i+=1
			try:
				pwords=getList("./webpages/"+category+"/"+page)
				pwords['_category']=category
				database.append(pwords)
			except:
				print(page," makes problem")
	#prepare database
	make_training_set(database)
	print("Training set created")	
