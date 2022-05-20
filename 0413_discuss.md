# 0413汇报

--------

@File    :   0413_discuss.md
@Time    :   2022/04/14 08:59:37
@Auth    :   Ming(<3057761608@qq.com>)
@Vers    :   0.1
@Desc    :   Li-MASnCl3
@Refe    :   url1; url2

--------

## 理论和方法

### H bond 

- 体系中存在氢键
  - CH3N3中的H与无机框架中的Cl
  - 使用DFT+D3范德华修正
  - 文献
- 使用AIM理论中的bcp处电子密度，近似键能
  - 文献：J. Comput. Chem. 2019, 40, 2868–2881
    ![](./images/2022-04-15-10-17-48.png)
  - 文献量子化学方法计算bcp，而vasp的结果普遍偏高
    ![](./images/2022-04-15-10-20-59.png)

### Li bond

- 体系存在大量锂键或类似锂键的作用
  - 传统锂键：$$ X···Li-Y (X=NH3, Me3N, H2O, Me2O; Y=Cl, Br)$$，键能(0.64 eV, Li2S6@pyridinic nitrogen in graphene)，锂键无方向性、无饱和性
  - 课题体系：$$H3NCH3···Li-Y (Y=Cl,Br,Pb)$$，数量多；正电荷多，CH3相对于Li+是富电子；猜测键能更低
  - 证明：CHGDIFF，LDOS，bcp(获得近似键能，分析成键相对强弱，需要验证)
- 锂离子迁移能垒低
  - 锂键或类锂键距离合适、数量多

### 验证bcp方法适用于课题体系

**文献工作**

- 氢键文献：量子化学+氢键分子体系；bcp电子密度和键能的线性关系
- 锂键文献：量子化学+锂键分子体系、掺杂石墨烯体系；键能

**方法验证**

- vasp复现氢键文献：获得bcp电子密度，与文献比较，证明vasp可以近似代替量子化学方法
- vasp复现锂键文献：获得bcp电子密度和键能，与氢键的bcp电子密度和键能关系式比较，证明bcp方法可用于锂键体系
- 问题1，体系不同：文献的bcp方法，独立分子体系，但课题体系为分子+无机框架的块体
- 问题2：锂键键能文献少

## 数据整理

### 计算参数

**结构计算**

INCAR参数：
- 范德华修正：IVDW=11
- ENCUT=500, EDIFF=1E-5, EDIFG=-0.01(opt) / 600, 1E-6(dos)
- PREC=A, ISMEAR=0, SIGMA=0.01
- NELECT=402 # 体系带一个单位正电荷

KPOINTS: 3 3 3(opt) / 4 4 4(dos)

**neb计算**
INCAR参数：
- LCLIMB=T, ICHAIN=0, IBRION=3, POTIM=0, IOPT=1, SPRING=-5
- IMAGES = 12 or 15
- normal: EDIFF=1E-5, EDIFFG=-0.05
- accurate: EDIFF=1E-6, EDIFFG=0.03

其余与opt一致

### 不同位置、不同方向

以 Lii+@MASnCl3 为例

#### pos

POS1: 3/4, 1/4, 2/4
![MASnCl3-pos1](./images/2022-04-10-16-40-40.png)
POS2: 3/4, 2/4, 3/4
![MASnCl3-pos2](./images/2022-04-10-22-11-50.png)
POS3: 2/4, 1/4, 3/4
![MASnCl3-pos3](./images/2022-04-10-22-28-52.png)

embedded energy
![MASnCl3-embedded-energy](./images/111-pos-embedded-energy.png)

cdd
![MASnCl3-pos1-cdd](./images/2022-04-10-23-36-56.png)
![MASnCl3-pos2-cdd](./images/2022-04-11-00-37-03.png)
![MASnCl3-pos3-cdd](./images/2022-04-11-17-02-05.png)

DOS
![MASnCl3-pos1-dos](./images/111-11-dos.png)
![MASnCl3-pos2-dos](./images/111-21-dos.png)
![MASnCl3-pos3-dos](./images/111-31-dos.png)

LDOS
![MASnCl3-pos1-ldos](./images/111-11-ldos.png)
![MASnCl3-pos2-ldos](./images/111-21-ldos.png)
![MASnCl3-pos3-ldos](./images/111-31-ldos.png)

