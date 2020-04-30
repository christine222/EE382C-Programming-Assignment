import subprocess
import numpy as np
import string
import os

CREATE_CONFIG_2P1 = True 
RUN_2P1 = False

def generate_fattree_configs(configfiles, tapering, traffic):
    with open("examples/fattree_config", 'r') as configfile:
        lines = configfile.readlines()
        for i, line in enumerate(lines):
            if "t =" in line:
                taper_line = i
            if "traffic = " in line:
                traffic_line = i
        lines.append("")

    for t in tapering:
        for tr in traffic:
            filename = "examples/fattree_config_" + str(t) + "_" + str(tr)
            lines[taper_line] = "t = " + t + ';\n'
            lines[traffic_line] = "traffic = " + str(tr) + ';\n'
            lines[-1] = "stats_out = " + filename + ".m;\n"
            with open(filename, 'w') as configfile:
                configfile.writelines(lines)
            configfiles.append(filename)

    return configfiles

# Create configs for Part 2.1
if CREATE_CONFIG_2P1:
    configfiles = []
    tapering = ["1", "2", "4"]
    traffic = ['uniform', 'transpose', 'bitcomp']

    configfiles = generate_fattree_configs(configfiles, tapering, traffic)

# Run Part 2.1
if RUN_2P1:
    processes = []
    for configfile in configfiles:
        with open(configfile + ".txt", "wb") as out:
            p = subprocess.Popen(["./booksim", configfile], stdout=out, stderr=out)
            processes.append(p)
    for p in processes: p.wait()

