"""
# TODO: Check the position of the tip box

Generates SOLO hso files given command line inputs

Returns paths to newly generated .hso files
"""
import os
import sys
import time
import argparse
from liquidhandling import SoloSoft
from liquidhandling import Plate_96_Corning_3635_ClearUVAssay


# SOLO PROTOCOL STEPS    
def generate_hso_file(
        payload, 
        temp_file_path,
): 
    """generate_hso_file

    Description: 
        Generates SOLOSoft .hso file for substrate inoculations from used substrate plate into 
        a new substrate plate

    Args:
        payload (dict): input variables from the wei workflow
        temp_file_path (str): file path to temporarily save hso file to 
    """
    
    # extract payload variables
    # try: 
    #     pass
    #     # no variables needed from payload right now
    # except Exception as error_msg: 
    #     raise error_msg

    # other program variables
    flat_bottom_z_shift = 2  # Note: 1 is not high enough (tested)
    inoculant_transfer_volume = 10  
    tip_box_position = "Position1"

    # * Initialize soloSoft
    soloSoft = SoloSoft(
        filename=temp_file_path,
        plateList=[
            "TipBox.50uL.Axygen-EV-50-R-S.tealbox",  
            "Empty",
            "TipBox.50uL.Axygen-EV-50-R-S.tealbox",  
            "Plate.96.Corning-3635.ClearUVAssay",
            "DeepBlock.96.VWR-75870-792.sterile",
            "Empty",
            "Empty",
            "Empty",
        ],
    )

    # First transfer 
    soloSoft.getTip(tip_box_position)
    soloSoft.aspirate(
        position="Position6",
        aspirate_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            4, 
            inoculant_transfer_volume
        ),
        aspirate_shift=[0, 0, flat_bottom_z_shift],
    )
    soloSoft.dispense(
        position="Position4",
        dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            1,                 
            inoculant_transfer_volume
        ),
        dispense_shift=[0, 0, flat_bottom_z_shift],
    )

    # Second transfer 
    soloSoft.getTip(tip_box_position)
    soloSoft.aspirate(
        position="Position6",
        aspirate_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            8, 
            inoculant_transfer_volume
        ),
        aspirate_shift=[0, 0, flat_bottom_z_shift],
    )
    soloSoft.dispense(
        position="Position4",
        dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            5,                 
            inoculant_transfer_volume
        ),
        dispense_shift=[0, 0, flat_bottom_z_shift],
    )

    # Third transfer
    soloSoft.getTip(tip_box_position)
    soloSoft.aspirate(
        position="Position6",
        aspirate_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            12, 
            inoculant_transfer_volume
        ),
        aspirate_shift=[0, 0, flat_bottom_z_shift],
    )
    soloSoft.dispense(
        position="Position4",
        dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            9,                 
            inoculant_transfer_volume
        ),
        dispense_shift=[0, 0, flat_bottom_z_shift],
    )

    # shuck tip and save instructions to .hso file
    soloSoft.shuckTip()
    soloSoft.savePipeline()