#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_table(sys.argv[1])
# df2 = pd.read_table(sys.argv[2])
#
# expr_R = df["FPKM"]
# expr_G = df2["FPKM"]
#
# log_R = np.log2(expr_R + 1)
# log_G = np.log2(expr_G + 1)
#
# the_m = log_R - log_G
# the_a = 0.5 * (log_R + log_G)
#
# plt.figure()
# plt.scatter(the_a, the_m, alpha = 0.1, color ='b')
# plt.xlabel("A")
# plt.ylabel("M")
# plt.title("SRR072893 v SRR072915")
# plt.tick_params(axis='x',top='off')
# plt.tick_params(axis='y',right='off')
# plt.savefig("MA_plot2.png")
# plt.close()

df_n1 = pd.read_table(sys.argv[1])
df_n2 = pd.read_table(sys.argv[2])

df_f1 = df_n1["FPKM"]
df_f2 = df_n2["FPKM"]

log_f1 = np.log(df_f1 + 1)
log_f2 = np.log(df_f2 + 1)

x = log_f1 - log_f2
y = 0.5 * (log_f1 + log_f2)

plt.figure()
plt.scatter(y, x, alpha = 0.2)
plt.xlabel("M")
plt.ylabel("A")
plt.title("MA plot of SRR072893 and SRR072915")
plt.savefig("MA_plot.png")
plt.close()
