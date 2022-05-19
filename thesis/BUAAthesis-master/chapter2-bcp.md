# chapter2

--------

@File    :   chapter2-bcp.md
@Time    :   2022/05/17 23:33:49
@Auth    :   Ming(<3057761608@qq.com>)
@Vers    :   0.1
@Desc    :   chapter2: 金属有机钙钛矿中氢键的分析
@Refe    :   url1; url2

--------

## 引言

在有机金属卤化物钙钛矿系统中，有机分子的氢原子和无机框架中的卤素原子容易形成氢键，进而影响体系的结构、性能。
Svane等人==svaneHowStrongHydrogen2017==开发出针对该体系的氢键强度计算方法，并发现该类化合物的氢键键能明显较弱。
Varadwaj等人==varadwajSignificanceHydrogenBonding2019==深入研究了氢键和其他非共价相互作用对无机八面体倾斜的影响。
对于本文研究的体系，大量存在的氢键可能对锂离子的迁移路径及能垒产生不可忽略的影响（有机金属卤化物钙钛矿中氢键键能约为$2~6 kcalmol^{-1}$==svaneHowStrongHydrogen2017==，即 $0.09~0.26 kcalmol^{-1}$，与锂离子迁移能垒 $0.45 eV$相当）。因此，有必要开发出从计算结果中快速获取体系氢键性质的方法，特别是氢键的键能。

## 利用分子中的原子理论研究氢键

分子中的原子理论（Atoms in molecules，AIM）==baderQuantumTheoryMolecular1991b==是一种量子化学模型，基于电子密度标量场的拓扑性质划分空间，使得每个区域仅包含一个原子核，从而定义出量子化学观点下的原子，并给出原子的部分性质。
AIM理论在提出之后不断发展，广泛应用于化学体系的理论研究。
AIM理论认为，当且仅当两个原子之间被一个零通量面分隔开，且该零通量面上有一个$(3,-1)$临界点时，认为两个原子间存在键。其中临界点指电子密度梯度为零的点，$(3,-1)$临界点指该临界点的海森矩阵的本征值中有两个负值和一个正值，该点被称为键临界点（bond critical point，bcp）。几何意义上，键临界点为电子密度标量场上的一阶鞍点；代数意义上，键临界点为满足如下关系式的空间位置：
$$
\Vert \nabla\rho(x,y,z)  \Vert = 0; \\
(\nabla\nabla\rho)u_i = \lambda_i u_i\quad (i=1,2,3); \\
\lambda_i \neq 0 \quad (i=1,2,3);\\
\sum_{i=1}^3\text{sign}(\lambda_i) = -1.  
$$
其中，
$$
\nabla\rho(x,y,z) = 
\begin{bmatrix}
    \partial\rho/\partial x & \partial\rho/\partial y & \partial\rho/\partial z
\end{bmatrix}; \\
\nabla\nabla\rho= 
    \begin{bmatrix}
        \displaystyle\frac{\partial^2 \rho}{\partial x^2} & \displaystyle\frac{\partial^2 \rho}{\partial x\partial y} & \displaystyle\frac{\partial^2 \rho}{\partial x \partial z} \\
        \displaystyle\frac{\partial^2 \rho }{\partial y \partial x} & \displaystyle\frac{\partial^2 \rho }{\partial y^2} & \displaystyle\frac{\partial^2 \rho }{\partial y \partial z} \\
        \displaystyle\frac{\partial^2 \rho }{\partial z \partial x} & \displaystyle\frac{\partial^2 \rho }{\partial z \partial y} & \displaystyle\frac{\partial^2 \rho }{\partial z^2}
    \end{bmatrix}; 
$$

在最近的研究中，Emamian等人==emamianExploringNaturePredicting2019==通过构造一系列具有代表性的氢键体系，通过量子化学的方法计算证明，利用氢键的键临界点处的电子密度可以可靠地估计氢键强度，并给出了相应的关系式。

![bcp键能关系式](../../images/bcp-energy.png)

(a)针对所有氢键体系的bcp处电子密度和氢键键能直接拟合的结果，尽管决定系数 $R^2$ 较好，但平均绝对百分误差 $MAPE$ 很大，因此拟合结果在预测氢键键能上无实际意义；针对(b)不带电氢键体系和(c)带电体系的bcp处电子密度和氢键键能分别进行拟合的结果，决定系数 $R^2$ 和 平均绝对百分误差 $ MAPE $ 结果均很好。

但是该工作主要基于量子化学方法和分子体系，尚无充分的数据证明关系式适用于DFT理论下的固体体系。

## 代码实现

