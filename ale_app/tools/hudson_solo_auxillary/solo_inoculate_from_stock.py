"""
Generates SOLO hso files given command line inputs

Returns paths to newly generated .hso files
"""
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
        Generates SOLOSoft .hso file for first substrate inoculations from stock culture plate

    Args:
        payload (dict): input variables from the wei workflow
        temp_file_path (str): file path to temporarily save hso file to 
    """
    
    # extract payload variables
    try: 
        inoculant_stock_columns = payload['inoculant_stock_columns']
  
    except Exception as error_msg: 
        # TODO: how to handle this?
        raise error_msg


    # other program variables
    deepwell_z_shift = 0.5
    flat_bottom_z_shift = 2  # Note: 1 is not high enough (tested)
    inoculant_transfer_volume = 10  # TODO: check that this volume is right
    destination_columns = [1,5,9]

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

    for i in range(3): 
        soloSoft.getTip("Position1")
        soloSoft.aspirate(
            position="Position5",
            aspirate_volumes=DeepBlock_96VWR_75870_792_sterile().setColumn(
                inoculant_stock_columns[i], 
                inoculant_transfer_volume
            ),
            aspirate_shift=[0, 0, deepwell_z_shift],
        )
        soloSoft.dispense(
            position="Position4",
            dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
                destination_columns[i], 
                inoculant_transfer_volume
            ),
            dispense_shift=[0, 0, flat_bottom_z_shift],
        )

    soloSoft.shuckTip()
    soloSoft.savePipeline()
    
    