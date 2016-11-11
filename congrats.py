#!/usr/bin/env python 

import json

print("tweet,followers_count,retweet_count")

for line in open("tweets.json"):
    tweet = json.loads(line)
    if not tweet['user']['verified']:
        continue
    if 'retweeted_status' not in tweet:
        print("https://twitter.com/%s/status/%s,%s,%s" % (
            tweet['user']['screen_name'],
            tweet['id'],
            tweet['user']['followers_count'],
            tweet['retweet_count']
        ))

