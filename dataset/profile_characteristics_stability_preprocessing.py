#!/usr/bin/env python
# coding: utf-8

## $ mkdir precomputed
## $ cat dataset_list.txt |while read line; do python stability_analysis.py -i ./${line}-anon.csv -o ./precomputed/; done

import pandas as pd
import numpy as np
import argparse
from sklearn.preprocessing import QuantileTransformer
import datetime

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", help="path to dataset with data", type=str, required=True)
parser.add_argument("-o", "--output_folder", help="path to directory where to store data", type=str, required=True)

args = parser.parse_args()
input_dataset = args.input_file
output_dir = args.output_folder


# Read the csv
print(datetime.datetime.now(), "Reading csv: (this may take approx 20 min per one csv) ", input_dataset)
#df = pd.read_pickle(input_dataset)
df = pd.read_csv(input_dataset, header=[0], index_col=[0])
df.index = pd.to_datetime(df.index)
print(datetime.datetime.now(), "Csv read: ", df.shape)

#Save the dataset
file_ip_characteristics = output_dir + input_dataset.replace('.csv', '').split('/')[-1] + ".pkl"
print(datetime.datetime.now(), 'Saving original dataset to pickle: ', file_ip_characteristics)
pd.to_pickle(df, file_ip_characteristics)

# Aaggregate over the hour of the week, i.e 168 values in total
df['Hour'] = df.index.hour
df['DayOfWeek'] = df.index.dayofweek

print(datetime.datetime.now(), "Computing mean and std")
profile_mean = df.groupby(by=['DayOfWeek', 'Hour']).agg(np.nanmean)
profile_std  = df.groupby(by=['DayOfWeek', 'Hour', ]).agg(np.nanstd)

# Save mean to pickle
file_mean = output_dir + input_dataset.replace('.csv', '').split('/')[-1] + "_mean_by_hour.pkl"
print(datetime.datetime.now(), "Saving mean to: ", file_mean)
pd.to_pickle(profile_mean, file_mean)

# Save std to picle
file_std = output_dir + input_dataset.replace('.csv', '').split('/')[-1] + "_std_by_hour.pkl"
print(datetime.datetime.now(), "Saving std to: ", file_std)
pd.to_pickle(profile_std, file_std)

# Mean of the means over the hours in a week
print(datetime.datetime.now(), "Computing mean of means and stds")
mean_of_means = profile_mean.apply(np.nanmean)
# Mean of the stdandard deviation over the hours over the hours in a week
mean_of_stds = profile_std.apply(np.nanmean)

# Compute the IP characteristics
print(datetime.datetime.now(), "Compute ip_characteristics")
profile_mean = profile_mean.transpose()
profile_std = profile_std.transpose()

# Create columns for mean
columns_mean = []
for column in profile_mean.columns:
    new_colum = "Mean_D_" + str(column[0]) + "_H_" + str(column[1]) 
    columns_mean.append(new_colum)


profile_mean.droplevel(0, axis=1)
profile_mean.columns = columns_mean

# Create columns for std
columns_std = []
for column in profile_std.columns:
    new_colum = "Std_D_" + str(column[0]) + "_H_" + str(column[1]) 
    columns_std.append(new_colum)

profile_std.droplevel(0, axis=1)
profile_std.columns = columns_std

# Concat the datasets
ip_characteristics = pd.concat([mean_of_means, mean_of_stds, profile_mean, profile_std], axis=1)
ip_characteristics.columns = ['mean_of_means', 'mean_of_stds'] + columns_mean + columns_std

#Save the dataset
file_ip_characteristics = output_dir + input_dataset.replace('.csv', '').split('/')[-1] + "_ip_characterstics_stability.pkl"
print(datetime.datetime.now(), 'Saving ip_characteristics to: ', file_ip_characteristics)
pd.to_pickle(ip_characteristics, file_ip_characteristics)





