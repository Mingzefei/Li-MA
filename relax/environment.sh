#!/bin/bash
#--------------------------------------------------
# @File : environment.sh
# @Time : 2022/05/18 17:42:41
# @Auth : Ming 
# @Vers : 1.0
# @Desc : environment of Li-MA
# @Usag : source relax/environment
#--------------------------------------------------

# here set the PATH and LANG
# PATH=
# LANG=zh_CN.UTF-8
# export PATH

if test $# -eq 0
then
    LM_path=`pwd`
    echo "LM_path=$LM_path"
else
    LM_path="$1"
    echo "LM_path=$LM_path"
fi

export LM_path

# set relax path
export PATH=${PATH}:"${LM_path}/relax"