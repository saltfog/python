
from numpy import *

import numpy
import wx
import os

#wx Object Creation
app = wx.App()

filename = wx.FileSelector()
#import file
pressureHydro = loadtxt(filename, unpack=True)
#numpy calculations

print pressureHydro
stdev = numpy.std(pressureHydro)
mean = numpy.mean(pressureHydro)

print "MEAN", mean
print "Standard Devation", stdev
#MEOP for Technology
MEOP = input("Enter MEOP of Inflator: ")
safety_factor = (mean - (stdev *3)) / MEOP

if safety_factor > 1.5:
    print 'Safety Factor is Acceptable'
else:
    print 'Safety Factor is not Acceptable'

print 'USCAR Safety Factor', safety_factor

fo = open('pressureout.txt','w')
fo.write('"MEAN" %d,"STANDARD DEV" %d,"SAFETY FACTOR" %.2f' % (mean, stdev, safety_factor))
fo.close()

app.MainLoop()

