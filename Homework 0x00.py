'''
Author: Michael Shokoohi
Term: Fall 2025
Course: Mechatronics ME 405
Assignment Description: Write a python Script that is capable of reading a csv file and plotting the data
                        Note that the csv file should be able to have cells with white space or comments that are ignored by script. 
                        The only import allowed is matplotlib
'''
from matplotlib import pyplot as plt




DataFile= 'data.csv'
X_Data=[]
Y_Data=[]

def ReadCsv():
   with open(DataFile,'r') as f: 
    # Grabbing the header of the file 
    header= f.readline().strip().split(',')

    for row in f:
        RawData=row.strip().split(',')

        try: 
          float(RawData[0])
          float(RawData[1])
        
        except ValueError:
          continue
         

     
        X_Data.append(RawData[0])
        Y_Data.append(RawData[1])
    #print(f"X Data: {X_Data}")
    #print(f"Y Data: {Y_Data}")

    return True, X_Data, Y_Data, header[0], header[1]


       

def PlotData(X_Data,Y_Data,X_Label,Y_Label):

    plt.plot(X_Data,Y_Data,color='Blue', linewidth=2, linestyle='--', marker='o')
    plt.xlabel(X_Label) 
    plt.ylabel(Y_Label)
    plt.xticks([])
    plt.yticks([])
    plt.show()



if __name__== "__main__":
    _, X_Data, Y_Data,X_Label,Y_Label=ReadCsv()
    PlotData(X_Data,Y_Data,X_Label,Y_Label)
    
