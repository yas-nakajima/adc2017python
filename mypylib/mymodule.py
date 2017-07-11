import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt 

def getbackground(infits):
    
    data = fits.getdata(infits)
    med = np.median(data)
    std = np.std(data)
    
    for i in range(5):
        xx = np.where((data > med - 3 * std) & (data < med + 3 * std))
        med = np.median(data[xx])
        std = np.std(data[xx])
   
    return med, std


def showfits(infits):
    
    med, std = getbackground(infits)
    imdata = fits.getdata(infits)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(imdata, plt.cm.gray, vmin=med - std, vmax = med + 5 * std, origin='lower', interpolation='none')
    plt.show()
