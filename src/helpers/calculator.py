#All calculations go here

def mileage_for_previous_refill(previous_reading, current_reading, previous_volume):
    return round(float((current_reading - previous_reading)/previous_volume), 2)

def economic_effeciency_for_previous_refill(previous_reading, current_reading, previous_amount):
    return round(float((current_reading - previous_reading)*100/previous_amount), 2)
    
def mileage_from_specific_bunk():
        pass
