import subprocess
import numpy as np
import string
import os

CREATE_CONFIG_1P5 = True 
RUN_1P5 = True

def generate_mesh_configs(configfiles, injection_rates, use_flits):
    with open("examples/meshconfig", 'r') as configfile:
        lines = configfile.readlines()
        for i, line in enumerate(lines):
            if "injection_rate =" in line:
                ir_line = i
            if "injection_rate_uses_flits" in line:
                uf_line = i
            if "routing_function" in line:
                rf_line = i
            if "num_vcs" in line:
                vc_line = i
        lines.append("")

    for rate in injection_rates:
        filename = "examples/meshconfig_" + str(use_flits) + "_" + str(rate)
        lines[ir_line] = "injection_rate = " + str(rate) + ';\n'
        lines[uf_line] = "injection_rate_uses_flits = " + str(use_flits) + ';\n'
        lines[-1] = "stats_out = " + filename + ".m;\n"
        with open(filename, 'w') as configfile:
            configfile.writelines(lines)
        configfiles.append(filename)

    return configfiles

# Create configs for Part 1.5
if CREATE_CONFIG_1P5:
    configfiles = []
    injection_rates = ["0.01", "0.05", "0.10", "0.15", "0.20", "0.25"]
    use_flits = 1

    configfiles = generate_mesh_configs(configfiles, injection_rates, use_flits)

# Run Part 1.5
if RUN_1P5:
    processes = []
    for configfile in configfiles:
        with open(configfile + ".txt", "wb") as out:
            p = subprocess.Popen(["./booksim", configfile], stdout=out, stderr=out)
            processes.append(p)
    for p in processes: p.wait()

