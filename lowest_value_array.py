# Created by : Sidney Kang
# Created on : 13 Nov. 2017
# Created for : ICS3UR
# Daily Assignment - Unit5-03
# This program

def find_lowest_value(arrays = []):
    value_number_in_array = 0
    
    for value in arrays:
        if value_number_in_array == 0:
           value_number_in_array = value
        else:
             if value_number_in_array > value:
                value_number_in_array = value
             else: 
             	  value_number_in_array = value_number_in_array
                            
    return value_number_in_array                                 


array = [5,4,7,9,3,6]
find_lowest_value(array)

min_value = find_lowest_value(array)
print("The min value of the array is: " + str(min_value))
