# jobs have done

--------

@File    :   have_done.md
@Time    :   2022/03/08 15:30:25
@Auth    :   Ming(<3057761608@qq.com>)
@Vers    :   0.1
@Desc    :   Li-MA 已完成任务
@Refe    :   url1; url2

--------

## 111-MASnCl3-Li的迁移

### MASnCl3_opt
- INCAR 参数
  - 均使用范德华修正 IVDW=11
  - ENCUT=500,EDIFF=1E-5,EDIFG=-0.01
  - PREC=A,ISMEAR=0,SIGMA=0.10
- 理想的POSCAR(01/1-MASnCl3/2super/bu_ISIF3)
  - -441.84588321 eV
  - MA取向一致，[011] 
  - 11.11568, 11.43881, 11.52084 A
  - 86.7325, 89.5966, 90.2868 degree
- POSCAR from E402/3-2c_02 without Li+(01/1-MASnCl3/2super/bu_32c02ISIF3)
  - -442.01551540 eV
  - MA存在[011]和[01-1]两种取向，且交替出现
  - 11.11530, 11.43800, 11.51986 A
  - 86.7335, 89.5949, 90.2900 degree
- POSCAR reflect(01/1-MASnCl3/2super_reflect/bu_opt3)
  - -442.13734118 eV
  - MA取向混乱，但基本同族<110>
  - 11.44991, 11.51821, 11.17014 A (此处未和上面一一对应)
  - 90.0985, 88.4462, 87.4658 degree
### MASnCl3-Li+_opt
- INCAR 参数
  - 均使用范德华修正 IVDW=11
  - ENCUT=500,EDIFF=1E-5,EDIFG=-0.01
  - PREC=A,ISMEAR=0,SIGMA=0.10
- pos1(理想poscar，3/4,1/4,2/4)(01/1-MASnCl3/Li-2super-E402/pos1/bu_opt)
  - -447.44199364 eV
  - Li+ 上方的 MA 取向由 [011] 变为 [010]
  - ISIF=2
  - bcp
- pos1_eq(理想poscar，3/4,3/4,2/4)(01/1-MASnCl3/Li-2super-E402/pos1_eq)
  - -447.48399818 eV (与 pos1 相差大约 0.04 eV)
  - Li+ 上方的 MA 取向由 [011] 变为 [010]
  - ISIF=2
  - cdd
  - bcp
  - bader 
- **pos1_1-2c03**(NEB_1-2c03，3/4,1/4,2/4)(01/1-MASnCl3/Li-2super-E402/NEB_1-2c/test_03/opt2)
  - -447.72212813 eV
- **pos1_eq_here**(**pos1_1-2c03**, 3/4,3/4,2/4)(01/1-MASnCl3/Li-2super-E402/pos1_eq_here)
  - -447.72212171 eV(较 pos1_eq 更低)
  - 正八面体旋转严重
  - ISIF=2
  - bcp
  - bader
- **pos1_eqeq_here**(**pan pos1_eq_here/contcar**, 1/4,1/4,2/4)(01/1-MASnCl3/Li-2super-E402/pos1_eqeq_here)
  - -447.72212348 eV(与 pos1_eq_here 一致)
  - bader
- pos2(3/4,2/4,3/4)(01/1-MASnCl3/Li-2super-E402/pos2)
  - ideal poscar: -447.55608033 eV (opt2)
  - diff=1e-6, ediffg=-0.01, opt2_contcar: -447.61270183 eV (check2)
  - 能量差异过大
- **pos2_3-2c10**(NEB_3-2c10, 3/4,2/4,3/4)(01/1-MASnCl3/Li-2super-E402/NEB_3-2c/test_10/opt)
  - -447.65485865 eV
  - bcp
- pos2_eq(ideal poscar, 3/4,2/4,1/4)(01/1-MASnCl3/Li-2super-E402/pos2_eq)
  - -447.56666865 eV
- **pos2_eq_here**(**pan 3-2c_10**, 3/4,2/4,1/4)(01/1-MASnCl3/Li-2super-E402/pos2_eq_here)
  - -447.65485615 eV
  - cdd
  - bcp
  - bader
- pos3(2/4,1/4,3/4)(01/1-MASnCl3/Li-2super-E402/pos3)
  - ideal poscar: -447.41835993 eV
  - diff=1e-6, ediffg=-0.01, opt2_contcar: -447.41837459 eV 
- pos3_eq(2/4,1/4,1/4)(01/1-MASnCl3/Li-2super-E402/pos3_eq)\
  - -447.41931544 eV
  - cdd
  - bcp
  - bader
