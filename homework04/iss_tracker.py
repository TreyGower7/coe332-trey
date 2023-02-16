from flask import Flask
import json
import xmltodict
import requests 
import math

"""getting iss trajectory data and doing calculations 

This script gets the data from an xml file from NASA and imports the data. Then we store the cordinates in vectors(lists) for specific epochs in the data set. Where we then want to do some basic calculations.

Typical Usage Example:

    first get the epoch you want from the list using:
        curl localhost:5000/epochs
    then use the epoch to calculate some data:
        curl localhost:5000/epochs/2023-061T12:00:00.000Z/speed
        [
        7.659431437012692
        ]   
"""
app = Flask(__name__)

@app.route('/', methods=['GET']) 
def get_data():
    """From the NASA website this function retrieves data
    
    Args:
        None

    Returns:
        A dictionary named iss_data containing the data imported from an xml file using python requests library
        **Can also return a string if the data does not get retrieved**
    """
    url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
    response = requests.get(url)
    if response.status_code == 200:
        iss_data = xmltodict.parse(response.text)
        return iss_data
    else:
        return 'failed to retrieve data'

@app.route('/epochs', methods=['GET'])
def get_epochs():
    """Seperates all epochs from dictionary of iss_data
    Args:
        None
    Returns: 
        A list named epochs of all the epochs in the data set
    """
    iss_data = get_data()
    epoch_data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']
    return epoch_data

@app.route('/epochs/<epoch>', methods=['GET'])
def vec_epochs(epoch):
    """isolates an epoch from the list of epochs
    Args:
        epoch (a specific epoch we want to look at)

    Returns:
        A vector(list) named spec_epoch taken from specific data in the list of epochs
    """
    spec_epoch = []
    epoch_data = get_epochs()
    for x in range(len(epoch_data)):
        if epoch == str(epoch_data[x]['EPOCH']):
            spec_epoch = epoch_data[x]
            return spec_epoch

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def speed_epoch(epoch):
    """Calulates speed for a specific epoch vector
    Args:
        epoch (a specific epoch we want to calculate for)

    Returns:
       dictionary containing speed for instantaneous speed at a given epoch
    """
    spec_epoch = vec_epochs(epoch)
    z_dot = float(spec_epoch['Z_DOT']["#text"])
    y_dot = float(spec_epoch['Y_DOT']["#text"])
    x_dot = float(spec_epoch['X_DOT']["#text"])
    speed = math.sqrt(x_dot**2 + y_dot**2 + z_dot**2)
    return {speed}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
