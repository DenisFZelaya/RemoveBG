import os
from rembg import remove
from flask import Flask, render_template, request, redirect, url_for, jsonify
from PIL import Image

app = Flask(__name__)

def remove_background(input_image_path, output_image_path):
    input_image = Image.open(input_image_path)
    output_image = remove(input_image)
    output_image.save(output_image_path)
    return output_image_path, input_image_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        if not os.path.exists('uploads'):
            os.makedirs('uploads')

        input_path = "uploads/input_image.jpg"
        output_path = "static/output_image.png"
        file.save(input_path)
        output_path, original_path = remove_background(input_path, output_path)
        return jsonify({'output_path': output_path, "original_path": input_path})

if __name__ == '__main__':
    app.run(debug=True)
