#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

import sys
from twitter import *
import re
#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = sys.argv[1], count=100)

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
	text = result["text"]
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
	for url in urls:
		text = text.replace(url,'')
	text= text.replace('\n','')
	print "(%s) %s" % (result["created_at"], text)
