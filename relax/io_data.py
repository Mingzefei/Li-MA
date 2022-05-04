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

def read_bader(data_file:str, atoms:list)->list:
    """
    read bader valence from valence.npy
    :param data_file: './data/111-11-pos1/valence.npy'
    :param atoms: ['Li1','MA2',...]
    :return valences: [1.2, -0.1, ...]
    
    """
    data = np.load(data_file, allow_pickle=True).item()
    valences = []
    for atom in atoms:
        valences.append(data[atom])
    return valences

def read_neb_H_bcp(data_dir:str)->list:
    """
    read bcp sum from H_bcp_data.npz
    :param data_file: './data/111-121-neb1'
    :return bcp_sum: [0.1, 0.02, ...]
    
    """
    total = []
    
    if 'neb1' in data_dir or 'neb2' in data_dir:
        images = [ str(x).rjust(2,'0') for x in range(12+2) ]
    elif 'neb3' in data_dir:
        images = [ str(x).rjust(2,'0') for x in range(15+2) ]
    
    for image in images:
        data_file = data_dir+'/'+image+'/H_bcp_data.npz'
        data = np.load(data_file, allow_pickle=True)
        total.append(data['sum'].item()['total'])
        
    return total

def read_neb_Li_bcp(data_dir:str)->list:
    """
    read bcp sum from Li_bcp_data.npz
    :param data_file: './data/111-121-neb1'
    :return bcp_sum: [0.1, 0.02, ...]
    
    """
    total = []
    
    if 'neb1' in data_dir or 'neb2' in data_dir:
        images = [ str(x).rjust(2,'0') for x in range(12+2) ]
    elif 'neb3' in data_dir:
        images = [ str(x).rjust(2,'0') for x in range(15+2) ]
    
    for image in images:
        data_file = data_dir+'/'+image+'/Li_bcp_data.npz'
        data = np.load(data_file, allow_pickle=True)
        total.append(data['sum'].item()['total'])
        
    return total

def main():
    
    pass

if __name__ == '__main__':
    main()