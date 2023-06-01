from flask import Flask, jsonify
from signal_transformer import get_demand_data
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app, version="1.0", title="FFT Signal Decomposer", description="Single endpoint decomposing the Spanish Power Demand signal using Fast Fourier Transform.")
fft_ns = Namespace("", description="Converts signal from its original domain (time) to a representation in the frequency domain.")
api.add_namespace(fft_ns)

@fft_ns.route('/frequency-spectrum', methods=['GET'])
class GetFrequency(Resource):
    def get(self):
        """Using data from 02/09/2018-06/10/2018"""
        fft_results = get_demand_data()
        if fft_results is not None:
            return jsonify(fft_results)
        else:
            return jsonify({"error": "Error retrieving data"}), 500

if __name__ == '__main__':
    app.run()




