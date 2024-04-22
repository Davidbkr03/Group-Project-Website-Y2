from flask import Flask, request, jsonify
from PIL import Image
from transformers import pipeline

app = Flask(__name__)

# Load the model
classifier = pipeline("image-classification", model="nsfw_image_detection")

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    #debug to show image has been received
    print("Image received")

    # Read the image file
    image_file = request.files['image']
    img = Image.open(image_file)

    # Classify the image
    result = classifier(img)

    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
