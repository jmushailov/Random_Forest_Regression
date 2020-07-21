import os
from fredapi import Fred
import pandas as pd
import time

# FRED method. Setting the API Key as an environmental variable and creating the list
os.environ['FRED_API_KEY'] = ''
# Alternatively (to avoid having the api key in the script), use:
    # fred = Fred(api_key='insert api key')

def get_fred(list_for_fred, observation_start = '2015-01-01', observation_end = '2020-07-01'):
    fred = Fred()
    merge_df = pd.DataFrame() # Create df to hold all the fred variables
    counter = 0 # For tracking whether to merge the DF or just overwrite the DF (First pull)
    
    for i in list_for_fred:
        data = fred.get_series(i, observation_start = observation_start, observation_end = observation_end)
        data = data.reset_index()
        data.columns = ['date_for_merge', i]
        if counter == 0:
            merge_df = data # If first pull, no variable to merge on, so just overwrite
        else:
            merge_df = pd.merge(merge_df, data, on = 'date_for_merge') # If >1st pull, just merge on date
        counter += 1
        time.sleep(3) # Slight delay to not over-query    
    
        
    return merge_df

# GETs all releases for series
def get_all(list_for_fred):
    fred = Fred()
    merge_df = pd.DataFrame() # Create df to hold all the fred variables
    counter = 0 # For tracking whether to merge the DF or just overwrite the DF (First pull)
    
    for i in list_for_fred:
        data = fred.get_series_all_releases(i)
        data = data.reset_index()
        data.columns = ['date_for_merge', i]
        if counter == 0:
            merge_df = data # If first pull, no variable to merge on, so just overwrite
        else:
            merge_df = pd.merge(merge_df, data, on = 'date_for_merge') # If >1st pull, just merge on date
        counter += 1
        time.sleep(3) # Slight delay to not over-query    
    
    
# Searching prorammatically
def query_fred(search_term):
    fred = Fred()
    return(pd.DataFrame(fred.search(search_term)))
