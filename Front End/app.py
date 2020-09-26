from flask import Flask, request, render_template, redirect
# from flask_cors import cross_origin
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = load_model("../CNN_on_MNIST.h5")

@app.route("/")
# @cross_origin()
def home():
    return render_template("canvas.html")

#########################################################################
# with app.app_context():

@app.route("/predict", methods = ["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

        # img = img.imresize(img,(28,28))
        img = Image.open(r"C:\Users\iprak\Downloads\image.jpeg")
        # convert the image to grayscale
        img = img.convert(mode='L')

        # Saving new image
        img.save(r'C:\Users\iprak\Desktop\grayscale_converted.jpg')

        # Loading Grayscale Image
        img_conv = Image.open(r"C:\Users\iprak\Desktop\grayscale_converted.jpg")

        # report the size of the image
        print(img_conv.size)

        # resize image and ignore original aspect ratio
        img_resized = img_conv.resize((28,28))

        # report the size of the thumbnail
        print(img_resized.size)

        # Saving new image
        img_resized.save(r'C:\Users\iprak\Desktop\grayscale_converted_compressed.jpg')

        # Loading Compressed Image
        img_example = Image.open(r"C:\Users\iprak\Desktop\grayscale_converted_compressed.jpg")

        # convert image to numpy array
        data_example = np.asarray(img_example)
        data_example.shape

        # Reshaping image as taken by the model
        data_reshape_example = data_example.reshape(1,28,28,1)

        # To see new shape
        data_reshape_example.shape

        # Predicting the number
        output = model.predict_classes(data_reshape_example)
        print(output)

        return render_template("canvas.html", prediction_text = "The digit is {}".format(output[0]))

        # render_template("canvas.html")



#########################################################################




if __name__ == "__main__":
    app.run(debug=True)
    app.run_server(debug=False)
