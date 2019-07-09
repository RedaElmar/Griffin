###################################################
#"""WWS - Weather Web Scrapper"""                ##
#                         """Reda EL MARHOUCH""" ##
#                    Griffin                     ##
###################################################

import pandas
import requests
from bs4 import BeautifulSoup

page = requests.get("https://weather.com/fr-MA/temps/parheure/l/7151e112f115f627b087448ccd404dc11d8f1f246ab4af8e868d8f97d2935891")
soup=BeautifulSoup(page.content,"html.parser")
al=soup.find("div",{"class":"locations-title hourly-page-title"}).find("h1").text
table=soup.find_all("table",{"class":"twc-table"})
l=[]
for elt in table:
 for i in range(len(elt.find_all("tr"))-1):
  d = {}  
  d["time"]=elt.find_all("span",{"class":"dsx-date"})[i].text
  d["date"]=elt.find_all("div",{"class":"hourly-date"})[i].text
  d["desc"]=elt.find_all("td",{"class":"description"})[i].text 
  d["temp"]=elt.find_all("td",{"class":"temp"})[i].text 
  d["precip"]=elt.find_all("td",{"class":"precip"})[i].text
  d["wind"]=elt.find_all("td",{"class":"wind"})[i].text  
  d["humidity"]=elt.find_all("td",{"class":"humidity"})[i].text 
  l.append(d)
df = pandas.DataFrame(l,columns= ["date","time", "wind","temp","humidity","precip","desc"])
al=al.replace(",", "")
al=al.replace(" ", "_")
df.to_excel(al+".xlsx")
#df.to_csv(al+".csv") for comma separated version

