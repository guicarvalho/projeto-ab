from flask import Flask, jsonify
from flask.views import MethodView
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class CarsAPI(MethodView):
    def get(self):
        cars = [
            {
                "modelo": "VOYAGE Trendline 1.6 T.Flex 8V 4p",
                "marca": "VW - VolksWagen",
                "cod_fipe": "005380-5",
            },
            {
                "modelo": "Way 1.6 Total Flex 8V Mec.",
                "marca": "Wake",
                "cod_fipe": "074001-2",
            },
            {
                "modelo": "Way 1.8 Total Flex 8V Mec.",
                "marca": "Wake",
                "cod_fipe": "074002-0",
            },
            {
                "modelo": "Buggy  Walk Sport 1.6 8V 58cv",
                "marca": "Walk",
                "cod_fipe": "061001-1",
            },
        ]
        return jsonify(cars)


app.add_url_rule("/api/v1/cars", view_func=CarsAPI.as_view("cars"))
