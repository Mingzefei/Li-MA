# together

--------

@File    :   together.md
@Time    :   2022/05/20 17:25:30
@Auth    :   Ming(<3057761608@qq.com>)
@Vers    :   1.0
@Desc    :   chapter1：绪论；chapter2
@Refe    :   url1; url2

--------

# chapter1

## 锂金属电极保护膜及离子输运

锂离子电池凭借自身容量大，工作电压高，以及循环寿命长等优点，成为最常用的电化学储能设备之一。然而，锂金属电极的应用一直面临诸多挑战，例如，充放电循环中体积膨胀，锂金属与电解液之间界面反应复杂，电沉积过程中负极表面枝状晶体生长难以控制，甚至存在“死锂”(图1a)等1。这些都严重影响了锂金属负极的安全稳定和高效。

![](../../images/Li-anode.png)

图 1 (a)锂金属电极在充放电过程中产生锂枝晶和死锂；(b)抑制锂枝晶的方法

目前，科研工作者从实验上证明，设计合适的保护层是解决上述问题的有效手段之一。已开发的保护层包括聚合物型、无机型，以及合金型等。

Lopez等人==lopezEffectsPolymerCoatings2018==对聚合物型保护层进行分析和比较，发现该类保护层的机械性能影响锂离子沉积的宏观均匀性，而其化学性质影响沉积的局部形态。

Liu等人==liuMixedLithiumIon2020==通过硫化硒与锂金属的气固反应制得Li2S/Li2Se保护层，使得LiFePO4、S/C及LiNi0.6Co0.2Mn0.2O2全电池在电池循环性能上均有所提升。其中，Li2Se较Li2S的锂离子迁移能垒更低，表现出更好的离子导电率，在一定程度上抑制了锂枝晶的形成。

Guo等人==guoDendritefreeLithiumDeposition2020==根据Ag和Au的良好亲锂性，通过反应在电极表面形成亲锂的合金层，降低了锂离子成核势垒，从而实现锂的均匀沉积。

通过在锂金属电极表面覆盖保护层，一方面减少锂金属与电解液之间复杂的界面反应，提高了电池效率；另一方面对锂离子的迁移和沉积进行调控，从而实现抑制枝晶生长1。

因此，为有针对性地设计新型高效保护膜，其中的锂离子输运行为引起了人们的注意。

Wei等人==文献weiKineticsTuningLiIon2015==通过理论计算和实验相结合，阐明了LiNixMnyCozO2(NMC,x+y+z=1)材料中调节锂离子扩散动力学的方法。随着材料体系含锂量的不同，存在两种不同的迁移方式。

Dathar等人==文献datharCalculationsLiIonDiffusion2011==较为系统地研究了橄榄石磷酸盐FePO4和LiFePO4中的锂离子扩散动力学，通过考虑块体、表面、缺陷等因素影响，解释了前人理论计算和实验测量间的数值差距。

Yang等人==文献yangLiIonDiffusion2011==从实验表征和理论计算上对橄榄石磷酸盐LiFePO4中锂离子迁移机理进行研究，发现其中包括两个过程：锂离子在PO4基团相邻Li位点之间跳跃；Fe离子协同运动，进而形成反位缺陷，促进锂离子扩散。

Iddir等人==文献iddirLiIonDiffusion2010==对单斜Li2CO3中锂离子迁移进行计算模拟，发现锂离子沿Li2CO3开放通道的能垒（0.28 eV）远低于跨平面方向能垒（0.60 eV），该过程中锂离子与O依次发生断键和成键。

在近期的研究中Yao等人将光电材料有机金属卤化物钙钛矿用作锂金属电极保护膜，实验结果证明了其有效性。而有机金属卤化物钙钛矿为锂离子提供了新型的输运环境，其中存在的复杂作用关系，可能启发人们设计新型保护膜。

综上，人们已经对Li2CO3、LiFePO4等锂电池体系材料的锂离子输运行为进行多方面的研究，并发现其中的机理受环境、缺陷等因素影响，该过程中锂离子与相关原子的成键断键或协同运动都会显著影响迁移能垒。

## 金属有机钙钛矿

金属有机钙钛矿因其能带结构合适、光电转化效率高等优点，被用于高效太阳能电池的研发。当前，对于金属有机钙钛矿的晶体结构、能带结构等方面，人们已有较全面的研究。
钙钛矿的基本结构如下所示7，由B位金属离子和X位卤素原子形成立方框架，A位阳离子填充其中。

