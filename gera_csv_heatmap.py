from itertools import combinations
import pandas as pd
import numpy as np
import re
import seaborn as sns
from matplotlib import pyplot as plt
from read_sequences import read_sequences
import os
sns.set()

_, sequences_names = read_sequences("./heatmap_inputs/sequences.txt")
if not os.path.exists("./resultado_heatmap/"):
    os.makedirs("./resultado_heatmap/")

matrix = np.zeros((len(sequences_names), len(sequences_names)), float)
matrix[:] = 100
value = 0
for c_names, idxs in zip(combinations(list(sequences_names), 2), combinations(np.arange(len(sequences_names)), 2)):
    file = open("./heatmap_inputs/" + " ".join(c_names) + ".txt", "r")
    for line in file.readlines():
        if line[:13] == "# Similarity:":
            value = re.search(r"\((.*?)%\)", line).group(1)
    matrix[idxs[1], idxs[0]] = value
    matrix[idxs[0], idxs[1]] = value

dataframe = pd.DataFrame(matrix, index=sequences_names, columns=sequences_names)
dataframe.to_csv("./resultado_heatmap/heatmap.csv")

plt.figure(dpi=100, figsize=(14, 9))
sns.heatmap(dataframe)
plt.savefig("./resultado_heatmap/heatmap.png")
