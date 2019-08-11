from flask import Flask, jsonify, make_response, request
from flask_restful import reqparse, Api, Resource
import werkzeug

from process import Form1

app = Flask(__name__)
upload_folder ='./uploads/'
app.config['UPLOAD_FOLDER'] = upload_folder
api = Api(app)

def error_response():
    return make_response(jsonify({'code': 1412, 'message': "invalid argument"}))
field = None

class GetPdfFile(Resource):
    def post(self):
        # try:
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.FileStorage, location='files')
        args = parser.parse_args()
        # print(args)
        pdf_file = args['file'] 
        pdf_file.save(upload_folder+'s.jpg')
        return jsonify({'result': "success"})
    
    def get(self):
        f = Form1(fname=upload_folder+'s.jpg')
        # get 
        field = [i[0] for i in f.overwrite2image()]
        return jsonify({'result': field})

class FillBlank(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('result')
        args = parser.parse_args()
        print(args)
        return jsonify({'result': "success"})

api.add_resource(GetPdfFile, '/get_pdf_file')
api.add_resource(FillBlank, '/response')

app.run(host='0.0.0.0', port=5000, debug=True)
        