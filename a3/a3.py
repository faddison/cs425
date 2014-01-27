from PIL import Image
from PIL import ImageDraw
import numpy as np
import math
import ncc
from scipy import signal

def MakePyramid(image, minsize):
    images = [image];
    return MakePyramidHelper(images, image, minsize);
    
def MakePyramidHelper(images, image, minsize):
    x = image.size[0];
    y = image.size[1];
    if (x < minsize or y < minsize):
        return images;
    else:
        image = image.resize((int(x*0.75),int(y*0.75)), Image.BICUBIC)
        images.append(image);
        return MakePyramidHelper(images, image, minsize);

def ShowPyramid(images):
    f = 0.75;
    a = images[0].size[0];
    n = len(images);
    x = a*((1-f**n)/(1-f)) # geometric series
    image = Image.new("L",(int(np.ceil(x)),int(np.ceil(a))));
    offset = 0;
    
    for i in range(n):
        image.paste(images[i], (int(np.ceil(offset)), 0));
        offset += images[i].size[0];
    
    image.show();
    return image;
    
def FindTemplate(pyramid, template, threshold):
    array = ncc.normxcorr2D(image, template);
    matches = list();
    
    for x in range(len(array)):
        for y in range(len(array)):
            if (array[x][y] > threshold):
                matches.append((x,y));
    
    draw = ImageDraw.Draw(pyramid);
    for p in matches:
        draw.point(p,fill="red");
    del draw;
    
    pyramid.show();
    #print array;
    
    # go through the array and find all locations above 'threshold'
    # for all locations draw them on the original image
    return;

image = Image.open("C:/git/cs425/a3/faces/judybats.jpg");
minsize =50;
pyramid = MakePyramid(image, minsize)
#pyramidimage = ShowPyramid(pyramid);
pyramidimage = pyramid[0];

template = Image.open("C:/git/cs425/a3/faces/template.jpg");
FindTemplate(pyramidimage, template, 0.2);

