import subprocess
import numpy as np
import string
import os

"""
injection_rates = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

for rate in injection_rates:
    with open("examples/dragonflyconfig", "a") as configfile:
        configfile.write("injection_rate =" + str(rate) + ";\n")
        matlab_file = "dragonfly_" + str(int(rate*100)) + ".m;\n"
        configfile.write("stats_out = " + matlab_file)
        os.system('./booksim examples/dragonflyconfig')
"""

injection_rates = [0.01,0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]

for rate in injection_rates:
    file = "dragonfly_" + str(int(rate*100)) + ".m"
    outfile = open(file, "r")
    line = outfile.readline()
    while line:
        elements = line.strip().split(" ")
        if elements:
            if elements[0] == "plat(1)":
                print(elements[2].rstrip(';'))
                break
        line = outfile.readline()
    outfile.close()
