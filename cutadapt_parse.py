# This is my first Python script
import re
import pandas as pd
myfile = open("C:/Users/fhartley/Documents/Francesco/myfile.txt", 'rt')
dmf = myfile.read()
dmf = dmf.rstrip("\n")
print(dmf)
with open("C:/Users/fhartley/Documents/Francesco/"+dmf, 'rt') as cutadapt: # Open for reading text
    stats = pd.DataFrame()
    ab = []
    cd = []
    d = []
    efg = []
    for ln in cutadapt:
        if ln.startswith('Command line parameters'): # This selects the first line of the code
            a = ln.split("/")[-1] # This step extracts the filename
            ab.append(a.split("_")[0]) # This trims it to just the sample name
        elif ln.startswith('Total reads processed'):
            c = ln.split(" ")[-1]
            cd.append(c.rstrip("\n"))
        elif ln.startswith('Reads written'):
            d.append(ln.split(" ")[-2])
        elif ln.startswith('Quality-trimmed'):
            e = ln.split(" ")[-1]
            ef = e.rstrip("\n")
            efg.append(re.sub(r'[()]', '', ef))
    final_list = [ab,cd,d,efg]
    stats = pd.DataFrame(final_list).transpose()
    stats.columns = ['Sample', 'Total Reads', 'Reads Passing Filtering', 'Bases Failing Quality Check']
    print(stats)
    stats.to_csv("C:/Users/fhartley/Documents/Francesco/cutadapt_stats.csv")