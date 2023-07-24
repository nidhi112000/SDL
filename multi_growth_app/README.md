# Picture

Created with `python ../../draw_flow/draw.py -i demo.json -o demo.jpg`

![application, as drawn by draw.py.](demo.jpg)



# Multi-Plate Growth Assay Application

## Initial Setup and Finished Run Information

The setup for the multiple plate growth assay application should be as follows:

Stack 1: At the beginning of the script, Stack 1 will remain empty. It is the disposal location for used tip boxes and 96 well plate covers.
Stack 2: At the beginning of the script, Stack 2 will remain empty. It is the disposal location for both used 96 well plates and 96 deep well plates 
Stack 3: At the beginning of the script, Stack 3 will store sealed serial dilution plates (96 deep well). One serial dilution plate will be needed for every 2 runs of the experiment. At the end of the script, Stack 3 will remain empty.
Stack 4: At the beginning of the script, Stack 4 will store tip boxes without a cover. One tip box will be needed for every 2 runs of the experiment. At the end of the script, Stack 4 will remain empty.
Stack 5: At the beginning of the script, Stack 5 will store 96 well plates with their plate cover. One 96 well plate will be needed for every run of the experiment. At the end of the script, Stack 5 will remain empty.
Lid Nest 1: At the beginning of the script, Lid Nest 1 will remain empty. At the end of the script, Lid Nest 1 will hold the first disposed serial dilution plate. 
Lid Nest 2: At the beginning of the script, Lid Nest 2 will hold the first-used sealed growth media plate (96 deep well). One growth media plate will be needed for every 6 runs of the experiment. At the end of the script, Lid Nest 2 will hold the second disposed serial dilution plate. 
Lid Nest 3: At the beginning of the script, Lid Nest 3 will hold the second-used sealed growth media plate (96 deep well). One growth media plate will be needed for every 6 runs of the experiment. At the end of the script, Lid Nest 3 will hold the fourth disposed serial dilution plate. It will not be able to hold the third disposed serial dilution plate because the sealed-growth media plate will not be used until after the first 6 runs of the experiment have been completed.

*Due to space allocations, the current experimental setup is configured to accomodate at most 12 well plates. At the end of 12 runs, a new cell culture serial dilution plate will be needed on the Hudson Solo, which the PlateCrane will not be able to reach.  

## Installing the nodes

TODO: Update for parker+strange+local


## Running the application

The application uses an Excel template to run an experiment. Please download the template here: 

The first sheet of the Excel template, titled "Completed_Run_Layout," provides a master framework for the experimental run.

Scientists can indicate the total amount of runs they would like to incorporate in their experiment by using the dropdown arrow in in Cell B1 to select a number 1 through 12. This will autopopulate a series of run numbers in Row 3 that correspond to the experiment plate number. For example, run number 1 is the 1st plate that will be ran, run number 2 is the 2nd plate that will be ran, and so on.

For each run number in the chart, there will need to be a corresponding Antibiotic Type and Cell Culture Type that will be specified by using the dropdown arrow to select a number 1 through 12. This number will indicate the column number on the well plate corresponding to the cell or antibiotic type that the scientist would want to include.

Please ensure that all data in Rows 4 and 5 has an accompanied Row Number in the Excel file.

## Running the Campaigns

For the PCR campaign:

```
source ~/wei_ws/install/setup.bash
./wc_client_run.py -wf workflows/pcr_workflow.yaml
```

For the Growth campaign:

```
source ~/wei_ws/install/setup.bash
./wc_client_run.py -wf /workflows/growth_workflow.yaml
```

For the MoveTest campaign:
```
source ~/wei_ws/install/setup.bash
./wc_client_run.py -wf /workflows/move_test.yaml
```


