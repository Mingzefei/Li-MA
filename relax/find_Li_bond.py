#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : find_Li_bond.py
@Time : 2022/05/02 15:17:46
@Auth : Ming 
@Vers : 1.0
@Desc : find Li-H bond for AIM_bcp.py
@Usag : python find_Li_bond.py -dist 5 (-save Li_bcp_data.npz)
'''

# here put the import lib
from cmath import nan
from sys import argv, exit
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
import os
from tqdm import tqdm

def dist(a_cpos, b_cpos):
    sum = 0
    for i in range(len(a_cpos)):
        sum += (a_cpos[i] - b_cpos[i]) ** 2
    return sum ** 0.5
def get_cpos(dpos, xv, yv, zv, scale_factor)->list:
    """get cpos about x,y,z in C_method with facor=1.0"""
    # xtemp,ytemp,ztemp = 0,0,0
    # for i in range(len(dpos)):
    #     xtemp += xv[i] * dpos[i] * scale_factor
    #     ytemp += yv[i] * dpos[i] * scale_factor
    #     ztemp += zv[i] * dpos[i] * scale_factor
    # anslist = [xtemp, ytemp, ztemp]
    # return anslist
    xv, yv, zv = np.array(xv), np.array(yv),np.array(zv)
    cpos = dpos[0]*xv + dpos[1]*yv + dpos[2]*zv
    return list(cpos*scale_factor)
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
def read_contcar(file_name='CONTCAR'):
    """
    get contcar data from file_name=CONTCAR
    
    :param file_name: contcar file
    :return cell_param, cont_df:
    """
    def get_floatlist(s:str)->list:
        """turn a string to a float list"""
        return list(map(float, s.split()[0:3]))
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

    # zhengli
    cell_param = np.array([x_vector, y_vector, z_vector])*scale_factor
    atoms_index = [] # elemA1, elemA2, ...
    c_pos = [] # [elem, x_cpos, y_cpos, z_cpos]
    c_pos_temp = [] # [x_pos, y_pos, z_pos] list but maybe not in one cell
    for index,atom_elem in enumerate(atoms_elem):
        for atom_num in range(atoms_num[index]):
            atoms_index.append(atom_elem + str(atom_num+1))
            c_pos.append([atom_elem])    
    if pos_method == 'D':
        for index,pos in enumerate(positions):
            c_pos_temp.append(get_cpos(pos,x_vector,y_vector,z_vector,scale_factor))
            # c_pos[index] += get_cpos(pos,x_vector,y_vector,z_vector,scale_factor)
    elif pos_method == 'C':
        for index,pos in enumerate(positions):
            x_cpos = pos[0] * scale_factor
            y_cpos = pos[1] * scale_factor
            z_cpos = pos[2] * scale_factor
            c_pos_temp.append([x_cpos, y_cpos, z_cpos])
            # c_pos[index] += [x_cpos, y_cpos, z_cpos]
    # # pan c_pos to make c_pos in one cell
    for index,cpos_list in enumerate(c_pos_temp):
        dpos_list = get_dpos(cpos_list,x_vector,y_vector,z_vector,1) # [x_dpos, y_dpos, z_dpos]
        for index_dpos,dpos in enumerate(dpos_list):
            if dpos > 1:
                dpos_list[index_dpos] -= 1
            elif dpos < 0:
                dpos_list[index_dpos] += 1
        c_pos[index] += get_cpos(dpos_list,x_vector,y_vector,z_vector,1)
    
    colum_name = ['elem', 'x_cpos', 'y_cpos', 'z_cpos']
    cont_df = pd.DataFrame(c_pos, index=atoms_index, columns=colum_name)
    
    return cell_param, cont_df
    pass
def super_poscar(cell_param:np.ndarray, atoms_cpos:DataFrame)->DataFrame:
    """
    pan to get super cell for find H bond
    
    :param cell_param: ndarray of real_xv, real_yv, real_zv
    :param atoms_cpos: input atoms_cpos
    :return super_atoms_cpos: output atoms_cpos
    """
    super_atoms_cpos = pd.DataFrame({}, columns=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num']) #
    for atom in atoms_cpos.index:
        # if 'Cl' in atom or 'Br' in atom or 'I' in atom:
        if 'Li' in atom:

            elem, x_cpos, y_cpos, z_cpos = list(atoms_cpos.loc[atom])
            add_data = pd.DataFrame([elem, x_cpos, y_cpos, z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
            super_atoms_cpos = pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)

            x_dpos, y_dpos, z_dpos = get_dpos([x_cpos, y_cpos, z_cpos], cell_param[0], cell_param[1], cell_param[2], 1)
            
            def add_to_super(temp_x_dpos, temp_y_dpos, temp_z_dpos,cell_param,elem,atom,super_atoms_cpos):
                temp_x_cpos, temp_y_cpos, temp_z_cpos = get_cpos([temp_x_dpos, temp_y_dpos, temp_z_dpos],cell_param[0], cell_param[1], cell_param[2],1)
                add_data = pd.DataFrame([elem, temp_x_cpos, temp_y_cpos, temp_z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
                return pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)

            for temp_x_dpos in (x_dpos-1,x_dpos,x_dpos+1):
                for temp_y_dpos in (y_dpos-1,y_dpos,y_dpos+1):
                    for temp_z_dpos in (z_dpos-1,z_dpos,z_dpos+1):
                        super_atoms_cpos = add_to_super(temp_x_dpos,temp_y_dpos,temp_z_dpos,cell_param,elem,atom,super_atoms_cpos)

            # # a+1
            # temp_x_dpos,temp_y_dpos,temp_z_dpos = x_dpos + 1,y_dpos,z_dpos
            # temp_x_cpos, temp_y_cpos, temp_z_cpos = get_cpos([temp_x_dpos, temp_y_dpos, temp_z_dpos],cell_param[0], cell_param[1], cell_param[2],1)
            # add_data = pd.DataFrame([elem, temp_x_cpos, temp_y_cpos, temp_z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
            # super_atoms_cpos = pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)
            # # a-1
            # temp_x_dpos,temp_y_dpos,temp_z_dpos = x_dpos - 1,y_dpos,z_dpos
            # temp_x_cpos, temp_y_cpos, temp_z_cpos = get_cpos([temp_x_dpos, temp_y_dpos, temp_z_dpos],cell_param[0], cell_param[1], cell_param[2],1)
            # add_data = pd.DataFrame([elem, temp_x_cpos, temp_y_cpos, temp_z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
            # super_atoms_cpos = pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)   
            # # b+1
            # temp_x_dpos,temp_y_dpos,temp_z_dpos = x_dpos,y_dpos + 1,z_dpos
            # temp_x_cpos, temp_y_cpos, temp_z_cpos = get_cpos([temp_x_dpos, temp_y_dpos, temp_z_dpos],cell_param[0], cell_param[1], cell_param[2],1)
            # add_data = pd.DataFrame([elem, temp_x_cpos, temp_y_cpos, temp_z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
            # super_atoms_cpos = pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)
            # # b-1
            # temp_x_dpos,temp_y_dpos,temp_z_dpos = x_dpos,y_dpos - 1,z_dpos
            # temp_x_cpos, temp_y_cpos, temp_z_cpos = get_cpos([temp_x_dpos, temp_y_dpos, temp_z_dpos],cell_param[0], cell_param[1], cell_param[2],1)
            # add_data = pd.DataFrame([elem, temp_x_cpos, temp_y_cpos, temp_z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
            # super_atoms_cpos = pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)
            # # c+1
            # temp_x_dpos,temp_y_dpos,temp_z_dpos = x_dpos,y_dpos,z_dpos + 1
            # temp_x_cpos, temp_y_cpos, temp_z_cpos = get_cpos([temp_x_dpos, temp_y_dpos, temp_z_dpos],cell_param[0], cell_param[1], cell_param[2],1)
            # add_data = pd.DataFrame([elem, temp_x_cpos, temp_y_cpos, temp_z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
            # super_atoms_cpos = pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)
            # # c-1
            # temp_x_dpos,temp_y_dpos,temp_z_dpos = x_dpos - 1,y_dpos,z_dpos - 1
            # temp_x_cpos, temp_y_cpos, temp_z_cpos = get_cpos([temp_x_dpos, temp_y_dpos, temp_z_dpos],cell_param[0], cell_param[1], cell_param[2],1)
            # add_data = pd.DataFrame([elem, temp_x_cpos, temp_y_cpos, temp_z_cpos, atom], index=['elem', 'x_cpos', 'y_cpos', 'z_cpos', 'atom_num'])
            # super_atoms_cpos = pd.concat([super_atoms_cpos, add_data.T], ignore_index=True)
    # print(super_atoms_cpos)
    return super_atoms_cpos

def all_H_X_dist(atoms_cpos:DataFrame, super_atoms_cpos:DataFrame)->DataFrame:
    """
    get a df which index is H_num, colum append dist of Li_num
    
    :return all_dist: output dist of H-X
    """
    # X_column = list(atoms_cpos[atoms_cpos.elem == 'Cl'].index)
    # X_column += list(atoms_cpos[atoms_cpos.elem == 'Br'].index)
    # X_column += list(atoms_cpos[atoms_cpos.elem == 'I'].index)
    X_column = list(atoms_cpos[atoms_cpos.elem == 'Li'].index)
    H_index = list(atoms_cpos[atoms_cpos.elem == 'H'].index)
    all_dist = pd.DataFrame({},index=H_index,columns=X_column)
    # print(X_column,H_index,all_dist)
    for H_num in tqdm(all_dist.index):
        for X_index in super_atoms_cpos.index:
            X_num = super_atoms_cpos.iloc[X_index]['atom_num']
            H_cpos = atoms_cpos.loc[H_num,['x_cpos','y_cpos','z_cpos']]
            X_cpos = super_atoms_cpos.loc[X_index,['x_cpos','y_cpos','z_cpos']]
            the_dist = dist(H_cpos,X_cpos)
            if all_dist.loc[H_num,X_num] is np.NaN or all_dist.loc[H_num,X_num] > the_dist:
                all_dist.loc[H_num,X_num] = the_dist
    return all_dist
    pass
def print_passed_dist(all_dist:DataFrame, threshold:float, is_print=True)->dict:
    """
    dist < threshold atoms
    :param is_print=True: 'Li1-H2'...
    :return ans: list of bonds passed
    """
    # passed_atoms = {}
    ans = {}
    for H_num in all_dist.index:
        for X_num in all_dist.columns:
            the_dist = all_dist.loc[H_num][X_num]
            if the_dist <= threshold:
                # if is_print:
                #     print(H_num+'-'+X_num,end=' ')
                ans[H_num+'-'+X_num] = the_dist
                # # add to passed_atoms
                # if H_num not in passed_atoms.keys():
                #     passed_atoms[H_num] = {X_num: the_dist}
                # else:
                #     passed_atoms[H_num][X_num] = the_dist
    if is_print:
        print(*ans.keys())
    return ans
    # return passed_atoms
    pass

def print_help():
    print('usage      : python find_Li_bond.py -dist 5 (-save)')
    print('   -h      : print help')
    print('   -dist n : atoms < the dist n')
    print('   -save f : save data as Li_bond_list in file f(like Li_bond_data.npz) ')
    pass


def main():
    if '-h' in argv:
        print_help()
        exit(0)
    elif '-dist' in argv:
        threshold = float(argv[argv.index('-dist')+1])
        cell_param, cont_df = read_contcar(file_name='CONTCAR')
        super_atoms_cpos = super_poscar(cell_param, cont_df)
        print('finding Li-H bond (dist < %f)' % threshold)
        all_dist = all_H_X_dist(cont_df, super_atoms_cpos)
        if '-save' in argv:  
            datafile = argv[argv.index('-save')+1]
            passed_atoms = print_passed_dist(all_dist,threshold,False) # list

            np.savez(datafile, list=passed_atoms)
                
            print('Li-H bond(list, len=%d) save as %s' % (len(passed_atoms), datafile))
        else:
            passed_atoms = print_passed_dist(all_dist,threshold,True)
        exit(0)
    else:
        print_help()
        exit(1)
    pass

if __name__ == '__main__':
    main()