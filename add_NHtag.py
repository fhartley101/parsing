# -*- coding: utf-8 -*-

# Add an NH tag to Bowtie output so multi-mapping reads can be identified by featureCounts in the Subread package.

import os
cwd = os.getcwd()

with open (cwd+"/samplelist.txt", "rt") as samplelist: # open the list of samples
    for line in samplelist:
        filepath = str(cwd+"/"+str(line)) # extract the sample name from the list of samples and add the current working directory to create the filepath
        filepath = str(filepath).rstrip("\n")
        sample = str(line).rstrip("\n") 
        with open(filepath, "rt") as sam, open(cwd+"/"+sample+"_NH.sam", "wt", encoding='utf-8') as output: #open up the SAM file, and create a new file for the output to be stored in
            header = [] 
            reads = [] 
            for ln in sam: # for each line of the SAM file
                if ln.startswith("@"): 
                    header.append(ln[0:]) # attach the whole of the line to the header list
                else: 
                    a = ln.split("\t")[-1] # split the line (string) by tabs, and take the last value (e.g. XM:i:2)
                    ab = int(a.split(":")[-1]) -1 # further split this by colons, and take the last value (e.g. 2). The is the number of times the read has aligned plus 1. Convert this to an integer and -1 from it, giving the number of times the read mapped.
                    abc = "NH:i:"+str(ab) # add the value generated above to the string NH:i: to create the NH tag relevant for this line
                    reads.append(ln.rstrip("\n") +"\t"+abc+"\n") # paste the full line but attach this tag onto the end. The new line symbol must be removed from the original line (otherwise the NH tag is pasted onto a new line), then a tab is added along with the NH tag and a new line marker
            output.write(''.join(header)) # to the output file generated in the first line, add the header
            output.write(''.join(reads)) # to the output file, add the lines containing the reads with their new NH tag
              
