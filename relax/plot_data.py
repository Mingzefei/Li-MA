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

import io_data

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
    
    print(pos_dos_data.get_gap())
    
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
    
def plot_embedded_energy_1pos(pos_embedded_energy:list, title:str, save_file:str):
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
    
def plot_neb_barrier_1neb(neb_dist:list, neb_energy:list, label:str, title:str, save_file:str):
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
    
def plot_neb_barrier_3dir(all_neb_dist:list, all_neb_energy:list, all_label:list, title:str, save_file:str,xlim=(-5,50),ylim=(-0.1,0.6)):
    """
    plot one neb barrier
    :param all_neb_dist: [neb1_dist, neb2_dist, neb3_dist]
    :param all_neb_energy: [neb1_energy, neb2_energy, neb3_energy]
    :param all_label: ['NEB121','NEB131','NEB212']
    :param title: 'Li+@MASnCl3 NEB barrier'
    :param save_file: './images/111-all-barrier.png'
    """
    neb_fig = plt.figure(figsize=(8,4))
    neb_ax = plt.axes()
    for i in range(len(all_neb_dist)):
        x_dist = np.array(all_neb_dist[i])
        y_energy = np.array(all_neb_energy[i])
        x_line = np.linspace(x_dist.min(), x_dist.max(), 1000)
        y_line = make_interp_spline(x_dist, y_energy)(x_line)
        neb_ax.scatter(x_dist, y_energy, label=all_label[i])
        neb_ax.plot(x_line, y_line)
    neb_ax.set(xlim=(-5,50),ylim=(-0.1,0.6),xlabel='dist/A', ylabel='energy/eV', title=title)

    neb_ax.legend()
    neb_fig.show()
    neb_fig.savefig(save_file)
    
def plot_neb_barrier_4sys(all_neb_dist:list, all_neb_energy:list, all_label:list, title:str, save_file:str,xlim=(-5,70),ylim=(-0.1,0.6)):
    """
    plot one neb barrier
    :param all_neb_dist: [data_111_neb1['dist'],data_112_neb1['dist'],data_113_neb1['dist'],data_123_neb1['dist']]
    :param all_neb_energy: [data_111_neb1['energy'],data_112_neb1['energy'],data_113_neb1['energy'],data_123_neb1['energy']]
    :param all_label: ['MASnCl3','MASnBr3','MASnI3','MAPbI3']
    :param title: Li+@MABX3(B=Sn,Pb;X=Cl,Br,I) NEB121 barrier'
    :param save_file: './images/contrast-E-neb121-barrier.png'
    """
    neb_fig = plt.figure(figsize=(8,4))
    neb_ax = plt.axes()
    for i in range(len(all_label)):
        x_dist = np.array(all_neb_dist[i])
        y_energy = np.array(all_neb_energy[i])
        x_line = np.linspace(x_dist.min(), x_dist.max(), 1000)
        y_line = make_interp_spline(x_dist, y_energy)(x_line)
        neb_ax.scatter(x_dist, y_energy, label=all_label[i])
        neb_ax.plot(x_line, y_line)
    neb_ax.set(xlim=xlim,ylim=ylim,xlabel='dist/A', ylabel='energy/eV', title=title)

    neb_ax.legend()
    neb_fig.show()
    neb_fig.savefig(save_file)

    
def plot_H_bcp_1pos(data_file:str,title:str,save_file:str):
    """
    plot H_bcp bar of 8 MA with CH and NH
    :param datafile: './data/111-11-pos1-E403/H_bcp_data.npz'
    :param title: 'Li@MASnCl3-pos1-MA-H_bond-bcp'
    :param savefile: './images/111-11-E403-H-bcp.png'
    """

    bcp_data = np.load(data_file,allow_pickle=True)
    H_bcp = bcp_data['sum'].item()

    # print('CH-6',H_bcp['CH6'])
    # print('NH-6',H_bcp['NH6'])
    # print('MA-6',H_bcp['MA6'])
    # print('CH-4',H_bcp['CH4'])
    # print('NH-4',H_bcp['NH4'])
    # print('MA-4',H_bcp['MA4'])
    # print('sum of MA', sum(map(lambda x: H_bcp[x], ['MA1','MA2','MA3','MA4','MA5','MA6','MA7','MA8'])))

    MA_num = ["MA1", "MA2", "MA3", "MA4", "MA5", "MA6", "MA7", "MA8"]
    CH_H_bcp = list(map(lambda x: H_bcp[x], ['CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8']))
    NH_H_bcp = list(map(lambda x: H_bcp[x], ['NH1','NH2','NH3','NH4','NH5','NH6','NH7','NH8']))

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(MA_num, CH_H_bcp, label="CH3")
    ax.bar(MA_num, NH_H_bcp, bottom=CH_H_bcp, label="NH3")

    # ax.set(ylim=(0,0.15),xlabel='MA index',ylabel='bcp/a.u.',title=title)
    ax.set(ylim=(0,0.15),xlabel='MA index',ylabel='bcp/a.u.',title=title+'(total: '+str(H_bcp['total'])[0:6]+' a.u.)')

    ax.legend()
    fig.show()
    fig.savefig(save_file)
    
