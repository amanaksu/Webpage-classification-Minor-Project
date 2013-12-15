from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
import pylab

x=[]
y={}
ym={}


def main():
	data={400: {'rec.sport.hockey': 93.8888888888889, 'sci.crypt': 92.5, 'talk.religion.misc': 56.55555555555555, 'comp.graphics': 72.61111111111111, 'comp.os.ms-windows.misc': 63.555555555555564, 'comp.sys.ibm.pc.hardware': 59.11111111111111, 'sci.space': 92.3888888888889, 'talk.politics.mideast': 94.05555555555556, 'sci.med': 89.22222222222223, 'rec.motorcycles': 87.72222222222223, 'alt.atheism': 75.33333333333333, 'comp.windows.x': 73.77777777777777, 'misc.forsale': 64.66666666666667, 'rec.sport.baseball': 89.33333333333333, 'rec.autos': 80.6111111111111, 'sci.electronics': 75.94444444444444, 'comp.sys.mac.hardware': 69.77777777777777, 'talk.politics.misc': 72.6111111111111, 'talk.politics.guns': 82.83333333333333, 'soc.religion.christian': 95.53322166387493}, 600: {'rec.sport.hockey': 95.5, 'sci.crypt': 93.5, 'talk.religion.misc': 58.583333333333336, 'comp.graphics': 73.41666666666667, 'comp.os.ms-windows.misc': 71.41666666666667, 'comp.sys.ibm.pc.hardware': 68.58333333333333, 'sci.space': 92.5, 'talk.politics.mideast': 93.08333333333333, 'sci.med': 91.25, 'rec.motorcycles': 91.58333333333333, 'alt.atheism': 72.16666666666667, 'comp.windows.x': 78.91666666666667, 'misc.forsale': 68.91666666666667, 'rec.sport.baseball': 92.0, 'rec.autos': 84.75, 'sci.electronics': 79.33333333333333, 'comp.sys.mac.hardware': 73.75, 'talk.politics.misc': 73.33333333333333, 'talk.politics.guns': 82.83333333333333, 'soc.religion.christian': 96.80940386230058}, 700: {'rec.sport.hockey': 95.77777777777779, 'sci.crypt': 94.0, 'talk.religion.misc': 52.333333333333336, 'comp.graphics': 73.77777777777777, 'comp.os.ms-windows.misc': 71.1111111111111, 'comp.sys.ibm.pc.hardware': 68.66666666666667, 'sci.space': 92.44444444444446, 'talk.politics.mideast': 93.55555555555556, 'sci.med': 93.1111111111111, 'rec.motorcycles': 93.1111111111111, 'alt.atheism': 77.0, 'comp.windows.x': 82.22222222222223, 'misc.forsale': 71.0, 'rec.sport.baseball': 92.33333333333333, 'rec.autos': 86.11111111111113, 'sci.electronics': 79.22222222222221, 'comp.sys.mac.hardware': 74.66666666666667, 'talk.politics.misc': 72.8888888888889, 'talk.politics.guns': 85.33333333333333, 'soc.religion.christian': 96.52076318742985}, 100: {'rec.sport.hockey': 89.70370370370371, 'sci.crypt': 86.03703703703702, 'talk.religion.misc': 51.74074074074074, 'comp.graphics': 54.77777777777777, 'comp.os.ms-windows.misc': 43.59259259259259, 'comp.sys.ibm.pc.hardware': 46.03703703703704, 'sci.space': 83.14814814814814, 'talk.politics.mideast': 87.51851851851852, 'sci.med': 77.4074074074074, 'rec.motorcycles': 82.81481481481482, 'alt.atheism': 72.14814814814815, 'comp.windows.x': 59.40740740740741, 'misc.forsale': 46.18518518518518, 'rec.sport.baseball': 80.37037037037037, 'rec.autos': 65.48148148148148, 'sci.electronics': 57.44444444444445, 'comp.sys.mac.hardware': 52.59259259259259, 'talk.politics.misc': 74.37037037037037, 'talk.politics.guns': 70.8888888888889, 'soc.religion.christian': 91.00706057227796}, 200: {'rec.sport.hockey': 91.16666666666667, 'sci.crypt': 92.79166666666667, 'talk.religion.misc': 54.416666666666664, 'comp.graphics': 69.08333333333333, 'comp.os.ms-windows.misc': 52.916666666666664, 'comp.sys.ibm.pc.hardware': 53.291666666666664, 'sci.space': 87.54166666666667, 'talk.politics.mideast': 89.875, 'sci.med': 86.08333333333333, 'rec.motorcycles': 85.91666666666667, 'alt.atheism': 72.41666666666667, 'comp.windows.x': 68.45833333333333, 'misc.forsale': 52.875, 'rec.sport.baseball': 85.75, 'rec.autos': 75.875, 'sci.electronics': 63.958333333333336, 'comp.sys.mac.hardware': 56.875, 'talk.politics.misc': 76.75, 'talk.politics.guns': 77.375, 'soc.religion.christian': 97.11417816813048}, 500: {'rec.sport.hockey': 94.46666666666665, 'sci.crypt': 92.93333333333334, 'talk.religion.misc': 55.4, 'comp.graphics': 73.66666666666667, 'comp.os.ms-windows.misc': 68.2, 'comp.sys.ibm.pc.hardware': 63.0, 'sci.space': 91.0, 'talk.politics.mideast': 93.8, 'sci.med': 91.2, 'rec.motorcycles': 91.33333333333333, 'alt.atheism': 76.06666666666666, 'comp.windows.x': 74.73333333333333, 'misc.forsale': 68.93333333333332, 'rec.sport.baseball': 90.39999999999999, 'rec.autos': 83.46666666666667, 'sci.electronics': 76.26666666666667, 'comp.sys.mac.hardware': 67.53333333333333, 'talk.politics.misc': 72.73333333333333, 'talk.politics.guns': 82.2, 'soc.religion.christian': 97.38430583501007}, 900: {'rec.sport.hockey': 97.66666666666667, 'sci.crypt': 95.0, 'talk.religion.misc': 52.0, 'comp.graphics': 75.33333333333333, 'comp.os.ms-windows.misc': 70.33333333333333, 'comp.sys.ibm.pc.hardware': 74.0, 'sci.space': 92.66666666666667, 'talk.politics.mideast': 91.33333333333333, 'sci.med': 94.33333333333333, 'rec.motorcycles': 93.66666666666667, 'alt.atheism': 71.33333333333333, 'comp.windows.x': 79.33333333333333, 'misc.forsale': 75.0, 'rec.sport.baseball': 92.66666666666667, 'rec.autos': 85.66666666666667, 'sci.electronics': 86.33333333333333, 'comp.sys.mac.hardware': 78.33333333333333, 'talk.politics.misc': 74.33333333333333, 'talk.politics.guns': 82.33333333333333, 'soc.religion.christian': 96.56357388316151}, 300: {'rec.sport.hockey': 92.71428571428572, 'sci.crypt': 92.42857142857144, 'talk.religion.misc': 55.285714285714285, 'comp.graphics': 67.42857142857143, 'comp.os.ms-windows.misc': 58.904761904761905, 'comp.sys.ibm.pc.hardware': 58.857142857142854, 'sci.space': 88.90476190476191, 'talk.politics.mideast': 93.85714285714285, 'sci.med': 88.76190476190476, 'rec.motorcycles': 88.90476190476191, 'alt.atheism': 75.90476190476191, 'comp.windows.x': 74.33333333333333, 'misc.forsale': 59.57142857142858, 'rec.sport.baseball': 88.80952380952381, 'rec.autos': 80.04761904761905, 'sci.electronics': 72.76190476190476, 'comp.sys.mac.hardware': 66.57142857142857, 'talk.politics.misc': 72.71428571428572, 'talk.politics.guns': 81.90476190476191, 'soc.religion.christian': 96.98708751793401}, 800: {'rec.sport.hockey': 97.0, 'sci.crypt': 93.0, 'talk.religion.misc': 55.0, 'comp.graphics': 74.33333333333333, 'comp.os.ms-windows.misc': 72.83333333333333, 'comp.sys.ibm.pc.hardware': 67.83333333333333, 'sci.space': 93.5, 'talk.politics.mideast': 93.0, 'sci.med': 93.66666666666667, 'rec.motorcycles': 93.0, 'alt.atheism': 76.16666666666667, 'comp.windows.x': 86.66666666666667, 'misc.forsale': 73.83333333333333, 'rec.sport.baseball': 90.66666666666667, 'rec.autos': 87.66666666666667, 'sci.electronics': 80.83333333333333, 'comp.sys.mac.hardware': 75.66666666666667, 'talk.politics.misc': 77.33333333333333, 'talk.politics.guns': 82.66666666666667, 'soc.religion.christian': 96.61590524534687}}
	datam={200: {'comp.sys.ibm.pc.hardware': 53.291666666666664, 'sci.electronics': 63.958333333333336, 'comp.os.ms-windows.misc': 52.916666666666664, 'rec.sport.baseball': 85.75, 'rec.motorcycles': 85.91666666666667, 'comp.graphics': 69.08333333333333, 'sci.med': 86.08333333333333, 'alt.atheism': 72.41666666666667, 'sci.space': 87.54166666666667, 'rec.autos': 75.875, 'comp.windows.x': 68.45833333333333, 'talk.politics.mideast': 89.875, 'talk.religion.misc': 54.416666666666664, 'comp.sys.mac.hardware': 56.875, 'rec.sport.hockey': 91.16666666666667, 'talk.politics.guns': 77.375, 'soc.religion.christian': 97.11417816813048, 'sci.crypt': 92.79166666666667, 'talk.politics.misc': 76.75, 'misc.forsale': 52.875}, 300: {'comp.sys.ibm.pc.hardware': 58.857142857142854, 'sci.electronics': 72.76190476190476, 'comp.os.ms-windows.misc': 58.904761904761905, 'rec.sport.baseball': 88.80952380952381, 'rec.motorcycles': 88.90476190476191, 'comp.graphics': 67.42857142857143, 'sci.med': 88.76190476190476, 'alt.atheism': 75.90476190476191, 'sci.space': 88.90476190476191, 'rec.autos': 80.04761904761905, 'comp.windows.x': 74.33333333333333, 'talk.politics.mideast': 93.85714285714285, 'talk.religion.misc': 55.285714285714285, 'comp.sys.mac.hardware': 66.57142857142857, 'rec.sport.hockey': 92.71428571428572, 'talk.politics.guns': 81.90476190476191, 'soc.religion.christian': 96.98708751793401, 'sci.crypt': 92.42857142857144, 'talk.politics.misc': 72.71428571428572, 'misc.forsale': 59.57142857142858}, 400: {'comp.sys.ibm.pc.hardware': 59.11111111111111, 'sci.electronics': 75.94444444444444, 'comp.os.ms-windows.misc': 63.555555555555564, 'rec.sport.baseball': 89.33333333333333, 'rec.motorcycles': 87.72222222222223, 'comp.graphics': 72.61111111111111, 'sci.med': 89.22222222222223, 'alt.atheism': 75.33333333333333, 'sci.space': 92.3888888888889, 'rec.autos': 80.6111111111111, 'comp.windows.x': 73.77777777777777, 'talk.politics.mideast': 94.05555555555556, 'talk.religion.misc': 56.55555555555555, 'comp.sys.mac.hardware': 69.77777777777777, 'rec.sport.hockey': 93.8888888888889, 'talk.politics.guns': 82.83333333333333, 'soc.religion.christian': 95.53322166387493, 'sci.crypt': 92.5, 'talk.politics.misc': 72.6111111111111, 'misc.forsale': 64.66666666666667}, 100: {'comp.sys.ibm.pc.hardware': 46.03703703703704, 'sci.electronics': 57.44444444444445, 'comp.os.ms-windows.misc': 43.59259259259259, 'rec.sport.baseball': 80.37037037037037, 'rec.motorcycles': 82.81481481481482, 'comp.graphics': 54.77777777777777, 'sci.med': 77.4074074074074, 'alt.atheism': 72.14814814814815, 'sci.space': 83.14814814814814, 'rec.autos': 65.48148148148148, 'comp.windows.x': 59.40740740740741, 'talk.politics.mideast': 87.51851851851852, 'talk.religion.misc': 51.74074074074074, 'comp.sys.mac.hardware': 52.59259259259259, 'rec.sport.hockey': 89.70370370370371, 'talk.politics.guns': 70.8888888888889, 'soc.religion.christian': 91.00706057227796, 'sci.crypt': 86.03703703703702, 'talk.politics.misc': 74.37037037037037, 'misc.forsale': 46.18518518518518}, 500: {'comp.sys.ibm.pc.hardware': 63.0, 'sci.electronics': 76.26666666666667, 'comp.os.ms-windows.misc': 68.2, 'rec.sport.baseball': 90.39999999999999, 'rec.motorcycles': 91.33333333333333, 'comp.graphics': 73.66666666666667, 'sci.med': 91.2, 'alt.atheism': 76.06666666666666, 'sci.space': 91.0, 'rec.autos': 83.46666666666667, 'comp.windows.x': 74.73333333333333, 'talk.politics.mideast': 93.8, 'talk.religion.misc': 55.4, 'comp.sys.mac.hardware': 67.53333333333333, 'rec.sport.hockey': 94.46666666666665, 'talk.politics.guns': 82.2, 'soc.religion.christian': 97.38430583501007, 'sci.crypt': 92.93333333333334, 'talk.politics.misc': 72.73333333333333, 'misc.forsale': 68.93333333333332}}
	for category in categories:
		y[category]=[]
		ym[category]=[]
	for n in range(100,600,100):
		print('n=',n)
		x.append(n)
		for category in categories:
			y[category].append(data[n][category])
			ym[category].append(datam[n][category])
		

	total=[]
	totalm=[]
	for n in range(len(x)):
		total.append(0)
		totalm.append(0)
		for category in categories:
			total[n]+=y[category][n]
			totalm[n]+=ym[category][n]
		total[n]=total[n]/float(len(categories))
		totalm[n]=totalm[n]/float(len(categories))
		print('old',total[n],'modified',totalm[n])
		
		
		
		
		
						
	#Plot graph
	#for item in y:
	#	t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Overal performance",linewidth=4,linestyle='-',color='red')
	t=pylab.plot(x,totalm,label="Imroved performance",linewidth=4,linestyle='-',color='blue')
	t=pylab.xlabel('Number of train documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='lower right')
	t=pylab.title('Number of training documents vs accuracy')
	t=pylab.grid()
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
