import subprocess
import numpy as np
import string
import os

CREATE_CONFIG_1P2_1P3 = False
RUN_1P2_AND_1P3 = False
CREATE_CONFIG_1P4 = True
RUN_1P4 = True

def generate_dragonfly_configs(configfiles, injection_rates, use_flits, use_ugal=False):
    with open("examples/dragonflyconfig", 'r') as configfile:
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
        filename = "examples/dragonflyconfig_" + str(use_flits) + "_" + str(rate)
        if use_ugal:
            filename += "_ugal"
        lines[ir_line] = "injection_rate = " + str(rate) + ';\n'
        lines[uf_line] = "injection_rate_uses_flits = " + str(use_flits) + ';\n'
        if use_ugal:
            lines[rf_line] = "routing_function = ugal;\n"
            lines[vc_line] = "num_vcs = 3;\n"
        lines[-1] = "stats_out = " + filename + ".m;\n"
        with open(filename, 'w') as configfile:
            configfile.writelines(lines)
        configfiles.append(filename)

    return configfiles

# Create configs for Part 1.2
if CREATE_CONFIG_1P2_1P3:
    configfiles = []

    injection_rates = [0.02]
    use_flits = 0

    configfiles = generate_dragonfly_configs(configfiles, injection_rates, use_flits)

# Create configs for Part 1.3
    injection_rates = [0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
    use_flits = 1

    configfiles = generate_dragonfly_configs(configfiles, injection_rates, use_flits)

# Run Part 1.2 and Part 1.3
if RUN_1P2_AND_1P3:
    processes = []
    for configfile in configfiles:
        with open(configfile + ".txt", "wb") as out:
            p = subprocess.Popen(["./booksim", configfile], stdout=out, stderr=out)
            processes.append(p)
    for p in processes: p.wait()

# Create configs for Part 1.4
if CREATE_CONFIG_1P4:
    configfiles = []
    injection_rates = ["0.80", "0.85"]
    use_flits = 1

    configfiles = generate_dragonfly_configs(configfiles, injection_rates, use_flits, use_ugal=True)

# Run Part 1.4
if RUN_1P4:
    processes = []
    for configfile in configfiles:
        with open(configfile + ".txt", "wb") as out:
            p = subprocess.Popen(["./booksim", configfile], stdout=out, stderr=out)
            processes.append(p)
    for p in processes: p.wait()

