# Multi-Plate Growth Assay Application
## Alp Demirtas

## Initial Setup and Finished Run Information
![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/1e7b20f2-3f38-4797-a133-181871c163d1)

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

## Running the application

The application uses an Excel template to run an experiment. Please download the template here: 

[Download Excel File](https://raw.githubusercontent.com/AD-SDL/BIO_workcell/main/multi_growth_app/user_media/templates/Template%20Experiment%20Run%20Document.xlsx)

The first sheet of the Excel template, titled "Completed_Run_Layout," provides a master framework for the experimental run.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/ac13c17b-18e3-49c4-9e74-6356ce015b7a)


Scientists can indicate the total amount of runs they would like to incorporate in their experiment by using the dropdown arrow in in Cell B1 to select a number 1 through 12.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/a4b49cb8-1136-4a1e-944d-f1698def06c7)

This will autopopulate a series of run numbers in Row 3 that correspond to the experiment plate number. For example, run number 1 is the 1st plate that will be ran, run number 2 is the 2nd plate that will be ran, and so on.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/c303d200-10b5-4292-bd32-596ea9bca96e)

For each run number in the chart, there will need to be a corresponding Antibiotic Type and Cell Culture Type that will be specified by using the dropdown arrow to select a number 1 through 12. This number will indicate the column number on the well plate corresponding to the cell or antibiotic type that the scientist would want to include. 

Please ensure that all data in Rows 4 and 5 has an accompanied Row Number in the Excel file.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/785fdfb9-95c4-45d8-92a9-9fa2a0a46347)

To set the incubation time of the cells, modify Cell B2 with a number indicating the hours needed for incubation.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/af0a2d57-c900-4f31-9750-1c991207a794)

If a scientist wanted to have two runs, the first with a cell culture found in column 2 and antibiotic found in column 6 and the second with a cell culture found in column 4 and antibiotic found in column 1, with an incubation time of 12 hours, this is how they would fill out their Excel template.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/3947ac4f-fa6d-48f3-a0aa-557dacadb9c1)


The other sheets in the Excel file provide a schematic in the shape of a 96 deep well plate of the cell and antibiotic types that will be used in a specific run number. While these sheets are not currently being used, they have the framework for scientists to specify their desired concentrations of cell type and antibiotic at a certain index of the deep well plate.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/3a5d7b95-9258-44c1-b700-517e4e93cfc9)

Once the Excel document has been filled out, it should be added to the active_runs folder in the Potts computer located in BIO 446. The program will run the oldest file in the folder once it begins to run.

