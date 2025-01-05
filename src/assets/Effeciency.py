import src.assets.constants as constants

class Effeciency:
    def __init__(self, input_data):
        self.input_data = input_data
        
    def create_instance(self):
        return {
            constants.DATE: self.input_data[constants.DATE],
            constants.AMOUNT: self.input_data[constants.AMOUNT],
            constants.VOLUME: self.input_data[constants.VOLUME],
            constants.MILES: self.input_data[constants.MILES],
            constants.MILEAGE: 0.00,
            constants.ECONOMIC_EFFECIENCY: 0.00,
            constants.BUNK: self.input_data[constants.BUNK],
            constants.LOCATION: self.input_data[constants.LOCATION],
            constants.MILEAGE_STANDARD_DEVIATION: 0.00,
            constants.ECONOMY_STANDARD_DEVIATION: 0.00
        }