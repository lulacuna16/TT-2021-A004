import glob
import tensorflow as tf
from PIL import Image
from pathlib import Path
from numpy import asarray
import numpy as np
from keras.models import load_model

def a(path):
  image = Image.open(path)
  load_img_rz = np.array(image.resize((300,300)))
  return load_img_rz

redConv = tf.keras.models.load_model('./modeloNumerosEstaticos.h5')

paths = list(glob.glob('./*.jpg'))

img_p = []
for f in  paths:
  img_p.append(a(f))

img_prueba=np.array(img_p)

predicciones = redConv.predict(img_prueba)
predicciones_etq = np.argmax(predicciones,axis=1)
print("Predicciones")
for i in predicciones_etq:
    print(i+1, end=", ")