- **pos3_1-308**(NEB_1-308, 2/4,1/4,3/4)(01/1-MASnCl3/Li-2super-E402/NEB_1-3/test_08)
  - -447.64313418 eV
- **NOTE(0311): 重要的 pos 在 01/1-MASnCl3/Li-2super-E402/12-pos_used**
### MASnCl3-Li+_neb2
- between two different pos 
- most of them used for find aim pos 
- wd: 01/1-MASnCl3/Li-2super-E402/2-NEB2
### MASnCl3-Li+_neb3
- between posA-posB-posA_eq
- main NEB
- wd: 01/1-MASnCl3/Li-2super-E402/3-NEB3
- param
  - LCLIMB=T, ICHAIN=0, IBRION=3, POTIM=0, IOPT=1, SPRING=-5
  - normal: EDIFF=1e-5, EDIFFG=-0.05
  - accurate: EDIFF=1e-6, EDIFFG=-0.03
- 121_NEB
  - pos1_12c03 -> pos2_12c12 -> pos1_eq_here (b 方向)
  - barrier: 0.2540 eV
  - ![](./images/2022-03-17-11-41-19.png)
  - cdd 02 03 04 05 08 11 12
  - dos 02 03 04 05 08 11 12 
  - bcp 02 03 04 05 08 11 12
- 131_NEB
  - pos1_12c03 -> pos3_1308 -> pos1_eqeq_here (-a 方向)
  - barrier: 0.4754 eV
  - ![](./images/2022-03-17-11-45-07.png)
  - cdd 02 05 06 08 10
  - dos 02 05 06 08 10 
  - bcp 02 05 06 08 10
- 212n_NEB(./217contcar)
  - pos2_32c10 -> pos1_eq -> pos2_eq_here (-c 方向，接近 CH3)
  - barrier: 0.2852 eV
  - ![](./images/2022-03-17-11-46-32.png)
  - cdd 05 10 12
  - dos 05 10 12
  - bcp {01..15}
- ~~212_NEB~~stop
  - pos2_32c10 -> pos1_12c03 -> pos2_eq_here (-c 方向，接近 NH3)
  - barrier (较 212n 过大 )

## 112-MASnBr3-Li的迁移

### MASnBr3_opt
- INCAR 参数
  - 均使用范德华修正 IVDW=11
  - ENCUT=500,EDIFF=1E-5,EDIFG=-0.01
  - PREC=A,ISMEAR=0,SIGMA=0.10
- 理想的POSCAR(01/112-MASnBr3/2super/bu_384)
  - -429.44333762 eV
  - 11.62841, 11.80050, 11.91464 A
  - 86.0781, 89.7301, 90.3914 degree

### MASnBr3-Li+_opt
- INCAR 参数
  - 均使用范德华修正 IVDW=11
  - ENCUT=500,EDIFF=1E-5,EDIFG=-0.01
  - PREC=A,ISMEAR=0,SIGMA=0.10
- pos1(111_pos_1-2c03, 3/4,1/4,2/4)
  - -434.75308335 eV
  - bcp
- pos1_eq(here, 3/4,3/4,2/4)
  - -434.75308739 eV
- pos1_eqeq(here, 1/4,1/4,2/4)
  - -434.75308738 eV
- pos2(3/4,2/4,3/4)
  - -434.71087581 eV
  - bcp
- pos2_eq(here, 3/4,2/4,1/4)
  - -434.71082008 eV
- pos3(2/4,1/4/,3/4)
  - -434.74032798 eV

### MASnBr3-Li+_neb3

- 212n_NEB ==redo==
  - 21-pos2 -> 11-po1 -> 22-pos2_eq (-c 方向, 接近 CH3)
  - barrier: 0.2309 eV
  - ![](./images/2022-03-25-14-22-48.png)
  - failed 
    - barrier: 0.0857 eV(最高处) -0.0860 eV(最低处)
    - ![](./images/2022-03-17-11-50-44.png)
  - bcp {01..15}
- 121_NEB
  - 11-pos1 -> 21-pos2 -> 12-pos1_eq
  - based on 111-121_NEB
  - barrier: 0.1848 eV
  - ![](./images/2022-03-25-10-15-54.png)
  - failed
    - barrier: 0.1121 eV(最高处) -0.0068 eV(最低处)
    - ![](./images/2022-03-17-11-48-51.png)
- 131_NEB
  - 11-pos1 -> 31-pos3 -> 13-pos1_eqeq
  - based on 111-131_NEB
  - barrier: 0.3864 eV
  - ![](./images/2022-03-24-23-25-57.png)

