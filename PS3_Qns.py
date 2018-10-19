#!/usr/bin/env python

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt


def Question_1(): 

	fhand = open('CO-OPS__8729108__wl.csv')
	waterlevel=0
	waterlevel_list=[]
	date_time=0
	date_time_list =[]
	highest_waterlevel=0

	for line in fhand:
		delimiter = ','
		lines = (line.strip().split(delimiter))
		#Try to float the string, if can't skip it and append all others into the list to calculate max.
		try:
			waterlevel = float(lines[1])
			waterlevel_list.append(waterlevel)
		except:
			pass
		date_time = lines[0]
		date_time_list.append(date_time)

	#Find maximum water level in the list.
	highest_waterlevel = max(waterlevel_list)

	#Index the list so that corresponding Date Time matches the Max Water level.
	Max_waterlevel_index = waterlevel_list.index(highest_waterlevel)

	Max_waterlevel_date = date_time_list[Max_waterlevel_index]

	print("Result for Question 1: ", highest_waterlevel, Max_waterlevel_date)
	return 
	

def Question_2():

	#Find maximum water level in the Water level column.

	highest_waterlevel = df[" Water Level"].idxmax()

	#Print out corresponding Date time and Water Level for the Maximum water level. *df.loc indexes the dataframe(df).
	print("Result for Question 2: ", 
	df.loc[highest_waterlevel, "Date Time" : " Water Level"])
	return
	
def Question_3():

	#Each row is a difference of 6 minutes, therefore find the difference in water level between each row and create a new column.

	df['waterlevel_diff'] = df[" Water Level"].diff()

	#Find the max water level difference in the new column.

	highest_waterlevel_diff = df['waterlevel_diff'].idxmax()

	#print the indexed paramters associate with the highest_waterlevel_diff 0 = Date Time, 1 = Water Level, 8 = waterlevel_diff

	print("Result for Question 3: ", df.iloc[highest_waterlevel_diff,[0, 1, 8]])
	return

def Question_4():

	#Ploting graph in matplotlib

	Time, WaterLevel = df['Date Time'], df[' Water Level']

	fig = plt.figure()
	plt.plot(Time, WaterLevel)
	plt.xlabel('Time')
	plt.ylabel('WaterLevel')
	plt.title('Water Level Over Time')

	fig.savefig('waterlevel.png')
	print("Plot figure file generated")
	return


#Globally open pandas for each function, except for Question_1 and Question_extracredit.

df = pd.read_csv("/ufrc/zoo6927/share/nsng/problem_3/CO-OPS__8729108__wl.csv")

Question_1()
Question_2()
Question_3()
Question_4()
