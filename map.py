import tkinter as tk
from tkinter import filedialog
import csv
import util
import math
import matplotlib.pyplot as plt
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
                    coordinate_array.append([row[1], row[2], row[3], row[4],row[5],row[6]])
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

    print(f"{util.bcolors.OKGREEN}header file added...{util.bcolors.ENDC}")
    plt.xlabel('Steering Angle(degree)')
    plt.ylabel('Tire Angle(radian)')
    plt.plot(steer_array, tire_array)
    plt.show()
    