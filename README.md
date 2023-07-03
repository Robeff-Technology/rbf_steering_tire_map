  
# Python Script for Data Import and steering-tire angle map output

  

This script gives the wheel rotation angle information corresponding to the steering angle by transforming 3 different points obtained in the Cartesian coordinate system corresponding to the steering column angle given in the .csv file.

:exclamation:**The distance between the steering column and the rear axle must be entered correctly. Otherwise, all values will be calculated incorrectly.**

  

## Prerequisites

  

- Python 3.x

  

## Installation

  

1. Install Python from the official website: [Python.org](https://www.python.org)

2. Install the required libraries using pip:

```shell

pip  install  -r  requirements.txt

```

## Inputs

  

**CSV file**: The script expects a CSV file named 'data_log_format.csv' in the same directory. The file should have the following columns: 

 - Steering wheel angle -> actual steering angle (degree)
 -  P1Lat -> Latitude of the first position of the vehicle(degree)    
 - P1Lon -> Longitude of the first position of the vehicle(degree) 
 - P2Lat -> Latitude of the second position of the vehicle(degree)  
 - P2Lon -> Longitude of the second position of the vehicle(degree)   
 - P3Lat -> Latitude of the third position of the vehicle(degree)
 - P3Lon -> Longitude of the  third position of the vehicle(degree)
 
**Distance**: The distance between the steering column and the rear axle of the vehicle(meter)

## Output

- **steering_map.h** header file that include steering to tire map
- **steering_tire_map.csv** .csv file that include steering to tire map


## Usage

Clone the repository or download the script files.

Install the required dependencies using the installation steps mentioned above.

Open a terminal or command prompt and navigate to the directory containing the script.

Run the script using the following command:

```shell
python map.py
```