## 113-MASnI3-Li的迁移

### MASnI3_opt
- INCAR 参数
  - 均使用范德华修正 IVDW=11
  - ENCUT=500,EDIFF=1E-5,EDIFG=-0.01
  - PREC=A,ISMEAR=0,SIGMA=0.10
- 理想的POSCAR(01/113-MASnI3/2super/bu_384)
  - -416.09175303 eV
  - 12.38372, 12.54657, 12.58601 A
  - 87.3511, 89.7223, 90.2875 degree

### MASnI3-Li+_opt
- INCAR 参数
  - 均使用范德华修正 IVDW=11
  - ENCUT=500,EDIFF=1E-5,EDIFG=-0.01
  - PREC=A,ISMEAR=0,SIGMA=0.10
- pos1(111_pos_1-2c03, 3/4,1/4,2/4)
  - -422.17939748 eV
- pos1_eq(here, 3/4,3/4,2/4)
  - -422.17938491 eV
- pos1_eqeq(here, 1/4,1/4,2/4)
  - -422.17938492 eV
- pos2(3/4,2/4,3/4)
  - -422.20185290 eV
- pos2_eq(3/4,2/4,1/4)
  - -422.20178949 eV
  - cdd, bcp, bader
- pos3(2/4,1/4,3/4)
  - -422.19028607 eV

### MASnI3-Li+_neb3

- 212n_NEB
  - 21_pos2 -> 11_po1 -> 22_pos2_eq (-c 方向, 接近 CH3)
  - barrier: 0.3356 eV(最高处) -0.0096 eV(最低处)
  - ![](./images/2022-03-17-11-52-29.png)
  - bcp {01..15}
- 121_NEB
  - 11-pos1 -> 21-pos2 -> 12-pos1_eq
  - based on 111-121_NEB
  - barrier: 0.2037 eV(最高处) -0.0226 eV(最低处)
  - ![](./images/2022-03-17-11-53-50.png)
  - 32-neb redo(based on 112-121)
    - barrier: 0.1950 eV -0.0345 eV
    - ![](./images/2022-03-26-11-22-18.png)
- 131_NEB
  - 11 -> 31 -> 13
  - based on 111-131_NEB
  - barrier: 0.4463 eV
  - ![](./images/2022-03-18-09-14-23.png)
    - 32-neb redo(based on 112-131)
      - == normal 收敛后查看，视情况判断是否需要 accurate ==

## ~~110-MASnF3-Li的迁移~~

### MASnF3_opt

- 理想的POSCAR(01/110-MASnF3/2super)
  - -485.01298816 eV
- MA 取向一致，均为 [011] 但无极框架发生倾斜
  - 8.99322 10.72383 10.52295 A
  - 86.4205 89.8018 90.3752 degree



## 123-MAPbI3-Li的迁移

### MAPbI3_opt

- 理想的POSCAR(01/123-MAPbI3/2super)
  - -416.36530609 eV
  - MA 取向一致, [011]
  - 12.57420 12.69275 12.78958 A
  - 88.7975 89.9530 89.9700 degree

### MAPbI3-Li+_opt

- INCAR 参数
  - 均使用范德华修正 IVDW=11
  - ENCUT=500,EDIFF=1E-5,EDIFG=-0.01
  - PREC=A,ISMEAR=0,SIGMA=0.10
- pos1(111_pos_1-2c03, 3/4,1/4,2/4)
  - -422.78630603 eV
- pos1_eq(here, 3/4,3/4,2/4)
  - -422.78630413 eV
- pos1_eqeq(here, 1/4,1/4,2/4)
  - -422.78630354 eV
- pos2(3/4,2/4,3/4)
  - -422.63270982 eV
- pos2_eq(here, 3/4,2/4,1/4)
  - -422.63270412 eV
- pso3(2/4,1/4,3/4)
  - -422.65421558 eV

### MAPbI3-Li+_neb3

- ==212n_NEB(based on 113-212n)==
  - pos2 -> pos1_eq -> pos2_eq
  - barrier: 
- 121_NEB(based on 113-121)
  - pos1 -> pos2 -> pos1_eq
  - barrier: 0.4739 eV
  - ![](./images/2022-03-27-09-27-42.png)
- 131_NEB
  - pos1 -> pos3 -> pos1_eqeq
  - based on idpp.py
    - barrier: 0.3336 eV
    - ![](./images/2022-03-24-10-20-09.png)
  - ==based on 113-131==
    - barrier: 
    - 

## ~~211-SiNSnCl3-Li的迁移~~

### SiNSnCl3_opt

