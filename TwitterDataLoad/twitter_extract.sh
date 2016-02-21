#trend_py=$1
#search_py=$2

output=`python /Users/ranand/RealityHack/python-twitter-examples/twitter-trends.py | cut -f1 -d','`
echo $output

for tweet in $output:
do
	py

