'''
Created on Mar 27, 2015

@author: maxz
'''

def lim(x, perc=.1):
    r = x.max() - x.min()
    return x.min()-perc*r, x.max()+perc*r