![](../../images/perovskite.png)

金属有机钙钛矿的晶格类型受温度影响很大。以MAPbI3（结构如图3所示）为例，温度变化时，晶格中的PbI3八面体会发生旋转和倾斜，从而产生不同的相：低温时为正交相图3(a)；温度高于约162 K时为四方相3(b)；温度高于约330 K时为立方相3(c)8。

![](../../images/temp-struc.png)

图 3 CH3NH3PbI3在不同温度下的晶体结构示意图。(a) 正交相；(b) 四方相；(c) 立方相。图中黑色大球为Pb原子，灰色大球为 I 原子，灰色和 浅灰色小球分别为有机分子中的N和 C原子，白色小球为H原子8.

对于A位有机阳离子，如MA（CH3NH3，甲胺），通常存在取向。
Brivio等人9对MA的不同取向进行研究，认为<100>、<110>和<111>三种取向中以<100>取向热力学最稳定；而Giorgi10等人认为<111>最稳定。实验上，Wasylishen等人11通过光谱测量发现室温下MA有机阳离子存在快速旋转；而Frost等人12计算发现立方相APbI3(A=NH4，CH3NH3，CF3NH3和NH2CHNH2)中有机分子的旋转势垒分别为0.3，1.3，21.4和13.9 kJ/mol，受极性和尺寸影响。
通过调整B位金属阳离子和X位卤族元素，可以实现对带隙、晶格尺寸和稳定性的调控8。

此外，由于有机分子的存在，在研究该类钙钛矿材料的性质时需要特别考虑范德华力及其他可能的相互作用。实验和计算模拟==wangDensityFunctionalTheory2013、puScreeningPerovskiteMaterials2021、varadwajSignificanceHydrogenBonding2019==上均证实金属有机钙钛矿中存在氢键及其他非共价相互作用，并对材料的结构、能带等诸方面均有影响。

综上，研究金属有机钙钛矿，如MAPbI3，需要特别考虑其中有机阳离子的取向和转动，以及可能存在的氢键等相互作用对输运能垒的影响；此外，合理设计其中的金属阳离子和卤族元素可以提高材料稳定性等性能指标。

## 计算方法

### 密度泛函理论

基于密度泛函理论(Density function theory，DFT)的第一性原理计算可以精确计算固体系统的电子基态，因此在锂金属电池的计算模拟中应用广泛22。

1965年，Kohn和Sham 23在Thomas 24、Fermi等前人的研究基础上，提出了著名的Kohn-Sham方程，揭示了基态能量和电子密度间的确切关系。通过自洽求解Kohn-Sham方程，可以获得材料的总能量、稳定结构和能带等基础信息。

建立Kohn-Sham方程需要一些近似处理和定理支撑。首先，对于多粒子体系，在不考虑其他外场作用的前提下，定态薛定谔方程中哈密顿算符为
$$
\hat{H}=\hat{H}_e+\hat{H}_N+\hat{H}_{\mathrm{eN}}
$$
其中， 和 分别对应电子和原子核的能量(包括动能 、相互作用能 )， 对应电子与原子核间相互作用能，具体表示为
 
$$
\hat{H}_e(r)=\hat{T}_e(r)+\hat{V}_{\mathrm{ee}}(r)
$$
$$
\hat{H}_N(R)=\hat{T}_N(R)+\hat{V}_{\mathrm{NN}}(R)
$$
$$
\hat{H}_{\mathrm{eN}}(r,R)=\mathrm{ }\hat{V}_{\mathrm{eN}}(r,R)
$$

