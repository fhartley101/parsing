# Extract alignment statistics from Bowtie output and store in a csv

import pandas as pd

with open("C:/Users/fhartley/Documents/Project/bowtie/dmf811.o73915120", 'rt') as bowtie: # Open for reading text
    stats = pd.DataFrame()
    ab = []
    c = []
    d = []
    e = []
    for ln in bowtie:
        if ln.startswith('# reads processed'): # This selects the first line of the code
            a = ln.split(":")[-1] # This step extracts the total reads processed
            ab.append(a.rstrip("\n")) # This trims it to just the sample name
        elif ln.startswith('# reads with at least one'):
            c.append(ln.split(" ")[-2])
        elif ln.startswith('# reads that failed'):
            d.append(ln.split(" ")[-2])
        elif ln.startswith('# reads with alignments'):
            e.append(ln.split(" ")[-2])
    final_list = [ab,c,d,e]
    stats = pd.DataFrame(final_list).transpose()
    stats.columns = ['Reads processed', 'Reads that align', 'Reads that fail to align', 'Reads suppressed by -m 3']
    stats.index = ["WTCHG_7025", "WTCHG_7026", "WTCHG_7027", "WTCHG_7028", "WTCHG_7029", "WTCHG_7030", "WTCHG_7031", "WTCHG_7032", "WTCHG_7033", "WTCHG_7034", "WTCHG_7035", "WTCHG_7036", "WTCHG_7037", "WTCHG_7038", "WTCHG_7039"]
    print(stats)
    stats.to_csv("C:/Users/fhartley/Documents/Project/bowtie/bowtie_stats.csv")
