import requests
from datetime import datetime
startTime = datetime.now()

url = str("https://www.sitemap/sitemap-1-")
x = range(1, 16)
for n in x:
    r = requests.get(url+str(n)+".xml", allow_redirects=True)
    open('site'+str(n)+'.xml', 'wb').write(r.content)


print(datetime.now() - startTime)





