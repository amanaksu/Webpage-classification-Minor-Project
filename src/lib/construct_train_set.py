from os import system
from database import *
from constants import *
from functions import *
import MySQLdb




def construct_train_set(n):

	database=[]

	for category in categories:
		#try:
		db = MySQLdb.connect("localhost","root","","train" )
		cursor = db.cursor()
		cursor.execute("Select * from train where category='"+category+"' limit 0,"+str(n))
		documents=cursor.fetchall()
		for document in documents:
			text=document[0]+' '+document[2]
			words=seperateWords(text)
			words=convertToLower(words)
			words=removeStopWords(words)
			words=applyStemming(words)
			freq=genFreqDict(words)
			freq=removeAnom(freq)
			freq['_category']=category
			database.append(freq)
		db.close()
		'''except:
			print("Problem in database connectivity")'''
	#prepare database
	print(database)
	make_training_set(database)
	#print("Training set created")
