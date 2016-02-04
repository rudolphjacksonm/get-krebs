# Detect Python version and import correct modules
import sys

# Python 2.7
if sys.version[0] < 3:
  # Import urllib2
  import urllib2
  # Import RegEx
  import re
  #Import BeautifulSoup
  import beautifulsoup
else:
  from urllib.request import urlopen
  import re
  try:
    from bs4 import BeautifulSoup
  except: ImportError
    raise ImportError('No BeautifulSoup module found. Install BeautifulSoup before running this script.')

#Storing the URL and corresponding data in variables
url = 'https://krebsonsecurity.com'
query = urllib2.urlopen(url)

#Parsing data with BeautifulSoup
soup = BeautifulSoup(query)

#Taking all <div> tags that match class starting with "post"
all_posts = soup.findAll("div", {"class" : re.compile('post.*')})
#Getting the most recent div with matching class from array
last_post = all_posts[0]
#Getting just the data contained in paragraph tags
post_body = last_post.select('p')

print post_body
