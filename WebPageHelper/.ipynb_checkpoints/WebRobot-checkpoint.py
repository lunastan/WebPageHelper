from SqlCon import SqlCon 
from webpage import WebPage 
import pymssql

from SqlCon import SqlCon
conn = pymssql.connect("127.0.0.1:1433","sa","1234","WSE")
cs = conn.cursor()

url = "http://example.co.kr"
mcnt = 50


def UpdateMCnt(url,mcnt):
    cursor = SqlCon.Cursor() 
    query = str.format("update WebPage set mcnt={0} where (url='{1}')", mcnt, url)
    cursor.execute(query)
    SqlCon.Commit()

def FindWid(url):
    cursor = SqlCon.Cursor()    
    query = str.format("select wid from WebPage where (url='{0}')",url)
    cursor.execute(query)
    row = cursor.fetchone()
    if row:
        return row[0]
    return 0

def FindTitleUrlDescMCnt(url, wid):
    cursor = SqlCon.Cursor()    
    query = str.format("select title, url, description, mcnt from WebPage where (wid='{0}')", wid)
    cursor.execute(query)
    row = cursor.fetchone()
    if row:
        return row
    return 0

def FindCount(url):
    cursor = SqlCon.Cursor()    
    query = str.format("select count (*) from WebPage")
    cursor.execute(query)
    row = cursor.fetchone()
    if row:
        return row
    return 0



"""
import urllib.request as ureq
from bs4 import BeautifulSoup
from webpage import WebPage
from WebPageSql import WebPageSql
from CandidateSql import CandidateSql

while True:
   url, depth = CandidateSql.GetCandidate()
   if url == "":
       break
   else:
       print("{0},{1}".format(url,depth))
"""


#result = UpdateMCnt(url, mcnt)
#result = FindWid(url)
#result = FindTitleUrlDescMCnt(url, wid = 1)
#result = FindCount(url)
print(result)

conn.close()