根据Born-Oppenheimer近似28，将原子核的运动和核外电子的运动分开考虑：研究电子运动时原子核处于其瞬时位置上；研究原子核运动时不考虑电子在空间的具体分布。因此，对于电子，有
$$
\hat{H}=\hat{T}_{\mathrm{e}}(r)+\hat{V}_{\mathrm{ee}}(r)+\hat{V}_{\mathrm{NN}}(R)+\hat{V}_{\mathrm{eN}}(r,R)
$$
其中，表示原子核间排斥能的 近似为常数。由于式(3)对于多电子体系过于复杂，无法利用该式直接求解定态薛定谔方程。Hohenberg和Kohn利用粒子数密度函数$\rho(r)$作为基本变量，来表述体系的各种性质，并给出Hohenberg-Kohn定理23：不计自旋的全同费米子系统的基态能量是粒子数密度函数$\rho(r)$的唯一泛函；对给定的哈密顿量，能量泛函$E_0[\rho]$对正确的粒子数密度函数$\rho(r)$取极小值，并等于基态能量。其中，$\rho(r)$满足：
$$
\rho(r)=N\int_{}^{}\mathrm{d}r_1 \cdots \int_{}^{}\mathrm{d}r_N | \Psi (r,r_1,\cdots,r_N) |^2
$$
由此，体系的能量可写作
$$
E[\rho] = \Psi ^*(\hat{T}_{\mathrm{e}}+\hat{V}_{\mathrm{ee}}+\hat{V}_{\mathrm{ext}})\Psi
$$
其中，假定所有电子都具有相同的局域势$\nu (r)$ (包括电子之间的关联、原子核势场、外场等)，使用$\hat{V}_{\mathrm{ext}}$表示外势对电子的作用，有
$$
V_{\mathrm{ext}} = \int_{}^{}\mathrm{d}r\nu(r)\rho(r)
$$
使用无相互作用电子系统的相关量替代上述系统，并用$N$个单电子波函数$ \varphi _i(r) $组成密度函数$\rho(r)$，即
$$
\rho(r)=\sum_{i=1}^{N}|\varphi_i (r)|^2
$$
故电子动能
$$
T_{\mathrm{e}}=\sum_{i=1}^{N}\int_{}^{}\mathrm{d}r\varphi^*_i(r)(-\frac{1}{2}\nabla^2)\varphi_i(r)
$$
电子间相互作用
$$
V_{\mathrm{ee}} =\frac{1}{2}\iint_{}^{}\mathrm{d}r\mathrm{d'}\frac{\rho(r)\rho(r')}{|r-r'|}
$$
用交互关联项$V_{\mathrm{XC}}$表示其余相互作用及替代过程中损失的复杂性。由变分法，得著名的Kohn-Sham方程23
$$
{-\frac{1}{2}\nabla^2+V_{\mathrm{KS}[\rho(r)]}}\varphi_i(r)=E_i\varphi(r)
$$
其中
$$
V_{\mathrm{KS}}[\rho[r]]=\nu(r)+\int_{}^{}\mathrm{d}r'\frac{\rho(r')}{|r-r'|}+\frac{\delta E_{\mathrm{XC}}[\rho(r)]}{\delta\rho(r)}
$$
求解Kohn-Sham方程的难度主要在于，其中含有交换关联势能$V_{\mathrm{XC}}$，目前尚不知道确切形式，但已有许多有效近似方法。例如，局部密度近似(LDA)假设$V_{\mathrm{XC}}$只与局域密度有关而与整个体系密度无关，通过求解均匀电子气来构造VXC的解析形式。因此LDA一般试用于电子密度变化比较平缓的体系，能够有效处理金属，但对多数氧化物和盐存在较大偏差。Perdew 28提出了广义梯度近似(GGA)，在$V_{\mathrm{XC}}$中引入电子密度梯度，以此来改善误差。每个小范围的VXC不仅仅依赖于其自身的局域电子密度，同时也受到周围电子密度的影响。这使得近似更符合真实情况。GGA目前已衍生出多种形式，例如PW86 29、PW91 30。当系统中含有过渡元素或稀土元素时，系统的d，f轨道电子会趋于局部化，电子间的相互作用会使传统方法产生较大偏差，此时DFT + U方法更为有效，其中U是库伦作用参数，一般通过带隙等实验数据拟合得到。当LMBs中含有过渡元素或稀土元素时，可以尝试使用该方法31。改善LDA、GGA两种近似的另一种方式为考虑杂化泛函，将GGA的交换能$E^{GGA}_{\mathrm{X}}$与非局域的Hartree-Fock型交换能$E^{GGA}_{\mathrm{X}}$以一定比例$\alpha$混合，和GGA的关联能$E^{GGA}_{\mathrm{X}}$，共同构成交换关联能$E_{\mathrm{XC}}$，如下所示
$$
E_{\mathrm{XC}}=\alpha E^{HF}_{\mathrm{X}}+(1-\alpha)E^{GGA}_{\mathrm{X}}+E^{GGA}_{\mathrm{C}}
$$
进一步将$E^{HF}_{\mathrm{X}}$限制在短程内，即为HSE型杂化泛函32，在计算带隙方面更加准确，被广泛使用。但杂化泛函在处理性质相差较大的异质结构上并不理想，GW近似可以解决这一问题。实际中，GW近似在DFT计算后作为微扰执行，由此得到的能带计算结果与实际相符得很好。
以上为DFT的主要理论和方法，在实际应用中，许多计算程序已被封装，方便调用，例如VASP (Vienna Ab-initio Simulation Package)是目前进行DFT计算较为完备、最流行的商用软件之一，用户只需向其中输入研究对象、计算方法和待计算性质等命令即可进行计算。但合理应用的关键在于正确设置参数、选择合适的求解方法。例如，Shi等33将DFT与应力辅助扩散方程相结合，对几种集电器和相关合金中的锂扩散机理进行研究。其中根据金属材料(铜、银、锌等)特点、研究目标(体积变化、锂传输路径等)，使用GGA近似方法，并确定收敛判据、k点设置等相关参数。

### 微动弹性带

对于化学反应和原子迁移而言，在确定反应物（初始位置）和生成物（最终位置）的结构后，理论上两者间存在能量最小路径（minimum energy path,MEP），而过渡态为其上的最高点，即一阶鞍点。过渡态与反应物的能量之差即为反应能垒，是研究反应过程的最为基础、重要的参数。研究过渡态的分子结构、成键关系，有助于深入认识反应机理。因此，准确获得过渡态的结构十分重要。

微动弹性带（Nudged Elastic Band，NEB）及在此基础上发展的CI-NEB方法，是计算过渡态的常用方法。

首先，在反应物结构和生成物结构之间建立一系列结构（称为 image）；之后将相邻的image使用弹簧力进行连接，形成具有弹性的链条（即Elastic Band）；进而，对这一链条整体进行优化，使其受力最小，进而得到MEP；最后，结合能量、振动频率等信息，确定过渡态。

而CI-NEB方法则在NEB原方法之上，分解掉原子在特定方向上的受力，提高了过渡态搜索效率。

本课题将主要使用CI-NEB方法进行锂离子迁移过程的模拟和求解。

### 软件

在实际应用中，许多DFT计算程序已被封装为软件或脚本，以方便调用，例如VASP (Vienna Ab-initio Simulation Package)是目前进行DFT计算较为完备、最流行的商用软件之一，用户只需向其中输入研究对象、计算方法和待计算性质等命令即可进行计算。但合理应用的关键在于正确设置参数、选择合适的求解方法。
例如，Shi等33将DFT与应力辅助扩散方程相结合，对几种集电器和相关合金中的锂扩散机理进行研究。其中根据金属材料(铜、银、锌等)特点、研究目标(体积变化、锂传输路径等)，使用GGA近似方法，并确定收敛判据、k点设置等相关参数。

本课题将主要使用VASP软件进行材料体系的计算模拟，并用VTST提供的脚本重新编译VASP，以使用CI-NEB方法进行求解。

## 论文选题依据及安排

在最近的研究中，Yao等人2设计了金属有机钙钛矿型保护层，实验上证明该新型保护层在抑制枝晶生长、保证电池良好循环性能上有很好的效果。
然而，Yao等人的工作对锂离子在金属有机钙钛矿型保护层中的输运机理研究不足。他们的工作中仅就单个锂离子在MASnCl3和MAPbCl3中的输运路径进行初步计算模拟，在极性分子取向、多输运路径、协同输运等方面并未深入研究。因此，本课题在Yao等人的基础之上，通过计算模拟对有机金属卤化物钙钛矿型锂金属电极保护层锂离子输运的机制进行更为系统深入的研究。

论文安排如下：

1. 有机金属卤化物钙钛矿中存在大量氢键等相互作用，这可能对锂离子的输运机理等产生较大影响。因此，论文首先实现对其中氢键等成键的强度估计，并验证该方法的有效性。
2. 由于有机阳离子具有取向，锂离子在其中存在多个不等价的嵌入位置。论文将此就建立并计算分析锂离子嵌入的稳定模型，包括几何结构、电子结构、成键情况等。
3. 在锂离子嵌入模型的基础之上，建立并计算锂离子在不同点位间的迁移模型，并对其过渡态进行分析。论文将在最后说明氢键对锂离子输运过程的影响。


# chapter2

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

一般而言，同类型键的bcp处电子密度与键的强度呈正相关。
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

### vasp 计算结果的准确性

文献==emamianExploringNaturePredicting2019==中使用量子化学方法进行计算，而vasp软件通过DFT方法求解能带进行计算，两者计算方法存在差异。因此，有必要验证两种方法对于bcp处电子密度计算的一致性。

考虑到本课题研究的体系中多为 N-H···X（X=Cl,Br,I）类氢键，这里选用文献==emamianExploringNaturePredicting2019==中 FH-NH3（28号）、H2NH-F-（33号）和HF-HNH3+（30号）分子体系进行建模和vasp 计算，并求解bcp处电子密度。
建立$15\times15\times15 \r A$晶胞，使用The Materials Project数据库 == 脚注：https://materialsproject.org/ == 中分子数据。最终结果如下。

![](../../images/bcp-test1.png)

==表格==

根据计算结果，利用vasp进行的DFT计算获得的bcp处电子密度较文献==emamianExploringNaturePredicting2019==中使用的量子化学方法存在正向偏差，偏高 $ 13 ~ 21 \% $。该结果推测是由计算方法导致，一般而言，量子化学方法对分子体系的计算更为准确，而利用vasp进行的DFT计算，由于波函数展开方式、赝势等原因，对分子体系的计算可能存在偏差。当前误差对于本课题仍可接受，可用于成键强度的定性比较。

### 相关参数的精度检验

VASP对体系电子密度的计算结果，除受原子位置、赝势、波函数展开方式等影响之外，也可能受截断能、空间网格划分等计算参数影响。该部分将通过一系列实验，判断K点数量、截断能、空间网格划分（对应于KPOINTS输入文件，以及INCAR输入文件中ENCUT和NGXF、NGYF、NGZF参数）等对计算精度的影响，并由此确定合适的计算参数。

测试使用本课题研究的 Li+@MASnCl3 体系，以其中的 Li-H21 间 bcp 电子密度为测试对象，分别设置KPOINTS为 $2 \times 2 \times 2$、$3 \times 3 \times 3$、$4 \times 4 \times 4$、$5 \times 5 \times 5$、$6 \times 6 \times 6$；ENCUT为 450、500、550、600、650；NGF（NGXF、NGYF、NGZF参数均与NGF相等）为150、168、192、200、224。计算结果如下。

==图片并列放置==



![](../../images/kpoint-test.png)
![](../../images/encut-test.png)
![](../../images/ngf-test.png)

由结果可以看出，ENCUT和NGF参数对bcp电子密度影响最为显著（计算结果与软件默认参数所得结果相差约 15%），而KPOINTS对计算结果几乎无影响。
这里综合考虑计算精度和计算成本，将KPOINTS设置为$3 \times 3 \times 3$；ENCUT设置为600；NGF设置为192，进行VASP的电子自洽计算，进而求解bcp处电子密度。

### 与文献数据的对比

文献==svaneHowStrongHydrogen2017==通过分割有机阳离子和无机框架的方法，计算了 MAPbI3 等体系中的氢键键能，为 $ 0.09 ~ 0.27 eV $ 平均每个阳离子（MAPbI3体系为$0.27 eV$平均每个阳离子，$0.09 eV$平均每个氢键）。本课题针对 MAPbI3 体系建模计算，发现其中的有机阳离子提供的氢键配体数量更为复杂，而非文献==svaneHowStrongHydrogen2017==中给出的数量3；但是，通过将vasp求解得到的 bcp处电子密度 $0.012 ~ 0.017 a.u.$代入文献==emamianExploringNaturePredicting2019==所提供的电中性体系氢键键能拟合关系式，可得相应的单个氢键键能为$0.08 ~ 0.13 eV$，与文献值==svaneHowStrongHydrogen2017==$0.09 eV$相比略有高估，这与上文 VASP 高估 bcp 处电子密度的结论相一致。

## 结论

该部分实现并验证了根据vasp计算结果求解AIM理论中bcp处电子密度的方法，发现使用VASP的DFT计算较量子化学方法会高估bcp处电子密度；并将该方法应用于金属有机钙钛矿体系的氢键强度估计，通过与文献值比较，认为该方法可以简单、半定量地获得体系的氢键强度。
