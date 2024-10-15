"""
Name: Eliana Assefa
CSC 201
Programming Project 2-Checkpoint

This program reads a file in a specific format and draws
a map of a region using the latitude and longitude values
delineating the outline of subregions on the map. It is
either a map of the USA with subregions as states OR
a map of a state with subregions as counties.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):
I recived help from code help.

"""
MAX_SIZE = 700

from graphics2 import *
                           
def main():
    window = GraphWin('USA MAP', MAX_SIZE, MAX_SIZE)
    fin = open('purple/IL.txt', 'r')    # change IL to another state or USA to draw its map
    window.setBackground("White")
    first_line = fin.readline()
    first_line_list = first_line.split()
    min_x = float(first_line_list[0])
    min_y = float(first_line_list[-1])
    second_line = fin.readline()
    second_line_list = second_line.split()
    max_x = float(second_line_list[0])
    max_y = float(second_line_list[-1])
    third_line = fin.readline()
    window.setCoords(min_x, min_y, max_x, max_y)
    
    
    for index in range (int(third_line)):
        fin.readline()
        subregion_name = fin.readline()
        region_name = fin.readline()
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
        polygon.draw(window)
            
                                    
       
    
           
            
            
    
main()