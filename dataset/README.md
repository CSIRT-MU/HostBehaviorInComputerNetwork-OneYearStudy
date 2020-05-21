# Dataset


The dataset contains of the 9 separate csv files. Each of the files contains one year record of one characteristic. The computed characteristics are:

**Aggregations** - created from five-minute total volumes aggregated over one-hour disjoint windows using mean/max/min aggregation functions
- \# of flows (FL) - number of flows for a given source IP 
- \# of packets (PKT) - number of packets for a given source IP
- \# of bytes (BYT) - number of packets for a given source IP
- flow duration (DUR) - average flow duration in seconds

**Distinct Counts** - count of distinct values for each variable in five-minute window aggregated over one-hour disjoint windows using mean/max/min aggregation functions
- \# of peers (PEER) - number of distinct communication peers for a given source IP
- \# of ports (PORTS) - number of distinct destination ports for a given source IP
- \# of protocols (PROTO) - number of distinct communication protocols for a given source IP
- \# of AS numbers (AS) - number of distinct destination AS numbers for a given source IP
- \# of countries (CTRY) - number of distinct destination countries for a given source IP

## Download and Setup

_To ensure the proper function of the analysis notebooks, the datasets needs to be located in this directory._

To obtain the One-year Dataset of Host Behavior, please follow the instructions below:

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

### Preprocess Datasets for Faster Loading

4) Create folder for the precomputed datasets
```
$ mkdir precomputed
```
5) Precompute data
```
$ cat dataset_list.txt | while read line; do python stability_analysis.py -i ./${line}-anon.csv -o ./precomputed/; done
```