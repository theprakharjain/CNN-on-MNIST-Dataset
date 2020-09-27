from flask import Flask, request, render_template, redirect
# from flask_cors import cross_origin
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO
import numpy as np
import sklearn
import pickle
import pandas as pd
import base64
import cv2
import matplotlib as plt

app = Flask(__name__)
model = load_model("../CNN_on_MNIST.h5")

@app.route("/")
# @cross_origin()
def home():
    return render_template("canvas.html")


@app.route("/imagesave",  methods = ["GET", "POST"])
# @cross_origin()
def image_view():
    if request.method == "POST":
        # Fetching the Canvas URL through POST Method
        data_url = request.form["link"]

        # print(data_url)

        # Getting Rid of the unwanted content
        content = data_url.split(';')[1]
        # Getting Rid of the unwanted content and saving the needed UTF-8 string coded form of image
        image_encoded = content.split(',')[1]
        
        # Decoding the image using "base64" library
        img_bytes = base64.b64decode(image_encoded)

        # Converting the string code back to the byte code through "BytesIO" library
        # And opening it with help of "Pillow (PIL)" library
        # The converted image is in the form of RGBA (Reg, Green, Blue, Alpha(For Transparency))
        # This image can only be saved in png form and lacks the background
        image = Image.open(BytesIO(img_bytes))

        # converting the image into RGB Form RGBA through "Pillow (PIL)" library
        rgb_im = image.convert('RGB')

        ############################## Important Commands which can come in handy later (DO NOT DELETE)################

        # # To Save RGB covnverted Image
        # rgb_im.save(r'C:\Users\iprak\Desktop\grayscale_converted.jpeg')
        # # To convert image in Numpy Array
        # image_final = np.array(image)
        # # To print the shape of converted numpy array
        # print(image_final.shape)
        # # To show the image through opencv --- First parameter takes window as input
        # # In our case its not there, thus its left blank
        # cv2.imshow("", image_final)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        ############################## ################################################ ###############################

        # convert the image to grayscale
        img = rgb_im.convert(mode='L')

        # resize image and ignore original aspect ratio
        img_resized = img.resize((28,28))

        # convert image to numpy array
        data_example = np.asarray(img_resized)
        
        # Reshaping image as taken by the model
        data_reshape_example = data_example.reshape(1,28,28,1)

        # Predicting the number
        output = model.predict_classes(data_reshape_example)
        print(output)

        # Rendering the prediction on to the webpage
        return render_template("canvas.html", prediction_text = "The digit is {}".format(output[0]))


#######################################  Waste/Old Code ##############################################
# with app.app_context():

# @app.route("/predict", methods = ["GET", "POST"])
# # @cross_origin()
# def predict():
#     if request.method == "POST":

#         # img = img.imresize(img,(28,28))
#         img = Image.open(r"C:\Users\iprak\Downloads\image.jpeg")
#         # convert the image to grayscale
#         img = img.convert(mode='L')

#         # Saving new image
#         img.save(r'C:\Users\iprak\Desktop\grayscale_converted.jpg')

#         # Loading Grayscale Image
#         img_conv = Image.open(r"C:\Users\iprak\Desktop\grayscale_converted.jpg")

#         # report the size of the image
#         print(img_conv.size)

#         # resize image and ignore original aspect ratio
#         img_resized = img_conv.resize((28,28))

#         # report the size of the thumbnail
#         print(img_resized.size)

#         # Saving new image
#         img_resized.save(r'C:\Users\iprak\Desktop\grayscale_converted_compressed.jpg')

#         # Loading Compressed Image
#         img_example = Image.open(r"C:\Users\iprak\Desktop\grayscale_converted_compressed.jpg")

#         # convert image to numpy array
#         data_example = np.asarray(img_example)
#         data_example.shape

#         # Reshaping image as taken by the model
#         data_reshape_example = data_example.reshape(1,28,28,1)

#         # To see new shape
#         data_reshape_example.shape

#         # Predicting the number
#         output = model.predict_classes(data_reshape_example)
#         print(output)

#         return render_template("canvas.html", prediction_text = "The digit is {}".format(output[0]))




#############################################################################################################




if __name__ == "__main__":
    app.run(debug=True)
    app.run_server(debug=False)
