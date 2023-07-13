#!/usr/bin/env python3

from pathlib import Path
from rpl_wei import Experiment
import time
from tools.growth_curve_gladier_flow import c2_flow


def main():
    hidex_open = Path(
        "/home/rpl/workspace/BIO_workcell/growth_app/workflows/hidex_open.yaml"
    )
    hidex_close = Path(
        "/home/rpl/workspace/BIO_workcell/growth_app/workflows/hidex_close.yaml"
    )
    hidex_run = Path(
        "/home/rpl/workspace/BIO_workcell/growth_app/workflows/hidex_run.yaml"
    )

    final_test = Path("/home/rpl/workspace/BIO_workcell/growth_app/workflows/multiple_growth_curve/open_close_hidex.yaml")


    exp = Experiment("127.0.0.1", "8000", "Hidex_Test")
    exp.register_exp()

    # flow_info = exp.run_job(hidex_open.resolve(), payload=None, simulate=False)
    # flow_status = exp.query_job(flow_info["job_id"])
    # while (
    #     flow_status["status"] != "finished" and flow_status["status"] != "failure"
    # ):
    #     flow_status = exp.query_job(flow_info["job_id"])
    #     time.sleep(3)

    # run_info = flow_status["result"]
    # run_info["run_dir"] = Path(run_info["run_dir"])

    # print(run_info)

    # # Close Hidex
    # flow_info = exp.run_job(hidex_close.resolve(), payload=None, simulate=False)

    # flow_status = exp.query_job(flow_info["job_id"])
    # while (
    #     flow_status["status"] != "finished" and flow_status["status"] != "failure"
    # ):
    #     flow_status = exp.query_job(flow_info["job_id"])
    #     time.sleep(3)

    # run_info = flow_status["result"]
    # run_info["run_dir"] = Path(run_info["run_dir"])

    # print(run_info)

    # flow_info = exp.run_job(hidex_run.resolve(), payload=None, simulate=False)

    # flow_status = exp.query_job(flow_info["job_id"])
    # while (
    #     flow_status["status"] != "finished" and flow_status["status"] != "failure"
    # ):
    #     flow_status = exp.query_job(flow_info["job_id"])
    #     time.sleep(3)

    # run_info = flow_status["result"]
    # run_info["run_dir"] = Path(run_info["run_dir"])
    # print(run_info)

    flow_info = exp.run_job(hidex_run.resolve(), payload=None, simulate=False)

    flow_status = exp.query_job(flow_info["job_id"])
    while (
        flow_status["status"] != "finished" and flow_status["status"] != "failure"
    ):
        flow_status = exp.query_job(flow_info["job_id"])
        time.sleep(3)

    run_info = flow_status["result"]
    run_info["run_dir"] = Path(run_info["run_dir"])

    print(run_info)
    hidex_file_path = run_info["hist"]["run Hidex"]["action_msg"]
    hidex_file_path = hidex_file_path.replace('\\', '/')
    hidex_file_path = hidex_file_path.replace("C:/", "/C/")
    flow_title = Path(hidex_file_path) #Path(run_info["hist"]["run_assay"]["step_response"])
    fname = flow_title.name
    flow_title = flow_title.parents[0]
    print("Hidex File Path: ", hidex_file_path)
    print("Split: ", str(fname.split('.')[0]))
    print("Flow Title: ", flow_title)
    print("Fname: ", fname)
    print("Experiment: ", exp)
    c2_flow(exp_name = "hidex_test_run", plate_n = "1", time = str(time.strftime("%H:%M:%S", time.localtime())), local_path=flow_title, fname = fname, exp = exp)





if __name__ == "__main__":
    main()
