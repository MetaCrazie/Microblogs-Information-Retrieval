import json
import codecs, string

class Tweet_preprocess:
        
        def __init__(self):
                print self
        
        def detect_language(self, character):
                maxchar = max(character)
                if u'\u0900' <= maxchar <= u'\u097f':
                        return 'hindi'
                else: 
                        return 'not'
        
        def print_tweet_data(self, tweets):
                no_of_tweets = len(tweets)
                for i in range(0, no_of_tweets):                        
                        data = tweets[i]
                        print data['id']
                        print data['text']
                        
        def filter_tweets(self, tweets):
                filtered_tweets= []
                no_of_tweets = len(tweets)
                for i in range(0, no_of_tweets):                        
                        data = tweets[i]
                        tweet_text = data['text']
                        flag = 0
                        for word in tweet_text:
                                if self.detect_language(word)=='hindi':
                                        #print 'Removing tweet '+ str(i)
                                        flag += 1
                                        break
                        
                        if flag==0:
                                #print 'Appending tweet '+ str(i)
                                filtered_tweets.append(tweets[i])                
                return filtered_tweets
        
        def json_parser(self, json_file):
                tweets = []
                for line in open(json_file, 'r'):
                        tweets.append(json.loads(line))
                no_of_tweets = len(tweets)             
                return tweets
 
                
tweet_object = Tweet_preprocess()
tweet_array = tweet_object.json_parser('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/microblogs-crawl-directory/NepalQuake-code-mixed-training-tweets.jsonl')

#return filtered tweets:
fil=tweet_object.filter_tweets(tweet_array)
#tweet_object.print_tweet_data(fil)

