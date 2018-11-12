#!/usr/bin/env python
# encoding: utf-8

import csv 

if __name__ == '__main__':
	stockPercent = []
	# tweetDate = "" 
	with open('nasdaq.csv',encoding = 'utf-8') as stock:
		stock = csv.reader(stock, delimiter=',')
		first = 0
		prevIndex = 0
		change = 0
		for rowStock in stock: 			
			if (first != 0):
				#print(rowStock[2])
				change = ((float(rowStock[2]) - prevIndex) / float(rowStock[2])) * 100
				stockPercent.append([rowStock[1],change])
			first += 1
			prevIndex = float(rowStock[2])
						
	with open('nasdaq_cleaned.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["Date","Percent Change"])
		writer.writerows(stockPercent)
	#wiki = TextBlob("Python is a high-level, general-purpose programming language.")
	#print(TweetSentiment[3])