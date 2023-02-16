# The Safety of Water on Mars

folder contents / project objective
-----------------------------
Folder contains 2 .py scripts one analyze_water.py and one test_analyze_water.py. The objective here is to evaluate the water on mars to ensure it is safe for use.

Data Access
-----------------------------
using the python request library to send an http request to: https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

Description of Scripts
-----------------------------
The first, analyze_water.py gets the data using the python requests library. Reverses it to obtain most recent data. Then, calculates the average turbididty for five samples and
the time it will take for the water to be below the safety threshold. The second, test_analyze_water.py runs pytest on the first t
o ensure the calculations are working as intended.

Instructions on Use
-----------------------------
To use the analyze_water script ensure you have used the python request library to obtain the data via an http request and response of code 200. Then send the function calc_turb a dictionary the key to access the list inside the first dictionary and how many samples you want (e.g. calc_turb(data, 'turbidity_data', 5)). For the function calc_time_to_fall send it the value from calc_turb with calc_time_to_fall(turb).
