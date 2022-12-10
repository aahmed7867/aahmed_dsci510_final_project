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

    # as an example, the following operations are simulated

    # finding maximum records in Cairo city for 'alltime' time range
    print(max_n_param_in_city(dfs, 'tavg', 'Cairo', 'alltime', 10))
    # making some plots
    line_plot(dfs, 'alltime', 'Los_Angeles', ['tavg', 'wspd'])
    correlation_plot(dfs, 2020, 'Los_Angeles')
    scatter_plot(dfs, 2020, 'Sydney', ['tmin', 'tavg', 'tmax'])

main()