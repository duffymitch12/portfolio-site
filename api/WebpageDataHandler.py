from flask_restful import Api, Resource, reqparse
from utils import get_db, close_connection

class WebpageDataHandler(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "page", type=str, required=True, help="Page name cannot be blank"
        )
        args = parser.parse_args()

        page = args["page"]

        data = self.fetch_page_data(page)

        if data:
            return {"resultsStatus": "SUCCESS", "data": data}
        else:
            return {
                "resultStatus": "FAILURE",
                "message": f"No data found for page: {page}",
            }

    def fetch_page_data(self, page):
        allowed_pages = ['experience', 'projects', 'home']
        if page not in allowed_pages:
            return None

        db = get_db()
        query = f"SELECT * FROM {page}"
        table = db.execute(query).fetchall()
        data = []
        if page == "experience":
            for i in table:
                temp = {}
                temp['id'] = i[0]
                temp['title'] = i[1]
                temp['company'] = i[2]
                temp['filename'] = i[3]
                temp['locationState'] = i[4]
                temp['locationCity'] = i[5]
                temp['description'] = i[6]
                temp['startYear'] = i[7]
                temp['endYear'] = i[8]
                temp['startMonth'] = i[9]
                temp['endMonth'] = i[10]
                data.append(temp)
        # print(f"data: {data}")
        return data

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument("type", type=str)
        parser.add_argument("message", type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        request_type = args["type"]
        request_json = args["message"]
        # ret_status, ret_msg = ReturnData(request_type, request_json)
        # currently just returning the req straight
        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "No Msg"

        final_ret = {"status": "Success", "message": message}

        return final_ret
