import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

file = pd.read_csv('File Path')

a = file.head(10)

age = a['Age']
glu = a['Glucose']

i = True
while i == True:

    def glucose():
        plt.plot(glu, marker='o',linestyle='-', color='b')
        plt.title('Glucose')
        plt.xlabel('')
        plt.ylabel('Glucose Level')
        plt.grid(True)
        plt.show()
        return glucose
    
    def bp():
        a.BloodPressure.value_counts().plot(kind='density')
        plt.title("Blood Pressue")
        plt.grid(True)
        plt.show()
        return bp
    
    inp = input("1: Glucose\n2: Blood Pressure\n3: Quit\nEnter the value: ")
    if inp == "1":
        print(glucose())

    elif inp == "2":
        print(bp())

    elif inp == "3":
        break

    else:
        print("Enter the Number (1 to 3)")