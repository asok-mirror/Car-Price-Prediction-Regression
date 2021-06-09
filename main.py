from flask import Flask, render_template, request, json
from logic import Carlogic
from model import car

main = Flask(__name__, template_folder='templates')

carLogic = Carlogic.CarLogic()


@main.route('/')
def home():
    return render_template('home.html', car_name=carLogic.getCarInfo())


@main.route('/predictPrice', methods=['POST'])
def predictPrice():
    carData = car.CarDto(
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

    carPrice = carLogic.predictPrice(carData)

    return json.dumps({'status': 'OK', 'carPrice': carPrice})


if __name__ == '__main__':
    print('Application Started')
    main.run(debug=True)