![image](https://github.com/AD-SDL/BIO_workcell/assets/113743603/2d0ffdc4-1888-42bf-8126-68ad14c04556)


## Starting the Terminal Windows and C# Clients

To start a successful run, three terminal windows will need to be started in addition to starting C# clients on the Windows computer.

In the first terminal window, navigate to home/workspace/BIO_workcell/scripts and execute the prompt ./run_bionuc.sh. This will activate all of the ROS (Robot Operating System) nodes, the Sealer, Peeler, PlateCrane, and Liconic. 

In the second terminal window, navigate to home/workspace/BIO_workcell/scripts and execute the prompt ./run_wei_server.sh. This will activate the WEI server and worker, which will handle the execution of the Yaml Workflows.

Switch over to the Windows computer and start the Hudson Solo and Hidex C# cleints.

In the third terminal window, navigate to home/workspace/BIO_workcell/multi_growth_app and execute the prompt python multi_growth_app.py. This will run the experiment.

## Global Variables
ORIGINAL_ANTIBIOTIC_CONCENTRATION - Array with length of 12 that specifies the original stock concentration of each antibiotic type in its respective column. Must be filled in at the start of the experiment run. Example: [1, 0, 0, 1, 0, 0, 0, .3, 0, 0, .75, 0] indicates that there is antibiotic concentration of 1 M in column one, 1 M in column four, 0.3 M in column eight, and 0.75 M in column 11 of the stock antibiotic concentration plate.

ORIGINAL_CELL_CONCENTRATION - Array with length of 12 that specifies the original stock concentration of each cell type in its respective column. Must be filled in at the start of the experiment run. Example: [1, 0, 0, 1, 0, 0, 0, .3, 0, 0, .75, 0] indicates that there is cell concentration of 1 M in column one, 1 M in column four, 0.3 M in column eight, and 0.75 M in column 11 of the stock cell concentration plate.

TOTAL_CELL_COLUMN_CONCENTRATION - An 8 row x 12 column array detailing the cell concentration across each row of a 96 deep well plate for each row

TOTAL_TREATMENT_COLUMN_CONCENTRATION - An 8 row x 12 column array detailing the antibiotic concentration across each row of a 96 deep well plate for each row

CULTURE_PAYLOAD - An array that details which cell culture column the Hudson Solo should use for each liquid handling run

MEDIA_PAYLOAD - An array that details which antibiotic treatment column the Hudson Solo should use for each liquid handling run

HIDEX_UPLOADS - An array that holds the titles for the readings uploaded to Globus

COMPLETED_CELL_COLUMNS - An array that keeps track of which cell columns were used for which plate number each run during the experiment

COMPLETED_ANTIBIOTIC_COLUMNS - An array that keeps track of which cell columns were used for which plate number each run during the experiment

PLATE_BARCODES - An array that keeps track of the plate barcode for its specific plate number

CREATED_COMPLETED_FILE - A Boolean that keeps track of whether the completed_run Excel document has been completed

COMPLETED_FILE_NAME - A string that keeps track of the name of the completed_run  Excel document

EXPERIMENT_FILE_PATH - A string that keeps track of the file path for the Excel document containing the experimental outline

## Functions

def run_experiment(total_iterations, incubation_time_sec) - This function runs the experimental workflow continuously for a specified number of iterations and incubation time (in seconds). It requires that the CULTURE_PAYLOAD and MEDIA_PAYLOAD be filled with entries between 1 and 12 corresponding to the desired column of cells or antibiotic and must be greater than or equal to the length of the total_iterations.

def determine_payload_from_excel() - This function reads the oldest Excel file in the active_runs folder and populates the CULTURE_PAYLOAD and MEDIA_PAYLOAD global variables. It also returns the number of iterations specified in the Excel document and the incubation time in seconds for the set of runs.

def delete_experiment_excel_file() - This function deletes the Excel document specifying the run once the run has finished. It should be called at the end of a run to ensure the same experiment is not accidentally repeated twice. 

def process_experimental_results() - This function compiles the T0 and T12 run data for each run from the https://acdc.alcf.anl.gov/ Portal and synthesizes it into one Completed_Run Excel document in the completed_runs folder. This allows for scientists to receive a compiled summary for each of their runs in one document.

The following functions are called within run_experiment():

def dispose(completed_iterations) - If the amount of completed T0 Readings is a factor of 2, it will dispose the tip box in Index 3 of the Hudson Solo into Stack 1 and will dispose the serial dilution plate in Index 6 of the Hudson Solo into Stack 2. If the amount of completed T0 Readings is a factor of 6, it will dispose the growth media deep well plate in Index 2 of the Hudson Solo into Stack 2. 

def setup(iteration_number) - For all iterations, the PlateCrane will uncover a 96 deep well plate and place it on Index 4 of the Hudson Solo. If the amount of completed T0 Readings is a factor of 2, the PlateCrane will set up the tip box on Index 3 of the Hudson Solo and serial dilution plate on Index 6 of the Hudson Solo. If the amount of completed T0 Readings is a factor of 6, the PlateCrane well set up the growth media plate on Index 2 of the Hudson Solo. 

def T0_Reading(liconic_plate_id) - Will run the liquid handling setup for the desired antibiotic and cell types specified in the Excel file, produce a T0 reading on the Hidex, seal the 96 well plate, and finally place the plate in the incubator.

def T12_Reading(liconic_plate_id) - Will unload the plate off the incubator, peel the sealant off the 96 deep well plate, produce a T12 reading on the Hidex, and finally place the used well plate in Stack 2.

def run_WEI(file_location, payload_class, Hidex_Used = False, Plate_Number = 0) - Runs the Yaml workflow specified at the given file_location and passes in the given payload_class. If the Hidex is run within the experiment, Hidex_Used should be true to upload the data to Globus and the Plate_Number should be specified to identify the results.

def return_barcode() - When a camera is implemented into the experimental setup, this will return the barcode of a 96 deep well plate currently being run in the experiment.

def assign_barcode() - This will assign the returned barcode to its plate number by appendinng it to the PLATE_BARCODES array.

The following functions are called within process_experimental_results():

def read_globus_data(title_name = '', t0_reading = True, plate_number = 0) - Reads Hidex data with the given experimental title_name from the https://acdc.alcf.anl.gov/ Portal and returns it as a Pandas dataframe. 

def return_line_of_best_fit(worksheet) - Reads the line of best fit from the Treatment Concentration and Cell Density data in a workbook found in the format of those in the completed_runs folder

## Tools

ai_model - This folder provides the capabilities to run an AI Model within the application. It has four accessible methods: 

predict_experiment(num_prediction_requests, original_antibiotic_concentration, original_cell_concentration) - Makes a number of predictions defined by num_prediction_requests for stock antibiotic and cell concentrations defined by original_antibiotic_concentration and original_cell concentration. If calling the function from the application file, can use ORIGINAL_ANTIBIOTIC_CONCENTRATION and ORIGINAL_CELL_CONCENTRATION global variables.

train_model(complete_file_path) - Trains the model based on data from an Excel file specified at the location of complete_file_path

load_model() - Loads the AI model from a designated file path.

save_model() - Saves the AI model at a designated file path.

gladier_flow - This folder provides the capabilities to upload Hidex data to the https://acdc.alcf.anl.gov/ Portal using Globus.

hudson_solo_auxillary - This folder provides the capabilities to translate liquid handling protocols into a readable format for the Hudson Solo.

## Sample Code Workflows to Implement in main() Script

Method for Running Experiment from Excel:

def sample_method_for_growth_assay_run():

    iteration_runs, incubation_time = determine_payload_from_excel()

    run_experiment(iteration_runs, incubation_time)

    process_experimental_results()

    delete_experiment_excel_file()

Method for Exploring AI Integration:

def sample_method_implementing_ai():

    ai_actions.load_model()

    path_name = str(pathlib.Path().resolve()) + "\\multi_growth_app\\completed_runs\\" + "07-20-2023 at 13.19.40 Completed Run.xlsx"
    
    ai_actions.train_model(path_name)

    treatment_column, treatment_concentration, cell_column, cell_concentration, predictions = ai_actions.predict_experiment(3 ,
    ORIGINAL_ANTIBIOTIC_CONCENTRATION, ORIGINAL_CELL_CONCENTRATION)

    ai_actions.save_model()

## Debugging Guide

Code runs first PlateCrane step and then does not continue to run - Restart the ROS nodes by pressing CTRL + C in any of the tabs of the first terminal window defined above and typing the prompt tmux kill-session. After this, re-run ./run_bionuc.sh

Code is stuck on Refill Tips command in setup()- Close the Hudson Solo C# client and start it back up again.
