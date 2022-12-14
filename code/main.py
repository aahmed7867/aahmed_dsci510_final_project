from get_data import *
from run_analysis import *
from visualize_results import *


def main():
    '''
    This function combines all the subprocesses into a single main process, using previously defined functions.
    '''
    # load_data()   # to load the data from the API
    dfs = read_csv_files()  # reading all the CSV files and making the dataframes dictionary
    # combining dataframes and making the 'alltime' dictionaries
    dfs = combine_df_city(dfs)

    cities = ['Los_Angeles', 'New_Delhi', 'London',
              'Sydney', 'Rio_De_Janeiro', 'Cairo']

    max_records = {'Los_Angeles': {}, 'New_Delhi': {},
                   'London': {}, 'Sydney': {}, 'Rio_De_Janeiro': {}, 'Cairo': {}}
    for city in cities:
        # finding the maximum 5 records for each city in 'alltime' time range
        available_columns = dfs['alltime'][city].columns
        for col in list(available_columns)[1:]:
            df_max = max_n_param_in_city(
                dfs, col, city, 'alltime', 1)

            max_records[city][col] = df_max[col].values[0]

    print('Maximum "tavg" values for the 6 cities in each year.\n')
    for city in cities:
        for y in range(2018, 2021):
            df_max = max_n_param_in_city(
                dfs, 'tavg', city, y, 1)

            print('Maximum "tavg" in', city, 'in the year',
                  y, 'is', df_max['tavg'].values[0])

        print()

    print('Minimum "tavg" values for the 6 cities in each year.\n')
    for city in cities:
        for y in range(2018, 2021):
            df_min = min_n_param_in_city(
                dfs, 'tavg', city, y, 1)

            print('Minimum "tavg" in', city, 'in the year',
                  y, 'is', df_min['tavg'].values[0])

        print()

    bar_plot(max_records)
    # making some plots

    line_plot(dfs, 'alltime', cities, ['tavg'])
    # correlation_plot(dfs, 2020, 'Los_Angeles')
    scatter_plot(dfs, 'alltime', 'Sydney', ['tmin', 'tavg', 'tmax'])


main()