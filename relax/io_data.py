#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : io_data.py
@Time : 2022/05/02 10:07:23
@Auth : Ming 
@Vers : 1.0
@Desc : read data from file or save data
@Usag : import io_data
'''

# here put the import lib
import numpy as np

def read_neb_barrier(data_file:str):
    """
    read neb barrier data from neb.dat
    :param data_file: './data/111-121-neb1/neb.dat'
    :return dist, energy: (list, list)
    """
    dist, energy = [], []
    f = open(data_file)
    data = f.readlines()
    for image_data in data:
        temp = image_data.split()
        dist.append(float(temp[1]))
        energy.append(float(temp[2]))
    return dist, energy
    

def main():
    
    pass

if __name__ == '__main__':
    main()