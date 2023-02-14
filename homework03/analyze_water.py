import requests 
import json
import math

"""calculates waters turbidity then compares with a threshold to give a time value when the water will be safe for use again.

Typical Usage Example:
    turb = calc_turb(data, 'turbidity_data', 5)
    ttf = calc_time_to_fall(turb)

"""
def calc_turb(data: dict, listkey: str, quant: int) -> float:
    """This function calculates average turbidity

    Args:
        A dictionary data, whose value is a time series list of dictionaries containing sample of water.
        A list key to access the list of dicts
        quant is an integer of how much of the data we want
    Returns:
        float quantity named turb representing turbidity
    """
    avg_turb = 0
    data[listkey].reverse()

    for x in range(quant):     
        a0 = data[listkey][x].get("calibration_constant")
        I90 = data[listkey][x].get("detector_current")
        avg_turb += a0 * I90 #in NTU Units (0 - 40)
    
    return avg_turb/quant

def calc_time_to_fall(turb: float) -> float:
    """Calculates water's time to fall below a safe consumable threshold
    
    Args:
        A value turb with the average of the 5 most recent tubidity data gatherings
    
    Constants:
        thresh = the threshold for safe water in NTU
        d = the factor of decay per hour
    Returns:
        scalar quantity named ttf representing the time for a fall below a safe threshold
    """
    thresh = 1.0 #NTU
    d = .02
    b = (math.log(thresh/turb))/(math.log(1-d))
    if turb > thresh:
        return round(b,3)
    else:
        return 0


def main():
    url = "https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
    else:
        print('failed to retrieve data')
    turb = calc_turb(data, 'turbidity_data', 5)
    ttf = calc_time_to_fall(turb)
    
    print("Average turbidity based on most recent five most recent measurements = %s" %turb)
    if ttf == 0:
        print("Info: Turbidity is below threshold for safe use")
    else:
        print("Warning: Turbidity is above threshold for safe use")
    
    print("Minimum time required to return below a safe threshold = %s" %ttf)

        

if __name__ == '__main__':
    main()