def plot_neb_H_bcp_1neb(data_dir:str,title:str,save_file:str,smooth_line=False,use_dist=False,ylim='auto'):
    """
    plot one neb H bcp sum
    :param data_dir: './data/111-121-neb1'
    :param title: 'Li+@MASnCl3 NEB121 H bond bcp'
    :param save_file: './images/111-121-H-bcp-sum.png'
    :param smooth_line: use smooth line
    :param use_dist: use dist as x
    :param ylim: ylim
    """
    
    H_bcp_total = io_data.read_neb_H_bcp(data_dir=data_dir)
    dist_x, _ = np.array(io_data.read_neb_barrier(data_file=data_dir+'/neb.dat'))
    image_x = np.array((range(len(dist_x))))
    bcp_y = H_bcp_total
    if use_dist:
        x = dist_x
        xlabel = 'dist/A'
    else:
        x = image_x
        xlabel = 'images'
    
    neb_fig = plt.figure(dpi=120) # figsize=(14,7)
    neb_ax = plt.axes()
    if smooth_line:
        x_line = np.linspace(x.min(), x.max(), 1000)
        y_line = make_interp_spline(x, bcp_y)(x_line)

        neb_ax.scatter(x, bcp_y, c='k', label='H bond total')
        neb_ax.plot(x_line, y_line, c='k')

    else:
        neb_ax.plot(x, bcp_y, '-o', linewidth=2, label='H bond total')

    if ylim == 'auto' or ylim == 'Auto':
        neb_ax.set(xlabel=xlabel, ylabel='bcp/a.u.', title=title)
    else:
        neb_ax.set(ylim=ylim,xlabel='images', ylabel='bcp/a.u.', title=title)
    
    neb_ax.legend()
    neb_fig.show()
    neb_fig.savefig(save_file)
    
def plot_neb_Li_bcp_1neb(data_dir:str,title:str,save_file:str,smooth_line=False,use_dist=False,ylim='auto'):
    """
    plot one neb H bcp sum
    :param data_dir: './data/111-121-neb1'
    :param title: 'Li+@MASnCl3 NEB121 Li bond bcp'
    :param save_file: './images/111-121-Li-bcp-sum.png'
    :param smooth_line: use smooth line
    :param use_dist: use dist as x
    :param ylim: ylim
    """
    
    Li_bcp_total = io_data.read_neb_Li_bcp(data_dir=data_dir)
    dist_x, _ = np.array(io_data.read_neb_barrier(data_file=data_dir+'/neb.dat'))
    image_x = np.array((range(len(dist_x))))
    bcp_y = Li_bcp_total
    if use_dist:
        x = dist_x
        xlabel = 'dist/A'
    else:
        x = image_x
        xlabel = 'images'
    
    neb_fig = plt.figure(dpi=120) # figsize=(14,7)
    neb_ax = plt.axes()
    if smooth_line:
        x_line = np.linspace(x.min(), x.max(), 1000)
        y_line = make_interp_spline(x, bcp_y)(x_line)

        neb_ax.scatter(x, bcp_y, c='k', label='Li bond total')
        neb_ax.plot(x_line, y_line, c='k')

    else:
        neb_ax.plot(x, bcp_y, '-o', linewidth=2, label='Li bond total')

    if ylim == 'auto' or ylim == 'Auto':
        neb_ax.set(xlabel=xlabel, ylabel='bcp/a.u.', title=title)
    else:
        neb_ax.set(ylim=ylim,xlabel='images', ylabel='bcp/a.u.', title=title)
    
    neb_ax.legend()
    neb_fig.show()
    neb_fig.savefig(save_file)

def plot_neb_H_Li_bcp_1neb(data_dir:str,title:str,save_file:str,smooth_line=False,use_dist=False,ylim=(0,1)):
    """
    plot one neb H bcp sum
    :param data_dir: './data/111-121-neb1'
    :param title: 'Li+@MASnCl3 NEB121 H and Li bond bcp'
    :param save_file: './images/111-121-H-Li-bcp-sum.png'
    :param smooth_line: use smooth line
    :param use_dist: use dist as x
    :param ylim: ylim
    """
    H_bcp_total = np.array(io_data.read_neb_H_bcp(data_dir=data_dir))
    Li_bcp_total = np.array(io_data.read_neb_Li_bcp(data_dir=data_dir))
    add_up = H_bcp_total + Li_bcp_total
    dist_x, energy_y = np.array(io_data.read_neb_barrier(data_file=data_dir+'/neb.dat'))
    image_x = np.array((range(len(dist_x))))
    
    bcp_y = [H_bcp_total,Li_bcp_total,add_up]
    if use_dist:
        x = dist_x
        xlabel = 'dist/A'
    else:
        x = image_x
        xlabel = 'images'
    label = ['H bond', 'Li bond', 'add up']
    
    neb_fig = plt.figure(dpi=120) # figsize=(14,7)
    neb_ax = plt.axes()
    for i in range(len(bcp_y)):
        if smooth_line:
            x_line = np.linspace(x.min(), x.max(), 1000)
            y_line = make_interp_spline(x, bcp_y[i])(x_line)

            neb_ax.scatter(x, bcp_y[i], c='k', label=label[i])
            neb_ax.plot(x_line, y_line, c='k')

        else:
            neb_ax.plot(x, bcp_y[i], '-o', linewidth=2, label=label[i])

    neb_ax.set(ylim=ylim,xlabel=xlabel, ylabel='bcp/a.u.', title=title)
    
    neb_ax.legend()
    neb_fig.show()
    neb_fig.savefig(save_file)
    


def main():
    
    pass

if __name__ == '__main__':
    main()