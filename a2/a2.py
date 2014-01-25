from PIL import Image
import numpy as np
import math
from scipy import signal



def boxfilter(n):
    if (n % 2 == 0):
        raise AssertionError("Dimension must be odd");
    else:
        return np.zeros((n,n));
		
#print boxfilter(4);	

def gauss1d(sigma):
    #  exp(- x^2 / (2*sigma^2))
    inc = 1;
    range = (sigma*6)/2;
    array =  np.arange( range*-1, range+inc, inc);
    array = (array**2)*-1/(2 * sigma**2);
    return array;

print gauss1d(0.3);	
print gauss1d(0.5);	
print gauss1d(1);	
print gauss1d(2);

def gauss2d(sigma):
    return "fk me";
    
print gauss2d(1);