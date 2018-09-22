import string
import csv
import pandas as pd

fp=open('fnames.csv','r')
readval=pd.read_csv(fp,header=None)

df = pd.read_csv('catg.csv', sep=',', skipinitialspace=True )

lp=open('fileffw.csv','w')
lp.write("KIDSFIELD,SEXID,RA,DEC,MSRB,Reff,MAG_R,SERSI"),lp.write('\n')
for i in range(0,16594):
     a=str(readval.iloc[i])
     b=a.split('_')
     a1=str(df.iloc[i][2])
     a2=str(df.iloc[i][3])
     b1= str(b[0][1:])
     b2= str(b[1])
     lp.write(str(df.iloc[i][0])),lp.write(","),lp.write(str(df.iloc[i][1])),lp.write(","),lp.write(b1.strip()),lp.write(","),\
     lp.write(b2),lp.write(","),lp.write(str(df.iloc[i][4])),lp.write(","),lp.write(str(df.iloc[i][5])),lp.write(","),\
     lp.write(str(df.iloc[i][6])),lp.write(","),lp.write(str(df.iloc[i][7]))
     lp.write('\n')





