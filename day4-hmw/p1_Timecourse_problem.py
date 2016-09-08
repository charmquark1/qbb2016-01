#!/usr/bin/env python

# Usage: ./01-timecourse.py <metadata.csv> <ctab_dir>
#     e.g. ./01-timecourse.py samples.csv ~/data/results/stringtie


import sys
import pandas as pd
import matplotlib.pyplot as plt


df_meta = pd.read_csv( sys.argv[1] )
df_replicates = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[3] 


fem_Sxl = []

df_01 = df_meta[ "sex" ] == "female"
for sample in df_meta [ df_01 ]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_02 = df[ "t_name"] == "FBtr0331261"
    fem_Sxl.append(df[ df_02 ]["FPKM"].values)
    
male_Sxl = []

df_03 = df_meta[ "sex" ] == "male"
for sample in df_meta [ df_03 ]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_04 = df[ "t_name"] == "FBtr0331261"
    male_Sxl.append(df[ df_04 ]["FPKM"].values)

fem_rep_Sxl = []

df_AA = df_replicates[ "sex" ] == "female"
for sample in df_replicates [ df_AA]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_AB = df[ "t_name"] == "FBtr0331261"
    fem_rep_Sxl.append(df[ df_AB ]["FPKM"].values) 
    
male_rep_Sxl = []

df_BB = df_replicates[ "sex" ] == "male"
for sample in df_replicates [ df_BB]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_BC = df[ "t_name"] == "FBtr0331261"
    male_rep_Sxl.append(df[ df_BC ]["FPKM"].values)




# [ 1, 0, 2, 10, 50, 100]

plt.figure()
plt.plot(fem_Sxl, label ="female")
plt.plot(male_Sxl, 'r-', label="male")
plt.plot([4, 5, 6, 7], male_rep_Sxl,'ro')
plt.plot([4, 5, 6, 7], fem_rep_Sxl, 'bo')
plt.xticks(range(0, 8), ["10", "11", "12", "13", "14A", "14B", "14C", "14D"], rotation = 'horizontal')
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance")
plt.title("Sxl")
plt.legend(["Females", "Males"], loc="upper left")

plt.savefig("p1_timecourse_plot.png")
plt.close()

