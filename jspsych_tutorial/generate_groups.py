"""Generates groups.js from csv file"""

import csv
import json

# The csv file path relative to this python file that contains the metadata. Must contain 4 columns
# 1. "file_name" : The file name of the image relative to HTML file
# 2. "condition" : What condition the image belongs to, each trial name should correspond to a unique condition.
# Each section should contain trails from all conditions.
# 3. "section" : What section the image belongs to, each trial should correspond to a unique section.
# Participants are shown trials from only the section they are assigned.
# 4. "Trial" : Smallest unit of organization, images with the same trial name appear in the same trial.

CSVFILEPATH = "images/StimulusMetaData.csv"

# json file path relative to this python file, to place groups.js.  Should looks something like
# "assets/scripts/groups.js". groups.js will contain 2 constants, the first is called groups.
# This is a nested data structure, the first layer is a dictionary, with keys corresponding to a section
# the value is a dictionary, with keys corresponding to trials, and values corresponding to an array of
# image file paths with the corresponding trial and section.
# The second constant is condition_map.  This is a dictionary with keys corresponding to the trial name,
# and values to the condition they are associated with.

JSONFILEPATH = "scripts/groups.js" # TODO


data = {}
condition_data = {}

# Open CSV File
with open(CSVFILEPATH, 'r', encoding='UTF-8') as csvFile:
    csvReader = csv.DictReader(csvFile)

    # Test fieldnames to determine that all columns are present
    fieldnames = csvReader.fieldnames
    if 'file_name' not in fieldnames:
        raise KeyError('file_name not found')
    if 'condition' not in fieldnames:
        raise KeyError('condition not found')
    if 'section' not in fieldnames:
        raise KeyError('section not found')
    if 'trial' not in fieldnames:
        raise KeyError('trial not found')

    # Populate data and condition_data
    for row in csvReader:

        filePath = row['file_name']
        condition = row['condition']
        section = row['section']
        trial = row['trial']

        if section not in data:
            data[section] = {}
        if trial not in data[section]:
            data[section][trial] = []
        data[section][trial].append(filePath)
        if trial not in condition_data:
            condition_data[trial] = condition

# Save data and condition_data to JSONFILEPATH
with open(JSONFILEPATH, 'w', encoding="UTF-8") as jsFile:
    jsFile.write('const groups = ')
    jsFile.write(json.dumps(data, indent = 4))
    jsFile.write('\n\nconst condition_map = ')
    jsFile.write(json.dumps(condition_data, indent = 4))
