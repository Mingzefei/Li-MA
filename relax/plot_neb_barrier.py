#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : plot_neb_barrier.py
@Time : 2022/03/15 14:40:53
@Auth : Ming 
@Vers : 1.1 # add print dist and energy
@Desc : plot neb barrier
@Usag : python plot_neb_barrier.py data_file(made by nebbarrier.pl) save_fig_name
'''

# here put the import lib
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

plt.style.use(['science','no-latex'])

def read_data(data_file):
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

def plot_one_barrier(dist_np, energy_np, title):
    """
    plot one barrier curve by inter_spline method
    :param dist_np, energy_np: dist and energy in np form
    :param title: fig's title
    """
    all_images_num = len(dist_np)
    x_dist = dist_np
    y_energy = energy_np
    max_index, min_index = y_energy.argmax(), y_energy.argmin()
    x_line = np.linspace(x_dist.min(), x_dist.max(), 400)
    y_line = make_interp_spline(x_dist, y_energy)(x_line)
    
    # scatter
    plt.scatter(x_dist, y_energy, c='black')
    # smooth line
    plt.plot(x_line, y_line, c='black', label=title)
    
    # mark the min and max energy
    # plt.text(x_dist[min_index], y_energy.min()-0.005, 'image %02d: %.3f eV' % (min_index,y_energy.min()), fontsize=6, ha='center')
    # plt.text(x_dist[max_index], y_energy.max()+0.005, 'image %02d: %.3f eV' % (max_index,y_energy.max()), fontsize=6, ha='center')
    
    # title and label
    # plt.title(title)
    plt.legend()
    plt.xlabel('dist/A')
    plt.ylabel('energy/eV')
    
    # plt.show()


def main():
    
    from sys import argv, exit
    
    def help_print():
        print('usage      : python plot_neb_barrier.py data_file(made by nebbarrier.pl) save_fig_name')
    
    if '-h' in argv:
        help_print()
        exit(0)
    elif len(argv) == 3:
        python_script, data_file, save_fig_name = argv
        dist_np, energy_np = read_data(data_file)
        
        print('dist =', list(dist_np))
        print('energy =', list(energy_np))
        
        plt.figure(dpi=100)
        plot_one_barrier(dist_np, energy_np, save_fig_name)
        
        plt.savefig('./'+save_fig_name+'.jpg', bbox_inches='tight')
        # plt.show()
        exit(0)
    else:
        print('input wrong, your input:',argv)
        help_print()
        exit(1)

if __name__ == '__main__':
    main()