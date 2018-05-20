from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

from bs4 import BeautifulSoup 

# handle exceptions 
try:
	html = urlopen("http://developer.android.com/")
# if there is an HTTP error
except HTTPError as e:
	print(e)
# if there is no server or the server cannot be reached
except URLError as e:
	print("No server")
else:
	print('Success')

# soupobj = BeautifulSoup(html.read())

# check for attribute/tag errors potentially

try:
	possibleBadContent = soupobj.nonExistingTag.anotherTag
except AttributeError as e:
	print('No possible tag')
else;
	if possibleBadContent == None:
		print('no tag')
	else:
		print(possibleBadContent)

# putting it all together
def receiveTitle(url):
	try: 
		html = urlopen(url)
	except HTTPError as e:
		return None 
	try:
		soupObj = BeautifulSoup(html.read())
		header1 = soupobj.body.h1
	except AttributeError as e:
		return None 
	return header1

title = receiveTitle("https://developer.android.com/")
if title == None:
	print("Cannot be found")
else:
	print(title)

