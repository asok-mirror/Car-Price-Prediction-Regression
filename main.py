from flask import Flask, render_template, redirect, jsonify, request, json
from logic import carData
from model import car

main = Flask(__name__, template_folder='templates')

carData.loadData()


@main.route('/')
def home():
    return render_template('home.html', car_name=carData.getCarInfo())


@main.route('/predictPrice', methods=['POST'])
def predictPrice():
    cardata = car.CarDto(
        carModel=request.form["car-model"],
        year=request.form["year"],
        kmDriven=request.form["km-driven"],
        fuel=request.form["fuel"],
        sellerType=request.form["seller-type"],
        transmission=request.form["transmission"],
        owner=request.form["owner"],
        mileage=request.form["mileage"],
        engine=request.form["engine"],
        maxPower=request.form["max-power"],
        torque=request.form["torque"],
        seats=request.form["seats"],
    )
    # carModel = request.form["car-model"]
    # year = request.form["year"]
    # kmDriven = request.form["km-driven"]
    # fuel = request.form["fuel"]
    # sellerType = request.form["seller-type"]
    # transmission = request.form["transmission"]
    # owner = request.form["owner"]
    # mileage = request.form["mileage"]
    # engine = request.form["engine"]
    # maxPower = request.form["max-power"]
    # torque = request.form["torque"]
    # seats = request.form["seats"]
    carPrice = carData.predictPrice(cardata)

    return json.dumps({'status': 'OK', 'carPrice': carPrice})


if __name__ == '__main__':
    print('Application Started')
    main.run(debug=True)
