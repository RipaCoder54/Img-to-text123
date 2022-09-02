import cv2
import pytesseract
from PIL import Image
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import urllib.request

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'
app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route("/")
@cross_origin(supports_credentials=True)
def index():
    return "Welcome to the Course of Api"
@app.route("/getText", methods = ['POST'])
@cross_origin(supports_credentials=True)
def getText():
    input_json = request.get_json()
    url = input_json['img']
    urllib.request.urlretrieve(url, "text.jpg")
    path_to_image = 'text.jpg'
    img = Image.open(path_to_image)
    text = pytesseract.image_to_string(img)
    print(text)
    return jsonify({"text" : text})







if __name__ == "__main__":
    app.run(debug=True, port=8000)  