#!/usr/bin/env python
# encoding: utf-8

import csv 
from textblob import TextBlob
#from numpy import genfromtxt

if __name__ == '__main__':
	TweetSentiment = []
	with open('CNBCnow_tweets.csv', encoding = 'utf-8') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		first = 0
		number = -1
		prevDate = ""
		currentDate = ""
		totalPol = 0
		totalSub = 0
		for row in csv_reader:
			#print(number)
			number+=1
			currentDate = row[1][:10]
			if (currentDate == prevDate or first == 0):
				totalPol += TextBlob(row[2]).sentiment.polarity
				totalSub += TextBlob(row[2]).sentiment.subjectivity
			else:
				TweetSentiment.append([prevDate,number,totalPol/number,totalSub/number])
				number = 0
				totalPol = TextBlob(row[2]).sentiment.polarity
				totalSub = TextBlob(row[2]).sentiment.subjectivity
			prevDate = currentDate
			first += 1
			#TweetSentiment.append([row[1],TextBlob(row[2]).sentiment.polarity,TextBlob(row[2]).sentiment.subjectivity])
			#print(row[1][:10])
			#print(TweetSentiment[number-1])
	with open('TweetSentiment.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["created_at","number","polarity","subjectivity"])
		writer.writerows(TweetSentiment)
	#wiki = TextBlob("Python is a high-level, general-purpose programming language.")
	#print(TweetSentiment[3])