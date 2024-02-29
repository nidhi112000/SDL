# Growth Curve WEI Workflow

ONE ASSAY PLATE VERSION

## Initial Setup

Before running the Growth Curve workflow, visually check each machine in the bio workcell to ensure that it is powered on, and ready to perform its task in the workflow as follows. See documentation on the [bio workcell](https://github.com/AD-SDL/BIO_workcell.git)
### SOLO Liquid Handler
Our Hudson SOLO liquid handler was expanded to contain 8 deck positions, 7 of which are required for this growth curve workflow.

- Make sure the SOLO liquid handler is powered on and that the proper labware is placed on the SOLO deck as described below
#### Deck Layout

<figure align="center">
<img src="https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/figures/SOLO_deck_positions.png"  width="75%" height="75%" alt="SOLO deck positions with labels">

<figcaption>Labware layout on SOLO at start of Growth Curve workflow</figcaption>
</figure>

<br>

<figure align="center">
<img src="https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/figures/gc_layout_at_start.png"  width="75%" height="75%" alt="Labware layout at start of growth curve workflow">

<figcaption>Top-down view of SOLO deck positions 1 though 8</figcaption>
</figure>

- Position 1: Media stock plate
    - Example labware: Thermo Scientific™ Abgene™ 96 Well 2.2mL Polypropylene Deepwell Storage Plate
    - 2 adjacent columns filled with media per assay plate created
        (ex. media in columns 1 and 2 for 1 assay plate)

- Position 2: Heat Nest (EMPTY)
    - Note: Bio workcell contains a heat nest at SOLO deck position 2 but the heat nest is not required for this protocol

- Position 3: EMPTY at start
    - 180uL Filter Tip Box will be placed on this location by the plate crane at the start of the workflow
    - Example labware: Axygen™ Automation Tips - 180uL, sterile, filtered
    - 5 columns of tips used per assay plate created

- Position 4: EMPTY at start
    - an empty assay plate will be placed on this location by the plate crane at the start of the workflow

- Position 5: Culture stock plate
    - Example labware: Thermo Scientific™ Abgene™ 96 Well 2.2mL Polypropylene Deepwell Storage Plate
    - 1 column of cultured stock cells per assay plate created
    - Thaw plate before workflow begins if culture stock plate is taken from the freezer.

- Position 6: Treatment serial dilution plate
    - Example labware: Thermo Scientific™ Abgene™ 96 Well 2.2mL Polypropylene Deepwell Storage Plate
    - An empty half of treatment serial dilution plate is needed per assay plate created

- Position 7: Culture dilution plate
    - Example labware: Thermo Scientific™ Abgene™ 96 Well 2.2mL Polypropylene Deepwell Storage Plate
    - One empty column required per assay plate created

- Position 8: Treatment stock plate 
    - This labware contains the treatment which will be serial diluted and applied to the cells in the assay plate.
    - Thermo Scientific™ Abgene™ 96 Well 2.2mL Polypropylene Deepwell Storage Plate
    - One column of treatment stock plate used per assay plate created

### Plate Crane EX

#### Stack layout

- Stack 1: EMPTY at start 
    - Used assay plates will be stored here after the growth curve workflow is complete
- Stack 2: EMPTY at start 
    - Used tip boxes will be stored here after the growth curve workflow is complete
- Stack 3: EMPTY
- Stack 4: New 180uL tip boxes 
    - Axygen™ Automation Tips - 180uL, sterile, filtered
- Stack 5: Empty assay plates
    - Falcon™ 96-Well, Cell Culture-Treated, Flat-Bottom Microplate, Non-sterile

### Azenta Microplate Sealer

[Azenta Microplate Sealer](https://github.com/AD-SDL/a4s_sealer_module.git)

Loaded Seal
- Azenta Gas Permiable Heat Seals (4ti-0598) 
https://www.azenta.com/products/gas-permeable-heat-seal

### Azenta Microplate Seal Remover (Peeler)
- Ensure the peeler is powered on and set up according to the instructions in the repo above. Check to make sure the Peeler is loaded with a tape roll and that there is enough tape to complete the workflow (2 peels required per assay plate created.
### LiCONiC StoreX STX88 Incubator

[Liconic Incubator Repo](https://github.com/AD-SDL/liconic_module.git)

- Ensure the incubator is powered on and set up according to instructions in the above repo.
    

## Workflow Details 

### Main Application Files  
- [growth_curve_app.py: main application python file](https://github.com/AD-SDL/BIO_workcell/blob/casey_dev/growth_app/growth_curve_app.py)
- [create_plate_T0.yaml: workflow #1, create assay plate and T0 hidex sense reading](https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/workflows/create_plate_T0.yaml)
- [read_plate_T0.yaml: workflow #2, T12 hidex sense reading](https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/workflows/read_plate_T12.yaml)
- [solo_step1.py: liquid handling part 1](https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/tools/hudson_solo_auxillary/solo_step1.py)
- [solo_step2.py: liquid handling part 2](https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/tools/hudson_solo_auxillary/solo_step2.py)
- [solo_step3.py: liquid handling part 3](https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/tools/hudson_solo_auxillary/solo_step3.py)

### Workflow Steps 

<figure align="center">
<img src="https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/figures/growth_curve_one_plate.jpg"  width="75%" height="75%" alt="SOLO deck positions with labels">

<figcaption>Growth Curve application action sequence</figcaption>
</figure>

1. Plate Crane transfers new 180 uL tip box from Stack 4 to SOLO deck position 3
2. Plate Crane transfers new assay plate with lid from Stack 5 to SOLO deck position 4
3. Plate Crane removes lid from assay plate on SOLO deck position 4 and places it on Lid Nest 2
    <figure align="center">
<img src="https://github.com/AD-SDL/BIO_workcell/blob/main/growth_app/figures/stack_layout.jpeg"  width="75%" height="75%" alt="stack locations with labels">
4. SOLO liquid handler runs step 1 of assay plate prep
    - SOLO step 1: dilute cells and transfer to assay plate
        - Transfer 60uL media from 2 columns of media reservoir into each well of assay plate
        - Dilute specified column of stock cells from culture stock plate into one column of culture 1:10 dilution plate
        - Transfer 30uL of 1:10 diluted cells from culture 1:10 dilution plate into each well of assay plate
5. SOLO liquid handler runs step 2 of assay plate prep
    - SOLO step 2: prep treatment serial dilutions
        - Transfer media from two columns of media reservoir into specified half of treatment serial dilution plate
        - Transfer treatment from specified column of treatment dilution plate into first column (either 1 or 7) of specified half of treatment serial dilution plate
        - Serial dilute treatment from first column into all but last column of specified half of treatment serial dilution plate

6. SOLO liquid handler runs ste 3 of assay plate prep
    - SOLO step 3: transfer serial diluted treatment into assay plate
        - Transfer 90uL from each column of prepared treatment serial dilutions into each well in each half of assay plate, within each half working from lowest treatment concentration to highest. 
7. Hidex opens door 
8. Plate Crane transfers completed assay plate from SOLO deck position 4 to Hidex drawer
9. Hidex takes initial time 0 hour (T0) absorbance OD(590) readings of the assay plate
10. New Hidex data file is sent away for processing via Globus Tranfer service
11. Hidex opens door 
12. Plate Crane transfers assay plate from Hidex drawer to Sealer
13. Hidex closes door 
14. Sealer seals assay plate 
15. Plate Crane transfers assay plate from Sealer to Liconic Nest 
16. Liconic loads assay plate into specified stack and slot 
17. Liconic begins shaking 
18. Assay plate is incubated with shaking for 12 hours
19. Liconic unloads assay plate from specified stack and slot
20. Plate Crane transfers assay plate from Liconic Nest to Peeler 
21. Peeler peels assay plate
22. Hidex opens door
23. Plate Crane transfers assay plate from Peeler to Hidex drawer
24. Hidex takes final time 12 hour (T12) absorbance OD(590) readings of the assay plate 
25. Hidex opens door
26. Plate Crane transfers assay plate from Hidex drawer to Stack 1 (disposal)
27. Hidex closes door


## Running the Application

Once the initial setup is complete and all the labware are in the correct positions, follow these steps to make sure that all of the devices are ready and to run the experiment.

### Windows Clients

The clients for the SOLO and Hidex instruments are both located on the attached Windows computer, and must be activated from that computer.

### SOLO client

In order to activate the Hudson Solo client, open a Visual Studio window containing the Solo project, and run the code

### Hidex client

In order to activate the Hidex client, open a Visual Studio window containing the Hidex project, and run the code

### Running the ROS2 Nodes
Once both of the listeners on the Windows computer are running, navigate back to the Linux computer. We must start the ROS2 nodes for the remainder of the instruments and ensure that they are all in a READY state.

### Building the ROS Clients

open a terminal and from the home directory, enter the following in order to build and source all of your ROS clients and ensure there are no errors in their code.

```
cd wei_ws
colcon build
source ~/wei_ws/install/setup.bash
```

### Activating the ROS Nodes

In the same terminal, run the following commands to activate each of the required ROS nodes in their own tmux window

```
cd
cd workspace/BIO_workcell/scripts
./run_bionuc.sh
```

### Navigate in between TMUX shells
Once the TMUX session is started, you can navigate in between windows to check all the nodes. Number that correspond to the nodes are listed along bottom of the window.
- `Ctrl+B` 
- `Desired window number`

If you know that TMUX session is running in the background, you can reopen the session on your shell with below commands.

- `tmux a`
- `Ctrl+B`
- `w`
- Choose the window you want to display

### Activate the WEI Server

After ensuring all of your nodes are broadcasting a READY state, you can now activate the wei server

```
cd
cd workspace/BIO_workcell/scripts
./run_wei_server.sh
```

This should open up two additional tmux windows containing the WEI worker and server

### Running the Growth Assay

You are now able to execute the Growth Assay.

```
cd
cd workspace/BIO_workcell/growth_app
source /opt/ros/humble/setup.bash  
source ~/wei_ws/install/setup.bash
python growth_curve_app.py
```



