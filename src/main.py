import numpy as np

input_file_path = "data/in.csv"
output_file_path = "data/out.csv"
output_file_path_copy_paste = "data/out_copy_paste.txt"

# Variables
T0 = 25+273.15
B = 3950
R0 = 100_000
R = 24_000
qTot = 4096

# Functions
def math_function(q):
    T = (1/(1/T0 + 1/B * np.log((R/((qTot/q) -1))/R0))) - 273.15
    return T


lut_size = 128

listT = []
listQ = []

for i in range(lut_size):
    q = i * (qTot/lut_size) + 0.0000001
    listQ.append(int(q))
    listT.append(int(math_function(q)))

with open(output_file_path, "w") as f:
    for i in range(lut_size):
        f.write(f"{str(listQ[i])} , {str(listT[i])}\n")

with open(output_file_path_copy_paste, "w") as f:
    for i in range(lut_size):
        f.write(f"{str(listT[i])} , ")
