import requests
import numpy as np
import matplotlib.pyplot as plt


def decompose_signal(json_data):

    values = [entry["value"] for entry in json_data["indicator"]["values"]]
    signal = np.array(values)
    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal))
    amplitudes = np.abs(fft_result)

    return {
         "frequencies":frequencies.tolist(),
         "amplitudes":amplitudes.tolist()
    }
   

def get_demand_data():

    response = requests.get("https://api.esios.ree.es/indicators/1293",
                            headers={"Accept": "application/json",
                                     "Content-type": "application/json",
                                     "x-api-key": "e2992dca39033d2832aca7b6957a1c8c3d785936d89a7129272c0c8b57306096"},
                            params={"start_date": "2018-09-02T00:00:00Z",
                                    "end_date": "2018-10-06T00:00:00Z"})

    if response.status_code == 200:
        json_data = response.json()
        return decompose_signal(json_data)
        
    else:
        print("Error retrieving data:", response.status_code)
        return None
    

def plot_results(frequencies, amplitudes):
        
        plt.plot(frequencies, amplitudes)
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.title("FFT - Frequency Domain")
        plt.show()

