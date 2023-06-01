from flask import Flask, jsonify, redirect, render_template
from signal_transformer import get_demand_data
from flasgger import Swagger
import plotly.graph_objs as go
import json
import plotly.utils

app = Flask(__name__)
template = {
    "swagger": "2.0",
    "info": {
        "title": "FFT Signal Decomposer API",
        "description": "API documentation",
        "version": "1.0"
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "paths": {}
}
swagger = Swagger(app, template=template)


@app.route('/plot/', methods=['GET'])
def plot():
    
    result = get_demand_data()
    amplitudes = result["amplitudes"]
    frequencies = result["frequencies"]

    data = [
        go.Scatter(
            x=frequencies,
            y=amplitudes,
        )
    ]
    layout = go.Layout(
        title='Frequency Spectrum',
        xaxis=dict(title='Frequencies'),
        yaxis=dict(title='Amplitudes'),
        autosize=False,
        width=1200,
        height=600,
        margin=dict(l=50, r=50, t=50, b=50),
        hovermode='closest',
    )
    fig = go.Figure(data=data, layout=layout)

    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('plot.html', plot_json=plot_json)


@app.route("/", methods=['GET'])
def root():
    return redirect('/apidocs/')


@app.route('/frequency-spectrum', methods=['GET'])
def get_freq():
    """
    Converts spanish power demand signal data during 02/09/2018-06/10/2018 from its original domain (time) to a representation in the frequency domain .
    ---
    responses:
      200:
        description:  Frequency and amplitude values after applying FFT.
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
