from flask import Flask, send_file, request, Response
from flask_basicauth import BasicAuth
import io

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'sadguru'  # Set your username here
app.config['BASIC_AUTH_PASSWORD'] = 'isha143'  # Set your password here
basic_auth = BasicAuth(app)

visitor_count = 0

@app.route('/')
def serve_blank_image():
    global visitor_count
    visitor_count += 1  # Increment visitor count each time someone accesses the image
    
    # Generate a blank image (1x1 pixel)
    blank_image = io.BytesIO()
    blank_image.write(b'\x00\x00\x00')  # RGB value for black (can be white or any color)
    blank_image.seek(0)
    
    # Return the image with an appropriate content type
    return send_file(blank_image, mimetype='image/png')

@app.route('/visitor_count')
@basic_auth.required
def show_visitor_count():
    return f"Visitor Count: {visitor_count}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

