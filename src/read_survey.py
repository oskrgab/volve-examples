import pandas as pd
from datetime import datetime

def parse_well_survey(file_path):
    well_name = ""
    survey_date = None
    surface_ew = 0.0
    surface_ns = 0.0
    water_depth = 0.0
    kb_wh = 0.0
    kb_msl = 0.0
    survey_df = pd.DataFrame()
    
    with open(file_path, 'r', encoding='latin1') as file:
        lines = file.readlines()
        survey_start = False
        survey_data = []
        for line in lines:
            if 'WELL NAME:' in line:
                well_name = line.split(':')[1].strip()
            elif 'Survey Date:' in line:
                survey_date = datetime.strptime(line.split(':')[1].strip(), '%d.%m.%Y')
            elif 'Surface EW:' in line:
                surface_ew = float(line.split(':')[1].strip().replace('m', ''))
            elif 'Surface NS:' in line:
                surface_ns = float(line.split(':')[1].strip().replace('m', ''))
            elif 'Water Depth:' in line:
                water_depth = float(line.split(':')[1].strip().replace('m', ''))
            elif 'KB-WH:' in line:
                kb_wh = float(line.split(':')[1].strip().replace('m', ''))
            elif 'KB-MSL:' in line:
                kb_msl = float(line.split(':')[1].strip().replace('m', ''))
            elif 'SURVEY LIST' in line:
                survey_start = True
                continue
            elif survey_start:
                if line.strip():
                    survey_data.append(line.strip().split())
    
    if survey_data:
        max_columns = max(len(row) for row in survey_data)
        for row in survey_data:
            while len(row) < max_columns:
                row.append(None)
        survey_df = pd.DataFrame(survey_data[1:], columns=survey_data[0][:max_columns])
    
    return {
        'well_name': well_name,
        'survey_date': survey_date,
        'surface_ew': surface_ew,
        'surface_ns': surface_ns,
        'water_depth': water_depth,
        'kb_wh': kb_wh,
        'kb_msl': kb_msl,
        'survey': survey_df
    }
