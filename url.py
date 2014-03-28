import urlib2

def page(url):
       def get(url):
              return urllib.urlopen(url).read()
       return get(url)

print (page('http://ya.ru/'))
print (page ('http://google.com/'))