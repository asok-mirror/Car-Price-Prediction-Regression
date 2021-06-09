import pandas as pd
from model import car
import pickle


class CarLogic:
    model = None

    def __init__(self):
        self.carInfo = pd.read_csv('artifacts/car_data.csv')
        self.loadData()

    def loadData(self):
        # global carInfo
        # global model
        with open("artifacts/car_model.pickle", "rb") as f:
            CarLogic.model = pickle.load(f)

    def getCarInfo(self):
        return self.carInfo.name.sort_values().to_list()

    def predictPrice(self, car: car.CarDto):

        # x_test = pd.DataFrame([[car.carModel, car.year, car.kmDriven, car.fuel, car.sellerType, car.transmission,
        #                         car.owner, car.mileage, car.engine, car.maxPower, car.torque, car.seats]],
        #                       columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner',
        #                                'mileage',
        #                                'engine', 'max_power', 'torque', 'seats'], dtype=object)
        x_test = pd.DataFrame([['Toyota Innova Crysta 2.5 VX BS IV', 2011, 60000.0, 'Diesel', 'Individual', 'Manual',
                                'First Owner', 12.8, 2494.0, 102.0, 20.0, 7.0]],
                              columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner',
                                       'mileage',
                                       'engine', 'max_power', 'torque', 'seats'], dtype=object)
        try:
            result = CarLogic.model.predict(x_test)[0]
            return "Predicted car price is Rs. <b>" + str(result) + "</b>"
        except Exception as error:
            print(error)
            return error
