#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : plot_neb_pos.py
@Time : 2022/03/14 19:58:54
@Auth : Ming 
@Vers : 1.0
@Desc : make poscar which neb images pos togetcher
@Usag : python plot_neb_pos.py pos1 pos2 pso3
'''

# here put the import lib
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

def read_contcar(file_name='CONTCAR'):
    """
    read information from CONTCAR
    :param file_name: the file where to get information
    :return cell_param, cont_df: cell parameters, ndarray of real_xv, real_yv, real_zv; cont_df, dataframe of atoms
    """
    
    def get_floatlist(s:str)->list:
        """turn a string to a float list"""
        return list(map(float, s.split()))
    def get_cpos(dpos, xv, yv, zv, scale_factor)->list:
        """get cpos about x,y,z in C_method with facor=1.0"""
        xtemp,ytemp,ztemp = 0,0,0
        for i in range(len(dpos)):
            xtemp += xv[i] * dpos[i] * scale_factor
            ytemp += yv[i] * dpos[i] * scale_factor
            ztemp += zv[i] * dpos[i] * scale_factor
        anslist = [xtemp, ytemp, ztemp]
        return anslist
    def get_dpos(cpos, xv, yv, zv, scale_factor)->list:
        """get dpos about x,y,z in D_method whth factor=1.0"""
        # matrix 
        det_temp = (xv[2]*yv[1]*zv[0] - xv[1]*yv[2]*zv[0] - xv[2]*yv[0]*zv[1] + xv[0]*yv[2]*zv[1] + xv[1]*yv[0]*zv[2] - xv[0]*yv[1]*zv[2]) * scale_factor
        xtemp_ndet = (yv[2]*zv[1]-yv[1]*zv[2])*cpos[0] - (yv[2]*zv[0]-yv[0]*zv[2])*cpos[1] + (yv[1]*zv[0]-yv[0]*zv[1])*cpos[2]
        ytemp_ndet = - (xv[2]*zv[1]-xv[1]*zv[2])*cpos[0] + (xv[2]*zv[0]-xv[0]*zv[2])*cpos[1] - (xv[1]*zv[0]-xv[0]*zv[1])*cpos[2]
        ztemp_ndet = (xv[2]*yv[1]-xv[1]*yv[2])*cpos[0] - (xv[2]*yv[0]-xv[0]*yv[2])*cpos[1] + (xv[1]*yv[0]-xv[0]*yv[1])*cpos[2]
        xtemp,ytemp,ztemp = xtemp_ndet/det_temp, ytemp_ndet/det_temp, ztemp_ndet/det_temp
        anslist = [xtemp, ytemp, ztemp]
        return anslist
        
    # read
    # file_path = 'C:/Users/Hua/1_workbench/AIM/'
    file_path = './'
    file = open(file_path + file_name)
    description = file.readline() # line 1: description
    scale_factor = float(file.readline()) # line 2: universal sacling parameters
    x_vector = get_floatlist(file.readline()) # line 3: lattice vector x
    y_vector = get_floatlist(file.readline()) # line 4: lattice vector y
    z_vector = get_floatlist(file.readline()) # line 5: lattice vector z
    atoms_elem = file.readline().split() # line 6: elements
    atoms_num = list(map(int, file.readline().split())) # line 7: numbers of atoms
    # line 8: selective dynamics or method of postions('C' or 'D')
    temp = file.readline()
    if ('sele' in temp) or ('Sele' in temp):
        selective_dynamics = True
        pos_method = file.readline()[0]
    else:
        selective_dynamics = False
        pos_method = temp[0]
    
    positions = [] # line 9(to the end): positions
    for i in range(sum(atoms_num)):
        pos = get_floatlist(file.readline())
        positions.append(pos[0:3])
        
    # zhengli_dpos
    cell_param = np.array([x_vector, y_vector, z_vector])*scale_factor
    atoms_index = [] # elemA1, elemA2, ...
    d_pos = [] # [elem, x_dpos, y_dpos, z_dpos]
    d_pos_temp = [] # [x_pos, y_pos, z_pos] list but maybe not in one cell
    for index,atom_elem in enumerate(atoms_elem):
        for atom_num in range(atoms_num[index]):
            atoms_index.append(atom_elem + str(atom_num+1))
            d_pos.append([atom_elem])    
    if pos_method == 'D':
        for index,pos in enumerate(positions):
            d_pos_temp.append(pos)
    elif pos_method == 'C':
        for index,pos in enumerate(positions):
            d_pos_temp.append(get_dpos(pos,x_vector,y_vector,z_vector,scale_factor))
    # pan d_pos_temp to make d_pos in one cell
    for index,dpos_list in enumerate(d_pos_temp):# [x_dpos, y_dpos, z_dpos]
        for index_dpos,dpos in enumerate(dpos_list):
            if dpos > 1:
                dpos_list[index_dpos] -= 1
            elif dpos < 0:
                dpos_list[index_dpos] += 1
        d_pos[index] += dpos_list
    
    colum_name = ['elem', 'x_dpos', 'y_dpos', 'z_dpos']
    cont_df = pd.DataFrame(d_pos, index=atoms_index, columns=colum_name)
    
    return cell_param, cont_df

def read_head_conter(file_name='CONTCAR'):
    """read head of CONTCAR, stop at position"""
    
    def get_floatlist(s:str)->list:
        """turn a string to a float list"""
        return list(map(float, s.split()))
    # read
    # file_path = 'C:/Users/Hua/1_workbench/AIM/'
    file_path = './'
    file = open(file_path + file_name)
    description = file.readline() # line 1: description
    scale_factor = file.readline() # line 2: universal sacling parameters
    x_vector_s = file.readline() # line 3: lattice vector x
    y_vector_s = file.readline() # line 4: lattice vector y
    z_vector_s = file.readline() # line 5: lattice vector z
    atoms_elem_s = file.readline() # line 6: elements
    atoms_num_s = file.readline() # line 7: numbers of atoms
    # line 8: selective dynamics or method of postions('C' or 'D')
    temp = file.readline()
    if ('sele' in temp) or ('Sele' in temp):
        selective_dynamics = True
        pos_method = file.readline()[0]
    else:
        selective_dynamics = False
        pos_method = temp[0]    
    
    # zhengli
    return [description, scale_factor, x_vector_s, y_vector_s, z_vector_s, atoms_elem_s, atoms_num_s, 'D']

def together(list_of_df):
    """
    together all df of list of df
    :param list_of_df: df input
    :return all_df: output
    """
    all_df = pd.concat(list_of_df, ignore_index=True)
    return all_df

def print_contcar(list_of_file):
    """list of file: files input, like ['01_CONTCAR', 02_CONTCAR']"""
    num_image = len(list_of_file)
    head = read_head_conter(list_of_file[0])
    atoms_elem_list = head[5].split()
    atoms_num = map(int,head[6].split())
    all_atoms_num_s = ''
    for num in atoms_num:
        all_atoms_num_s += str(num*num_image)+' '
    head[6] = all_atoms_num_s + '\n'
    
    print(*head)
    
    list_of_df = []
    for file in list_of_file:
        cell_param, cont_df = read_contcar(file)
        list_of_df.append(cont_df)
    all_df = together(list_of_df)
    for atoms in atoms_elem_list:
        atoms_pos = all_df.loc[all_df.elem == atoms, ['x_dpos','y_dpos','z_dpos']]
        for index in atoms_pos.index:
            print(*list(atoms_pos.loc[index]))

def main():
    from sys import argv, exit
    
    def help_print():
        print('usage      : python plot_neb_pos.py pos1 pos2 pso3')
    
    if '-h' in argv:
        help_print()
        exit(0)
    elif len(argv) > 2:
        list_of_file = argv[1:]
        print_contcar(list_of_file)
        exit(0)
    else:
        print('input wrong, your input:',argv)
        help_print()
        exit(1)
    pass

if __name__ == '__main__':
    main()