#### NEB

![MASnCl3-neb121](./images/2022-04-14-09-49-14.png)
![MASnCl3-neb131](./images/2022-04-14-09-51-34.png)
![MASnCl3-neb212](./images/2022-04-14-09-53-23.png)

energy
![MASnCl3-neb-energy](./images/contrast-P-111-neb-barrier.png)

Li+ valence
![MASnCl3-neb-Li-bader](./images/contrast-P-111-neb-Li-bader.png)


Li-H bcp total
![MASnCl3-neb-Li-H-bcp-total](./images/contrast-P-111-neb-Li-H-bcp-total.png)

Li-H bcp
![MASnCl3-neb121-bcp](./images/111-121-bcp.png)
![MASnCl3-neb131-bcp](./images/111-131-bcp.png)
![MASnCl3-neb212-bcp](./images/111-212-bcp.png)


### 替换无机部分

MASnCl3、MASnBr3、MASnI3、MAPbI3

晶格参数

MASnCl3 : MASnBr3 : MASnI3 : MAPbI3 = 1 : 1.0372 : 1.1010 : 1.1168

![](./images/contrast-E-supercell-constant.png)

#### pos1

![MASnCl3-pos1](./images/2022-04-14-09-27-47.png)

![MASnCl3-pos1-cdd](./images/2022-04-10-23-36-56.png)



![MASnCl3-pos1-dos](./images/111-11-dos.png)
![MASnBr3-pos1-dos](./images/112-11-dos.png)
![MASnI3-pos1-dos](./images/113-11-dos.png)
![MAPbI3-pos1-dos](./images/123-11-dos.png)

![MASnCl3-pos1-ldos](./images/111-11-ldos.png)
![MASnBr3-pos1-ldos](./images/112-11-ldos.png)
![MASnI3-pos1-ldos](./images/113-11-ldos.png)
![MAPbI3-pos1-ldos](./images/123-11-ldos.png)


#### pos2

![MASnCl3-pos2](./images/2022-04-14-09-30-46.png)
![MASnCl3-pos2-cdd](./images/2022-04-11-00-37-03.png)

![MASnCl3-pos2-dos](./images/111-21-dos.png)
![MASnBr3-pos2-dos](./images/112-21-dos.png)
![MASnI3-pos2-dos](./images/113-21-dos.png)
![MAPbI3-pos2-dos](./images/123-21-dos.png)

![MASnCl3-pos2-ldos](./images/111-21-ldos.png)
![MASnBr3-pos2-ldos](./images/112-21-ldos.png)
![MASnI3-pos2-ldos](./images/113-21-ldos.png)
![MAPbI3-pos2-ldos](./images/123-21-ldos.png)

#### pos3

![MASnCl3-pos3](./images/2022-04-14-09-34-25.png)
![MASnCl3-pos3-cdd](./images/2022-04-11-17-02-05.png)

![MASnCl3-pos3-dos](./images/111-31-dos.png)
![MASnBr3-pos3-dos](./images/112-31-dos.png)
![MASnI3-pos3-dos](./images/113-31-dos.png)
![MAPbI3-pos3-dos](./images/123-31-dos.png)

![MASnCl3-pos3-ldos](./images/111-31-ldos.png)
![MASnBr3-pos3-ldos](./images/112-31-ldos.png)
![MASnI3-pos3-ldos](./images/113-31-ldos.png)
![MAPbI3-pos3-ldos](./images/123-31-ldos.png)

#### all pos

**嵌入能**
![](./images/contrast-E-embedded-energy.png)

**LiX距离**（临近，pos1:X6, pos2:X6, pos3:X9 ）

![](./images/contrast-E-distX.png)

**Li化合价**

![](./images/contrast-E-Li+-valence.png)

**X化合价**（临近Li，pos1:X6, pos2:X6, pos3:X9 ）

![](./images/contrast-E-X-valence.png)

**Li-H最小bcp**

![](./images/contrast-E-min-Li-H-bcp.png)

**Li-H最大bcp**

![](./images/contrast-E-max-Li-H-bcp.png)

**Li-H最小dist**（临近）

![](./images/contrast-E-min-Li-H-dist.png)

**Li-H最大dist**（临近）

![](./images/contrast-E-max-Li-H-dist.png)

