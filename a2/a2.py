from PIL import Image
import numpy as np
import math
from scipy import signal



def boxfilter(n):
    if (n % 2 == 0):
        raise AssertionError("Dimension must be odd");
    else:
        return np.full((n, n), 1/float(n*n));
		
#print boxfilter(5);	

# problem here with positive or negative values
def gauss1d(sigma):
    #  exp(- x^2 / (2*sigma^2))
    inc = 1;
    length = sigma*6; # get the length of the array                                      
    length = length + 1 if length % 2 == 0 else length; # adjust the length to be odd
    range = np.ceil(length/2); # get the range (distance) from the center of array. 
    array =  np.arange( range*-1, range+inc, inc); # generate the array and values
    array = (array**2)/(2 * sigma**2); # apply the gaussian function to the array
    factor = np.sum(array); # get the sum of all values
    array /= float(factor); # normalize array values based on sum
    return array;

'''
print gauss1d(0.3);	
print gauss1d(0.5);	
print gauss1d(1);	
print gauss1d(2);
'''

def gauss2d(sigma):
    a0 = gauss1d(sigma);
    a1 = a0[np.newaxis];
    a2 = np.transpose(a1);
    array = signal.convolve(a1,a2); 
    return array;

'''
print gauss2d(0.5);   
print gauss2d(1);
'''

def gaussconvolve2d(image,sigma):
    return signal.convolve2d(image,gauss2d(sigma),'same');
    
def gaussconvolve2dImage(filename, sigma):
    im = Image.open(filename);
    im.show();
    im = im.convert('L')
    im.show();
    imgarray = gaussconvolve2d(np.asarray(im), sigma);
    im = Image.fromarray(imgarray)
    im.show();
    
gaussconvolve2dImage("C:/git/cs425/a2/property-taxes.jpg", 1);

'''
#5. Gaussian convolution efficiency:

It is more efficient to use separability

'''