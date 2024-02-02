import tkinter as tk
from tkinter import filedialog
import csv
import util
import math
import matplotlib.pyplot as plt
from pyproj import Proj, transform



def lat_long_to_utm(latitude, longitude):
    # Define the projection for WGS 84 (EPSG:4326)
    wgs84 = Proj(proj='latlong', datum='WGS84')

    # Define the projection for UTM (EPSG:32600 for zone 1, adjust the zone based on your location)
    utm = Proj(proj='utm', zone=1, datum='WGS84')

    # Convert latitude and longitude to UTM
    utm_easting, utm_northing = transform(wgs84, utm, longitude, latitude)

    return utm_easting, utm_northing


L = 0.0

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select csv file",
        filetypes=(("csv files", "*.csv"), ("All files", "*.*"))
    )

    return file_path

def submit():
    global L
    input_text = entry.get()
    try:
        input_val = float(input_text.replace(',', '.'))
        L = input_val
    except Exception as err:
        print(f'{util.bcolors.FAIL}An error occured ->{err}{util.bcolors.ENDC}')
        exit()
    window.quit()

def disable_event():
   exit()

steer_array = []
tire_array = []
coordinate_array = []
if __name__ == '__main__':
    # Create the main window
    window = tk.Tk()
    window.resizable(False, False)
    label_text = "Distance between front axle(m):"
    label = tk.Label(window, text=label_text)
    label.pack(side=tk.LEFT)
    entry = tk.Entry(window)
    entry.pack(side=tk.LEFT)

    # Create a submit button
    submit_button = tk.Button(window, text="Enter", command=submit)
    submit_button.pack()

    window.protocol("WM_DELETE_WINDOW", disable_event)
    window.mainloop()
    excel_path = open_file_dialog()
    try:
        if excel_path:
            with open(excel_path, 'r') as csv_file:
                read_column = csv.reader(csv_file)
                next(read_column)
                for row in read_column:
                    steer_array.append(row[0])
                    x1,y1 = lat_long_to_utm(float(row[1]), float(row[2]))
                    x2,y2 = lat_long_to_utm(float(row[3]), float(row[4]))
                    x3,y3 = lat_long_to_utm(float(row[5]), float(row[6]))

                    coordinate_array.append([x1, y1, x2, y2, x3, y3])
        else:
            print(f'{util.bcolors.FAIL}.csv file not added{util.bcolors.ENDC}')
            exit()
        for i in range(len(steer_array)):
            radius = util.calculate_circle_radius(float(coordinate_array[i][0]), float(coordinate_array[i][1]), float(coordinate_array[i][2]), float(coordinate_array[i][3]), float(coordinate_array[i][4]), float(coordinate_array[i][5])) 
            a = math.atan(L / radius)
            if float(steer_array[i]) > 0 :
                tire_array.append(a)
            else :
                tire_array.append( a * -1)

        # Create the header file
        header_filename = 'steering_map.h'
        util.create_header_file(header_filename, steering_array=steer_array, tire_array=tire_array)
    except Exception as err:
        print(f'{util.bcolors.FAIL}An error occured ->{err}{util.bcolors.ENDC}')
        exit()

    with open("steering_tire_map.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Steering Angle(degree)', 'Tire Angle(rad)'])
        for i in range(len(steer_array)):
            writer.writerow([steer_array[i], tire_array[i]])

    print(f"{util.bcolors.OKGREEN}header file added...{util.bcolors.ENDC}")



    plt.plot(steer_array, tire_array)

    delta_y = float(tire_array[len(tire_array) - 1]) - float(tire_array[0])
    delta_x = float(steer_array[len(steer_array) - 1]) - float(steer_array[0])
    slope = delta_y / delta_x
    print(f"slope = {slope}")
    linear_array = []
    for i in range(len(steer_array)):
        linear_array.append( float(steer_array[i]) * slope)
    plt.plot(steer_array, linear_array)
    plt.show()
    