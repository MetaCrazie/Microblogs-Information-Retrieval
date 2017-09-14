import json

class Tweet_parser:
        
        def __init__(self):
                print self
        
        def json_parser(self, json_file):
                tweets = []
                for line in open(json_file, 'r'):
                        tweets.append(json.loads(line))
                no_of_tweets = len(tweets)
                for i in range(0, no_of_tweets):                        
                        data = tweets[i]
                        print data['text']
                        print data['id']
                return tweets
                
object = Tweet_parser()
tweet_object = object.json_parser('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/microblogs-crawl-directory/NepalQuake-code-mixed-training-tweets.jsonl')

