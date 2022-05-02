#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : plot_data.py
@Time : 2022/05/01 10:20:19
@Auth : Ming 
@Vers : 1.0
@Desc : def plot for data_arrangement.ipynb
@Usag : import ./relax/plot_data.py
'''

# here put the import lib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter,BSPlotter,BSPlotterProjected,DosPlotter

plt.style.use(['science','no-latex'])


def plot_dos(data_file:str, title:str, save_file:str):
    """
    plot total DOS and PDOS
    :param data_file: './data/111-11-pos1/vasprun.xml'
    :param title: 'Li+@MASnCl3-pos1-DOS'
    "param save_file: './images/111-11-dos.png'
    """
    #read data
    pos_dos_vasprun = Vasprun(data_file)
    pos_dos_data = pos_dos_vasprun.complete_dos
    # plot
    pos_plt_dos = DosPlotter(stack=False, fig_size=(12,8))
    pos_plt_dos.add_dos('total dos', pos_dos_vasprun.tdos)
    pos_plt_dos.add_dos_dict(pos_dos_data.get_spd_dos())
    # pos_plt_dos.show(xlim=(-20,10),ylim=(0,200))
    pos_plt_dos.save_plot(save_file, img_format=u'png', xlim=(-20,10),ylim=(0,200), title=title)
    
def plot_ldos(data_file:str, atoms:list, title:str, save_file:str):
    """
    plot LDOS
    :param data_file: './data/111-11-pos1/vasprun.xml'
    :param atoms: ['Li1','H14','H22','H21']
    :param title: 'Li+@MASnCl3-pos1-LDOS'
    "param save_file: './images/111-11-ldos.png'
    """
    #read data
    pos_dos_vasprun = Vasprun(data_file)
    pos_dos_data = pos_dos_vasprun.complete_dos
    # plot
    pos_plt_ldos = DosPlotter(stack=False)
    pos_plt_ldos.add_dos_dict(pos_dos_data.get_atom_dos(atoms))
    # pos_plt_ldos.show(xlim=(-20,10),ylim=(0,0.3))
    pos_plt_ldos.save_plot(save_file, img_format=u'png', xlim=(-20,10),ylim=(0,0.3),title=title)
    
def plot_embedded_energy(pos_embedded_energy:list, title:str, save_file:str):
    """
    plot pos1, pos2, pos3 embedded energy
    :param pos_embedded_energy: [pos1_embedded_energy, pos2_embedded_energy, pos3_embedded_energy]
    :param title: 'Li+@MASnCl3 Li+ embedded energy'
    :param save_file: './images/111-pos-embedded-energy.png'
    """
    fig_pos_bar = plt.figure(dpi=120)
    ax_pos_bar = plt.axes()

    # pos_embedded_energy = [pos1_embedded_energy, pos2_embedded_energy, pos3_embedded_energy]
    ax_pos_bar.bar(range(3), pos_embedded_energy, width=0.5)
    for x,y in enumerate(pos_embedded_energy):
        plt.text(x,y-1,'%s' %round(y,2),ha='center')
    ax_pos_bar.set(xlabel='Li ion\'s position', ylabel='embedded energy/eV',xlim=(-0.5,2.5),ylim=(-12, 0),title=title)
    ax_pos_bar.set_xticks(range(3), ['pos1','pos2','pos3'])
    fig_pos_bar.show()
    fig_pos_bar.savefig(save_file)
    
def plot_one_neb_barrier(neb_dist:list, neb_energy:list, label:str, title:str, save_file:str):
    """
    plot one neb barrier
    :param neb_dist: [0.0, 2.946125, 5.899253, ... 37.756896]
    :param neb_energy: [0.0, 0.055123, ... 6e-06]
    :param label: 'NEB121'
    :param title: 'Li+@MASnCl3 NEB barrier'
    :param save_file: './images/111-121-barrier.png'
    """
    x_dist = np.array(neb_dist)
    y_energy = np.array(neb_energy)
    x_line = np.linspace(x_dist.min(), x_dist.max(), 1000)
    y_line = make_interp_spline(x_dist, y_energy)(x_line)

    neb_fig = plt.figure(dpi=120)
    neb_ax = plt.axes()
    neb_ax.scatter(x_dist, y_energy, c='k', label=label)
    neb_ax.plot(x_line, y_line, c='k')
    neb_ax.set(xlabel='dist/A', ylabel='energy/eV', title=title)

    neb_ax.legend()
    neb_fig.show()
    neb_fig.savefig(save_file)
    
def plot_3dir_neb_barrier(all_neb_dist:list, all_neb_energy:list, all_label:list, title:str, save_file:str):
    """
    plot one neb barrier
    :param all_neb_dist: [neb1_dist, neb2_dist, neb3_dist]
    :param all_neb_energy: [neb1_energy, neb2_energy, neb3_energy]
    :param all_label: ['NEB121','NEB131','NEB212']
    :param title: 'Li+@MASnCl3 NEB barrier'
    :param save_file: './images/111-all-barrier.png'
    """
    neb_fig = plt.figure(dpi=120)
    neb_ax = plt.axes()
    for i in range(3):
        x_dist = np.array(all_neb_dist[i])
        y_energy = np.array(all_neb_energy[i])
        x_line = np.linspace(x_dist.min(), x_dist.max(), 1000)
        y_line = make_interp_spline(x_dist, y_energy)(x_line)
        neb_ax.scatter(x_dist, y_energy, label=all_label[i])
        neb_ax.plot(x_line, y_line)
    neb_ax.set(xlabel='dist/A', ylabel='energy/eV', title='Li+@MASnBr3 NEB barrier')

    neb_ax.legend()
    neb_fig.show()
    neb_fig.savefig(save_file)

def main():
    
    pass

if __name__ == '__main__':
    main()