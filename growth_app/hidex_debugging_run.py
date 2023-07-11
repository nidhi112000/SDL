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
    flow_info = exp.run_job(hidex_run.resolve(), payload=None, simulate=False)
    flow_status = exp.query_job(flow_info["job_id"])
    while(flow_status["status"] != "finished" and flow_status["status"] != "failure"):
        flow_status = exp.query_job(flow_info["job_id"])
        time.sleep(3)



if __name__ == "__main__":
    main()
