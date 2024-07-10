#%% Importing libraries
import pandas as pd
from src.read_survey import parse_well_survey
from pathlib import Path
#%% Define well_dev and well_logs paths
well_dev_path = Path("data/well_dev")
well_logs_path = Path("data/well_logs/interpretation")
#%% Parse well survey data
well_dev_data = []
for file_path in well_dev_path.glob('*'):
    well_dev_data.append(parse_well_survey(file_path))

# %%
