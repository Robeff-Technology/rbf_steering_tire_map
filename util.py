import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
def create_header_file(filename, steering_array, tire_array):
    with open(filename, 'w') as file:
        file.write('#ifndef STEERING_MAP_H\n')
        file.write('#define STEERING_MAP_H\n\n')
        file.write('\n')
        file.write(f'static const float steering_angle[{len(steering_array)}] =' + ' {')
        for i in range(len(steering_array)):
            file.write(str(steering_array[i]))
            if i != len(steering_array) - 1:
                file.write(', ')
        file.write('};\n')

        file.write(f'static const float tire_angle[{len(tire_array)}] =' + ' {')
        for i in range(len(tire_array)):
            file.write(str(tire_array[i]))
            if i != len(tire_array) - 1:
                file.write(', ')
        file.write('};\n')

        file.write('#endif  // STEERING_MAP_H\n')

def calculate_circle_radius(x1, y1, x2, y2, x3, y3):
    # Find slopes and midpoints of two line segments
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y3 - y2) / (x3 - x2)
    midpoint1 = ((x1 + x2) / 2, (y1 + y2) / 2)
    midpoint2 = ((x2 + x3) / 2, (y2 + y3) / 2)

    # Calculate slopes of perpendicular bisectors
    if m1 == 0:
        m1_perpendicular = math.inf
    else:
        m1_perpendicular = -1 / m1

    if m2 == 0:
        m2_perpendicular = math.inf
    else:
        m2_perpendicular = -1 / m2

    # Calculate y-intercepts of perpendicular bisectors
    b1 = midpoint1[1] - m1_perpendicular * midpoint1[0]
    b2 = midpoint2[1] - m2_perpendicular * midpoint2[0]

    # Calculate the intersection point of perpendicular bisectors (circle center)
    center_x = (b2 - b1) / (m1_perpendicular - m2_perpendicular)
    center_y = m1_perpendicular * center_x + b1

    # Calculate the distance between the center and any of the three points (circle radius)
    radius = math.sqrt((x1 - center_x) ** 2 + (y1 - center_y) ** 2)

    return radius