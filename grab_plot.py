#creating a script to scrape data (schiller index and consumer sentiment data)
import urllib2
from bs4 import BeautifulSoup
import unicodedata
import matplotlib.pyplot as plt

url = "http://www.sca.isr.umich.edu/data-archive/mine.php"
data = urllib2.urlopen(url).read()
soup = BeautifulSoup(data)
date = []
csi = []


for tr in soup.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 3:
        if unicodedata.normalize('NFKD', tds[0].text).encode('ascii','ignore') == "Month":
            continue
        else:
            date = unicodedata.normalize('NFKD', tds[1].text).encode('ascii','ignore') + unicodedata.normalize('NFKD', tds[0].text).encode('ascii','ignore') + '01'

##            month.append(float(unicodedata.normalize('NFKD', tds[0].text).encode('ascii','ignore')))
##            year.append(float(unicodedata.normalize('NFKD', tds[1].text).encode('ascii','ignore')))
            csi.append(float(unicodedata.normalize('NFKD', tds[2].text).encode('ascii','ignore')))

plt.plot(csi)
plt.ylabel('University of Michican Sentiment Index')
plt.show()
