# BIO_workcell



<figure align="center">
<img src="https://github.com/AD-SDL/BIO_workcell/tree/main/bio_workcell/figures/UpdatedHudsonWithLabels.png"  width="75%" height="75%" alt="BIO workcell with Labels">

<figcaption>BIO workcell in Argonne's biology building</figcaption>
</figure>

The Bio workcell is located in Argonne National Laboratory's Biology Building and contains the following instruments as labeled above. 

1. Hudson PlateCrane EX
2. Hudson SOLO liquid handler 
3. Hidex Sense Microplate Reader 
4. Azenta a4S Automated Plate Heat Sealer
5. Azenta Automated Plate Seal Remove
6. LiCONiC StoreX STX88 Automated Incubator



## Running An Experiment

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

### Running the Experiment

You are now able to execute the experiment.

```
cd
cd workspace/BIO_workcell/*name of app*_app
source /opt/ros/humble/setup.bash  
source ~/wei_ws/install/setup.bash
python *name_of_app*.py
```



