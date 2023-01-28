import random
import json
random.seed()

def generate_sites() -> dict :
    
    """
    generate site will compute random integer site ids, assign their composition based off id then randomize lattitude and longitude

    Args:
        None
    Return:
        ind_site(dict):  just a dictionary to be stored in list that is stored in a dictionary 

    """
    ind_site = {}
    
    site_id = random.randint(1,3);
    
    if site_id == 1:
        composition = "stony"
    if site_id == 2:
        composition = "iron"
    else:
        composition ="stony-iron"
    
    ind_site["Site_id"] = site_id
    ind_site["Latitude"] = random.uniform(16.0, 18.0)
    ind_site["Longitude"] = random.uniform(82.0, 84.0)
    ind_site["Composition"] = composition
    return ind_site


sites = {"sites": [{}]}
for x in range(5):
    sites["sites"].append(generate_sites())


with open('generated_sites.json', 'w') as f:
    f.write(json.dumps(sites, indent = 4))
