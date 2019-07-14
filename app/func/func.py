from app import Resource,reqparse,ConnectToDB

class Comment(Resource):
    def get(self):
        conn = ConnectToDB()
        clsvar = conn.get_all_records()
        return clsvar

    parser = reqparse.RequestParser()
    parser.add_argument('cText',
    type=str
    # required=True,
    # help="Comment Text cannot be blank"
    )
    parser.add_argument('cPosted',
    type=str
    # required=True,
    # help="Comment Posted By cannot be blank"
    )
    parser.add_argument('rId',
    type=int
    # required=True,
    # help="Root ID cannot be blank"
    )
    parser.add_argument('cAssoc',
    type=int
    )

    def post(self):
        data = Comment.parser.parse_args()
        conn = ConnectToDB()
        conn.insert_records(**data)
        return {"Sucess":"Comment is Successfully posted!"}
    
    delparser = reqparse.RequestParser()
    delparser.add_argument('cId',
    type=int
    # required=True,
    # help="Comment ID cannot be blank"
    )
    def delete(self):
        data = Comment.delparser.parse_args()
        conn = ConnectToDB()
        conn.deleteComment(**data)
        return {"Sucess":"Record Successfully Deleted of Comment ID {0}".format(data['cId'])}

    putparser = reqparse.RequestParser()
    putparser.add_argument('cText',
    type=str)
    # required=True,
    # help="Comment Text cannot be blank")
    putparser.add_argument('cId',
    type=int)
    # required=True,
    # help="Comment ID cannot be blank"
    def put(self):
        data = Comment.putparser.parse_args()
        conn = ConnectToDB()
        conn.updatecomment(**data)
        return {"Sucess":"{0} value is Successfully Updated with {1}".format(data['cText'],data['cId'])}