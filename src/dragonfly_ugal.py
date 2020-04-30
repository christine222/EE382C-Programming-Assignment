import subprocess
import numpy as np
import string
import os


injection_rates = [0.75, 0.8, 0.85]

for rate in injection_rates:
    with open("examples/dflyconfigugal", "a") as configfile:
        configfile.write("injection_rate =" + str(rate) + ";\n")
        matlab_file = "dflyugal_" + str(int(rate*100)) + ".m;\n"
        configfile.write("stats_out = " + matlab_file)
        os.system('./booksim examples/dflyconfigugal')

for rate in injection_rates:
    file = "dflyugal_" + str(int(rate*100)) + ".m"
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
