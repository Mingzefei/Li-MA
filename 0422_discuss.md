# 0422汇报

--------

@File    :   0422_discuss.md
@Time    :   2022/04/22 14:13:12
@Auth    :   Ming(<3057761608@qq.com>)
@Vers    :   0.1
@Desc    :   Li-MASnCl3
@Refe    :   url1; url2

--------

## Li+@MASnCl3-pos1

### POSCAR

![](./images/2022-04-22-14-29-28.png)

### embedded energy

opt: -9.1509 eV
old: -9.36 eV

```python
# Li_energy = -0.03229124
Li_ion_energy = 3.4838
pos1_energy = -447.7221
pos1_MASnCl3_energy = -442.05496
```

### CHGCAR

max = 0.5, min = 0

![](./images/2022-04-22-12-43-01.png)

![](./images/2022-04-22-14-56-26.png)

### DIFF

max = 0.004, min = -0.004

![](./images/2022-04-22-13-54-23.png)

![](./images/2022-04-22-14-57-40.png)

### ELF

max = 1, min = 0

![](./images/2022-04-22-13-43-24.png)
![](./images/2022-04-22-14-55-08.png)

### bader valence

**Li+@MASnCl3**

- CH-6 0.4393109999999999
- NH-6 0.3410960000000003
- MA-6 0.7804070000000002
- CH-4 0.4690200000000001
- NH-4 0.33796000000000004
- MA-4 0.8069800000000001

![](./images/111-11-bader-valence.png)

**fix_MASnCl3**

- CH-6 0.47133599999999987
- NH-6 0.3168549999999999
- MA-6 0.7881909999999998
- CH-4 0.4673090000000001
- NH-4 0.33118099999999995
- MA-4 0.79849

![](./images/111-11-bader-valence-MASnCl3-fix.png)

**opt_MASnCl3**

- CH-6 0.4785299999999998
- NH-6 0.3198660000000002
- MA-6 0.798396
- CH-4 0.46848199999999995
- NH-4 0.3278289999999999
- MA-4 0.7963109999999999

![](./images/111-11-bader-valence-MASnCl3-opt.png)

## Li@MASnCl3-pos1

### POSCAR

![](./images/2022-04-22-14-24-06.png)

### embedded energy

opt: -2.2007 eV

```python
Li_energy = -0.03229124
# Li_ion_energy = 3.4838
E403_pos1_energy = -444.28625728
E403_pos1_MASnCl3_energy = -442.05328653
```

### CHGCAR

max = 0.5, min = 0

![](./images/2022-04-22-14-04-32.png)
![](./images/2022-04-22-15-06-51.png)

### DIFF

max = 0.004, min = -0.004

![](./images/2022-04-22-13-51-54.png)
![](./images/2022-04-22-15-07-34.png)

### ELF

max = 1, min = 0

![](./images/2022-04-22-14-53-03.png)
![](./images/2022-04-22-14-54-13.png)

### bader valence

**Li+@MASnCl3**

- CH-6 0.44935999999999987
- NH-6 0.3235990000000002
- MA-6 0.7729590000000001
- CH-4 0.46665900000000016
- NH-4 0.32945199999999986
- MA-4 0.796111

![](./images/111-11-eE403-bader-valence.png)

