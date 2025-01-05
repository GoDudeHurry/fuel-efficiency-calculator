import src.helpers.calculator as calc
from src.assets.Effeciency import Effeciency
import src.assets.constants as constants
from src.helpers.pandas_helper import update_csv
import src.helpers.graphical_representation as plotter

class DataProcessor:
    def __init__(self, bike, data):
        self.bike = bike
        self.data = data
        self.output_list = []
        self.total_economy = 0.00
        self.total_mileage = 0.00        
        self.compute_total_effeciency()
        self.compute_effeciency_for_previous_refill()
        self.update_csv_with_calculations()
        self.plot_analysis_graphs()
        
    def compute_total_effeciency(self):
        total_distance = self.data[-1][constants.MILES] - self.data[0][constants.MILES]
        total_amount = 0.00
        total_volume = 0.00
        for index in range(len(self.data)-1):
            total_amount += self.data[index][constants.AMOUNT]
            total_volume += self.data[index][constants.VOLUME]
        
        self.total_economy = round(float(total_distance*100/total_amount), 2)
        self.total_mileage = round(float(total_distance/total_volume), 2)
        
        print(f"Total effeciency(MEAN MILEAGE) is {self.total_mileage} km/lit.")
        print(f"Total effeciency(MEAN ECONOMY) is {self.total_economy} km/Rs. 100")
        
        
    def compute_effeciency_for_previous_refill(self):
        print(f"Started processing data")
        
        for index in range(len(self.data)):
            output_item = Effeciency(self.data[index]).create_instance()
            if index == len(self.data) - 1:
                self.output_list.append(output_item)
            else:
                output_item[constants.MILEAGE] = calc.mileage_for_previous_refill(
                    self.data[index][constants.MILES],
                    self.data[index+1][constants.MILES],
                    self.data[index+1][constants.VOLUME]
                )
                
                output_item[constants.ECONOMIC_EFFECIENCY] = calc.economic_effeciency_for_previous_refill(
                    self.data[index][constants.MILES],
                    self.data[index+1][constants.MILES],
                    self.data[index+1][constants.AMOUNT]
                )
                
                output_item[constants.MILEAGE_STANDARD_DEVIATION] = round(output_item[constants.MILEAGE] - self.total_mileage, 2)
                output_item[constants.ECONOMY_STANDARD_DEVIATION] = round(output_item[constants.ECONOMIC_EFFECIENCY] - self.total_economy, 2)

                self.output_list.append(output_item)
                
    def update_csv_with_calculations(self):
        update_csv(self.output_list, constants.BIKES[self.bike]["OUTPUT_FILE_LOCATION"], constants.BIKES[self.bike]["EFFICIENCY_FILENAME"])
        print(f"File uploaded succesfully at {constants.BIKES[self.bike]['OUTPUT_FILE_LOCATION'] + constants.BIKES[self.bike]['EFFICIENCY_FILENAME']}")
        
    def plot_analysis_graphs(self):
        plotter.plot_mileage(constants.BIKES[self.bike], self.output_list, self.total_mileage)
        plotter.plot_mileage_deviation(constants.BIKES[self.bike], self.output_list)
        plotter.plot_economy(constants.BIKES[self.bike], self.output_list, self.total_economy)
        plotter.plot_economy_deviation(constants.BIKES[self.bike], self.output_list)