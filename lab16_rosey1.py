"""
Programe Name: Lab16_rosey1.py
Author: Rosemond Fordjour
Purpose: Analyze umemployement rate data from OHUR.csv using 
enumerate() and plot trends over time using mathplotlib.
Date: December 09, 2025
"""





import csv 
from datetime import datetime 
import matplotlib.pyplot as plt


# Store dates and unemployment values
dates = []
unemployment_rates = []

# Open CSV file
filename = "OHUR.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #  Analyze header using enumerate 
    print("CSV Header Fields:")
    for index, column in enumerate(header_row):
        print(index, column)

    # - Read rows -
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])
        except ValueError:
            # Skip invalid rows
            continue
        else:
            dates.append(date)
            unemployment_rates.append(rate)

# -- Plot the data --
plt.style.use("seaborn-v0_8")

plt.figure(figsize=(10,5))
plt.plot(dates, unemployment_rates, linewidth=2)

# Labels
plt.title("U.S. Unemployment Rate Over Time")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")

plt.tight_layout()
plt.show()


