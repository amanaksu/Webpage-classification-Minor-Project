from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from web import *
from functions import *
from naive_bayes import *

def main():
	url=input("Enter url : ")
	obj=HtmlFile(url)
	text=obj.getPureText()
	words=seperateWords(text)
	words=convertToLower(words)
	words=removeStopWords(words)
	words=applyStemming(words)
	freq=genFreqDict(words)
	freq=removeAnom(freq)
	print("Category of webpage is ",naive_bayes(freq))
	
	
if __name__ == "__main__":
	exit(main())
