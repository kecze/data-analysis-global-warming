import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame
import math

root = tk.Tk()
root.title('Global warming data visualization')
#root.geometry('800x800')
root.state('zoomed')

filename = 'climate_change_indicators.csv'
df = pd.read_csv(filename)
df.set_index("Country", inplace=True)
countries = df.index.values

def on_button(country):
    print("Showing the analysis for: " + country)
    generate_plot(country)


def create_buttons(countries):
    num_cols = 5
    num_rows = math.ceil(len(countries)/num_cols)
    for index, country in enumerate(countries):
        button = tk.Button(root, text= country, command = lambda c=country: on_button(c))
        row = index // num_cols
        col = index % num_cols
        button.grid(row=row, column=col, sticky='ew')
        root.grid_columnconfigure(col, weight=1)

    for row in range(num_rows):
        root.grid_rowconfigure(row, weight=1)


def generate_plot(country):
    plt.style.use('ggplot')
    plt.figure(figsize=(15,5))
    plt.title(country + " temperatures change")
    plt.plot(range(1961,2023),df.loc[country,'F1961':'F2022'].values)
    plt.xlabel('Year')
    plt.xticks(rotation=45)
    plt.ylabel('Temperature change corresponding to the period 1951-1980')
    plt.show()

create_buttons(countries)
root.mainloop()
