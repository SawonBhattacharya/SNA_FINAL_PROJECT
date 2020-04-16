#import packages
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

def jamaat_effect():
	result=pd.read_csv('ba_values.csv')
	#print(result)
	result=result.set_index(["Name of State / UT"])
	#ddf=result.diff(axis=1)
	#result.plot()
	result.plot(figsize=(500,100),kind="bar")
	#plt.grid(True)
	plt.ylabel('No of Cases Confirmed',fontsize=20,color='blue')
	plt.xlabel('Name of State / UT',fontsize=20)
	plt.title('COVID-19 Outbreak due to Tablighi Jamaat',fontsize=30,color='red')
	plt.show()
jamaat_effect()