import sqlite3
from app.models.comments import OneComment
class ConnectToDB:
    def __init__(self):
        self.conn = sqlite3.Connection("Comments_data.db")

    def insert_records(self,**kwargs):
        id = int(self.get_latest_id())+1
        self.conn.execute("INSERT INTO Comments Values (?,?,?)",[id,kwargs['cText'],kwargs['cPosted']])
        self.conn.commit()
        self.conn.execute("INSERT INTO Comments_Assoc Values (?,?,?)",[kwargs['rId'],id,kwargs['cAssoc']])
        self.conn.commit()
        print("Sucess !")

    def get_all_records(self):
        abc = self.get_latest_id()
        print(abc)
        result = self.conn.execute("SELECT c.cId,c.cText,c.cPosted,ca.rId,ca.cAssoc FROM Comments as c INNER JOIN Comments_Assoc as ca ON c.cId = ca.cId;")
        record = result.fetchall()
        commentslist = []
        for i in range(0,len(record)):
            commentslist.append(vars(OneComment(*record[i])))
        return commentslist
    
    def get_latest_id(self):
        result = self.conn.execute("SELECT c.cId,c.cText,c.cPosted,ca.rId,ca.cAssoc FROM Comments as c INNER JOIN Comments_Assoc as ca ON c.cId = ca.cId;")
        record = result.fetchall()
        return record[len(record)-1][0]
    
    def updatecomment(self,**kwargs):
        self.conn.execute("UPDATE Comments SET cText = ? WHERE cId = ?",[kwargs['cText'],kwargs['cId']])
        self.conn.commit()
        print("Success !")
    
    def deleteComment(self,**kwargs):
        self.conn.execute("DELETE from Comments WHERE cId= ?",[kwargs['cId']])
        self.conn.commit()
        self.conn.execute("DELETE from Comments_Assoc WHERE cId= ?",[kwargs['cId']])
        self.conn.commit()
        print("Success !")
