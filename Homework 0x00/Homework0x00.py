'''
Author: Michael Shokoohi
Term: Fall 2025
Course: Mechatronics ME 405
Assignment Description: Write a python Script that is capable of reading a csv file and plotting the data
                        Note that the csv file should be able to have cells with white space or comments that are ignored by script. 
'''
from matplotlib import pyplot as plt
import numpy as np


#Initializing lists to hold X data from column 1 and Y data from column 2
X_Data=[]
Y_Data=[]

def ReadCsv(File):
  '''
  Input: a csv file that needs to be read in format r"The file directory you want in windows format" 
  
  Description: Only data in the first two columns of each row are converted to type float and stored in lists to be output. Note that the 
  first row is presumed to be the header and is therefore only used for labeling the x and y axis so the values in those cells are neglected. 

  Output: True on successful execution, X_Data (list of float), Y_Data (list of float), X-axis label (string), Y-axis label (string)
  '''
   
  # Opening the predefined csv Data file 
  with open(File,'r') as f: 
    # Grabbing the header of the file 
    header= f.readline().strip().split(',')

    # Iterating through all rows of the csv file
    for id, row in enumerate(f):
        RawData=row.strip().split(',')

        # Checking if the vales in the first 2 columns of each row
        # are able to be converted to float. This ignores the entries with words or symbols
        try: 
          float(RawData[0])
          float(RawData[1])
        
        except ValueError:
          print(f"error Row number:{id+2} value:{row}")
          continue
        print(f"Row number:{id+2} value:{row}")
        # Creating the lists for X and Y data 
        X_Data.append(float(RawData[0]))
        Y_Data.append(float(RawData[1]))
    return True, X_Data, Y_Data, header[0], header[1]


def PlotData(X_Data: list,Y_Data: list,X_Label:str,Y_Label:str):
    """
    Input: X Y data as lists and the X Y axis labels as strings

    Description: Creates and displays a plot of Y vs. X 
    """
    # Creating plot
    plt.plot(X_Data,Y_Data,color='Blue', linewidth=2, linestyle='--', marker='o')
    plt.xlabel(X_Label) 
    plt.ylabel(Y_Label)

    # Using the max and min from X and Y to be used for creating axis ticks
    X_Min=min(X_Data)
    X_Max=max(X_Data)
    X_Step=(max(X_Data)-min(X_Data))/5
    Y_Min=min(Y_Data)
    Y_Max=max(Y_Data)
    Y_Step=(max(Y_Data)-min(Y_Data))/5
    plt.xticks(np.arange(X_Min,X_Max+X_Step,X_Step))
    plt.yticks(np.arange(Y_Min,Y_Max+Y_Step,Y_Step))

    # Displaying graph
    plt.show()
    



if __name__== "__main__":
  '''
  #Defining the csv file to read (File is within the same directory)
  File= input("Input the file name, if using sample data file input:-" 
  "             \n Format input as XXXX.csv: ")

  # If the File name input was - swapping it for the actual sample file name 
  if File == "-":
    File= 'data0x00.csv'
 '''
  File= 'data0x00.csv'

  _, X_Data, Y_Data,X_Label,Y_Label=ReadCsv(File)
  PlotData(X_Data,Y_Data,X_Label,Y_Label)
    
