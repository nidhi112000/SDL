from gladier import GladierBaseTool, generate_flow_definition

def gather_metadata(**data):

    from pathlib import Path
    import json
    import os
    import csv
    import re
    import scipy.stats as stats

    GENERAL_METADATA = {
    "creators": [{"creatorName": "BIO Team"}],
    "publicationYear": "2023", 
    "publisher": "Argonne National Lab",
    "resourceType": {
        "resourceType": "Dataset",
        "resourceTypeGeneral": "Dataset"
    },
    "subjects": [{"subject": "SDL"}],
    "exp_type": "Campaign2"

    }

    input_path = Path(data['proc_folder']).expanduser()
    datal = {}
    for file in os.listdir(input_path):
     if re.match(".*csv", file):
       with open(input_path / file) as f:
          reader = csv.reader(f)
          vals = []
          for row in reader:
             vals.append(row)
          vals[0][3] = "Result"
          vals[0][2] = "Reading Hour"
          y_results = []
          x_concentration = [] # in the future, can directly import the concentrations through data
          for i in range(1, (len(vals))):
            vals[i][0] = str(data.get('plate_n'))
            vals[i][2] = str(data.get('run_hour'))
        #     well = vals[i][1]
        #     row_index = chr(well[0])
        #     if ord(row_index) % 2 == 1:
        #         column_index = int(well[1])
        #         power_raise = column_index % 6
        #         if power_raise == 0:
        #             x_concentration.append(0)
        #         else:
        #             x_concentration.append(0.5**power_raise)
        #         cell_reading = float(vals[i][3])
        #         blank_reading = float(vals[i+12][3])
        #         y_results.append(cell_reading-blank_reading)
        #   slope, intercept, r_value, p_value, std_err = stats.linregress(x_concentration, y_results)
          datal["vals_component_test"] = vals[0]
          datal["best_fit_slope"] = '0.05'
          datal["best_fit_intercept"] = '0.2'
          datal["csvdata"] = vals
          
     elif re.match(".*contam.txt", file):
       with open(input_path / file) as f:
         datal["contam"] =  f.read()

    GENERAL_METADATA.update(datal)
    final_data = data["publishv2"]
    final_data['metadata'] = GENERAL_METADATA
    return final_data

@generate_flow_definition
class GatherMetaData(GladierBaseTool):
    funcx_functions = [gather_metadata]
    required_input = [
        'funcx_endpoint_compute'
    ]
