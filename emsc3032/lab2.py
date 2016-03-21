from emsc3032.lab1 import lpmn
import numpy as np
from os.path import join, split

datadir = join(split(__file__)[0], 'data/')


def read_sph(filename):
    data=np.loadtxt(filename)
    n=data[:,0]
    m=data[:,1]
    C=data[:,2]
    S=data[:,3]
    Cmat=np.zeros([int(max(n)+1),int(max(n)+1)])
    Smat=np.zeros([int(max(n)+1),int(max(n)+1)])
    for i in range(len(C)):
        Cmat[int(n[i]),int(m[i])]=C[i]
        Smat[int(n[i]),int(m[i])]=S[i]
    return Cmat, Smat


def expDtofloat(s):
    return float(s.replace(b'D',b'E'))


def sph_sum(lat,lon,C,S,process=None):
    colat=90-lat
    if np.isscalar(colat) :
        colat = np.array([colat])
    if np.isscalar(lon) :
        lon = np.array([lon])
    res=np.zeros([len(colat),len(lon)])
    m=np.zeros_like(C)
    colat_r=np.radians(colat)
    lon_r=np.radians(lon)
    degmax=C.shape[0]-1
    if process != None and process != "geoid":
        n,h,l,k = np.loadtxt(datadir+'Load_Love2_CM.dat',unpack=True,\
                             converters={1:expDtofloat,2:expDtofloat, 3:expDtofloat})
        n=n[:degmax+1]
        h=h[:degmax+1]
        k=k[:degmax+1]
        l=l[:degmax+1]
    coeff=np.zeros(degmax+1)
    Cconvert = C.copy()
    Sconvert = S.copy()

    if process == 'geoid':
        coeff[1:]+=6371.0e3
    elif process=='ewh':
        coeff[2:]=1/3.0*6371.0e3*5.515*(2*n[2:]+1)/(1+k[2:])
    elif process=='visco':
        coeff[1:]=6371.0e3*(1.1677*n[1:]-0.5233)
    elif process=='defH':
        coeff[2:]=6371.0e3*h[2:]/(1+k[2:])
    elif process=='defV':
        coeff[2:]=6371.0e3*l[2:]/(1+k[2:])
    if process != None:
        Cconvert=Cconvert*coeff[:,None]*np.sqrt(2)
        Sconvert=Sconvert*coeff[:,None]*np.sqrt(2)

    for i in range(C.shape[0]):
        m[:,i]=i

    for i,clat in enumerate(colat_r):
        cos_colat = np.cos(clat)
        Plm=lpmn(cos_colat,degmax)
        for j,lonval in enumerate(lon_r):
            coslon= np.cos(m*lonval)
            sinlon= np.sin(m*lonval)
            res[i,j]=np.sum(Plm*(coslon*Cconvert+sinlon*Sconvert))

    shp = res.shape
    if shp[0]==(1) and shp[1]==1:
        res=float(res[0,0])
    elif shp[0]==1 or shp[1]==1:
        res=res.ravel()
    return res
