import requests

resp = requests.get('http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=8f357ea7d1c62d6ee8ea6c6f6938b970:3:74484189')
if resp.status_code != 200:
	# ERROR
	exit(0)
pop_news = resp.json()
for news in pop_news['results']:
	title = news['title']
	url = news['url']
	type = news['type']
	abstract = news['abstract']
	published_date = news['published_date']
	try:
		dec_facet = news['dec_facet']
	except Exception:
		dec_facet = ''
	try:
		org_facet = news['org_facet']	
	except Exception:
		org_facet = ''
	try:
		per_facet = news['per_facet']
	except Exception:
		per_facet = ''
	try:
		geo_facet = news['geo_facet']
	except Exception:
		geo_facet = ''
	print "title"+','+"url"+','+"type"+','+"abstract"+','+"published_date"+','+"dec_facet"+','+"org_facet"+','+"per_facet"+','+"geo_facet"
	print title+','+url+','+type+','+abstract+','+published_date+','+str(dec_facet)+','+str(org_facet)+','+str(per_facet)+','+str(geo_facet)
	
