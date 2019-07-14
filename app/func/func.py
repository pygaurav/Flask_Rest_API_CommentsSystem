from app import Resource,reqparse,ConnectToDB,request

class Comment(Resource):
    def get(self):
        conn = ConnectToDB()
        clsvar = conn.get_all_records()
        return clsvar

    def post(self):
        data = request.get_json(force=True)
        conn = ConnectToDB()
        conn.insert_records(**data)
        return {"Sucess":"Comment is Successfully posted!"}
    

    def delete(self):
        data = request.get_json(force=True)
        conn = ConnectToDB()
        conn.deleteComment(**data)
        return {"Sucess":"Record Successfully Deleted of Comment ID {0}".format(data['cId'])}

    def put(self):
        data = request.get_json(force=True)
        conn = ConnectToDB()
        conn.updatecomment(**data)
        return {"Sucess":"{0} value is Successfully Updated with {1}".format(data['cText'],data['cId'])}