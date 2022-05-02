#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : select_bcp_dat.py
@Time : 2022/03/29 19:38:28
@Auth : Ming 

@Vers : 1.1 # add dist check
@Desc : get bcp.dat file for plto_neb_barrier from bcp_result(by AIM_bcp.py)
@Usag : python select_bcp_dat.py atom_1-atom_2 atom_A(all bcp) ... (> this_bcp.dat)
'''

'''
# bcp.dat file:
total image 15 ! no print here
image 00 ! no print here
atom_1 atom_2 bcp (dist norm)
atom_1 atom_3 bcp (dist norm)
...
image 16 ! no print here
atom_1 atom_5 bcp ! no print here
...
'''

"""
print format:
atom_1 atom_2 bcp (dist norm)
atom_1 atom_3 bcp (dist norm)
"""

# here put the import lib
import os
import numpy as np

def get_CNH(H_num):
    """return CH_num or NH_num by H_num"""
    if H_num in ['H1','H17','H9']:
        return 'CH1'
    elif H_num in ['H33','H25','H41']:
        return 'NH1'
    elif H_num in ['H2','H18','H10']:
        return 'CH2'
    elif H_num in ['H34','H26','H42']:
        return 'NH2'
    elif H_num in ['H3','H19','H11']:
        return 'CH3'
    elif H_num in ['H35','H27','H43']:
        return 'NH3'
    elif H_num in ['H4','H20','H12']:
        return 'CH4'
    elif H_num in ['H36','H28','H44']:
        return 'NH4'
    elif H_num in ['H5','H21','H13']:
        return 'CH5'
    elif H_num in ['H37','H29','H45']:
        return 'NH5'
    elif H_num in ['H6','H22','H14']:
        return 'CH6'
    elif H_num in ['H38','H30','H46']:
        return 'NH6'
    elif H_num in ['H7','H23','H15']:
        return 'CH7'
    elif H_num in ['H39','H31','H47']:
        return 'NH7'
    elif H_num in ['H8','H24','H16']:
        return 'CH8'
    elif H_num in ['H40','H32','H48']:
        return 'NH8'
    
def get_MA(CNH_num):
    """return MA_num from CH_num or NH_num"""
    num = CNH_num.split('H')[-1] # str
    return 'MA'+num
    
    
    
def print_selected_bcp(data_file, interest_atom1, interest_atom2=None):
    atoms_passed = {} # key is npos for repeat check; value is [atom_with, density, distB]
    f = open(data_file)
    while True:
        line = f.readline()
        if 'find the bcp between ' + interest_atom1 in line:
            # find interest_atom
            atom_with = line.split()[-1]
            if ':' in atom_with:
                atom_with = atom_with.replace(':', '')
            # read density
            info_line = f.readline()
            density = info_line.split()[1]
            # tight check
            norm = float(info_line.split()[-1])
            distA_index = info_line.split().index('distA')
            distA = float(info_line.split()[distA_index+2])
            distB_index = info_line.split().index('distB')
            distB = float(info_line.split()[distB_index+2])
            if norm < 20 and (distA + distB) < 3: # 10
                # print(interest_atom, atom_with, density)
                npos_index = info_line.split().index('npos')
                npos = info_line.split()[npos_index+1:npos_index+1+3] # type is list
                npos = eval(npos[0]+npos[1]+npos[2])# type is tuple
                #repeat check
                if npos not in atoms_passed.keys():
                    atoms_passed[npos] = [atom_with, density, distB, norm]
                else:
                    # meet two atom_with use the same bcp, select the nearest one
                    if distB < atoms_passed[npos][2]:
                        atoms_passed[npos] = [atom_with, density, distB, norm]
        elif line == '':
            break
    # print
    if interest_atom2 == None:
        for value in atoms_passed.values():
            print(interest_atom1, value[0], value[1], str(value[2])+'A' ,value[3])
        return
    else:
        for value in atoms_passed.values():
            if interest_atom2 == value[0]:
                print(interest_atom1, value[0], value[1], str(value[2])+'A' ,value[3])
                return
        # cannot find interest_atom2
        return


def main():
    from sys import argv, exit
    
    def help_print():
        print('usage      : python select_bcp_dat.py atom_1-atom_2 atom_A(all bcp) ... (> this_bcp.dat) | python -file (bcp_data.npz)')
        print('   -file f : input file f to select atoms bcp interest, like H_bcp-data.npz from find_H_bond.py -dist 3 -save f &  AIM_bcp.py -file f')
        print('note       : must have bcp_result(AIM_bcp.py -normal > bcp_result)')
    if '-h' in argv:
        help_print()
        exit(0)
    elif '-file' in argv:
        # input
        if len(argv) >= 3:
            infile = argv[argv.index('-file')+1]
        elif len(argv) == 2:
            infile = 'bcp_data.npz'
        else:
            help_print()
            exit(1)
            
        if infile not in os.listdir():
            print('cannot find input file:', infile)
            exit(1)
        else:
            indata = np.load(infile,allow_pickle=True)
            
            bond_list = indata['list'].item() # dict
            bcp_ans = indata['ans'].item() # dict
            
            bcp_passed, MA_sum = {},{}
            npos_passed = []
            list_of_MA = ['CH'+str(x+1) for x in range(8)] + ['NH'+str(x+1) for x in range(8)] + ['MA'+str(x+1) for x in range(8)]
            for elem in list_of_MA:
                MA_sum[elem] = 0 # add CH1 CH2 NH3 MA4 ... to bcp_passed
            MA_sum['total'] = 0
                
            for bond in bond_list.keys():
                flag_passed = True
                if bond in bcp_ans.keys():
                    density, cpoint, npoint, distA, distB, norm = bcp_ans[bond]
                    # norm check 
                    if norm > 50:
                        flag_passed = False
                    # repeat check 
                    if npoint not in npos_passed:
                        pass
                    else: # meet two atom_with use the same bcp, select the nearest one # todo
                        # for key in bcp_passed.keys():
                        #     if npoint == bcp_passed[key]
                        pass
                    if flag_passed:
                        bcp_passed[bond] = density
                        atomA, atomB = bond.split('-')
                        H_num = atomA if 'H' in atomA else atomB
                        MA_sum[get_CNH(H_num)] += density
                        MA_sum[get_MA(get_CNH(H_num))] += density
                        MA_sum['total'] += density
                        npos_passed.append(npoint)
            # save
            print('select %d/%d bcp, add to %s as passed and sum' % (len(bcp_passed), len(bcp_ans), infile))
            np.savez(infile, list=bond_list, ans=bcp_ans, passed=bcp_passed, sum=MA_sum)
            exit(0)
                    
            
            
            
    elif len(argv) > 1:
        bcp_result_file = './bcp_result'
        for key in argv[1:]:
            if '-' in key: # atom_1-atom2
                atom1, atom2 = key.split('-')
                print_selected_bcp(bcp_result_file, atom1, atom2)
            else: # atom_1
                atom = key
                print_selected_bcp(bcp_result_file, atom, None)
        exit(0)
    else:
        print('input wrong, your input:',argv)
        help_print()
        exit(1)
    pass

if __name__ == '__main__':
    main()