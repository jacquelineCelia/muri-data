#!/usr/bin/python
import os
import sys
import string
from optparse import OptionParser

def ParseData(fn, sens):
   fin = open(fn)
   line = fin.readline()
   while line:
      tokens = line.strip().split('<EOS>')      
      aligns = list()
      for a in tokens:
         if a != "":
            aligns.append(a.strip())
      sens.append(aligns)
      line = fin.readline()
   fin.close()

def MergeToBitex(eng_sens, fra_sens, fn_out):
   # sanity check
   if len(eng_sens) != len(fra_sens):
      print "number of alignments in english is different from that of foreign lang"
      print "# eng alignments: ", len(eng_sens), " # fra alignments: ", len(fra_sens) 
   else:
      fout = open(fn_out, 'w')
      for idx, fra_sen in enumerate(fra_sens):
         if len(fra_sen) != len(eng_sens[idx]):
            print "number of sentence groups mismatch"
            print "# eng sens: ", len(eng_sens[idx]), " # fra sens: ", len(fra_sen) 
            print eng_sens[idx]
            print fra_sen
         else:
            for i in range(len(fra_sen)):
               fout.write(fra_sen[i] + ' ||| ' + eng_sens[idx][i] + '\n')
      fout.close()

def main():
   parser = OptionParser()
   parser.add_option("-e", dest = "eng", help = "english file")
   parser.add_option("-f", dest = "fra", help = "french file")
   parser.add_option("-o", dest = "out", help = "output file")
   (options, args) = parser.parse_args()
   if len(args) != 0:
      parser.error("incorrect number of arguments, please type -h for more help.")

   eng_sens = list()
   fra_sens = list()
   
   print "parsing english data..."
   ParseData(options.eng, eng_sens)

   print "parsing foreign data..."
   ParseData(options.fra, fra_sens)

   print "merge into an output file..."
   MergeToBitex(eng_sens, fra_sens, options.out)

if __name__ == "__main__":
   main()
