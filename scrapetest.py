# urlopen can read the file streams easily
from urllib.request import urlopen
#outputs all the html code from the frontpage of espn.com 
html = urlopen("http://espn.com")
print(html.read())