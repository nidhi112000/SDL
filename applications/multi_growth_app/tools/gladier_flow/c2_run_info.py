from gladier import GladierBaseTool, generate_flow_definition


def add_run_info(**data):
    """
    Extracts Raw OD(590) data from Hidex excel file into csv file

    :param str filename: filename of Hidex excel file to convert

    output: path of new csv file (str)

    """
    import os
    from pathlib import Path
    import pandas as pd
    import csv
    import re
    from io import StringIO


    plot_directory_path = data.get("proc_folder")
    csv_file = os.path.join(plot_directory_path, data.get('csv_file'))
    ba_csv_file =  os.path.join(plot_directory_path, "blank_adj_" + data.get('csv_file'))
    data_filename = data.get('csv_file').split('.')[0]
#    blank_adj_df, data_filename, plot_directory_path

    csv_df = pd.read_csv(csv_file)
    blank_adj_df = pd.read_csv(ba_csv_file)
    blank_adj_df = blank_adj_df.iloc[:, [3]]
    blank_adj_df.columns = ["Blank Adjusted Result"]

    results_data = pd.concat([csv_df, blank_adj_df], axis=1)

    experiment_info_string = data.get('experiment_run_df')

    if experiment_info_string == '':
        results_data.to_csv(data.get("proc_folder") + "/run_info_" + data.get('csv_file'), encoding="utf-8", index=False)
    else:
        experiment_info_df = pd.read_csv(StringIO(experiment_info_string))

        csv_df = pd.concat([results_data, experiment_info_df], axis=1)
        csv_df.to_csv(data.get("proc_folder") + "/run_info_" + data.get('csv_file'), encoding="utf-8", index=False)

    # experiment_info_df.to_csv(csv_filepath, encoding="utf-8", index=False)
    # excel_OD_data.to_csv(csv_filepath, encoding="utf-8", index=False)
    return data.get("proc_folder") + "/run_info_" + data.get('csv_file')



@generate_flow_definition
class C2_Add_Run_Info(GladierBaseTool):
    funcx_functions = [add_run_info]
    required_input = ['funcx_endpoint_compute']
