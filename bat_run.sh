#!/bin/bash
#--------------------------------------------------
# @File : bat_run.sh
# @Time : 2022/05/02 22:43:38
# @Auth : Ming 
# @Vers : 1.0
# @Desc : bat run bcp for data
# @Usag : bash bat_run.sh
#--------------------------------------------------

# here set the PATH and LANG
# PATH=
# LANG=zh_CN.UTF-8
# export PATH

relax_path=/mnt/c/Users/Hua/1_workbench/Li-MA/relax
data_path=/mnt/c/Users/Hua/1_workbench/Li-MA/data

# make parallel_dic
rm ${data_path}/parallel_dir 2>/dev/null # dir
rm ${data_path}/parallel_out* 2>/dev/null # out
rm ${data_path}/parallel_err* 2>/dev/null # err
rm ${data_path}/WARNNING 2>/dev/null # warnning
for i in ${data_path}/*
do
    if [[ ${i} == *"pos"* ]]; then
        cd ${i}
        pwd >> ${data_path}/parallel_dir
        # run_Li_bond
        # run_H_bond
        cd ../../
    elif [[ ${i} == *"neb"* ]]; then
        cd ${i}
        pwd >> ${data_path}/parallel_dir
        for j in ./*
        do
            if [ -d $j ]; then
                cd ${j}
                pwd >> ${data_path}/parallel_dir
                # run_Li_bond
                # run_H_bond
                cd ../
            fi
        done
        cd ../../
    elif [[ ${i} == *"ideal"* ]]; then
        cd ${i}
        pwd >> ${data_path}/parallel_dir
        # run_H_bond
        cd ../../
    fi
done

function run_Li_bond(){
    if [ -f "CHGCAR_sum" ] && [ -f "CONTCAR" ]; then
        python ${relax_path}/find_Li_bond.py -dist 3.1 -save Li_bcp_data.npz
        python ${relax_path}/AIM_bcp.py -file Li_bcp_data.npz
        python ${relax_path}/select_bcp_dat.py -file Li_bcp_data.npz
        echo ""
    else
        echo "WARNNING:`pwd`" >> ${relax_path}/../data/WARNNING
    fi
}

function run_H_bond(){
    if [ -f "CHGCAR_sum" ] && [ -f "CONTCAR" ]; then
        python ${relax_path}/find_H_bond.py -dist 3.1 -save H_bcp_data.npz
        python ${relax_path}/AIM_bcp.py -file H_bcp_data.npz
        python ${relax_path}/select_bcp_dat.py -file H_bcp_data.npz
        echo ""
    else
        echo "WARNNING:`pwd`" >> ${relax_path}/../data/WARNNING
    fi
}

function convert_png(){
    for file in `ls -a ./`
    do
        if [[ ${file} == *'.png' ]]; then
            echo `pwd` ${file}
            # convert -resize "811000@" ${file}.scale5 ${file}
            # convert -crop 640x638+320+0 ${file} ${file}
            cp ${file} ${file}.scale1.cut
        fi
    done
        
}


function CMD {        

	echo "Job $1 Ijob $2 start"

    job_path=`sed -n "${1}p" ${data_path}/parallel_dir`
    cd ${job_path}
    # pwd

    # run bcp
    if  [[ ${job_path} == *ideal* ]]; then
        cp d31_H_bcp_data.npz H_bcp_data.npz # save dist = 3.1
        # run_H_bond
    else
        cp d31_H_bcp_data.npz H_bcp_data.npz # save dist = 3.1
        cp d31_Li_bcp_data.npz Li_bcp_data.npz # save dist = 3.1
        # run_H_bond
        # run_Li_bond
    fi

    # convert
    # convert_png
	echo "Job $1 Ijob $2 end"
}



Njob=$(cat ${data_path}/parallel_dir | wc -l)    # ????????????
Nproc=4    # ?????????????????????????????????
PID=() # ??????PID?????????, ??????PID???????????????????????????????????????
for((i=1; i<=Njob; )); do
	for((Ijob=0; Ijob<Nproc; Ijob++)); do
		if [[ $i -gt $Njob ]]; then
			break;
		fi
		if [[ ! "${PID[Ijob]}" ]] || ! kill -0 ${PID[Ijob]} 2> /dev/null; then
			CMD $i $Ijob >>${data_path}/parallel_out_$Ijob 2>>${data_path}/parallel_err_$Ijob &
			PID[Ijob]=$!
			i=$((i+1))

            printf "\rNjob(%d)/Nproc(%d): %d/%d " $Njob $Nproc $i $Ijob
		fi
	done
done

wait
# out and err
cd ${data_path}
cat parallel_out_* > parallel_out
cat parallel_err_* > parallel_err
