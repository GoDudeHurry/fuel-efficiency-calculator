import src.assets.constants as constants

class Refill:
    def __init__(self, date, amount, volume, miles, bunk, location):
        self.amount = amount
        self.volume = volume
        self.miles = miles
        self.miles_start = miles_start
        self.miles_end = miles_end
        self.date = date
        self.bunk = bunk
        self.location = location
        print(f"Detalis received!")
        
    def as_dict(self):
        return {
            constants.DATE: self.date,
            constants.AMOUNT: self.amount,
            constants.VOLUME: self.volume,
            constants.MILES: self.miles,
            constants.BUNK: self.bunk,
            constants.LOCATION: self.location
        }