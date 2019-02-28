from bs4 import BeautifulSoup
import urllib.request
import sys

def make_soup(url):
    #r=requests.get(url)
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html)

url1= sys.argv[1]

def get_images(url):
    soup=make_soup(url)
    images= [img for img in soup.findAll('img')]
    print (str(len(images))+" images found")
    print ('Downloading images to current working directory.')
    image_links = [each.get('src') for each in images]
    for each in image_links:
    	filename=each.split('/')[-1]
    	urllib.request.urlretrieve(each, filename)
    return image_links

if __name__ == "__main__":
    get_images(url1)