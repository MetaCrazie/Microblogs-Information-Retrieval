import tweet_preprocess
from tweet_preprocess import Tweet_preprocess

class Tweet_dataset:
        
        def __init__(self):
                print self
                
        def generate_output(self, tweets, tweet_id_need, tweet_id_avail):
                no_of_tweets = len(tweets)
                
                Y= []
                need = 0
                avail = 0
                for i in range(0, no_of_tweets):
                        data = tweets[i]
                        tweet_text = data['text']
                        tweet_id = str(data['id'])
                        
                        if tweet_id in tweet_id_need:
                                Y.append(1)
                                need += 1
                        elif tweet_id in tweet_id_avail:
                                Y.append(2)
                                avail += 1
                        else:
                                Y.append(0)
                #print 'need: '+ str(need)
                #print 'availability: '+str(avail)
                return Y
                
        def read_id(self, file_path):
                array = []
                with open(file_path, "r") as inpfile:

                        for line in inpfile:
                                line = line.strip()
                                array.append(line)
                return array
                

mObj = Tweet_dataset()
pObj = Tweet_preprocess()

#read IDs of need and available tweets
need_tweet_IDs = mObj.read_id('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/development-set-directory/NepalQuake-need-tweetids-development-set.txt')
avail_tweet_IDs = mObj.read_id('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/development-set-directory/NepalQuake-availability-tweetids-development-set.txt')

tweet_array = pObj.json_parser('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/microblogs-crawl-directory/NepalQuake-code-mixed-training-tweets.jsonl')
#return filtered tweets:
tweets=pObj.filter_tweets(tweet_array)

Y = mObj.generate_output(tweets, need_tweet_IDs, avail_tweet_IDs)
#print Y                