VASP 的输出文件 CHGCAR 中记录了体系的原子核位置和价电子空间电子密度。
为保证结果的准确性，通过在 VASP 的计算设置文件 INCAR 中增加 “LAECHG=.TRUE.” 并通过 VTST 提供的脚本获得包含体系全部电子的空间电子密度文件 CHGCAR_sum。
针对该文件编写 python 脚本，获取体系的 bcp 处电子密度。其伪代码如下，完整代码已上传至 GitHub，详细见 https://github.com/Mingzefei/Li-MA/blob/master/relax/AIM_bcp.py 。==改为脚注==

```latex
\usepackage{algorithm}
\usepackage{algorithmicx}
\usepackage{algpseudocode}
\floatname{algorithm}{算法}
\begin{algorithm}
	\renewcommand{\algorithmicrequire}{\textbf{Input:}}
	\renewcommand{\algorithmicensure}{\textbf{Output:}}

    \caption{获取指定原子间 bcp 处电子密度}
	\label{alg1}
	\begin{algorithmic}[1]
                \Require 
                        $atomA(x^a,y^a,z^a)$: 原子A坐标;
                        $atomB(x^b,y^b,z^b)$: 原子B坐标;
                        $\rho(x_n,y_n,z_n)$: 离散空间电子密度;
                        $eps1,eps2$: 条件阈值
                \State 转换原子A和B实际坐标到离散空间中坐标 $(x_n^a,y_n^a,z_n^a),(x_n^b,y_n^b,z_n^b)$
                \State $ grad(x_n,y_n,z_n) \gets \nabla \rho(x_n,y_n,z_n)$
                \State $ hess(x_n,y_n,z_n) \gets \nabla grad(x_n,y_n,z_n)$
                \State $ chg^{bcp} \gets 0$
                \For{ $ x_n $ in $ \mathrm{range}(\min(x_n^a,x_n^b),\max(x_n^a,x_n^b)) $ }
                \For{ $ y_n $ in $ \mathrm{range}(\min(y_n^a,y_n^b),\max(y_n^a,y_n^b)) $ }
                \For{ $ z_n $ in $ \mathrm{range}(\min(z_n^a,z_n^b),\max(z_n^a,z_n^b)) $ }
                        \State $ module \gets \Vert grad(x_n,y_n,z_n) \Vert$
                        \If {$ module < eps1$}
                                \State $\lambda_1,\lambda_2,\lambda_3 \gets \mathrm{eig}(hess(x_n,y_n,z_n)) $
                                \State $condition1 \gets \bigwedge_{i=1}^3 \left[\mathrm{abs}(\lambda_i)< eps2\right]$
                                \State $condition2 \gets \left[\sum_{i=1}^3 \mathrm{sign}(\lambda_i)\right] = -1$
                                \If{$condition1 \wedge condition2 $}
                                        \If{$chg^{bcp} = 0 \vee module^{bcp}>module$}
                                                \State $chg^{bcp} \gets chg(x_n,y_n,z_n)$
                                                \State $module^{bcp} \gets module $
                                        \EndIf
                                \EndIf
                        \EndIf
                \EndFor
                \EndFor
                \EndFor
                \Ensure $chg^{bcp}$
	\end{algorithmic} 
\end{algorithm}
```

## 计算结果及分析

这部分通过构建相关体系，验证上述方法的有效性，即通过 bcp 处电子密度可以对氢键强度进行估计。

### bcp 处电子密度的准确性

文献==emamianExploringNaturePredicting2019==中使用量子化学方法进行计算，而vasp软件通过DFT方法求解能带进行计算，两者计算方法存在差异。因此，有必要验证两种方法对于bcp处电子密度计算的一致性。

考虑到本课题研究的体系中多为 N-H···X（X=Cl,Br,I）类氢键，这里选用文献==emamianExploringNaturePredicting2019==中 FH-NH3（28号）、H2NH-F-（33号）和HF-HNH3+（30号）分子体系进行建模和vasp 计算，并求解bcp处电子密度。
建立$15\times15\times15 \r A$晶胞，使用The Materials Project数据库 == 脚注：https://materialsproject.org/ == 中分子数据。最终结果如下。

![](../../images/bcp-test1.png)

==表格==

根据计算结果，利用vasp进行的DFT计算获得的bcp处电子密度较文献==emamianExploringNaturePredicting2019==中使用的量子化学方法存在正向偏差，偏高 $ 13 ~ 21 \% $。该结果推测是由计算方法导致，一般而言，量子化学方法对分子体系的计算更为准确，而利用vasp进行的DFT计算，由于波函数展开方式、赝势等原因，对分子体系的计算并不十分准确。但在当前