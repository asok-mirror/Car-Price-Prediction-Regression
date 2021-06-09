import pandas as pd
from model import car
import pickle

global carInfo
global model


def loadData():
    global carInfo
    global model
    carInfo = pd.read_csv('artifacts/car_data.csv')
    with open("artifacts/car_model.pickle", "rb") as f:
        model = pickle.load(f)


def getCarInfo():
    return carInfo.name.sort_values().to_list()


def predictPrice(car: car.CarDto):
    # X_test = [[car.carModel, car.year, car.kmDriven, car.fuel, car.sellerType, car.transmission, car.owner, car.mileage, car.engine, car.maxPower, car.torque, car.seats]]

    X_test = pd.DataFrame([[car.carModel, car.year, car.kmDriven, car.fuel, car.sellerType, car.transmission, car.owner, car.mileage, car.engine, car.maxPower, car.torque, car.seats]],
                          columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner',
                                   'mileage',
                                   'engine', 'max_power', 'torque', 'seats'], dtype=object)
    # X_test = pd.DataFrame([['Toyota Innova Crysta 2.5 VX BS IV', 2011, 60000.0, 'Diesel', 'Individual', 'Manual',
    #                        'First Owner', 12.8, 2494.0, 102.0, 20.0, 7.0]],
    #                      columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner',
    #                               'mileage',
    #                               'engine', 'max_power', 'torque', 'seats'], dtype=object)
    # X_test =  [['Toyota Innova Crysta 2.5 VX BS IV', 2011, 60000, 'Diesel', 'Individual', 'Manual', 'First Owner', 12.8, 2494, 102, 20, 7]]
    try:
        result = model.predict(X_test)[0]
        return "Predicted car price is Rs. <b>" + str(result) + "</b>"
    except Exception as error:
        print(error)
        return error
