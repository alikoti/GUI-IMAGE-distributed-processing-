from flask import Flask, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/process", methods=["POST"])
def process_image():
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Read and process image
    image = cv2.imread(filepath)
    processed_image = cv2.dilate(image, np.ones((5, 5), np.uint8), iterations=1)

    output_path = os.path.join(UPLOAD_FOLDER, "processed_dilation.png")
    cv2.imwrite(output_path, processed_image)

    return send_file(output_path, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
