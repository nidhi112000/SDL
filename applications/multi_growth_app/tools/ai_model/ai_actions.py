import logging
from argparse import ArgumentParser
from pathlib import Path
import pandas as pd 
import pathlib
import openpyxl
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
from openpyxl.utils.dataframe import dataframe_to_rows
from sklearn.model_selection import train_test_split
import scipy.stats as stats

TENSORFLOW_MODEL = None
AI_MODEL_FILE_PATH = str(pathlib.Path().resolve()) + "\\multi_growth_app\\tools\\ai_model\\tensorflow_model"
#AI_MODEL_FILE_PATH = str(pathlib.Path().resolve()) + "/tensorflow_model"

def predict_experiment(num_prediction_requests, original_antibiotic_concentration, original_cell_concentration):
    global TENSORFLOW_MODEL
    #Predict the Model on the Data frame
    #Sort the combinations and output the one/two/three/...twelve that need AI modeling
    predictions = []
    prediction_df = return_combination_data_frame(original_antibiotic_concentration, original_cell_concentration)
     # Make prediction on the combination using the trained model
    numeric_columns = ['Treatment Column', 'Treatment Concentration', 'Cell Column', 'Cell Concentration']
    prediction_df[numeric_columns] = prediction_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    prediction = TENSORFLOW_MODEL.predict(prediction_df)
    prediction_df['Predictions'] = prediction

    prediction_df = prediction_df.sort_values('Predictions')

    # Select the set of smallest values defined by num_prediction_requests
    selected_rows = prediction_df.head(num_prediction_requests)

    treatment_column = selected_rows['Treatment Column'].values
    treatment_concentration = selected_rows['Treatment Concentration'].values
    cell_column = selected_rows['Cell Column'].values
    cell_concentration = selected_rows['Cell Concentration'].values
    predictions = selected_rows['Predictions'].values

    return treatment_column, treatment_concentration, cell_column, cell_concentration, predictions

def return_combination_data_frame(original_antibiotic_concentration, original_cell_concentration):
    combinations_df = pd.DataFrame(columns=['Treatment Column', 'Treatment Concentration', 'Cell Column', 'Cell Concentration'])

    treatment_values = []
    treatment_indices = []
    culture_values = []
    culture_indices = []

    for i in range (1,13):
        antibiotic_concentration_type = original_antibiotic_concentration[i-1]
        if(antibiotic_concentration_type != 0 and antibiotic_concentration_type != None):
            for j in range(1,6):
                treatment_values.append(antibiotic_concentration_type/2**j)
                treatment_indices.append(i)
            treatment_values.append(0)
            treatment_indices.append(6)

    for i in range(1,13):
        cell_concentration_type = original_cell_concentration[i-1]/10
        if(cell_concentration_type != 0 and antibiotic_concentration_type != None):
            culture_values.append(cell_concentration_type)
            culture_indices.append(i)

    for x in range(0, len(treatment_values)):
        for y in range(0, len(culture_values)):
            latest_row = {
                'Treatment Column': treatment_indices[x], 
                'Treatment Concentration': treatment_values[x],
                'Cell Column': culture_indices[y],
                'Cell Concentration': culture_values[y] 
            }
            latest_row_df = pd.DataFrame(latest_row, index=[0])
            combinations_df = pd.concat([combinations_df, latest_row_df], ignore_index=True)

    return combinations_df
    
def train_model(complete_file_path):
    global TENSORFLOW_MODEL
    training_df = pd.DataFrame(columns=['Treatment Column', 'Treatment Concentration', 'Cell Column', 'Cell Concentration', 'Growth Rate'])
    completed_workbook = openpyxl.load_workbook(complete_file_path)
    for sheet_name in completed_workbook.sheetnames:
        current_sheet = completed_workbook[sheet_name]
        for i in range(5, 53):
            latest_row = {
                'Treatment Column': current_sheet["B" + str(int(i))].value, 
                'Treatment Concentration': current_sheet["C" + str(int(i))].value,
                'Cell Column': current_sheet["D" + str(int(i))].value,
                'Cell Concentration': current_sheet["E" + str(int(i))].value,
                'Growth Rate' : current_sheet["F" + str(int(i))].value,
            } 
            latest_row_df = pd.DataFrame(latest_row, index=[0])
            training_df = pd.concat([training_df, latest_row_df], ignore_index=True)

    numeric_columns = ['Treatment Column', 'Treatment Concentration', 'Cell Column', 'Cell Concentration', 'Growth Rate']
    training_df[numeric_columns] = training_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    training_df = training_df.dropna()  # Drop rows with missing or non-numeric values

    X = training_df[['Treatment Column', 'Treatment Concentration', 'Cell Column', 'Cell Concentration']]
    y = training_df['Growth Rate']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    TENSORFLOW_MODEL.compile(optimizer='adam', loss='mse')
    TENSORFLOW_MODEL.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

def load_model():
    #Bring in Global Tensorflow Model
    global TENSORFLOW_MODEL
    global AI_MODEL_FILE_PATH
    #Load a Tensorflow Model if a model exists at the file path. If one does not exist, it creates a new model to use
    if os.path.exists(AI_MODEL_FILE_PATH):
        TENSORFLOW_MODEL = tf.keras.models.load_model(AI_MODEL_FILE_PATH)
    else:
        input_dim = 4 #Cell type, Antibiotic Type, Concentration 1, Concentration 2
        num_classes = 1 #Growth Rate

        TENSORFLOW_MODEL = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(num_classes, activation='softmax')
        ])

        TENSORFLOW_MODEL.compile(optimizer='adam', loss='mean_squared_error')
    
def save_model():
    global AI_MODEL_FILE_PATH
    TENSORFLOW_MODEL.save(AI_MODEL_FILE_PATH)
