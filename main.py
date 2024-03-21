import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk

root = tk.Tk()
root.title('Global warming data visualization')
root.geometry('800x600')
root.mainloop()

filename = 'climate_change_indicators.csv'
df = pd.read_csv(filename)

print(df.head())