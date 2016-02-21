#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------

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
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/docs/api/1/get/trends/%3Awoeid
# 2347563 - SFO
#-----------------------------------------------------------------------
results = twitter.trends.place(_id = 23424977)

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

def nytimesFormat (trend):
	formattedTrend=trend
	if trend.strip()[0]=='#':
		formattedTrend= formattedTrend.lstrip('#')
		formattedTrend = camel_case_split(formattedTrend)
		formattedTrend= ' '.join(formattedTrend)
	return formattedTrend
	
		
print "USA TRENDS"
for location in results:
	for trend in location["trends"]:
		new_trend = nytimesFormat(trend["name"])
		print trend["name"]+','+new_trend+','+str(trend["tweet_volume"])+','+location['locations'][0]['name']
