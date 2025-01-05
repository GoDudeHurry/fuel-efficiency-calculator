import src.assets.constants as constants
from matplotlib import pyplot as plt
  
def plot_mileage(bike_meta, data, mean):
    y_points = get_points(data, constants.MILEAGE)
    plt.plot(y_points, marker = 'D', linestyle='-.', color='g')
    plt.axhline(y=mean)
    plt.xlabel("Refill")
    plt.ylabel("Mileage(km/litre)")
    plt.savefig(bike_meta["OUTPUT_FILE_LOCATION"] + bike_meta["MILEAGE_PLOT"])
    plt.close()
    
def plot_mileage_deviation(bike_meta, data):
    y_points = get_points(data, constants.MILEAGE_STANDARD_DEVIATION)
    plt.plot(y_points, marker = 'D', linestyle='-.', color='r')
    plt.xlabel("Refill")
    plt.ylabel("Deviation of Mileage(km/litre)")
    plt.savefig(bike_meta["OUTPUT_FILE_LOCATION"] + bike_meta["MILEAGE_DEVIATION_PLOT"])
    plt.close()

def plot_economy(bike_meta, data, mean):
    y_points = get_points(data, constants.ECONOMIC_EFFECIENCY)
    plt.plot(y_points, marker = 'D', linestyle='-.', color='g')
    plt.axhline(y=mean)
    plt.xlabel("Refill")
    plt.ylabel("Mileage(km/Rs. 100)")
    plt.savefig(bike_meta["OUTPUT_FILE_LOCATION"] + bike_meta["ECONOMY_PLOT"])
    plt.close()

def plot_economy_deviation(bike_meta, data):
    y_points = get_points(data, constants.ECONOMY_STANDARD_DEVIATION)
    plt.plot(y_points, marker = 'D', linestyle='-.', color='r')
    plt.xlabel("Refill")
    plt.ylabel("Deviation of Mileage(km/Rs. 100)")
    plt.savefig(bike_meta["OUTPUT_FILE_LOCATION"] + bike_meta["ECONOMY_DEVIATION_PLOT"])
    plt.close()

def get_points(data, param):
    points = []
    for index in range(len(data)-1):
        points.append(data[index][param])

    return points


