
"""
Generates steps 1, 2, and 3 SOLO hso files given command line inputs

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
        Generates SOLOSoft .hso file for step 1 of the substrates workflow

        Step 1 of the growth curve protocol includes:
            - 1:10 dilution of cells from source culture plate
            - transfer of 1:10 diluted cells into assay plate

    Args:
        payload (dict): input variables from the wei workflow
        temp_file_path (str): file path to temporarily save hso file to 
    """
    
        # extract payload variables
    try: 
        # treatment = payload['treatment'] 
        substrates_start_column = payload['substrates_start_column_2']
        # tiprack_start_column = payload['tiprack_start_column']
        # plates_start_column = payload['plates_start_column']
        # media_start_column = payload['media_start_column']
        # treatment_dil_half = payload['treatment_dil_half']
    except Exception as error_msg: 
        # TODO: how to handle this?
        raise error_msg


# * Other program variables
    blowoff_volume = 10
    # num_mixes = 3
    media_z_shift = 0.5
    reservoir_z_shift = 0.5  # z shift for deep blocks (Deck Positions 3 and 5)
    flat_bottom_z_shift = 2  # Note: 1 is not high enough (tested)

    # Step 1 variables
    substrates_transfer_volume_s1 = 150
    # culture_transfer_volume_s1 = 30
    # half_dilution_media_volume = 99
    # dilution_culture_volume = 22
    # culture_plate_mix_volume_s1 = 100  # mix volume increased for test 09/07/21
    # culture_plate_num_mix = 7
    # culture_dilution_num_mix = 10
    # growth_plate_mix_volume_s1 = 40
    # culture_dilution_mix_volume = 180

    """
    STEP 1: INNOCULATE GROWTH PLATE FROM SOURCE BACTERIA PLATE -----------------------------------------------------------------
    """
    # * Initialize soloSoft (step 1)
    soloSoft = SoloSoft(
        filename=temp_file_path,
        plateList=[
            "TipBox.180uL.Axygen-EVF-180-R-S.bluebox",
            "Empty",
            "DeepBlock.96.VWR-75870-792.sterile",
            "Plate.96.Corning-3635.ClearUVAssay",
            "Plate.96.Corning-3635.ClearUVAssay",
            "Plate.96.Corning-3635.ClearUVAssay",
            "Plate.96.Corning-3635.ClearUVAssay",
            "Plate.96.Corning-3635.ClearUVAssay",
        ],
    )

    # * Fill all columns of empty 96 well plate (corning 3383 or Falcon - ref 353916) with fresh substrates (12 channel in Position 1, media_start_column and media_start_column+1)
    soloSoft.getTip("Position1")  
    # j = 1
    for i in range(1, 13):  # first half plate = media from column 1
        soloSoft.aspirate(
            position="Position3",
            aspirate_volumes=DeepBlock_96VWR_75870_792_sterile().setColumn(
                substrates_start_column_2, substrates_transfer_volume_s1
            ),
            aspirate_shift=[0, 0, media_z_shift],
        )
        soloSoft.dispense(
            position="Position7",
            dispense_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(
                i, substrates_transfer_volume_s1
            ),
            dispense_shift=[0, 0, flat_bottom_z_shift],
        )

    soloSoft.shuckTip()
    soloSoft.savePipeline()