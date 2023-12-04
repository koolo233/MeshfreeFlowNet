## 使用描述

### 安装环境

```bash
conda create -n dedalus
conda activate dedalus

# install DedalusV2
## from conda
conda env config vars set OMP_NUM_THREADS=1
conda env config vars set NUMEXPR_MAX_THREADS=1
conda install -c conda-forge dedalus c-compiler "h5py=*=mpi*" "cython<3.0"
## or from repo
CC=mpicc pip3 install --no-cache http://github.com/dedalusproject/dedalus/zipball/v2_master/
```

### 生成数据
```bash
# Check the arguments / simulation parameters.
python rayleigh_benard.py -h
# Run with 4 mpi processes (additional flags can be added to change simulation params.)
mpiexec -n 4 python3 rayleigh_benard.py
# Merge processes
python -m dedalus merge_procs snapshots
# Convert into npz file to be consumed by the machine learning pipeline
python convert_to_npz.py -f 'snapshots/snapshots_s*.h5' -o 'rb2d_ra1e6_s42.npz'
```


## Dedalus Installation Instructions

需要安装[DedalusV2](https://dedalus-project.readthedocs.io/en/v2_master/pages/installation.html#installing-the-dedalus-package)，V3有较大变化

可以直接使用conda安装
```commandline
conda env config vars set OMP_NUM_THREADS=1
conda env config vars set NUMEXPR_MAX_THREADS=1
conda install -c conda-forge dedalus c-compiler "h5py=*=mpi*" "cython<3.0"
```

或是直接源码安装
`CC=mpicc pip3 install --no-cache http://github.com/dedalusproject/dedalus/zipball/v2_master/`

Please follow the following steps for installing Dedalus. Modifed instructions from [here](https://dedalus-project.readthedocs.io/en/latest/installation.html).

Before starting these steps, make sure that you have a working conda installation. If not follow the instructions on the [conda installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) page.
```bash
# Download and run the official installation script.
wget https://raw.githubusercontent.com/DedalusProject/conda_dedalus/master/install_conda.sh
bash install_conda.sh
```

## Create the simulation file for the ML pipeline
Follow the following steps to create a simulation
```bash
# Make sure dedalus environment is activated
conda activate dedalus
# Check the arguments / simulation parameters.
python rayleigh_benard.py -h
# Run with 4 mpi processes (additional flags can be added to change simulation params.)
mpiexec -n 4 python3 rayleigh_benard.py
# Merge processes
python -m dedalus merge_procs snapshots
# Convert into npz file to be consumed by the machine learning pipeline
python convert_to_npz.py -f 'snapshots/snapshots_s*.h5' -o 'rb2d_ra1e6_s42.npz'
```

## Create a video of the simulation
```bash
# Generate png frames
python plot_slices.py snapshots/*.h5
# Stich png frames into video
bash create_video.sh
```
