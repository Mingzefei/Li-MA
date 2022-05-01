#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : plot_neb_barrier_bader.py
@Time : 2022/03/30 09:35:47
@Auth : Ming 
@Vers : 1.1 # add print
@Desc : plot neb's barrier and bader valance which has two Y axises and X axis(dist)
@Usag : python plot_neb_barrier_bader.py neb.dat(barrier data) valence.dat(bader valace data) save_fig_name
'''

'''
# bcp.dat file:
total image 15
image 00
atom_1 valence
atom_2 valence
...
image 16
atom_1 valence
...
'''

# here put the import lib
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

plt.style.use(['science','no-latex'])

def read_barrier_data(data_file):
    """
    read data from neb barrier data_file
    :param data_file: data
    :return dist_np, energy_np: dist and energy in np form
    """
    dist, energy = [], []
    f = open(data_file)
    data = f.readlines()
    for image_data in data:
        temp = image_data.split()
        dist.append(float(temp[1]))
        energy.append(float(temp[2]))
    return np.array(dist), np.array(energy)

def read_valence_data(data_file)->dict:
    """
    read data from valence data_file
    :para data_file: data
    :return valence_dict: dict of chosed atom, like {'atom1':np.array(valence_each_image), ...}
    """
    valence_dict = {}
    f = open(data_file)
    data = f.readlines()
    # total image
    if 'total image' in data[0]:
        total_image = int(data[0].split()[-1])
    else:
        print('cannot find total image for %s' % data_file)
        print('need \'total image 12\' in the first line of file')
        return
    for line in data[1:]:
        if 'image' in line:
            this_image = int(line.split()[-1])
        else:
            atom, valence = line.split()[0:2]
            valence = float(valence)
            this_key = atom
            
            if this_key not in valence_dict.keys():
                valence_dict[this_key] = np.zeros(total_image)
            
            valence_dict[this_key][this_image] = valence
            
    return valence_dict

def plot_one_fig(dist_np, energy_np, valence_dict, title):
    """
    plot one figure, which barrier curve and valence curve by inter_spline method
    :param title: fig's title
    """
    total_image = len(dist_np)
    x_dist = dist_np
    y_left = energy_np # left y
    y_right = valence_dict
    
    x_line = np.linspace(x_dist.min(), x_dist.max(), 500)
    
    fig = plt.figure(figsize=(8,4))
    # y_left energy
    y_left_line = make_interp_spline(x_dist, y_left)(x_line)
    ax1 = fig.add_subplot(111)
    ax1.plot(x_line, y_left_line, c='black', label='energy')
    ax1.scatter(x_dist, y_left, c='black')
    ax1.set_ylabel('energy/eV')
    ax1.legend(loc=2)
    
    # y_right bcp
    ax2 = ax1.twinx() # use the same x
    for key, value in y_right.items():
        # value_line = make_interp_spline(x_dist, value)(x_line)
        # ax2.plot(x_line, value_line, label=key)
        # ax2.scatter(x_dist, value)
        ax2.plot(x_dist, value, '-', label=key)
    ax2.set_ylabel('bader\'s valence/e')
    ax2.legend(loc=1)
    
    ax1.set_xlabel('distance/A')
    
    plt.title(title)
    # plt.show()

def main():
    from sys import argv, exit
    
    def help_print():
        print('usage      : python plot_neb_barrier_bader.py neb.dat(barrier data) valence.dat(bader valace data) save_fig_name')
    
    if '-h' in argv:
        help_print()
        exit(0)
    elif len(argv) == 4:
        python_script, barrier_file, bcp_file, save_fig_name = argv
        dist_np, energy_np = read_barrier_data(barrier_file)
        valence_dist = read_valence_data(bcp_file)
        
        print('dist =', list(dist_np))
        print('energy =', list(energy_np))
        print('charge =', valence_dist)
        plot_one_fig(dist_np, energy_np, valence_dist, save_fig_name)
        
        plt.savefig('./'+save_fig_name+'.png', bbox_inches='tight')
        # plt.show()
        exit(0)
    else:
        print('input wrong, your input:',argv)
        help_print()
        exit(1)
    pass

if __name__ == '__main__':
    main()