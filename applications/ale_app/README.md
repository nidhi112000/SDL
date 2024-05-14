# Adaptive Lab Evolution Applicaiton

## Project Description

We propose to apply the self-driven-lab (SDL) capability to develop a synthetic biology platform using the highly naturally competent *Acinetobacter baylyi* (ADP1) as a host strain. As our first step for this engineering effort, we will develop novel degradation pathways utilizing the concept of adaptive lab evolution (ALE). We plan to automate the process of continuously monitoring, assaying, sampling, and transferring successful evolved strains to fresh media. Media conditions will be automatically adjusted as needed to further drive the ALE process (e.g. increasing toxins/inhibitors or decreasing degradation targets to further drive selection). As this process continues, samples will be collected and sequenced to determine specifically what the most successful current variants are. The second step involves the use of “connector primers” that allow for the random insertion of multiple copies of multiple candidate genes into specific chosen locations on the ADP1 genome. This permits us to grow ADP1 in the presence of a large library of primers and candidate genes for desired functions, and continuously select for strains that integrate the ideal combinations of genes to optimally maximize a desired activity.

The current experiment, described in more detail below, will automate the preparation of Biolog/substrate plates, the inoculation of the Biolog plates followed by incubation and transfer of culture to fresh media at fixed interval for an extended period of time. Bacterial growth will be monitored before and after each transfer.

## Basic Application and Robotic Steps 

1. Preparation of substrate plates

    In one step, all wells of 96-well flat bottom microplates will be filled with pre-prepared substrate solution. 

2. Inoculation of substrate plate

    First column of the substrate plate will be inoculated with ADP1 and ADP1 with DNA (in triplicate)
    
3. Absorbance readings and new inoculation at set time intervals

    The inoculated substrate plates will be transferred to a plate reader and T0 will be recorded and then it will be incubated for 24 hours. After incubation plate will be transferred to a plate reader for an absorbance reading at O.D 590 nm (T1). After the reading, the next column in the substrate plate will be inoculated from the previous column and then returned to the incubator. This cycle of incubation and absorbance reading will continue until all columns of all substrate plates prepped in step 1 are used. 


### 1. Preparation of substrate plate and inoculation

Two application python files must be run in succession to complete this section of the experiment. Running the first application file (Adaptive_Lab_Evolution_step1_app.py) will execute robotic actions required to produce Substrate/Biolog plate. Second application file (Adaptive_Lab_Evolution_step2_app.py) which will inoculate the substrate plate.

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

##### 1c. Run Second Application File
TODO













