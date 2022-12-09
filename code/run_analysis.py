import pandas as pd
import os


def read_csv_files():
    csv_files_list = os.listdir('data/')    
    df_dict = {2018: {}, 2019: {}, 2020: {}}    
    for fname in csv_files_list:
        df = pd.read_csv('data/'+fname)
        df.dropna(axis=1, inplace=True) 
        city = fname[0:-22] 
        year = int(fname.split('.')[0].split('_')[-1])
        df_dict[year][city] = df   

    return df_dict


def combine_df_city(df_dict):
    df_dict['alltime'] = dict()
    for city in df_dict[2018].keys():
        df_dict['alltime'][city] = pd.concat(
            [df_dict[2018][city], df_dict[2019][city], df_dict[2020][city]], ignore_index=True)

    return df_dict


def max_n_param_in_city(df_dict, param, city, year, n):
    df = df_dict[year][city].sort_values(param, ascending=False)
    return df.iloc[0:n, :]


def min_n_param_in_cityr(df_dict, param, city, year, n):
    df = df_dict[year][city].sort_values(param, ascending=True)
    return df.iloc[0:n, :]