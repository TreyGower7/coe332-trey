from flask import Flask, request
import redis
import json
import requests

app = Flask(__name__)

def get_redis_client():
    """
    Gets the redis client
    Args:
        None
    Returns:
        the redis client with host redis-db in order to interact and get from the docker-compose.yml file
    """
    return redis.Redis(host= 'redis-db', port=6379,db=0)
rd = get_redis_client()

@app.route('/plot', methods=['GET'])
def plot():

    file_bytes = open('mysinewave.png', 'rb').read()
    rd.set('plot', file_bytes)
    return rd.get('plot')

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def data():
    """
    POST's (loads), GET's (returns), or DELETE's the data from HGNC from the redis database.
    Args:
        None
    Returns:
        Returns a json formated list of all the data in the data set
    """

    if request.method == 'POST':
        url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json'
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            rd.set('gene_data', json.dumps(data))
            return 'Gene Data Posted'
        else:
            return 'Data failed to retrieve'


    if request.method == 'GET':
        try:
            json_data = json.loads(rd.get('gene_data'))
            return json_data
        except:
            return 'Data not found (use path /data with POST method to fetch it)'
    if request.method == 'DELETE':   
        rd.delete('gene_data')
        return 'Gene Data deleted'

@app.route('/genes', methods=['GET'])
def genes() -> list:
    """
    Returns the whole data set
    Args:
        None    
    Returns:
        Returns a json formated list named hgnc_ids of all gene identifiers in the data set
    """
    try:
        hgnc_ids = []
        json_data = data()

        for x in range(len(json_data['response']['docs'])):
            hgnc_ids.append(json_data['response']['docs'][x]['hgnc_id'])
        return hgnc_ids
    except:
       return 'Data not found (use path /data with POST method to fetch it)'

@app.route('/genes/<string:hgnc_id>', methods=['GET'])
def genes_hgnc(hgnc_id: str) -> dict:
    """
    Gets the gene data from a specific gene given and identifier key
    Args:
        hgnc_id - an identifier for which gene to pull data from
    Returns:
        a dictionary (hgnc_data) containing all data pertaining to a specific gene
    """
    try:
        
        json_data = data()
        for h_id in json_data['response']['docs']:
            if h_id['hgnc_id'] == hgnc_id:
                return [h_id]

        raise TypeError
    except TypeError:
        return f'invalid hgnc_id input or no data found with error'

def get_config() -> dict:
    """
    Function attempts to find a configuration for the user if not we use the default configuration
    Args:
        none
    Returns:
        dictionary with configuration information such as debug setting.
    """
    default_config = {"debug": True}
    try:
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Couldn't load the config file; details: {e}")
    return default_config

if __name__ == '__main__':
    config = get_config()
    if config.get('debug', True):
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run(host='0.0.0.0')
