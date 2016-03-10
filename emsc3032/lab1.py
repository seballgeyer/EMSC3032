# -*- coding: utf-8 -*-

"""

Created on Mon Feb 29 2016


@author: Sebastien Allgeyer

"""


import numpy as np

try:
    xrange
except NameError:
    xrange=range


def lpmn(X,ndeg):
    """ Generates the associated Legender polynomial of argument X up to the degree ndeg
    it returns an array [ndeg+1,ndeg+1] of the Associated legender function of argument X. for all ordre > degree, the returned value is 0.0
    :param X: The argument of the Associated Legender Functions
    :param ndeg: Maximum degree
    Return Plm
    """

    Plm=np.zeros([ndeg+1,ndeg+1])
    #assert abs(X)<1, "X (%f) must belong to [-1;1]" % id
    if abs(X)>1:
        raise Exception("X (=%f) must belong to [-1;1]"%(X))
    #Plm=sp.zeros([ndeg,ndeg])
    Plm[0,0]=1
    Plm[1,0]=X
    #legendre Pol
    for l in xrange (1,ndeg):
        Plm[l+1,0]=((2*l+1)*X*Plm[l,0]-(l)*Plm[l-1,0])/(l+1)
    #normalise
    for l in xrange(1,ndeg+1):
        Plm[l,0]=np.sqrt(2*l+1)*Plm[l,0]
    #return Plm
    A=1.0-X*X
    #if abs(X=-1 or 1)
    # Set all value of Plm (!=0, all) to 0 ... It's already done!
    if A==0:
        return Plm
    SQa=np.sqrt(A)
    #Fill the first values.
    Plm[1,1]=SQa*np.sqrt(1.5)
    Plm[2,1]=3*SQa*X*np.sqrt(2.5/3.0)
    Plm[2,2]=3*A*np.sqrt(5/24.0)
    #return Plm
    #Now we have enough data for the recurence formulas.
    for l in xrange(3,ndeg+1):
        su=1.0
        for j in xrange(1,l+1):
            s=(2.0*j-1)/(2.0*j)
            su=su*np.sqrt(A*s)
        Plm[l,l]=np.sqrt(2.0*l+1.0)*su
        
        su=1.0
        for j in xrange(2,l+1):
            s=(2.0*j-1)/(2.0*j-2.0)
            su=su*np.sqrt(A*s)
        Plm[l,l-1]=X*np.sqrt(2.0*l+1)*su
        
        for m in xrange(l-2,0,-1):
            C=2.0*(m+1.0)/np.sqrt((l+m+1.0)*(l-m))
            C=C*X/SQa
            D=(l+m+2.0)*(l-m-1.0)/((l+m+1.0)*(l-m))
            D=np.sqrt(D)
            Plm[l,m]=C*Plm[l,m+1]-D*Plm[l,m+2]
        #normalise
        #Plm[:,1:-1]*=np.sqrt(2)
    return Plm
