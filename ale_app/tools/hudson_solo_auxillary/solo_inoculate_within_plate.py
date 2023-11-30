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
        Generates SOLOSoft .hso file for substrate inoculations between columns within
        substrate plate based on loop number

    Args:
        payload (dict): input variables from the wei workflow
        temp_file_path (str): file path to temporarily save hso file to 
    """
    
    # extract payload variables
    try: 
        loop_num = payload['loop_num']
        start_column = loop_num % 4  # see note below

        """
        Transfers based on payload variable 'loop_num: 
            if loop_num % 4 == 1: 
                column 1 -> column 2
                    = (loop_num % 4) -> (loop_num % 4) + 1
                column 5 -> column 6 
                    = (loop_num % 4) + 4 -> (loop_num % 4) + 5
                column 9 -> column 10
                    = (loop_num % 4) + 8 -> (loop_num % 4) + 9
            if loop_num % 4 == 2: 
                column 2 -> column 3
                    = (loop_num % 4) -> (loop_num % 4) + 1 (same pattern as above)
                column 6 -> column 7 
                    = (loop_num % 4) + 4 -> (loop_num % 4) + 5  (same pattern as above)
                column 10 -> column 11
                    = (loop_num % 4) + 8 -> (loop_num % 4) + 9  (same pattern as above)
            if loop_num % 4 == 3: 
                column 3 -> column 4
                    = (loop_num % 4) -> (loop_num % 4) + 1 (same pattern as above)
                column 7 -> column 8 
                    = (loop_num % 4) + 4 -> (loop_num % 4) + 5  (same pattern as above)
                column 11 -> column 12
                    = (loop_num % 4) + 8 -> (loop_num % 4) + 9  (same pattern as above)   

            NOTE: I'm using the variable start_column = loop_num % 4 for simplicity
        """

    except Exception as error_msg: 
        # TODO: how to handle this?
        raise error_msg

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
        position="Position4",
        aspirate_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            start_column, 
            inoculant_transfer_volume
        ),
        aspirate_shift=[0, 0, flat_bottom_z_shift],
    )
    soloSoft.dispense(
        position="Position4",
        dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            start_column + 1,                 
            inoculant_transfer_volume
        ),
        dispense_shift=[0, 0, flat_bottom_z_shift],
    )

    # Second transfer 
    soloSoft.getTip(tip_box_position)
    soloSoft.aspirate(
        position="Position4",
        aspirate_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            start_column + 4, 
            inoculant_transfer_volume
        ),
        aspirate_shift=[0, 0, flat_bottom_z_shift],
    )
    soloSoft.dispense(
        position="Position4",
        dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            start_column + 5,                 
            inoculant_transfer_volume
        ),
        dispense_shift=[0, 0, flat_bottom_z_shift],
    )


    # Third transfer
    soloSoft.getTip(tip_box_position)
    soloSoft.aspirate(
        position="Position4",
        aspirate_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            start_column + 8, 
            inoculant_transfer_volume
        ),
        aspirate_shift=[0, 0, flat_bottom_z_shift],
    )
    soloSoft.dispense(
        position="Position4",
        dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
            start_column + 9,                 
            inoculant_transfer_volume
        ),
        dispense_shift=[0, 0, flat_bottom_z_shift],
    )

    # shuck tip and save instructions to .hso file
    soloSoft.shuckTip()
    soloSoft.savePipeline()