- 理想的POSCAR(01/211-SiNSnCl3/2super/bu_opt3)
  - -408.31731174 eV
  - SiN 取向一致，均为 [011] 但无机框架发生倾斜，近似断裂
  - 11.58048 12.23337 11.60527 A
  - 94.3911 86.9765 90.8615 degree

### SiNSnCl3-Li+_opt

### SiNSnCl3-Li+_neb3

## 311-COSnCl3-Li的迁移

### COSnCl3_opt

- 理想的POSCAR(01/311-COSnCl3/2super/bu_opt2)
  - -388.71529487 eV
  - CO 取向一致，均为 [010] 但 O 端靠近 Cl ，无机框架稳定
  - 11.41059 11.26557 11.46540 A
  - 91.4146 88.5610 88.5412 degree

### COSnCl3-Li+_opt

### COSnCl3-Li+_neb3

## ~~411-BOSnCl3-Li的迁移~~

### BOSnCl3_opt

- 理想的POSCAR
  - -343.34324377 eV
  - BO 与 Cl 成键，无机框架倾斜严重，近似三方
  - 11.53373 11.58282 11.70584 A
  - 104.8709 73.4449 105.7636 degree

### BOSnCl3-Li+_opt

### BOnCl3-Li+_neb3

## a-MASnCl3-Fdoped

### MASnCl3-Fdoped-Li+_opt

- ini_t_opt(3/4,2/4,3/4, pos2)(01/a_MASnCl3_Fdoped/12-pos_used/ini_t_opt/bu_opt3)
  - -449.37114711 eV
  - 11.11568 11.43881 11.52084 eV
  - 86.7325 89.5966 90.2868 degree
- fin_opt(3/4,2/4,1/4, pos2_eq)(01/a_MASnCl3_Fdoped/12-pos_used/fin_opt/bu_opt2)
  - -449.24847131 eV
  - 11.11568 11.43881 11.52084 eV
  - 86.7325 89.5966 90.2868 degree

### MASnCl3-Fdoped-Li+_neb3

- ~~212n_NEB~~ stop

## notes

- 0311
  - 首先，根据理想 POSCAR(ISIF=3) 计算晶格常数
  - 接着，基于新的晶格常数和 MASnCl3-Li+_opt(pos 1,2,3 ISIF=2) 计算ABX3-Li+_opt
  - 再根据ABX3-Li+_opt计算ABX3_opt
- 实验组
  - 110,111,112,113: MASn(F,Cl,Br,I)
  - 113,123: MA(Sn,Pb)I # 待定，结合11,12,13和稳定性
  - 111,211,311,411: (MA,SiN,CO,BO)SnCl
  - a: MASnCl3-Fdoped
- 文件结构
  - 111-MASnCl3
    - one
    - 2super
    - Li-2super-E402(其余实验组略过)
      - 1-pos_all(非必须)
      - 12-pos_used
      - 2-NEB2(非必须)
      - 3-NEB3
      - work

- 路径、能垒、过渡态、能隙、bader
  - 212n：已计算
- 机理
  - Li-Cl成键断键
    - CHGDIFF
    - LDOS
  - Li-CH3类氢键作用
    - CHGDIFF
    - LDOS
  - MA取向影响体系总能量
    - 文献
  - 上述各项对能垒的贡献

### AIM-bcp 测试

- KPOINTS 
- NGXF, NGYF, NGZF
- ENCUT

==精确至小数点后四位==

## 脚本修改

### plot_atom_dos

修改文件 dos.py, usage: dos_data.get_atom_dos(['Li1','C2'])

```python
# after dos_data.get_element_dos()
    def get_atom_dos(self, atoms: list[str]) -> Dict[SpeciesLike, Dos]:
        """
        Get atom projected Dos.
        
        Returns:
            dict of {atom_str: Dos}
        """
        import re
        at_dos = {}
        for atom in atoms:
            el, num = re.findall(r'[0-9]+|[A-Z,a-z]+', atom) # get 'Sn','12' form 'Sn12'
            num = int(num)
            cont = 0
            for site, atom_dos in self.pdos.items():
                a_el = site.specie
                if el != str(a_el):
                    continue
                else:
                    cont += 1 # find 'Sn' and cont
                    if num == cont: # find 'Sn12'
                        for pdos in atom_dos.values():
                            if atom not in at_dos:
                                at_dos[atom] = pdos
                            else:
                                at_dos[atom] = add_densities(at_dos[atom], pdos)
        return {at: Dos(self.efermi, self.energies, densities) for at, densities in at_dos.items()}
```