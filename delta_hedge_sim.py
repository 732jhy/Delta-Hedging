# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:10:30 2020

@author: Justin Yu

Simple Delta-Hedge algorithm for portfolio of a single option
"""

import matplotlib.pyplot as plt
import numpy as np

def GBM_sim(S, mu, T, sigma, N):
    '''
    Simulates a single path of Geometric Brownian Motion
    
    Args:
        S - initial path value
        mu - mean parameter
        T - time parameter
        sigma - volatility parameter
        N - number of steps in the path
    '''
    dt = T/N
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W)*np.sqrt(dt)
    t = np.linspace(0, T, N)
    S = S*np.exp((mu - 0.5*sigma**2)*t + sigma*W)
    return S,t


path = GBM_sim(100,0.05,1.0,0.25,100);plt.plot(path[1], path[0])

































































