#http://cgcooke.github.io/Image-Deconvolution/

from scipy import mgrid,exp
import numpy as np
from numpy.fft import *
from PIL import Image

def makeGaussianPSF(radius,sizeX,sizeY):
    """ Returns a normalized 2D gauss kernel array for convolutions """   
    x,y = mgrid[-sizeY/2:sizeY/2, -sizeX/2:sizeX/2]
    g = exp(-(x**2/float(radius)+y**2/float(radius)))
    return(g / g.sum())

def convolve(Input, psf, epsilon):
    InputFFT = fftn(Input)
    psfFFT = fftn(psf)+epsilon
    convolved = ifftn(InputFFT*psfFFT)
    convolved = np.abs(convolved)
    return(convolved)

def deconvolve(Input, psf, epsilon):
    InputFFT = fftn(Input)
    psfFFT = fftn(psf)+epsilon
    deconvolved = ifftn(InputFFT/psfFFT)
    deconvolved = np.abs(deconvolved)
    return(deconvolved)

def makeMotionPSF(length,sizeX,sizeY):
    psf = np.zeros((sizeY,sizeX))
    psf[sizeY/2:sizeY/2+1,sizeX/2-length/2:sizeX/2+length/2] = 1
    return(psf/psf.sum())

def exportArrayAsImage(img,fileName):
    img = np.abs(img)
    img = np.where(img > 255, 255, img) 
    img = np.where(img < 0, 0, img) 
    img = img.astype(np.uint8)
    img = Image.fromarray(img)
    img.save(fileName)


epsilon = 0.00001
r=1000
Input = np.asarray(Image.open('Input.jpg').convert('L'))
sizeY,sizeX = Input.shape
psf = makeGaussianPSF(r,sizeX,sizeY)

#Visualize the PSF
exportArrayAsImage(psf*255.0/psf.max(),'PSF.png')

#Convolve the input
InputConv = np.abs(convolve(Input, psf, epsilon))

#Deconvolve the input
InputDeconv = deconvolve(InputConv, psf, epsilon)

#Visualize the convolved and deconvolved images
exportArrayAsImage(fftshift(InputConv),'Convolved.png')
exportArrayAsImage(InputDeconv,'Deconvolved.png')




