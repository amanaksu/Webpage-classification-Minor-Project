import sys
sys.path.insert(0, './lib') #set library location
from web import *
from functions import *


def main():
	address=input("Address:")
	testsite=WebSite(address)
	print("Title : "+testsite.getTitle())
	text=testsite.getPureText()
	words=seperateWords(text)
	words=convertToLower(words) # convert words to lowercase
	words=applyStemming(words)
	words=removeStopWords(words) # remove stop words
	freq=genFreqDict(words)
	print(freq)
	print("Number of uniq words : "+str(len(freq)))
	#print("Pure Text")
	#print(testsite.getPureText())
	

if __name__ == "__main__":
	sys.exit(main())

