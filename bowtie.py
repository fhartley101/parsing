# -*- coding: utf-8 -*-

# Extract alignment statistics from Bowtie output and store in a csv

import pandas as pd
samples = ["WTCHG_7025", "WTCHG_7026", "WTCHG_7027", "WTCHG_7028", "WTCHG_7029", "WTCHG_7030", "WTCHG_7031", "WTCHG_7032", "WTCHG_7033", "WTCHG_7034", "WTCHG_7035", "WTCHG_7036", "WTCHG_7037", "WTCHG_7038", "WTCHG_7039"]

colnames = ["Total Reads", "Aligned reads", "Reads which failed to align"]

df_bowtie = pd.DataFrame(index = samples, columns = colnames)
with open ("C:/Users/fhartley/Documents/Project/bowtie/dmf811.o73915120") as stats:
lines = stats.readlines()
    samplename = file.split("/")[-1][:-17]
    with open (file, "r") as bowtieoutput:
        a = bowtieoutput.read().splitlines() #split the bowtie output into separate lines
        ab = a[0].split(":")[1] #take line 1 of the output (0), then split in by the colon and take the second half [1]
        abc = int(ab)
        bc = a[1].split(":")[1] # takes second line of output, splits at colon and selects second half
        bcd = int(bc.split("(")[0])
        cd = a[2].split(":")[1] # third line of output
        cde = int(cd.split("(")[0])
    df_bowtie.at[samplename,"Total Reads"] = abc
    df_bowtie.at[samplename,"Aligned reads"] = bcd
    df_bowtie.at[samplename,"Reads which failed to align"] = cde
df_bowtie.sort_index(inplace=True)

df_bowtie.to_csv("C:/Users/fhartley/Desktop/woo.csv")
