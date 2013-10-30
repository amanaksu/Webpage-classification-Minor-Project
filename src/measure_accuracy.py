from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
from k_fold_accuracy import k_fold_accuracy
from accuracy_measure_n import accuracy_measure_n
import pylab
#threadLimiter = threading.BoundedSemaphore(10)
x=[]
y={}
yn={}
'''class myThread (threading.Thread):
	def __init__(self,element,c):
		threading.Thread.__init__(self)
		self.element = element
		self.c=c
	def run(self):
		threadLimiter.acquire()
		try:
			self.yn=k_fold_accuracy(self.element)
			print(self.yn)
			for category in self.c:
				y[category].append(self.yn[category])
	
		finally:
		        threadLimiter.release()


'''
def main():
	for category in categories:
		y[category]=[]
	for n in range(2,10):
		print('n=',n)
		x.append(n)
		yn=accuracy_measure_n(n)
		for category in categories:
			y[category].append(yn[category])
		

	total=[]
	for n in range(len(x)):
		total.append(0)
		for category in categories:
			total[n]+=y[category][n]
		total[n]=total[n]/float(len(categories))
		
		
		
		
		
						
	#Plot graph
	for item in y:
		t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Overal performance",linewidth=4,linestyle='--')
	t=pylab.xlabel('Number of train documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='upper right')
	t=pylab.title('Number of folds k vs accuracy')
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
