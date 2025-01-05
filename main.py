from src.assets.Refill import Refill
from src.helpers.pandas_helper import get_csv_as_list_of_dict, update_csv
from src.helpers.processor import DataProcessor
import src.assets.constants as constants

def start():
    print("Welcome to fuel effeciency calculator!\n\nPlease enter the following details:")
    for bike, bike_meta in constants.BIKES.items():
        input_list = get_csv_as_list_of_dict(
            bike_meta["INPUT_FILE_LOCATION"],
            bike_meta["INPUT_FILENAME"]
        )
        print("Do you want to process data from excel input file at:" + 
              bike_meta["INPUT_FILE_LOCATION"] + bike_meta["INPUT_FILENAME"])
        if input("(y/n)") == "y":
            print(f"Processing data from the excel file at {bike_meta['INPUT_FILE_LOCATION']}{bike_meta['INPUT_FILENAME']}")
            processor = DataProcessor(bike, input_list)

start()
