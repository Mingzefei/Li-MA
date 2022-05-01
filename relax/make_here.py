#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : make_here.py
@Time : 2022/03/11 21:42:25
@Auth : Ming 
@Vers : 1.0
@Desc : make_here for poscar or contcar
@Usag : python make_here.py ideal_POSCAR axis('x') dist(1/2) input_POSCAR (print POSCAR_here)
'''

# here put the import lib
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

def ddistAB(a_dpos, b_dpos):
    """d_pos distance from a to b"""
    ans = 0
    for i in range(3):
        ans += (a_dpos[i] - b_dpos[i]) ** 2 
    return np.sqrt(ans)

# read information from CONTCAT 
# cell_param and df
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

def pan(cont_df, axis, dist=1/2):
    """
    :param cont_df: input position in d_method
    :param axis: 'x', 'y' or 'z'
    :param dist: pan dist in d_method
    return pan_cont_df: panned cont_df in one cell
    """
    # get info
    pan_cont_list, elem_list = [], []
    for atom in cont_df.index:
        atom_info = list(cont_df.loc[atom])
        elem_list.append(atom_info[0])
        pan_cont_list.append(atom_info[1:4])
    # pan
    if axis == 'x':
        for i in range(len(pan_cont_list)):
            pan_cont_list[i][0] += dist
    elif axis == 'y':
        for i in range(len(pan_cont_list)):
            pan_cont_list[i][1] += dist
    elif axis == 'z':
        for i in range(len(pan_cont_list)):
            pan_cont_list[i][2] += dist
    else:
        print('wrong axis, it should bu \'x\', \'y\' or \'z\'')
        return 0
    # in one cell
    for i in range(len(pan_cont_list)):
        for j in range(3):
            if pan_cont_list[i][j] > 1:
                pan_cont_list[i][j] -= 1
            elif pan_cont_list[i][j] < 0:
                pan_cont_list[i][j] += 1
    # return
    
    for i in range(len(pan_cont_list)):
        pan_cont_list[i] = [elem_list[i]] + pan_cont_list[i]
    pan_cont_df = pd.DataFrame(pan_cont_list, index=cont_df.index, columns=cont_df.columns)
    
    return pan_cont_df
    

def get_key(cont_df, axis, dist=1/2):
    """
    :param cont_df: input position in d_method
    :return key: key of here (B in A)
    """
    key = []
    cont = list(map(list,cont_df.loc[:,'x_dpos':'z_dpos'].values))
    pan_cont_df = pan(cont_df, axis, dist)
    pan_cont = list(map(list,pan_cont_df.loc[:,'x_dpos':'z_dpos'].values))
    for atom in pan_cont:
        index, value = min(enumerate(cont), key=lambda x : ddistAB(x[1], atom))
        key.append(index)
    
    if len(key) == len(set(key)):
        return key
    else:
        print('key have repeated elem')
        return []
def use_key(pan_cont_df, input_key):
    """sort cont_df by key"""
    pan_cont_df = pan_cont_df.loc[:,'x_dpos':'z_dpos']
    if len(pan_cont_df.index) == len(input_key):
        pan_cont_df['key'] = input_key
        sort_cont_df = pan_cont_df.sort_values(by='key')
        return sort_cont_df.loc[:,'x_dpos':'z_dpos']
    else:
        print('input cont_df is not match input_key')
        return 0

def make_here(ideal_POSCAR, axis, dist, input_POSCAR):

    
    cell, df = read_contcar(ideal_POSCAR)
    key = get_key(df, axis, dist)
    input_cell, input_df = read_contcar(input_POSCAR)
    pan_input_df = pan(input_df, axis, dist)
    
    if len(input_df.index) == len(df.index):
        sort_cont_df = use_key(pan_input_df, key)
        return sort_cont_df
    elif len(input_df.index) > len(df.index):
        # get match and extra
        extra_index = []
        for index in pan_input_df.index:
            if index not in df.index:
                extra_index.append(index)
        match_input_df = pan_input_df.loc[[i for i in pan_input_df.index if i not in extra_index]]
        extra_input_df = pan_input_df.loc[[i for i in pan_input_df.index if i in extra_index]]
        # sort match
        sort_match_df = use_key(match_input_df, key)
        # deal with extra
        pan_extra_df = extra_input_df.loc[:,'x_dpos':'z_dpos']
        # insert extra into match
        ans_df = DataFrame(columns=['x_dpos','y_dpos','z_dpos'])
        count = 0
        for index in pan_input_df.index:
            if index in df.index:
                # ans_df = pd.concat([ans_df,DataFrame(sort_match_df.loc[index]).T], ignore_index=False)
                new = DataFrame(list(sort_match_df.iloc[count]), index=['x_dpos','y_dpos','z_dpos']).T
                count += 1
                ans_df = pd.concat([ans_df,new], ignore_index=True)
            else:
                new = DataFrame(list(pan_extra_df.loc[index]), index=['x_dpos','y_dpos','z_dpos']).T
                ans_df = pd.concat([ans_df,new], ignore_index=True)

        # for index in ans_df.index:
        #     print(*list(ans_df.loc[index]))
        return ans_df

def print_contcar(ideal_POSCAR, axis, dist, input_POSCAR):
  
    cont_df = make_here(ideal_POSCAR, axis, dist, input_POSCAR)
    head = read_head_conter(input_POSCAR)

    print(*head)
    for index in cont_df.index:
        print(*list(cont_df.loc[index]))


def main():
    ideal_POSCAR = 'POSCAR'
    axis = 'x'
    dist = 1/2
    input_POSCAR = 'input_POSCAR'
    
    from sys import argv, exit
    
    def help_print():
        print('usage      : make_here.py ideal_POSCAR axis(\'x\') dist(1/2) input_POSCAR')
    
    if '-h' in argv:
        help_print()
        exit(0)
    elif len(argv) == 5:
        python_script, ideal_POSCAR, axis, dist, input_POSCAR = argv
        dist = eval(dist)
        print_contcar(ideal_POSCAR, axis, dist, input_POSCAR)
        exit(0)
    else:
        print('input wrong, your input:',argv)
        help_print()
        exit(1)


if __name__ == '__main__':
    main()
    # debug()