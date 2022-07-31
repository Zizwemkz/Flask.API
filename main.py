from ast import arg
from email import message
from pickle import FALSE
from pydoc import Helper
from unicodedata import name
from flask import Flask,request,jsonify
from flask_restful import Api,Resource, abort,reqparse
import flask_restful
from sqlalchemy import true
from models.video import Video
import json

app = Flask(__name__)
api = Api(app)
video_db = Video()
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("Name",type=str,help="Name of the videos is required")
video_put_args.add_argument("Views",type=int,help="Views on the video", required=True)
video_put_args.add_argument("Likes",type=int,help="likes on the videos", required=True)
video_put_args.add_argument("Category",type=str,help="Views on the video", required=True)
video_put_args.add_argument("Link",type=str,help="likes on the videos", required=True)

class Helloworld(Resource):

    def abort_error_message_if_id_doesnt_exist(self, video_id):
        id_dont_match =  False
        for id in video_db.get_all_videos():
            id_dont_match = False if video_id in id[0] else True
        if id_dont_match:
            abort(404, message = "could'nt find video id")


    def abort_if_video_exist(self, video_id):
        id_dont_match =  False
        for id in video_db.get_all_videos():
            id_dont_match = True if video_id in id[0] else False
        if id_dont_match:
           abort(409, message = "Video already exist with the same id")

    def get(self,video_id):
        #self.abort_error_message_if_id_doesnt_exist(video_id)
        video_list = []
        for item in video_db.get_all_videos():
            video_list.append(item)
        return jsonify({'videos': video_list})

    def post(self):
            return {"data":"hello zeni"}

    def put(self, video_id):
        self.abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        content_type = request.headers.get('Content-Type')
        video_db.insert_values(args['Name'],args['Category'],args['Likes'],args['Views'], args['Link'])
        return "Done",201


    def delete(self,video_id):
        self.abort_error_message_if_id_doesnt_exist(video_id)
        video_db.delete_video(video_id)
        return 'video deleted', 204

api.add_resource(Helloworld,"/Helloworld/<int:video_id>")
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

