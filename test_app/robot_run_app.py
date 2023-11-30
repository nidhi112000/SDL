#!/usr/bin/env python3

from pathlib import Path
from wei import Experiment
import time

# from tools.gladier_flow.growth_curve_gladier_flow import c2_flow
from tools.hudson_solo_auxillary.hso_functions import package_hso
from tools.hudson_solo_auxillary import solo_multi_step1, solo_multi_step2, solo_multi_step3
from tools.hudson_solo_auxillary import solo_step1, solo_step2, solo_step3


def main():
    hidex_run = Path(
        "/home/rpl/workspace/BIO_workcell/test_app/workflows/hidex_run.yaml"
    )
    
    liconic_run = Path(
        "/home/rpl/workspace/BIO_workcell/test_app/workflows/liconic_run.yaml"
    )

    peeler_run = Path(
        "/home/rpl/workspace/BIO_workcell/test_app/workflows/peeler_run.yaml"
    )

    platecrane_run = Path(
        "/home/rpl/workspace/BIO_workcell/test_app/workflows/platecrane_run.yaml"
    )

    sealer_run = Path(
        "/home/rpl/workspace/BIO_workcell/test_app/workflows/sealer_run.yaml"
    )

    solo_run = Path(
        "/home/rpl/workspace/BIO_workcell/test_app/workflows/solo_run.yaml"
    )

    exp = Experiment("127.0.0.1", "8000", "Hidex_Test")
    exp.register_exp()

    payload = {
        "treatment": "col1",  # string of treatment name. Ex. "col1", "col2"
        "culture_column": 4,  # int of cell culture column. Ex. 1, 2, 3, etc.
        "culture_dil_column": 1,  # int of dilution column for 1:10 culture dilutions. Ex. 1, 2, 3, etc.
        "media_start_column": 1,  # int of column to draw media from (requires 2 columns, 1 means columns 1 and 2) Ex. 1, 3, 5, etc.
        "treatment_dil_half": 1,  #  int of which plate half to use for treatment serial dilutions. Options are 1 or 2.
        "tip_box_position": "3", # string of an integer 1-8 that identifies the position of the tip box when it is being refilled
    }

    # #Uncomment if Using Hudson Solo Liquid Handling

    # # Creating HSO Packages to send liquid handling protocols to the Hudson Solo.
    # # There are 3 separate hso files added because Hudson Solo caps the amount of steps per protocol.
    # exp.events.log_local_compute("package_hso")
    # hso_1, hso_1_lines, hso_1_basename = package_hso(
    #     solo_step1.generate_hso_file, payload, "/home/rpl/wei_temp/solo_temp1.hso"
    # )
    # hso_2, hso_2_lines, hso_2_basename = package_hso(
    #     solo_step2.generate_hso_file, payload, "/home/rpl/wei_temp/solo_temp2.hso"
    # )
    # hso_3, hso_3_lines, hso_3_basename = package_hso(
    #     solo_step3.generate_hso_file, payload, "/home/rpl/wei_temp/solo_temp3.hso"
    # )

    # # Add the HSO Packages to the payload to send to the Hudson Solo
    # payload["hso_1"] = hso_1
    # payload["hso_1_lines"] = hso_1_lines
    # payload["hso_1_basename"] = hso_1_basename

    # payload["hso_2"] = hso_2
    # payload["hso_2_lines"] = hso_2_lines
    # payload["hso_2_basename"] = hso_2_basename

    # payload["hso_3"] = hso_3
    # payload["hso_3_lines"] = hso_3_lines
    # payload["hso_3_basename"] = hso_3_basename

    flow_info = exp.start_run(liconic_run.resolve(), payload=payload, simulate=False)

    flow_status = exp.query_run(flow_info["run_id"])
    while (
        flow_status["status"] != "finished" and flow_status["status"] != "failure"
    ):
        flow_status = exp.query_run(flow_info["run_id"])
        time.sleep(3)

    run_info = flow_status["result"]
    run_info["run_dir"] = Path(run_info["run_dir"])

    print(run_info)
    
    #Uncomment if Hidex is being Run
    
    # hidex_file_path = run_info["hist"]["run Hidex"]["action_msg"]
    # hidex_file_path = hidex_file_path.replace('\\', '/')
    # hidex_file_path = hidex_file_path.replace("C:/", "/C/")
    # flow_title = Path(hidex_file_path) #Path(run_info["hist"]["run_assay"]["step_response"])
    # fname = flow_title.name
    # flow_title = flow_title.parents[0]

    # c2_flow(exp_name = "hidex_test_run", plate_n = "1", time = str(time.strftime("%H_%M_%S", time.localtime())), local_path=flow_title, fname = fname, exp = exp)





if __name__ == "__main__":
    main()
