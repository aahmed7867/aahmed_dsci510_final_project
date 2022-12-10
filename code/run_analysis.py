import pandas as pd
import os


def read_csv_files():
    '''
    This function reads all the CSV files in the specified folder and make dataframes from them.
    These  dataframes are stored in a dictionary by using year and city as keys.
    '''
    csv_files_list = os.listdir('data/')    # CSV file list
    df_dict = {2018: {}, 2019: {}, 2020: {}}    # output dictionary
    for fname in csv_files_list:
        # reading each CSV file and converting them into dataframes
        df = pd.read_csv('data/'+fname)
        df.dropna(axis=1, inplace=True) # dropping null columns
        city = fname[0:-22] # getting the city name from the file name
        year = int(fname.split('.')[0].split('_')[-1]) # getting the year from the file name
        df_dict[year][city] = df   # storing the dataframe

    return df_dict


def combine_df_city(df_dict):
    '''
    This function combines all three dataframes (2018, 2019, 2020) for each city and 
    store them using 'alltime' and city as keys.
    '''
    df_dict['alltime'] = dict()
    for city in df_dict[2018].keys():
        # combining three dataframes vertically
        df_dict['alltime'][city] = pd.concat(
            [df_dict[2018][city], df_dict[2019][city], df_dict[2020][city]], ignore_index=True)

    return df_dict


def max_n_param_in_city(df_dict, param, city, year, n):
    '''
    This function finds the maximum n records of a parameter in the specified dataframe by year and city.
    '''
    df = df_dict[year][city].sort_values(param, ascending=False)
    return df.iloc[0:n, :]


def min_n_param_in_cityr(df_dict, param, city, year, n):
    '''
    This function finds the minimum n records of a parameter in the specified dataframe by year and city.
    '''
    df = df_dict[year][city].sort_values(param, ascending=True)
    return df.iloc[0:n, :]

    #Github link - 