#!/usr/bin/python

from __future__ import division
import sys
import math
import cmath
import numpy as np
from numpy import genfromtxt
import csv
from decimal import Decimal
import os
import random
import csv


filename1 = sys.argv[1]

n_lines = 0
n_columns = 0

print "Simple code to convert csv tables to tex!"
print "Last edited by Hassan Harb, Oct 17, 2020"
print "Input file: ", filename1

with open(filename1,'r') as input:
     for line in input:
         inputline = line.split(",")
         n_lines = n_lines + 1
         n_columns = len(inputline)

n_table = n_lines * n_columns
rawtable = [" " for i in range(n_table)]

counter = 0
with open(filename1,'r') as input:
     for line in input:
         inputline = line.split(",")
         for entry in range (n_columns):
             rawtable[counter] = inputline[entry].decode('utf-8-sig')
             counter = counter + 1

filename2 = os.path.splitext(filename1)[0] + ".tex"

print "Output file: ", filename2

counter = 0
l_column = ["l " for i in range(n_columns)]

with open(filename2,'w') as output:
     output.write("\\begin{table}\n")
     output.write("\\begin{tabular}{")
     for j in range(n_columns):
         output.write("l ")
     output.write("}\n")

     for j in range(n_lines):
       for i in range(n_columns):
         if (j == 0 or j == 1):
           if (i == 0):
              output.write("\\hline\n")
         output.write(rawtable[counter])

         if (i == n_columns-1):
            output.write("\\\\ \n")

         else:
            output.write("&")
         counter = counter + 1
     output.write("\\hline")
     output.write("\n\\end{tabular}")
     output.write("\n\\label{Insert label here}")
     output.write("\n\\caption{Insert caption here}")
     output.write("\n\\end{table}\n")

print "All done!"