#### neb121

![MASnCl3-neb121](./images/2022-04-14-09-49-14.png)

![](./images/contrast-E-neb121-barrier.png)


<!-- ![MASnCl3-neb121-bcp](./images/111-121-bcp.png)
![MASnBr3-neb121-bcp](./images/112-121-bcp.png)
![MASnI3-neb121-bcp](./images/113-121-bcp.png)
![MAPbI3-neb121-bcp](./images/123-121-bcp.png)

![MASnCl3-neb121-bader](./images/111-121-bader.png)
![MASnBr3-neb121-bader](./images/112-121-bader.png)
![MASnI3-neb121-bader](./images/113-121-bader.png)
![MAPbI3-neb121-bader](./images/123-121-bader.png)

![MASnCl3-neb121-Libader](./images/111-121-Libader.png)
![MASnBr3-neb121-Libader](./images/112-121-Libader.png)
![MASnI3-neb121-Libader](./images/113-121-Libader.png)
![MAPbI3-neb121-Libader](./images/123-121-Libader.png) -->

**Li化合价**
![](./images/contrast-E-neb121-Li+-bader.png)
**Li-H bcp total**
![](./images/contrast-E-neb121-Li-H-bcp-total.png)

#### neb131

![MASnCl3-neb131](./images/2022-04-14-09-51-34.png)

![](./images/contrast-E-neb131-barrier.png)

<!-- ![MASnCl3-neb131-bcp](./images/111-131-bcp.png)
![MASnBr3-neb131-bcp](./images/112-131-bcp.png)
![MASnI3-neb131-bcp](./images/113-131-bcp.png)
![MAPbI3-neb131-bcp](./images/123-131-bcp.png)

![MASnCl3-neb131-bader](./images/111-131-bader.png)
![MASnBr3-neb131-bader](./images/112-131-bader.png)
![MASnI3-neb131-bader](./images/113-131-bader.png)
![MAPbI3-neb131-bader](./images/123-131-bader.png)

![MASnCl3-neb131-Libader](./images/111-131-Libader.png)
![MASnBr3-neb131-Libader](./images/112-131-Libader.png)
![MASnI3-neb131-Libader](./images/113-131-Libader.png)
![MAPbI3-neb131-Libader](./images/123-131-Libader.png) -->

**Li化合价**
![](./images/contrast-E-neb131-Li+-bader.png)
**Li-H bcp total**
![](./images/contrast-E-neb131-Li-H-bcp-total.png)


#### neb212

![MASnCl3-neb212](./images/2022-04-14-09-53-23.png)

![](./images/contrast-E-neb212-barrier.png)

<!-- ![MASnCl3-neb212-bcp](./images/111-212-bcp.png)
![MASnBr3-neb212-bcp](./images/112-212-bcp.png)
![MASnI3-neb212-bcp](./images/113-212-bcp.png)
![MAPbI3-neb212-bcp](./images/123-212-bcp.png)

![MASnCl3-neb212-bader](./images/111-212-bader.png)
![MASnBr3-neb212-bader](./images/112-212-bader.png)
![MASnI3-neb212-bader](./images/113-212-bader.png)
![MAPbI3-neb212-bader](./images/123-212-bader.png)


![MASnCl3-neb212-Libader](./images/111-212-Libader.png)
![MASnBr3-neb212-Libader](./images/112-212-Libader.png)
![MASnI3-neb212-Libader](./images/113-212-Libader.png)
![MAPbI3-neb212-Libader](./images/123-212-Libader.png) -->

**Li化合价**
![](./images/contrast-E-neb212-Li+-bader.png)
**Li-H bcp total**
![](./images/contrast-E-neb212-Li-H-bcp-total.png)


### 替换有机部分

MA(CH3NH3)/SiN/CO/BO：无机框架崩塌




## 文章框架

### Li+嵌入

- 嵌入能
- MA转动
- MA与Li的作用
  - 差分电荷密度
  - LDOS

### Li+迁移

#### 迁移过程

- Li围绕卤原子X圆周运动
  - MA旋转，降低位阻
  - MA与Li相互作用
- Li与卤原子断键成键，部分MA复位
  - 可能会形成能垒峰

#### 相互作用

用类锂键解释低能垒

## 其他

###### 相场