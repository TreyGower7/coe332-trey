# Interesting ISS Trajectory Data

folder contents / project objective
-----------------------------
Folder contains 1 .py script iss_tracker.py. The objective is to feed in the data, query it and return more interesting data we can do calculations with.

Data Access
-----------------------------
using the the iss_tracker python script and pythons import requests library we access and get data from the data set found here: 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'. The download contains data in 4 minute intervals of position, and velocity of the iss.

Description of Scripts
-----------------------------
The script iss_tracker.py gets the data from an xml file from NASA and imports the data. Then we store the cordinates in vectors(lists) for specific epochs in the data set. Then, this data is used to do some basic calculations.

Instructions on Use Using Existing Docker Image
-----------------------------
In your linux environment run the command:   
```sh  
docker pull tagower/iss_tracker:1.0
```
then
```sh  
docker run -it --rm -p 5000:5000 tagower/iss_tracker:1.0
```

Instructions on Use Building A New Docker Image
-----------------------------
In your linux environment run the command:   
```sh  
docker pull tagower/iss_tracker:1.0
```
then
```sh  
docker run -it --rm -p 5000:5000 tagower/iss_tracker:1.0
```

Correct Ports and Example Outputs
-----------------------------
Ensure when curling an image you use the second ip listed in green box (It could be different for you).
/Users/treygower/Desktop/Screenshot\ 2023-02-26\ at\ 9.38.31\ PM.png 
Example Outputs:

* For all paths usecurl localhost:5000/help

	To Delete or Post Data from the iss trajectory:
<<<<<<< HEAD
```sh
curl -X POST <GreenBoxIP>:5000/post-data 
```	
	or  
```sh  
curl -X DELETE <GreenBoxIP>:5000/delete-data
```
Outputs a string verifying status of the data such as: Data Delete
	
Other examples:
	curl localhost:5000/epochs
        returns all epochs in the data set (a big list!)
	or
	curl localhost:5000/epochs/<specific epoch you want from epoch data set>
	{
  	"EPOCH": "2023-061T12:00:00.000Z",
  	"X": {
    		"#text": "3578.8574821437401",
    		"@units": "km"
  	},
  	"X_DOT": {
    		"#text": "5.03904352218286",
    		"@units": "km/s"
  	},
  	"Y": {
    		"#text": "-5454.7252313410299",
    		"@units": "km"
  	},
  	"Y_DOT": {
    		"#text": "1.32725609415084",
    		"@units": "km/s"
  	},
  	"Z": {
    		"#text": "1908.4598652639199",
   		 "@units": "km"
  	},
  	"Z_DOT": {
    		"#text": "-5.6136727354188301",
    		"@units": "km/s"
  	}
	}		
	or
	curl localhost:5000/epochs/2023-061T12:00:00.000Z/speed
        [
        7.659431437012692
        ]   
