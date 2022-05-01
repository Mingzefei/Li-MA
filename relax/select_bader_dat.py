#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : select_bader_dat.py
@Time : 2022/03/29 22:49:40
@Auth : Ming 
@Vers : 1.1 // fix get_zval
@Desc : get valence from ACF.dat & OUTCAR & CONTCAR and print valence of atoms interested
@Usag : python select_bader_dat.py atom_1 elem_2 ...
'''

"""
print format:
atom_1 valence
atom_2 valence
"""

# here put the import lib
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
import os

# def get_zval(elem)->int:
#     """
#     return the elem(str)'s zval
#     """
    # atoms_zval = {
    #     'H'  : 1,
    #     'Li' : 3,
    #     'Be' : 4,
    #     'B'  : 5,
    #     'C'  : 6,
    #     'N'  : 7,
    #     'O'  : 8,
    #     'F'  : 9,
    #     'Na' : 11,
    #     'Mg' : 12,
    #     'Al' : 13,
    #     'Si' : 14,
    #     'P'  : 15,
    #     'S'  : 16,
    #     'Cl' : 17,
    #     'K'  : 19,
    #     'Ca' : 20,
    #     'Sc' : 21,
    #     'Ti' : 22,
    #     'V'  : 23,
    #     'Cr' : 24,
    #     'Mn' : 25,
    #     'Fe' : 26,
    #     'Co' : 27,
    #     'Ni' : 28,
    #     'Cu' : 29,
    #     'Zn' : 30,
    #     'Ga' : 31,
    #     'Ge' : 32,
    #     'As' : 33,
    #     'Se' : 34,
    #     'Br' : 35,
    #     'Sn' : 50,
    #     'I'  : 53,
    #     'Pb' : 82,
    # }
    # if elem in atoms_zval.keys():
    #     return atoms_zval[elem]
    # else:
    #     print('cannot find elem %s, you need add it in select_bader_dat.py file')
    #     return 9999

    
    

def read_contar(file_name='CONTCAR'):
    """
    to get atoms information
    :return all_atoms: dataframe of atoms in contar which colum is ['elem','zval']; index is elemA1, elemA2, ...
    """
    # read
    file = open(file_name)
    description = file.readline() # line 1: description
    scale_factor = float(file.readline()) # line 2: universal sacling parameters
    x_vector = file.readline() # line 3: lattice vector x
    y_vector = file.readline() # line 4: lattice vector y
    z_vector = file.readline() # line 5: lattice vector z
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
    
    atoms_index = [] # elemA1, elemA2, ...
    all_atoms = [] # 
    all_zval = os.popen('grep \'ZVAL\' OUTCAR | tail -n 1').readline().split() # get zval from OUTCAR
    all_zval = list(map(float, all_zval[2:]))
    for index,atom_elem in enumerate(atoms_elem):
        for atom_num in range(atoms_num[index]):
            atoms_index.append(atom_elem + str(atom_num+1))
            all_atoms.append([atom_elem, all_zval[index]])
    
    all_atoms = pd.DataFrame(all_atoms, index=atoms_index, columns=['elem','zval'])
    return all_atoms
    pass
def read_acf(file_name='ACF.dat')->list:
    """
    read data from ACF.dat
    :return bader_chg: list of bader_chg all atoms
    """
    file = open(file_name)
    columns = file.readline().split()
    file.readline() # tab line '-----------'
    
    acf = []
    while True:
        line = file.readline()
        if '--' not in line: # last tab line '--------'
            acf.append(float(line.split()[4]))
        else:
            break
    return acf

def main():
    from sys import argv, exit
    
    def help_print():
        print('usage      : python select_bader_dat.py atom_1 elem_2 ... | -all(get valence.npz)')
        print('note       : must have OUTCAR, CONTCAR and ACF.dat(chgsum.pl AECCAR0 AECCAR2 & bader CHGCAR -ref CHGCAR_sum)')
    if '-h' in argv:
        help_print()
        exit(0)
    elif '-all' in argv:
        # get valence
        all_atoms = read_contar()
        all_atoms['acf_chg'] = read_acf()
        all_atoms['valence'] = all_atoms['zval'] - all_atoms['acf_chg']   
        
        data = dict(all_atoms['valence'])

        data['CH1'] = data['H1']+data['H17']+data['H9']+data['C1']
        data['NH1'] = data['H33']+data['H25']+data['H41']+data['N1']
        data['MA1'] = data['CH1']+data['NH1']

        data['CH2'] = data['H2']+data['H18']+data['H10']+data['C2']
        data['NH2'] = data['H34']+data['H26']+data['H42']+data['N2']
        data['MA2'] = data['CH2']+data['NH2']

        data['CH3'] = data['H3']+data['H19']+data['H11']+data['C3']
        data['NH3'] = data['H35']+data['H27']+data['H43']+data['N3']
        data['MA3'] = data['CH3']+data['NH3']

        data['CH4'] = data['H4']+data['H20']+data['H12']+data['C4']
        data['NH4'] = data['H36']+data['H28']+data['H44']+data['N4']
        data['MA4'] = data['CH4']+data['NH4']

        data['CH5'] = data['H4']+data['H21']+data['H13']+data['C5']
        data['NH5'] = data['H37']+data['H29']+data['H45']+data['N5']
        data['MA5'] = data['CH5']+data['NH5']

        data['CH6'] = data['H6']+data['H22']+data['H14']+data['C6']
        data['NH6'] = data['H38']+data['H30']+data['H46']+data['N6']
        data['MA6'] = data['CH6']+data['NH6']

        data['CH7'] = data['H7']+data['H23']+data['H15']+data['C7']
        data['NH7'] = data['H39']+data['H31']+data['H47']+data['N7']
        data['MA7'] = data['CH7']+data['NH7']

        data['CH8'] = data['H8']+data['H24']+data['H16']+data['C8']
        data['NH8'] = data['H40']+data['H32']+data['H48']+data['N8']
        data['MA8'] = data['CH8']+data['NH8']

        np.save('valence', data)
        print('all data(dict) save as valence.npy')
            
        exit(0)
    elif len(argv) > 1:
        # get valence
        all_atoms = read_contar()
        all_atoms['acf_chg'] = read_acf()
        all_atoms['valence'] = all_atoms['zval'] - all_atoms['acf_chg']
        
        
        atoms_interested = argv[1:]
        for atom in atoms_interested:
            if atom in all_atoms.index:
                print(atom, all_atoms.loc[atom,'valence'])
            elif atom in list(all_atoms['elem']):
                atoms = all_atoms.loc[all_atoms.elem == atom, ['valence']]
                for index in atoms.index:
                    print(index, float(atoms.loc[index]))
            else:
                print(atom, 'cannot find in CONTCAR')

        exit(0)
    else:
        print('input wrong, your input:',argv)
        help_print()
        exit(1)


if __name__ == '__main__':
    main()