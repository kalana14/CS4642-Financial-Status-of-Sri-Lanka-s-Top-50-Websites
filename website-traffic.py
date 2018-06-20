from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests 
import urllib
import csv

#defining the url #n is the page count
n = 2
url = "https://www.alexa.com/topsites/countries/LK"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data = soup.find_all("div",{"class":"tr site-listing"})

pages=[]

for i in range(len(data)):

	main_list = []

	item = data[i]

	title = item.find(class_="td DescriptionCell").get_text()

	title = title.split()

	title = title[0]

	pages.append(str(title))

	main_list.append(title)
	print(title)

	url_2 = "http://www.siteworthtraffic.com/report/"
	url_2 = url_2 + str(title)

	page = requests.get(url_2)

	soup1 = BeautifulSoup(page.content, 'html.parser')

	data1 = soup1.find_all("div",{"class":"wrapper"})


	item1 = data1[0]

	stats = soup1.find(class_="styled").get_text()

	stats = stats.splitlines()

	main_list.append(stats)
	
	myData = []
	myData.append(main_list)

	myFile = open('document.csv',"a+")  
	with myFile:  
	    writer = csv.writer(myFile)
	    writer.writerows(myData)
	myFile.close()




