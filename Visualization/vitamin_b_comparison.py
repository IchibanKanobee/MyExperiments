import pandas as pd
import matplotlib.pyplot as plt

# Create a pandas DataFrame with both sets of values
data = {
    "Labels": [   
        
    "Thiamine",
    "Riboflavin",
    "Niacin",
    "B6-P5P",
    "B6-Parodoxin HCL",
    "Folate",
    "B12",
    "Biotin",
    "Panthotenic Acid",
    "Choline",
    "Inositol",
    "PABA",
    "Rhodiola Root Extract",
    "Hawthorn Berry Fruit"
    ],

    "Pure Lab": [
    50,
    25,
    165,
    40,
    0,
    400,
    500,
    250,
    200,
    60,
    165,
    0,
    0,
    0
    ],
          
    "Genestra": [
    50,
    25,
    100,
    25,
    0,
    400,
    400,
    300,
    110,
    25,
    25,
    0,
    0,
    0
 ],

    "Thorne": [
    50,
    25,
    80,
    25,
    0,
    200,
    100,
    80,
    250,
    14.1,
    0,
    0,
    0,
    0
    ],
    
    "AOR": [
    33.3,
    2.5,
    118,
    33.3,
    0,
    333.3,
    333.3,
    167,
    100,
    80,
    131,
    0,
    0,
    0
    ],   

    "NOW B-100": [
    100,
    100,
    100,
    0,
    100,
    400,
    100,
    100,
    100,
    10,
    10,
    10,
    0,
    0
    ], 
    
    "Garden of Life Raw B Complex" : [
    5,
    10,
    45,
    10,
    0,
    450,
    133,
    325,
    45,
    0,
    0,
    0,
    0,
    0
    ],
    
    "Vimergy Adapto B Complex": [
    60,
    11,
    50,
    20,
    0,
    850,
    1000,
    400,
    60,
    0,
    0,
    0,
    200,
    50
    ],       
      
}
df = pd.DataFrame(data)

# Plot the data using the DataFrame
df.plot(x="Labels", y=["Pure Lab", "Genestra", "Thorne", "AOR", "NOW B-100", "Garden of Life Raw B Complex", "Vimergy Adapto B Complex"], kind='bar')
plt.xlabel('Labels')
plt.ylabel('Values')
plt.show()

