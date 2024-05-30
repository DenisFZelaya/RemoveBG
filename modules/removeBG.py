from rembg import remove
import base64
from PIL import Image
import io


def remove_background(input_image_path):
    input_image = Image.open(input_image_path)
    output_image = remove(input_image)
    
    buffered = io.BytesIO()
    output_image.save(buffered, format="PNG")
    encoded_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return encoded_img