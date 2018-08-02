# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:30:38 2018

@author: rday
"""
import numpy as np

posns = ([[0.33333333333332,   0.66666666666665,   0.31943934568918,  0],    
  [-0.00000000000002,  -0.00000000000001,   0.65277267902252,  0],    
   [0.66666666666665,   0.33333333333332,   0.98610601235585,  0],    
   [0.66666666666668,   0.33333333333335,   0.18056065431082,  0],    
   [0.33333333333335,   0.66666666666668,   0.51389398764415,  0],  
   [0.00000000000002,   0.00000000000001,   0.84722732097748,  0],    
  [-0.00000000000001,  -0.00000000000001,   0.15277363902251,  0],    
   [0.66666666666665,   0.33333333333332,   0.48610697235585,  0],    
   [0.33333333333332,   0.66666666666665,   0.81944030568918,  0],    
   [0.33333333333335,   0.66666666666668,   0.01389302764415,  0],    
   [0.00000000000001,   0.00000000000001,   0.34722636097749,  0],    
   [0.66666666666668,   0.33333333333335,   0.68055969431082,  0],    
   [0.00000000000000,   0.31486811660227,   0.25000000000000,  1],     
   [0.66666666666667,   0.64820144993561,   0.58333333333333,  1],     
   [0.33333333333333,   0.98153478326894,   0.91666666666667,  1],     
   [0.68513188339780,   0.68513188339776,   0.24999999999999,  1],     
   [0.35179855006446,   0.01846521673110,   0.58333333333332,  1],     
   [0.01846521673113,   0.35179855006443,   0.91666666666665,  1],     
   [0.31486811660220,  -0.00000000000004,   0.25000000000001,  1],     
   [0.98153478326887,   0.33333333333330,   0.58333333333335,  1],     
   [0.64820144993554,   0.66666666666663,   0.91666666666668,  1],     
   [0.35179771006447,   0.33333333333337,   0.08333333333332,  1],     
   [0.01846437673113,   0.66666666666670,   0.41666666666665,  1],     
   [0.68513104339780,   0.00000000000004,   0.74999999999999,  1],     
   [0.98153562326887,   0.64820228993557,   0.08333333333335,  1],     
   [0.64820228993553,   0.98153562326890,   0.41666666666668,  1],     
   [0.31486895660220,   0.31486895660224,   0.75000000000001,  1],     
   [0.66666666666667,   0.01846437673106,   0.08333333333333,  1],     
   [0.33333333333333,   0.35179771006440,   0.41666666666667,  1],     
   [0.00000000000000,   0.68513104339773,   0.75000000000000,  1]])   

class orbital:
    
    def __init__(self,fpos,avec,index,label):
        self.fpos = fpos
        self.pos = np.dot(avec.T,fpos)
        self.index = index
        self.label = label

def basis(avec):
    basis = []
    for p in posns:
        basis.append(orbital(p[:3],avec,len(basis),p[-1]))
    return basis
    