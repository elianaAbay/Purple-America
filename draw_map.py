'''
Name: Eliana Assefa
CSC 201
Programming Project 2

This program draws a map to show presidential election results with subregions either colored
red/blue to show whether democrats/republicans won that subregion or colored a
shade of purple based on the proportion of deomocrat/republican/other votes. The
map can be chosen to display the USA subdivided by states or a state subdivided2
by counties. The user will enter data to choose USA or a state, the election year,
and whether a red/blue or purple map will be drawn.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):I recived assitance from Professor Muller on how to exit the file. Professor Muller helped me on understanding which filename to use
and where I am supposed to put the code for the files in.


'''

from graphics2 import *
import time

RED_BLUE_MAP = 1  # code for red/blue map
PURPLE_MAP = 2    # code for purple map
MAX_COLOR_NUM = 255   # maximum number for a color
MAX_SIZE = 1000  # maximum dimension of the graphics window

# list of valid state postal codes and 'USA' 
ABBREV_LIST = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN',
               'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MH', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT','NE',
               'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
               'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'USA']

# valid years for election data
YEAR_LIST  = ['1960', '1964', '1968', '1972', '1976', '1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']

'''
Creates and returns a dictionary mapping the subregion
name to red or blue indictating whether republicans or
democrates had more votes in that subregion

Params:
fin_elect (file): file object connected to the data file with voting data

Returns:
a dictionary matching a subregion to either red (democrat) or blue (republican)
'''
def make_red_blue_dict(fin_elect):
    dict = {}
    first_line = fin_elect.readline()  # We're not using this line
    for line in fin_elect:
        line_data = line.split(',')
        subregion = line_data[0].strip()
        republicanVotes = int(line_data[1])
        democraticVotes = int(line_data[2])
        otherVotes = int(line_data[3])
        
        # add code here to compare the election results
        if republicanVotes > democraticVotes:
            color = 'red'
        # and store 'red' or 'blue' in variable color
        elif democraticVotes > republicanVotes:
            color = 'blue'
 
        dict[subregion] = color
        # associates 'red' or 'blue' with the subregion name in a dictionary
    return dict
        
'''
Creates and returns a dictionary mapping the subregion
name to a color representing the proportion of republican
(red) votes, democratic (blue) votes, and independent
(green) votes for a particular presidential election.

Params:
fin_elect (file): file object connected to the data file with voting data

Returns:
a dictionary matching a subregion to a shade of purple
'''
def make_purple_dict(fin_elect):
    dict = {}
    first_line = fin_elect.readline()# We're not using this line
    for line in fin_elect:
        line_data = line.split(',')
        subregion = line_data[0].strip()
        republicanVotes = int(line_data[1])
        democraticVotes = int(line_data[2])
        otherVotes = int(line_data[3])
        # add code here to compare the election results
        red =  (republicanVotes / (republicanVotes+ democraticVotes + otherVotes)) * MAX_COLOR_NUM  
        green= (otherVotes / (republicanVotes+ democraticVotes + otherVotes)) * MAX_COLOR_NUM 
        blue = (democraticVotes / (republicanVotes+ democraticVotes + otherVotes)) * MAX_COLOR_NUM 
        # and store a shade of purple in variable color
        color = color_rgb(int(red),int(green),int(blue))
        
        dict[subregion] = color # associates a shade of purple with the subregion name in a dictionary
    return dict

def main():
    fileAbbrev = input("Do you want a map of USA or a state? Enter USA or state postal code: ")
    fileAbbrev = fileAbbrev.upper()
    
    #statment for finding the input from the ABBREV_LIST
    if fileAbbrev not in ABBREV_LIST:
        print("Not a valid abbrevation. Exiting program")
        exit(-1)
    #statment for finding the input from the YEAR_LIST)        
    electionYear = input("Which year's election 1960 - 2012 do you want to see? ")
    if electionYear not in YEAR_LIST:
        print("Not a valid year. Exiting program")
        exit(-1)
        
    map_type = int(input("Do you want a red/blue map(1) or purple map(2)? "))
    finName =  'purple/' + fileAbbrev + electionYear + '.txt'
    
    if map_type == RED_BLUE_MAP or map_type == PURPLE_MAP:
        #Reading from the functions
        if map_type == RED_BLUE_MAP:
            fin_elect = open(finName, 'r')
            dict = make_red_blue_dict(fin_elect)
        else:
            fin_elect = open(finName, 'r')
            dict = make_purple_dict(fin_elect)
         
        pointsFileName = 'purple/' +fileAbbrev + '.txt'
        
        #name of the file for the graphWin 
        nameofFile = fileAbbrev + ' ' + electionYear
        
        fin = open(pointsFileName, 'r')    # change IL to another state or USA to draw its map
        first_line = fin.readline()
        first_line_list = first_line.strip()
        first_line_list = first_line_list.split()
        min_x = float(first_line_list[0])
        min_y = float(first_line_list[-1])
        
        second_line = fin.readline()
        second_line_list = second_line.strip()
        second_line_list = second_line_list.split()
        max_x = float(second_line_list[0])
        max_y = float(second_line_list[-1])
        
        # scale the window step 8
        height = max_x - min_x
        width = max_y - min_y
        #statment to find the width and height of the file.
        if width > height:
            newSize = height/width * MAX_SIZE
            window = GraphWin(nameofFile, newSize, MAX_SIZE)
        else:
            newSize = width/height * MAX_SIZE
            window = GraphWin(nameofFile, MAX_SIZE, newSize)
        
        
        window.setBackground("White")
        window.setCoords(min_x, min_y, max_x, max_y)
        
        third_line = fin.readline()
        for index in range (int(third_line)):
            fin.readline()
            subregion_name = fin.readline().strip()
            region_name = fin.readline().strip()
            num_lines_for_subregion = fin.readline()
            vertex_list = []
            
            for count in range (int(num_lines_for_subregion)):
                co_ordinates = fin.readline()
                co_ordinates = co_ordinates.strip()
                co_ordinates_list = co_ordinates.split()
                x_coordinate = float(co_ordinates_list[0])
                y_coordinate = float(co_ordinates_list[-1])
                vertex_list.append(Point(x_coordinate, y_coordinate))
            polygon = Polygon(vertex_list)
            
            #setting the coolor for the map
            if subregion_name in dict:
                color = dict[subregion_name]
                polygon.setFill(color)
            else:
                color ='black'
                polygon.setFill(color)
                
                
            #drawing the polygon
            polygon.draw(window)   
        #closing the file
        fin.close()
        fin_elect.close()
       
    else:
        print("Not a valid choice. Exiting program.")
main()
