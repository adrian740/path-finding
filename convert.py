import numpy as np
import matplotlib.pyplot as plt

names = []

with open('cities south holland.csv') as f:
    lines = f.readlines()
for i in lines:
    names.append(i.split(",")[0].lower())

with open('nl.csv') as f:
    lines = f.readlines()

print(names, lines)