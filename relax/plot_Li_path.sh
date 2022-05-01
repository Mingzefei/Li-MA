#!/bin/bash
#--------------------------------------------------
# @File : plot_Li_path.sh
# @Time : 2022/04/11 17:37:19
# @Auth : Ming 
# @Vers : 1.0
# @Desc : plot Li path from MASnCl3 neb
# @Usag : plot_Li_path.sh 00_CONTCAR 01_CONTCAR ... (> Li_path_CONTCAR)
#--------------------------------------------------

# here set the PATH and LANG
# PATH=
# LANG=zh_CN.UTF-8
# export PATH

head -n 6 $1
echo "8    24     8    48     8     $#"
sed -n '8,104p' $1
for i in $@
do
    sed -n '105p' $i
done