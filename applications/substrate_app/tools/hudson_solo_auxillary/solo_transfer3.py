import os
import sys
import time
import argparse
from liquidhandling import SoloSoft
from liquidhandling import Reservoir_12col_Agilent_201256_100_BATSgroup, Plate_96_Corning_3635_ClearUVAssay, DeepBlock_96VWR_75870_792_sterile


# SOLO PROTOCOL STEPS    
def generate_hso_file(
        payload, 
        temp_file_path,
): 
    """generate_hso_file

    Description: 
        Generates SOLOSoft .hso file for step 3 of the substrate transfer workflow

        Basic steps:
            - transfer 150uL from substrate stock plate column 5 into each 12 columns of a 96 well plate at SOLO position 7
            - transfer 150uL from substrate stock plate column 6 into each 12 columns of a 96 well plate at SOLO position 8

    Args:
        payload (dict): input variables from the wei workflow
        temp_file_path (str): file path to temporarily save hso file to 
    """
    
    # extract payload variables  (a commented out example)
    # try: 
    #     # treatment = payload['treatment'] 
    #     # culture_column = payload['culture_column']
    #     # culture_dil_column = payload['culture_dil_column']
    #     # media_start_column = payload['media_start_column']
    #     # treatment_dil_half = payload['treatment_dil_half']
    # except Exception as error_msg:
    #     raise error_msg


# * Other program variables
    # general SOLO variables
    blowoff_volume = 10
    num_mixes = 3
    media_z_shift = 0.5
    reservoir_z_shift = 0.5  # z shift for deep blocks (Deck Positions 3 and 5)
    flat_bottom_z_shift = 2  # Note: 1 is not high enough (tested)

    # protocol specific variables
    substrate_transfer_volume = 150

    """
    SOLO STEP 3: TRANSFER SUBSTRATE STOCK INTO REPLICATE PLATES 4 AND 5  -----------------------------------------------------------------
    """
    # * Initialize soloSoft deck layout 
    soloSoft = SoloSoft(
        filename=temp_file_path,
        plateList=[
            "Empty",
            "DeepBlock.96.VWR-75870-792.sterile",       # substrate stock plate
            "TipBox.180uL.Axygen-EVF-180-R-S.bluebox",  # 180 uL tip box
            "Plate.96.Corning-3635.ClearUVAssay",       # substrate replicate plate
            "Plate.96.Corning-3635.ClearUVAssay",       # substrate replicate plate
            "Plate.96.Corning-3635.ClearUVAssay",       # substrate replicate plate
            "Plate.96.Corning-3635.ClearUVAssay",       # substrate replicate plate
            "Plate.96.Corning-3635.ClearUVAssay",       # substrate replicate plate
        ],
    )

    # * Fourth set of 12 substrate column transfers (Stock plate column 5 --> replicate plate in position 7)
    soloSoft.getTip("Position3")  
    for i in range(1, 13):  # repeat for all 12 columns of replicate plate
        soloSoft.aspirate(
            position="Position2",
            aspirate_volumes=Reservoir_12col_Agilent_201256_100_BATSgroup().setColumn(
                5, substrate_transfer_volume
            ),
            aspirate_shift=[0, 0, media_z_shift],
        )
        soloSoft.dispense(
            position="Position7",
            dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
                i, substrate_transfer_volume
            ),
            dispense_shift=[0, 0, flat_bottom_z_shift],
        )
    
    # * Fifth set of 12 substrate column transfers (Stock plate column 6 --> replicate plate in position 8)
    soloSoft.getTip("Position3")  # NOTE: Previous tips will be shucked automatically as part of .getTip() command
    for i in range(1, 13):  # repeat for all 12 columns of replicate plate
        soloSoft.aspirate(
            position="Position2",
            aspirate_volumes=Reservoir_12col_Agilent_201256_100_BATSgroup().setColumn(
                6, substrate_transfer_volume
            ),
            aspirate_shift=[0, 0, media_z_shift],
        )
        soloSoft.dispense(
            position="Position8",
            dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
                i, substrate_transfer_volume
            ),
            dispense_shift=[0, 0, flat_bottom_z_shift],
        )

    # * Dispense tips at end of protocol and process these instructions into a .hso file 
    soloSoft.shuckTip()
    soloSoft.savePipeline()
    