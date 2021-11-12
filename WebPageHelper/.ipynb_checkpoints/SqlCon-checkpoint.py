#SqlCon.py 
import pymssql 
class SqlCon: 
    conn = pymssql.connect("127.0.0.1:1433", "sa","1234","wse") 
    @staticmethod 
    def Cursor(): 
        return SqlCon.conn.cursor() 
    @staticmethod 
    def Close(): 
        SqlCon.conn.close() 
    @staticmethod 
    def Commit():
        SqlCon.conn.commit()

