#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : kcalmol2ev.py
@Time : 2022/05/18 17:51:43
@Auth : Ming 
@Vers : 1.0
@Desc : trans energy from kcal/mol to eV/one
@Usag : python kcalmol2ev.py num
'''

# here put the import lib
import scipy.constants as C

def kcalmol2ev(energy_kcalmol:float):
    cal2j = 4.1858
    NA = C.constants.Avogadro
    e = C.constants.e
    return energy_kcalmol * 1000 * cal2j / (e * NA)

def main():
    from sys import argv, exit
    
    def help_print():
        print('usage    :python kcalmol2ev.py energy(in kcal per mol)')
        
    if '-h' in argv:
        help_print()
        exit(0)
    elif len(argv) >= 2:
        for energy in argv[1:]:
            energy = float(energy)
            print('%.4f' % kcalmol2ev(energy))
    else:
        print('input wrong, your input:', argv)
        help_print()
        exit(1)
    pass

if __name__ == '__main__':
    main()