import os
import io
import base64

from flask import Flask, render_template, request, jsonify
from PIL import Image
import modules.openCV as openCVModules
import modules.removeBG as remBG

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    method = request.args.get('method')
    print("method: " + method)

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        if not os.path.exists('uploads'):
            os.makedirs('uploads')

        input_path = "uploads/input_image.jpg"
        file.save(input_path)

        output_path = ""

        if method == "binary":
            output_path = openCVModules.BinaryImg(input_path)

        if method == "rem_bg":
            output_path = remBG.remove_background(input_path)
            
        if method == "perspective_transformation":
            output_path = openCVModules.PerpectiveTransformation(input_path)
            
        if method == "laplacian":
            output_path = openCVModules.Laplacian(input_path)
            
        if method == "canny":
            output_path = openCVModules.Canny(input_path)

        return jsonify({'output_path': output_path })

if __name__ == '__main__':
    app.run(debug=True)
