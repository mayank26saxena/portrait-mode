import os, shutil
from io import BytesIO
import tarfile, tempfile
from six.moves import urllib
import numpy as np
from PIL import Image
import tensorflow as tf
import cv2
from deeplabmodel import *

def create_pascal_label_colormap():
    colormap = np.zeros((256, 3), dtype=int)
    ind = np.arange(256, dtype=int)

    for shift in reversed(range(8)):
        for channel in range(3):
            colormap[:, channel] |= ((ind >> channel) & 1) << shift
            ind >>= 3
    return colormap

def label_to_color_image(label):
    if label.ndim != 2:
        raise ValueError('Expect 2-D input label')

    colormap = create_pascal_label_colormap()

    if np.max(label) >= len(colormap):
        raise ValueError('label value too large.')
    return colormap[label]

def load_model():
    model_path = 'deeplab_model.tar.gz'
    MODEL = DeepLabModel(model_path)
    print('model loaded successfully!')
    return MODEL

def generate_blur_image(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian_blurred = cv2.GaussianBlur(img ,(51,51),0)
    median_blurred = cv2.medianBlur(img,15)
    cv2.imwrite('temp/gaussian_blurred.jpg', gaussian_blurred)
    cv2.imwrite('temp/median_blurred.jpg', median_blurred)

def generate_seg_image(path, MODEL):
    #MODEL = load_model()
    orignal_im = Image.open(path)
    resized_im, seg_map = MODEL.run(orignal_im)
    seg_image = label_to_color_image(seg_map).astype(np.uint8)
    cv2.imwrite('temp/seg_image.jpg', seg_image)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def execute_portrait_mode(path):
    ''' try:
        os.remove("/static/output/output.jpg")
    except Exception as e:
        print "Exception." + str(e)
    '''

    MODEL = load_model()
    orig_image = Image.open(path)

    createFolder('./temp/')

    generate_blur_image(path)
    generate_seg_image(path, MODEL)

    seg_image = Image.open("temp/seg_image.jpg") #Can be many different formats.
    blur_image = Image.open("temp/gaussian_blurred.jpg")
    seg_image = seg_image.resize((orig_image.size[0],orig_image.size[1]),Image.ANTIALIAS)
    seg_image.save("temp/new_seg_image.jpg", quality = 100) #saved resized image
    seg_image = Image.open("temp/new_seg_image.jpg")

    black = 0,0,0
    pix = seg_image.load()
    pix_blurred = blur_image.load()
    pix_true = orig_image.load()

    length = orig_image.size[0]
    breadth = orig_image.size[1]
    for i in range(1,length):
        for j in range(1,breadth):
            if(pix[i,j] != black and pix[i,j][2] > 100 and pix[i,j][2] < 140):
                pix_blurred[i, j] = pix_true[i, j]

    head, tail = os.path.split(path)
    file_name = tail.split('.')[0]
    output_file_name = file_name + "-portrait" + ".jpg"
    #print(output_file_name)

    #Remove temp folder
    try:
        shutil.rmtree('temp/')
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

    return blur_image, output_file_name
