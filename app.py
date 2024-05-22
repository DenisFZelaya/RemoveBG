import os
import io
import base64
from rembg import remove
from flask import Flask, render_template, request, jsonify
from PIL import Image

app = Flask(__name__)

def remove_background(input_image_path):
    input_image = Image.open(input_image_path)
    output_image = remove(input_image)
    
    buffered = io.BytesIO()
    output_image.save(buffered, format="PNG")
    encoded_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return encoded_img

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
        file.save(input_path)
        output_path = remove_background(input_path)
        return jsonify({'output_path': output_path})

if __name__ == '__main__':
    app.run(debug=True)
