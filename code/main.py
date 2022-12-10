from get_data import *
from run_analysis import *
from visualize_results import *


def main():
    dfs = read_csv_files()  
    dfs = combine_df_city(dfs)

    print(max_n_param_in_city(dfs, 'tavg', 'Cairo', 'alltime', 10))
    line_plot(dfs, 'alltime', 'Los_Angeles', ['tavg', 'wspd'])
    correlation_plot(dfs, 2020, 'Los_Angeles')
    scatter_plot(dfs, 2020, 'Sydney', ['tmin', 'tavg', 'tmax'])

main()