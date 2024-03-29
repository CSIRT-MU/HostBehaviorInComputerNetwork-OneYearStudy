# Host Behavior In ComputerNetwork: One Year Study

by **Tomas Jirsik** and **Petr Velan**


An associate repository with dataset and analyses to the paper titled [Host Behavior In Computer Network: OneYearStudy](https://ieeexplore.ieee.org/document/9250634)



## Abstract

 An analysis of a host behavior is an essential key for modern network management and security. A robust behavior profile enables the network managers to detect anomalies with high accuracy, predict the host behavior, or group host to clusters for better management. Hence, host profiling methods attract the interest of many researchers, and novel methods for host profiling are being introduced. However, these methods are frequently developed on preprocessed and small datasets. Therefore, they do not reflect the real-world artifacts of the host profiling, such as missing observations, temporal patterns, or variability in the profile characteristics in time. To provide the needed insight into the artifacts of host profiling in real-world settings, we present a study of the host behavior in the network conducted on a one-year-long real-world network dataset. In the study, we inspect the availability of the data for host profiling, identify the temporal patterns in host behavior, introduce a method for stable labeling of the hosts, and asses the variability of the host characteristics in the course of the year using the coefficient of variance. Moreover, we make the one-year dataset containing nine characteristics used for host behavior analysis available for public use and further research. We also share the record of analyses presented in the paper.


## Prerequisities

* Jupyter notebook (http://jupyter.org/)
* Python >= 3.7 (https://www.python.org/)
* Numpy (http://www.numpy.org/)
* Pandas (https://pandas.pydata.org/)
* Matplotlib (https://matplotlib.org/)
* Seaborn (https://seaborn.pydata.org/)
* Scikit-learn (http://scikit-learn.org/)

* At least 8 GB RAM free for analysis.


## Setup

1) Go to dataset directory

```
$ cd dataset
```

2) Download dataset from [Zenodo](https://zenodo.org/record/3799932)

```
$ wget https://zenodo.org/record/3799932/files/host-network-traffic-2019.tar.gz
```

3) Unzip the dataset
```
 tar -zxvf host-network-traffic-2019.tar.gz
```

4) Create folder for the precomputed datasets
```
$ mkdir precomputed
```

5) Precompute data
```
$ cat dataset_list.txt | while read line; do python profile_characteristics_stability_preprocessing.py -i ./${line}-anon.csv -o ./precomputed/; done
```

6) Go to `./analyses/` and run any `.ipynb` notebook with the analyses

## How to cite

```bibtex
@ARTICLE{9250634,
  author={Jirsik, Tomas and Velan, Petr},
  journal={IEEE Transactions on Network and Service Management}, 
  title={Host Behavior in Computer Network: One-Year Study}, 
  year={2021},
  volume={18},
  number={1},
  pages={822-838},
  doi={10.1109/TNSM.2020.3036528}}
```

## Acknowledgements

Petr Velan was supported by the ERDF project "CyberSecurity, CyberCrime and Critical Information Infrastructures Center of Excellence" (No. CZ.02.1.01/0.0/0.0/16\_019/0000822). 

Tomas Jirsik was supported by the Sharing and Automation for Privacy Preserving Attack Neutralization project. This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 833418.
