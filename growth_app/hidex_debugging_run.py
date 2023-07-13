#!/usr/bin/env python3

from pathlib import Path
from rpl_wei import Experiment
import time

def main():
    hidex_open = Path(
        "/home/rpl/workspace/BIO_workcell/growth_app/workflows/hidex_open.yaml"
    )
    hidex_close = Path(
        "/home/rpl/workspace/BIO_workcell/growth_app/workflows/hidex_close.yaml"
    )


    exp = Experiment("127.0.0.1", "8000", "Hidex_Test")
    exp.register_exp()

    flow_info = exp.run_job(hidex_open.resolve(), payload=None, simulate=False)
    flow_status = exp.query_job(flow_info["job_id"])
    while (
        flow_status["status"] != "finished" and flow_status["status"] != "failure"
    ):
        flow_status = exp.query_job(flow_info["job_id"])
        time.sleep(3)

    run_info = flow_status["result"]
    run_info["run_dir"] = Path(run_info["run_dir"])

    print(run_info)

    # Close Hidex
    flow_info = exp.run_job(hidex_close.resolve(), payload=None, simulate=False)

    flow_status = exp.query_job(flow_info["job_id"])
    while (
        flow_status["status"] != "finished" and flow_status["status"] != "failure"
    ):
        flow_status = exp.query_job(flow_info["job_id"])
        time.sleep(3)

    run_info = flow_status["result"]
    run_info["run_dir"] = Path(run_info["run_dir"])

    print(run_info)




if __name__ == "__main__":
    main()
