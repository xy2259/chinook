# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:22:12 2017

@author: rday

This script handles calculation of the Radial Integrals:
    int(dr r^3 j_lp(kf*r) R_nl(r))
for the photoemission matrix element calculations.
It loads the radial part of the wavefunction from electron_configs, which itself
takes Z and orbital label as arguments to do so.
The integration technique is based on a simple adaptive integrations algorithm
which is a sort of divide and conquer approach. For each iteration, the interval
is halved and the Riemann sum is computed. If the difference is below tolerance,
either one or both of the halves will return. If not, if either or both return diff
above tolerance, than the corresponding interval is again split and the cycle repeats
until the total difference over the domain is satisfactorily below tolerance.
In this way, the partition of the domain is non-regular, with regions of higher
curvature having a finer partitioning than those with flat regions of the function.

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
import electron_configs as econ


def integrand(r,arglist): #arglist: [lp,knorm,Z,orb]

    orb,_,_ = econ.Slater(arglist[2],arglist[3],r)

    tmp = (-1.0j)**arglist[0]*orb*r**3*sc.spherical_jn(arglist[0],r*arglist[1])

    return tmp

def rect(func,a,b,arglist):
    mid = (a+b)/2.0
    jac = abs(b-a)/6.0
    recsum = jac*(func(a,arglist)+4*func(mid,arglist)+func(b,arglist))
    return recsum

def recursion(func,a,b,tol,currsum,arglist):
    mid = (a+b)/2.0
  #  print mid
    sum_left = rect(func,a,mid,arglist)
    sum_right = rect(func,mid,b,arglist)
    err = abs(sum_left+sum_right-currsum)
    if err<=15*tol:
        return sum_left+sum_right
    return recursion(func,a,mid,tol/2.,sum_left,arglist)+recursion(func,mid,b,tol/2.,sum_right,arglist)

def integrate(func,a,b,tol,arglist):
    Q = recursion(func,a,b,tol,rect(func,a,b,arglist),arglist)
    return Q

def Bintegral(r_o,r_f,tol,lp,knorm,Z,orb):
    arglist = [lp,knorm,Z,orb]
    Q = integrate(integrand,r_o,r_f,tol,arglist)
    return Q

def direct(r,arglist): #arglist : [Z1,orb1,Z2,orb2]
    #for computing direct transition integral between two states
    orb1,_,_ = econ.Slater(arglist[0],arglist[1],r)
    orb2,_,_ = econ.Slater(arglist[2],arglist[3],r)
    
    return r**3*orb1*orb2

def direct_integrate(r_o,r_f,tol,Z,orbs):
    
    arglist = [Z[0],orbs[0],Z[1],orbs[1]]
    
    return integrate(direct,r_o,r_f,tol,arglist)
    



if __name__=="__main__":
    
    Z =  6
    
    lp = [0,2]
    r = [0,1]
#    
#    
#    Z = 26
#    lp = [1,3]
#    r = [0,25]
    tol = 0.5*10**-9
    hv = np.linspace(10,120,40)
    kn = np.sqrt(2*(9.11*10**-31)/(6.626*10**-34/(2*np.pi))**2*(hv-4.5)*(1.602*10**-19))/10**10
    Qp=np.zeros((len(hv)),dtype=complex)
    Qf = np.copy(Qp)
    for i in range(len(kn)):
        Qf[i] = Bintegral(r[0],r[1],tol,lp[1],kn[i],Z,'20')
        Qp[i] = Bintegral(r[0],r[1],tol,lp[0],kn[i],Z,'21')
    
    fig = plt.figure()
    ax = fig.add_subplot(1,2,1)
    ax.plot(hv,np.real(Qp),c='k')
    ax.plot(hv,np.real(Qf),c='r')
#    ax.legend(["d -> p","d -> f"],loc=4)
#    ax2 = fig.add_subplot(1,2,2)
#    ax2.plot(hv,(Qp/Qf))
#    ax2.set_title('Ratio of Radial Integrals--p:f')
#    ax.set_title('Radial Integrals from Fe3d')
#    plt.show()