#!/usr/bin/env python
# encoding: utf-8

import csv 

if __name__ == '__main__':
	TweetSentiment = []
	# tweetDate = "" 
	with open('TweetSentiment.csv') as tweet:
		tweet = csv.reader(tweet, delimiter=',')
		for rowTweet in tweet:
			#print(rowTweet[0])
			with open('nasdaq.csv',encoding = 'utf-8') as stock:
				stock = csv.reader(stock, delimiter=',')
				for rowStock in stock: 			
					#TweetSentiment.append([prevDate,number,totalPol/number,totalSub/number])
					
					if (rowStock[1] == rowTweet[0]):\
						TweetSentiment.append(rowTweet)
						
					#print(rowStock[1])
					#print(rowTweet[0])
					#print("False")
	with open('TweetSentiment_cleaned.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["created_at","number","polarity","subjectivity"])
		writer.writerows(TweetSentiment)
	#wiki = TextBlob("Python is a high-level, general-purpose programming language.")
	#print(TweetSentiment[3])