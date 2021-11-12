from SqlCon import SqlCon
from WebPageSql import WebPageSql
import pymssql

class CandidateSql:
 
    @staticmethod
    def AddCandidate(url,depth):
        cursor = SqlCon.Cursor()
        if WebPageSql.FindWid(url) != 0:
            return False
        query = str.format(
            "insert into Candidate (url,depth) values('{0}', {1})",url,depth)
        try:
           cursor.execute(query)           
           SqlCon.Commit()
        except:
            return False
        else:
            return True
    @staticmethod
    def GetCandidateID():
        cursor = SqlCon.Cursor()        
        query = str.format(
            "select MIN(id) from Candidate")
        try:
           cursor.execute(query)           
           row = cursor.fetchone()
           SqlCon.Commit()
        except:
            return 0
        else:
            if row:
                return row[0]
            return 0 
    @staticmethod
    def Remove(id):
        cursor = SqlCon.Cursor()        
        query = str.format(
            "delete from Candidate where id={0}",id)
        try:
           cursor.execute(query)
           SqlCon.Commit()
        except:
            return False
        else:
            return True
    @staticmethod
    def GetCandidate():
        id = CandidateSql.GetCandidateID()
        if id == 0: 
            return "",-1
        cursor = SqlCon.Cursor()        
        query = str.format(
            "select url,depth from Candidate where id={0}",id)
        try:
           cursor.execute(query)
           row = cursor.fetchone()
           SqlCon.Commit()
        except: 
            return "",-1
        else:
            if row:
                CandidateSql.Remove(id) 
                return row[0],row[1]
            return "",-1 