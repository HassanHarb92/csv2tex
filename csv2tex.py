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

with open(filename1,'r') as input:
     for line in input:
         inputline = line.split(",")
         print "length = ", len(inputline)
         n_lines = n_lines + 1
         n_columns = len(inputline)

print "Total number of rows = ", n_lines
print "Total number of columns = ", n_columns

n_table = n_lines * n_columns
rawtable = [" " for i in range(n_table)]
print rawtable

counter = 0
with open(filename1,'r') as input:
     for line in input:
         inputline = line.split(",")
         for entry in range (n_columns):
             print inputline[entry]
             rawtable[counter] = inputline[entry].decode('utf-8-sig')
             counter = counter + 1

print rawtable 
filename2 = os.path.splitext(filename1)[0] + ".tex"

counter = 0
l_column = ["l " for i in range(n_columns)]
print "l column = ", l_column

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

#with open(filename2,'r') as texin:
#     table = texin.read()
#     table = table.replace('^M','')
#     print table 
#     texin.close()
#
#print table
#
#texout = open(filename2,'wt')
#texout.write(table)


 
