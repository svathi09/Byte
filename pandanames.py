
from pandas import Series,DataFrame
import pandas as  pd
import os
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium .webdriver.support.ui import WebDriverWait
import time 
#from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get("https://www.ssa.gov/oact/babynames/limits.html")

elem=browser.find_element_by_link_text("National data")
elem.click()
time.sleep(120)
wait = WebDriverWait(browser,60)
path1='/home/svathi/Downloads/'
os.chdir(path1)
os.system('unzip names.zip -d ~/home/svathi/week2/w2d3')

"""import zipfile
path2=os.getcwd()
with zipfile.ZipFile("names.zip","r") as zip_ref:
    zip_ref.extractall("path2")"""


######yob1990.txt
years=range(1880,2017)
newlist1=[]

for year in years:
 path='names/yob%d.txt' %year
 frame=pd.read_csv(path,names=['name','sex','births'])
 frame['year']=year
 pieces.append(frame)
names=pd.concat(newlist1,ignore_index=True)
frame1=DataFrame(names)
##print(frame1)







def add_prop(newcol):   

 births=group.births.astype(float)
 newcol['prop']=births/births.sum()
 return group
names=names.groupby(['year','sex']).apply(add_prop)
print(names.head(5))


#extract a subset of data to  analyse top 1000 names of each year and sex combination
list2=[]
for year,group in names.groupby(['year','sex']):
 list2.append(group.sort_index(by='births',ascending=False)[:1000])
top1000=pd.concat(list2,ignore_index=True)
##print(top1000)



