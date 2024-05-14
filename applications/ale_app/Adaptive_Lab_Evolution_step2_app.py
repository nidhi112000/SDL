#!/usr/bin/env python3

from pathlib import Path

# from tools.gladier_flow.growth_curve_gladier_flow import c2_flow
from pathlib import Path
from tools.hudson_solo_auxillary.hso_functions import package_hso
# from tools.hudson_solo_auxillary import solo_step2
from tools.hudson_solo_auxillary import solo_step2
from rpl_wei import Experiment
import time

# The main script for running a single-cell plate growth assay. 
def main():
    #Accessing the paths for the T0 Workflow and the T12 workflow. 
    #The Paths will need to be changed if the corresponding Yaml file locations are changed
    wf_path_1 = Path(
        "/home/rpl/workspace/BIO_workcell/applications/applications/ale_zah_nidhi/workflows/create_substrate_plate_step2.yaml"
    )
 
    #Creates a WEI Experiment at the 8000 port and registers the expermient with the title Growth_Curve
    exp = Experiment("127.0.0.1", "8000", "Adaptive_Lab_Evolution")
    exp.register_exp()

    #Generate the payload for the T0 and T12 readings. The T0 and T12 Yaml files (at the position paths above) and hso_packages for the Hudson Solo (created below) will use the following values in the workflow
    payload = {
        # SUBSTRATE LOAD - STEP 1
        "substrates_start_column_1": 2,  # int of column to draw media from (requires 2 columns, 1 means columns 1 and 2) Ex. 1, 3, 5, etc.
 
    }

    # Creating HSO Packages to send liquid handling protocols to the Hudson Solo.
    exp.events.log_local_compute("package_hso")
    
    hso_2, hso_2_lines, hso_2_basename = package_hso(
        solo_step2.generate_hso_file, payload, "/home/rpl/wei_temp/solo_temp2.hso"
    )
    
    # Add the HSO Packages to the payload to send to the Hudson Solo
   

    payload["hso_2"] = hso_2
    payload["hso_2_lines"] = hso_2_lines
    payload["hso_2_basename"] = hso_2_basename

   
    # Run workflow file
    flow_info = exp.run_job(wf_path_1.resolve(), payload=payload, simulate=False)

if __name__ == "__main__":
    main()
