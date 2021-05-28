"""
Image Visualization Program.
It visualises data using image data stripes/bars.
Each data in the set has been scaled to be numbers between 0 and 1.
This program is based on an assignment by Nick Partlante
a lecturer at Stanford University, USA
By  Emmanuel W. Annor

"""
from simpleimage import SimpleImage

GREEN = 127
BLUE = 127

CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 200


def main():
    info()
    filename = get_file_name()      # Gets the filename from user
    data = get_data(filename)       # Retrieves data from file

    f_data = format_list(data)      # list of float values from the total number of data to the data values

    red = red_scale(f_data)     # Calculates the red color property

    width = cal_width(f_data)   # Retrieves the calculated width of the data
    x_width = 0     # Set to 0, x_width is used to update the pixel position

    canvas = fill_canvas(red, x_width, width)   # Creates data bars image
    canvas.show()   # Shows the visualized data as an image
    display_credits()   # Prints the credits and data source


def display_credits():
    # Prints the credits and data sources
    print('''
    
    This program is based on an assignment by Nick Partlante of Stanford University.
    Data Sources:
    Child mortality - https://ourworldindata.org/child-mortality
    Climate - https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/
    Illiteracy Data - https://data.unicef.org/topic/education/literacy/
    ''')


def fill_canvas(red, x_width, width):
    """

    :param red: is a list of red values
    :param x_width:
    :param width:
    :return: canvas: an image that containing stripes
    """
    # Creates A blank image
    canvas = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Loops through the list, red values
    for i in range(len(red)):
        # makes patch using make_path() function
        # using calculated red values
        patch = make_patch(red[i], width, CANVAS_HEIGHT)
        # Patches the canvas using the patch bars
        for x in range(patch.width):
            for y in range(patch.height):
                pixel = patch.get_pixel(x, y)
                canvas.set_pixel(x + x_width, y, pixel)
        # Adds the data bar width to the x_width
        x_width = x_width + width
    return canvas


def make_patch(red_pix, patch_width, patch_height):
    patch = SimpleImage.blank(patch_width, patch_height)
    for pixel in patch:
        pixel.red = red_pix
        pixel.green = GREEN
        pixel.blue = BLUE
    return patch


def format_list(d_list):
    value = d_list[1:]
    new_list = []
    for i in range(len(value)):
        new_list.append(float(value[i]))
    return new_list


def red_scale(lst):
    value = lst[1:]
    n_list = []
    for i in range(len(value)):
        n_list.append(int(value[i] * 255))
    return n_list


def get_data(filename):
    with open(filename) as f:
        data_list = [line.rstrip('\n') for line in f]
    return data_list


def columns(formatted_data):
    # accept data striped of the title and formatted into float type
    # and retrieves the number of columns passing it as an integer type
    return int(formatted_data[0])


def cal_width(formatted_data):
    """
    :param formatted_data: list consisting of float values; retrieves the total number of columns value
    :return: width i.e. the divides the canvas width with the number of columns
    """
    width = CANVAS_WIDTH // columns(formatted_data)
    return width


def info():
    print("This program visualises data using image data stripes/bars.")
    print("Enter the number associated with a data set below to visualize")
    print("""The available data are:
    1. Child mortality 
    2. Climate
    3. Illiteracy""")


def get_file_name():
    user_select = int(input("Enter number: "))
    if user_select == 1:
        filename = "data-child-mortality.txt"
        return filename
    elif user_select == 2:
        filename = "data-climate.txt"
        return filename
    elif user_select == 3:
        filename = "data-illiteracy.txt"
        return filename


if __name__ == '__main__':
    main()
