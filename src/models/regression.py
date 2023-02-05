from numpy.polynomial import legendre
import warnings
import numpy
import random

##########
#  globals
#
#  WARNING:  need to recode to remove dependence of beta on x-range!!!
##########
#   x range ... don't change
xmin = 0
xmax = 10
#   smoothing parameter for Smoothed Legendre Polynomials ... pairs with x-range!!
beta = 0.00001
#   scale parameter for noise
sigma = 0.2

##############################
#  support for making datasets
##############################


def setSigma(noise):
    global sigma
    sigma = noise

#  shift X domain to be in [-1,1]


def xshift(x):
    return ((x-xmin)/(xmax-xmin)*2.0 - 1.0)

# have to generate an x sample several times


def makeX(pts, uniform=False):
    if uniform:
        xm = numpy.linspace(xmin, xmax, pts)
    else:
        xm = xmin + numpy.sort(numpy.random.random([pts]))*(xmax-xmin)
    return xm

# here is a noise function


def addNoise(yt, laplace=False):
    if laplace:
        y = yt + sigma/2.0*numpy.random.laplace(size=yt.size)
    else:
        y = yt + sigma*numpy.random.randn(len(yt))
    return y

#  build a set of polynomial orders to use to fit


def makeOrders(points):
    orders = [int(points/1.2)]
    if orders[0] > 200:
        orders[0] = 200
    while orders[0]/2 > 2:
        orders.insert(0, int(orders[0]/2))
    return orders


def maxOrder(points):
    order = int(points/1.2)
    if order > 200:
        order = 200
    return order


####################
#  simple regression
####################
#  stops polyfit complaining about poor matrix
warnings.simplefilter('ignore', numpy.RankWarning)

#  return yts for poly fit to (xs,ys)


def linReg(xs, ys, xts, order):
    # build the polynomial, a Python object from numpy
    polynomial = numpy.poly1d(numpy.polyfit(xs, ys, order))

    #  build the fitted poly curve (xts,???) from the polynomial
    return polynomial(xts)

#  return a polynomial that is about as good as you get


def bestLinReg(func, xts, order):
    # fit with large amount of data and no noise
    numpts = order*50
    xb = numpy.linspace(xmin, xmax, numpts)
    yb = func(xb)
    return linReg(xb, yb, xts, order)




