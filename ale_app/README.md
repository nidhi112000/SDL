# Adaptive Lab Evolution Applicaiton

## Project Description

We propose to apply the self-driven-lab (SDL) capability to develop a synthetic biology platform using the highly naturally competent *Acinetobacter baylyi* (ADP1) as a host strain. As our first step for this engineering effort, we will develop novel degradation pathways utilizing the concept of adaptive lab evolution (ALE). We plan to automate the process of continuously monitoring, assaying, sampling, and transferring successful evolved strains to fresh media. Media conditions will be automatically adjusted as needed to further drive the ALE process (e.g. increasing toxins/inhibitors or decreasing degradation targets to further drive selection). As this process continues, samples will be collected and sequenced to determine specifically what the most successful current variants are. The second step involves the use of “connector primers” that allow for the random insertion of multiple copies of multiple candidate genes into specific chosen locations on the ADP1 genome. This permits us to grow ADP1 in the presence of a large library of primers and candidate genes for desired functions, and continuously select for strains that integrate the ideal combinations of genes to optimally maximize a desired activity.

The current experiment, described in more detail below, will automate the preparation of Biolog/substrate plates, the inoculation of the Biolog plates followed by incubation and transfer of culture to fresh media at fixed interval for an extended period of time. Bacterial growth will be monitored before and after each transfer.

## Basic Application and Robotic Steps 

1. Preparation of 10 substrate plates

    In two steps, all wells of 10, 96-well flat bottom microplates will be filled with pre-prepared stocks of different substrate concentrations. 

2. Inoculation of first substrate plates

    Two of the substrate plates prepared in the previous step will be inoculated with ADP1 in triplicate (columns 1, 5, and 9)
    
3. Absorbance readings and new inoculation at set time intervals

    The inoculated substrate plates will be incubated for a standard amount of time then transferred to a plate reader for an absorbance reading. After the reading, the next column in the inoculated substrate plate (columns 2, 6, and 10) will be inoculated from the previous column (columns 1, 5, and 9) then returned to the incubator. This cycle of incubation and absorbance reading will continue until all columns of all substrate plates prepped in step 1 are used. 


### 1. Preparation of 10 substrate plates

Two application python files must be run in succession to complete this section of the experiment. Running the first application file (Adaptive_Lab_Evolution_step1_app.py) will execute robotic actions required to produce the first 5 substrate microplates. A technician will then replace the lids on the newly prepped substrate plates and transfer them to Stack 5. They will also prep the SOLO deck with another set of 5 empty microplates then run the second application file (Adaptive_Lab_Evolution_step1_app.py) which will execute all robotic steps required to prep the second set of 5 substrate microplates. 

#### Running steps:
##### 1a. Set Up SOLO Deck

<!-- TODO: center align images -->
![Labware layout on SOLO deck at start of substrate prep](https://github.com/AD-SDL/BIO_workcell/blob/main/ale_app/figures/substrate_prep_SOLO_deck.png)

SOLO deck layout: 
- Position 1: 180uL Tip Box, full
- Position 2: Empty
- Position 3: Substrate Stock Deep Well Plate
    - columns 1-5 will be used in this application file
- Position 4: 96-well flat bottom microplate, empty
- Position 5: 96-well flat bottom microplate, empty
- Position 6: 96-well flat bottom microplate, empty
- Position 7: 96-well flat bottom microplate, empty
- Position 8: 96-well flat bottom microplate, empty

##### 1b. Run First Application File
TODO


##### 1c. Manual Cleanup and SOLO Deck Setup in Preparation for Second Application File 
TODO: manual cleanup

![Place substrate plates 1-5 in stack 5](https://github.com/AD-SDL/BIO_workcell/blob/main/ale_app/figures/substrate_prep_manual_cleanup_1.jpg)

<!-- TODO: center align images -->
![Labware layout on SOLO deck at start of substrate prep](https://github.com/AD-SDL/BIO_workcell/blob/main/ale_app/figures/substrate_prep_SOLO_deck.png)

SOLO deck layout: 
- Position 1: 180uL Tip Box, full
- Position 2: Empty
- Position 3: Substrate Stock Deep Well Plate
    - columns 7-11 will be used in this application file
- Position 4: 96-well flat bottom microplate, empty
- Position 5: 96-well flat bottom microplate, empty
- Position 6: 96-well flat bottom microplate, empty
- Position 7: 96-well flat bottom microplate, empty
- Position 8: 96-well flat bottom microplate, empty

##### 1d. Run Second Application File
TODO


##### 1e. Manual Cleanup
TODO











