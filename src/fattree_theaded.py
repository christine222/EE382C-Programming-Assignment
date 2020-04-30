import subprocess
import numpy as np
import string
import os

CREATE_CONFIG_2P1 = True 
RUN_2P1 = False
CREATE_CONFIG_2P2 = True
RUN_2P2 = False

def generate_fattree_configs(configfiles, injection_rate, tapering, traffic):
    with open("examples/fattree_config", 'r') as configfile:
        lines = configfile.readlines()
        for i, line in enumerate(lines):
            if "t =" in line:
                taper_line = i
            if "traffic = " in line:
                traffic_line = i
            if "injection_rate = " in line:
                ir_line = i
        lines.append("")

    for t in tapering:
        for tr in traffic:
            for rate in injection_rate:
                filename = "examples/fattree_config_" + str(rate) + "_" + str(t) + "_" + str(tr)
                lines[taper_line] = "t = " + t + ';\n'
                lines[traffic_line] = "traffic = " + str(tr) + ';\n'
                lines[ir_line] = "injection_rate = " + str(rate) + ';\n'
                lines[-1] = "stats_out = " + filename + ".m;\n"
                with open(filename, 'w') as configfile:
                    configfile.writelines(lines)
                configfiles.append(filename)

    return configfiles

# Create configs for Part 2.1
if CREATE_CONFIG_2P1:
    configfiles = []
    injection_rate = ["0.05"]
    tapering = ["1", "2", "4"]
    traffic = ["uniform", "transpose", "bitcomp"]

    configfiles = generate_fattree_configs(configfiles, injection_rate, tapering, traffic)

# Run Part 2.1
if RUN_2P1:
    processes = []
    for configfile in configfiles:
        with open(configfile + ".txt", "wb") as out:
            p = subprocess.Popen(["./booksim", configfile], stdout=out, stderr=out)
            processes.append(p)
    for p in processes: p.wait()

# Create configs for Part 2.2
if CREATE_CONFIG_2P2:
    configfiles = []
    injection_rate = ["0.10", "0.15", "0.20", "0.25", "0.30", "0.35", "0.40", "0.45", "0.50", "0.55"]
    tapering = ["1", "2", "4"]
    traffic = ["uniform", "transpose", "bitcomp"]

    configfiles = generate_fattree_configs(configfiles, injection_rate, tapering, traffic)

# Run Part 2.2
if RUN_2P2:
    processes = []
    for configfile in configfiles:
        with open(configfile + ".txt", "wb") as out:
            p = subprocess.Popen(["./booksim", configfile], stdout=out, stderr=out)
            processes.append(p)
    for p in processes: p.wait()
