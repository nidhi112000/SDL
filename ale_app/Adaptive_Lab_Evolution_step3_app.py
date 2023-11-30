#!/usr/bin/env python3

from pathlib import Path

from pathlib import Path
from tools.hudson_solo_auxillary.hso_functions import package_hso
from tools.hudson_solo_auxillary import solo_innoculate_from_stock
from wei import Experiment
import time


def main(): 
    # Specify all wokflow file paths

    wf_path_new_plate_stack5 = Path(
        "/home/rpl/workspace/BIO_workcell/ale_app/workflows/get_new_plate_stack5.yaml"
    )

    wf_path_new_plate_stack4 = Path(
        "/home/rpl/workspace/BIO_workcell/ale_app/workflows/get_new_plate_stack4.yaml"
    )

    wf_path_innoculate_from_stock = Path(
        "/home/rpl/workspace/BIO_workcell/ale_app/workflows/innoculate_from_stock.yaml"

    )
 
    #Creates a WEI Experiment at the 8000 port and registers the expermient with the title Growth_Curve
    exp = Experiment("127.0.0.1", "8000", "Adaptive_Lab_Evolution_step3")
    exp.register_exp()

    # Important payload variables
    payload = {
        "loop_num": loop_num,
        "innoculant_stock_columns": None,   # populated in loop below when i=0
        "shaker_speed": 30, 
        "plate_id": None
    }

    loop_num = 0

    while loop_num < 20: # there are 20 total cycles possible

        if loop_num == 0: # beginning of experiment
            """
            GET FIRST SUBSTRATE PLATES FROM STACK 5 AND 4, REMOVE LIDS, AND COMPLETE FIRST INNOCULATIONS
            """

            # Get new plate from stack 5 -> solo deck pos4, remove lid
            flow_info = exp.run_job(
                wf_path_new_plate_stack5.resolve(), 
                payload=payload, 
                simulate=False
            )  

            # generate necessary SOLO .hso files and update payload
            payload["innoculant_stock_columns"] = [1,2,3] 
            payload.plate_id = "1"

            # create hso files and package them for use in workflow
            hso, hso_lines, hso_basename = package_hso(
                solo_innoculate_from_stock.generate_hso_file, 
                payload, 
                "/home/rpl/wei_temp/solo_temp1.hso"
            )

            # add new hso details from above into payload
            payload["hso"] = hso
            payload["hso_lines"] = hso_lines
            payload["hso_basename"] = hso_basename

            # innoculate plate from stack 5, hidex reading, place in incubator
            flow_info = exp.run_job(
                wf_path_innoculate_from_stock.resolve(), 
                payload=payload, 
                simulate=False
            ) 

            # Get new plate from Stack 4
            flow_info = exp.run_job(
                wf_path_new_plate_stack4.resolve(), 
                payload=payload, 
                simulate=False
            )  

            # generate necessary SOLO .hso files and update payload
            payload["innoculant_stock_columns"] = [5,6,7]  # changed for next plate innoculation
            payload.plate_id = "2"

            hso, hso_lines, hso_basename = package_hso(
                solo_innoculate_from_stock.generate_hso_file, 
                payload, 
                "/home/rpl/wei_temp/solo_temp1.hso"
            )

            # add new hso details from above into payload
            payload["hso"] = hso
            payload["hso_lines"] = hso_lines
            payload["hso_basename"] = hso_basename

            # innoculate plate from stack 4, hidex reading, place in incubator
            flow_info = exp.run_job(
                wf_path_innoculate_from_stock.resolve(), 
                payload=payload, 
                simulate=False
            ) 

            # incubate for 6 hours (or 21600 seconds)
            time.sleep(21600)  

            loop_num += 1   # done with this loop

        if loop_num != 0:  # if not the very beginning of the protocol
            if loop_num % 4 == 0:  # innoculation transfer between plate
                
                # unload plate from incubator -> stack 4 (old)

                # get new plate from stack 5 (new)
                
                # innoculate 

                # repeat for other plate

                # incubate 6 hours

                loop_num += 1

            elif loop_num % 4 != 0:  # innoculation transfer within plates 
                
                # TODO

                loop_num += 1

            else: 
                # something went very wrong





if __name__ == "__main__":
    main()
