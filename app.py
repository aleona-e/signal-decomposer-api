from flask import Flask, jsonify
from signal_transformer import get_demand_data
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/frequency-spectrum', methods=['GET'])
def get_freq():
    """
    Converts spanish power demand signal data during 02/09/2018-06/10/2018 from its original domain (time) to a representation in the frequency domain.
    ---
    responses:
      200:
        description:  Frequency and amplitude values after applying FFT
        schema:
          type: object
          properties:
            amplitudes:
              type: array
              items:
                type: number
              example: [141883883, 575820.5569415133, 2064697.4945293446]
            frequencies:
              type: array
              items:
                type: number
              example: [0, 0.00020420665713702266, 0.0004084133142740453]
    """
    fft_results = get_demand_data()
    if fft_results is not None:
        return jsonify(fft_results)
    else:
        return jsonify({"error": "Error retrieving data"}), 500


if __name__ == '__main__':
    app.run()

