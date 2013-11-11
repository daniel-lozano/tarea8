import matplotlib.pyplot as plt
import numpy as np


def Pprime(float P,float Pp):
    
    return Pp


def Pdouble(float P,float Pp,float alpha,float Km1,float Km2,float So, float beta):
    a= alpha*(So-P)/(Km1+So-P) - beta*P/(Km2+P)
    return a


def rungekutta(float P, float Pp,float salto):

    
    
