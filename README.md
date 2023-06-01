# FFT Signal Decomposer API

This is a simple API built with Flask that converts the Spanish power demand signal data from its original time domain to a representation in the frequency domain using Fast Fourier Transform (FFT).
It also provides a visualization of the frequency spectrum using Plotly. 
This API uses the Spanish power demand signal data from a specific time range (02/09/2018 - 06/10/2018) and applies the FFT algorithm to convert it into the frequency domain. 

## Installation

To run this API locally, you need to follow these steps on your terminal:

1. Clone the repository:
  git clone https://github.com/aleona-e/signal-decomposer-api.git
  
2. Install the required dependencies:
  pip install flask numpy requests plotly flasgger
  
3. Run the API:
  python app.py
  
## Usage

### Endpoint

- "/frequency-spectrum": Retrieves the frequency and amplitude values obtained after applying FFT to the Spanish power demand signal data.

- "/plot": Generates a plot of the frequency spectrum using Plotly.

### API Documentation

The API is documented using Swagger UI. You can access the API documentation by visiting the following URL in your browser:

https://aleona.pythonanywhere.com/

The documentation provides details about the available endpoints, request/response formats, and example responses.

### Example Usage

To retrieve the frequency spectrum, you can send a GET request to the "/frequency-spectrum" endpoint.

https://aleona.pythonanywhere.com/frequency-spectrum

Example response:

{
"amplitudes": [141883883, 575820.5569415133, 2064697.4945293446],
"frequencies": [0, 0.00020420665713702266, 0.0004084133142740453]
}

To generate and view the plot of the frequency spectrum, you can access the "/plot" endpoint in your browser:

https://aleona.pythonanywhere.com/plot

### Note
Find the Postman collection in the /postmn.json file.



  
