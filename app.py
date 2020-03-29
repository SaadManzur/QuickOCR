from tesserocr import PyTessBaseAPI
from flask import Flask, redirect, render_template, url_for, request, flash
import numpy as np
import cv2 as opencv
from PIL import Image

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_file', methods=['POST'])
def process():
    img_file = request.files['img'].read()
    img = Image.fromarray(opencv.imdecode(np.fromstring(img_file, np.uint8), opencv.IMREAD_COLOR))

    with PyTessBaseAPI() as api:
        api.SetImage(img)
        flash(api.GetUTF8Text())

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=3500, host='0.0.0.0')