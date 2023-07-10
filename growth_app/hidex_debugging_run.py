#!/usr/bin/env python3

from pathlib import Path

# from rpl_wei.wei_workcell_base import WEI
from tools.c2_flow import c2_flow
from pathlib import Path
from rpl_wei import Experiment
import time


def main():
    hidex_run = Path(
        "/home/rpl/workspace/BIO_workcell/growth_app/workflows/multiple_growth_curve/open_close_hidex.yaml"
    )

    exp = Experiment("127.0.0.1", "8000", "Hidex_Test")
    exp.register_exp()

    # Run Hidex
    for i in range(1,11):
        print("Running Hidex Assay ", i)
        flow_info = exp.run_job(hidex_run.resolve(), payload=None, simulate=False)
        print("Finished Running Hidex Assay ", i)
        flow_status = exp.query_job(flow_info["job_id"])
        while(flow_status["status"] != "finished" and flow_status["status"] != "failure"):
            flow_status = exp.query_job(flow_info["job_id"])
            time.sleep(3)

        run_info = flow_status["result"]
        run_info["run_dir"] = Path(run_info["run_dir"])
        hidex_file_path = run_info["hist"]["run Hidex"]["action_msg"]
        hidex_file_path = hidex_file_path.replace('\\', '/')
        hidex_file_path = hidex_file_path.replace("C:/", "/C/")
        flow_title = Path(hidex_file_path) #Path(run_info["hist"]["run_assay"]["step_response"])
        fname = flow_title.name
        flow_title = flow_title.parents[0]
        print("Sending Query ", i, " to Globus")
        c2_flow("hidex_test", str(fname.split('.')[0]), hidex_file_path, flow_title, fname, exp)
        print("Sent Query ", i, " to Globus")


if __name__ == "__main__":
    main()
