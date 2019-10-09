# Main interface that takes either a file with a list of DOIs
# or a single DOI input and returns a bibtex file with their entries
#
# October 2016 Robert Shaw

from converters import *
from re import match
from re import search
from re import findall
from sys import stdin

entry={}

        

def GetBib(doi):
    print (doiToBib(doi).ToString())

def GetBibs(input_file, output_file):
    input = open(input_file, 'r')
    lines = input.readlines()
    output = open(output_file, 'w')
    outputcsv = open("tmp.csv", 'w')
    outputcsv.write("title , journal , year , number\n")
    for line in lines:
        out_re,out_re_csv = doiToBib(line.strip()).ToString()
        output.write(out_re)
        output.write("\n\n")
        outputcsv.write(out_re_csv)
        outputcsv.write("\n")
        print ("Completed " + line)

output = open('input.txt', 'w')
for line in stdin:
    if search('=', line.strip()):
        key, value = [v.strip(" {},\n\r") for v in line.split("=", 1)]
        if key == 'doi' or key == 'DOI':
            output.write(value)
            output.write('\n')
output.close()

GetBibs('input.txt','tmp.bib')      
    
