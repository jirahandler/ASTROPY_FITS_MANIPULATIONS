# !/usr/bin/env python3
import shutil
import csv
import pandas as pd
import fnmatch
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.io import fits
import os
import glob


fp=open('fileffw.csv','r')
reader=csv.reader(fp)
rows=list(reader)
num_lines: int=len(rows)

print("This is the catalogue file of Ultra Diffuse Galaxies:")
print("The number of lines in the file are:", num_lines)
print("The file table format is:")
print (rows[0])


#myrow=rows[1]
#myrow1=rows[num_lines-1]

#print("The first data set line is :")
#print(myrow)
#print("The last data set line is :")
#print(myrow1)

#print("This data file has data from SEXID:", myrow[1], "to SEXID:", myrow1[1] ,"\n")


#curdir=os.getcwd()
#print(curdir)
os.makedirs('Sorted_lists', exist_ok=True)


#file_header="KIDSFIELD,SEXID,RA,DEC,MSRB,Reff,MAG_R,SERSI"
#WARNING: do not open fileffw.csv in any other window, it alters the file stream.
def zero():
    df = pd.read_csv('fileffw.csv', sep=',', skipinitialspace=True)
    column_order = ['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']
    df=df[['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']]
    df.sort_values('MSRB',inplace=True)
    os.makedirs('Sorted_lists/msrb',exist_ok=True)
    df[column_order].to_csv('Sorted_lists/msrb/sorted_msrb_catg.csv',index = False)

def one():
    df = pd.read_csv('fileffw.csv', sep=',', skipinitialspace=True )
    column_order = ['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']
    df = df[['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']]
    df.sort_values('Reff', inplace=True)
    os.makedirs('Sorted_lists/reff',exist_ok=True)
    df[column_order].to_csv('Sorted_lists/reff/sorted_reff_catg.csv',index = False)

def two():
    df = pd.read_csv('fileffw.csv', sep=',', skipinitialspace=True )
    column_order = ['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']
    df = df[['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']]
    df.sort_values('MAG_R', inplace=True)
    os.makedirs('Sorted_lists/magtot',exist_ok=True)
    df[column_order].to_csv('Sorted_lists/magtot/sorted_magtot_catg.csv',index = False)

def three():
    df = pd.read_csv('fileffw.csv', sep=',', skipinitialspace=True)
    column_order = ['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']
    df = df[['KIDSFIELD', 'SEXID', 'RA', 'DEC', 'MSRB', 'Reff', 'MAG_R', 'SERSI']]
    df.sort_values('SERSI', inplace=True)
    os.makedirs('Sorted_lists/seri',exist_ok=True)
    df[column_order].to_csv('Sorted_lists/seri/sorted_seri_catg.csv',index = False)

def split(source_filepath, dest_folder, split_file_prefix,records_per_file):
    """
       `{split_file_prefix}_0.csv`
    """
    if records_per_file <= 0:
        raise Exception('records_per_file must be > 0')

    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)

        file_idx = 0
        records_exist = True

        while records_exist:

            i = 0
            target_filename = f'{split_file_prefix}_{file_idx}.csv'
            target_filepath = os.path.join(dest_folder, target_filename)

            with open(target_filepath, 'w') as target:
                writer = csv.writer(target)

                while i < records_per_file:
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # wrote the header, so delete the file
                os.remove(target_filepath)

            file_idx += 1

loopcycle=False

while loopcycle==False:

        print("Enter the number to sort your records  0: msrb, 1:reff 2: magtot 3: ser index: \n")

        inpval = int(input("The number you have entered is: \n "))

        if inpval==0:
            zero()
            loopcycle=True
            os.chdir('/home/soumyananda/Dropbox/Goswami/CATALOGRADEC_SPLICED/Sorted_lists/msrb/')
            f1 = open('fnames.csv', 'w')
            f2= open('sorted_msrb_catg.csv', 'r')
            f2r = pd.read_csv(f2, sep=',', skipinitialspace=True)
            num_start = f2r.iloc[1][4]
            print(num_start)
            t= num_lines-2
            num_end = f2r.iloc[t][4]
            print(num_end)
            val = (num_end - num_start) / 12
            print(val)
            for i in range(1, 13):
                resl=num_start + val*(i-1)
                resu = num_start + val * i
                print(resl,resu)
                os.chdir('/home/soumyananda/Dropbox/Goswami/CATALOGRADEC_SPLICED/Sorted_lists/msrb/')
                filename = "msrb_part_" + str(i) + ".csv"
                mrc = open(filename, 'w+')
                mrc.write('KIDSFIELD, SEXID, RA, DEC,MSRB, Reff, MAG_R, SERSI')
                mrc.write('\n')
                for j in range(1, num_lines-2):
                    if  resl <= f2r.iloc[j][4] <= resu:
                        spc=str(f2r.iloc[j][0])+' , '+str(f2r.iloc[j][1])+' , '+str(f2r.iloc[j][2])+' , '+str(f2r.iloc[j][3])+' , '+str(f2r.iloc[j][4])+' , '+str(f2r.iloc[j][5])+' , '+str(f2r.iloc[j][6])+' , '+str(f2r.iloc[j][7])
                        mrc.write(spc)
                        mrc.write('\n')
                mrc.close()
                os.chdir('/home/soumyananda/Dropbox/Goswami/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/')
                z = "Sorted_by_msrb_" + str(i)
                os.makedirs(z, exist_ok=True)
                os.chdir('/home/soumyananda/Dropbox/Goswami/CATALOGRADEC_SPLICED/Sorted_lists/msrb/')
                drc = open(filename, 'r')
                dfz = pd.read_csv(drc, delimiter=',')
                #print(dfz)
                n = len(dfz)
                print("number of objects:", n)
                for k in range(1, n):
                    btemp = str(dfz.iloc[k][2])
                    ctemp = str(dfz.iloc[k][3])
                    s1 = str(btemp) + "_" + str(ctemp) + "_GALEX_NUV.fits"
                    #print(s1)
                    f1.write(s1)
                    f1.write("\n")
                    os.chdir('/home/soumyananda/Dropbox/Goswami/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/')
                    for file in os.listdir('.'):
                        if fnmatch.fnmatch(file, s1):
                            temp = "/home/soumyananda/Dropbox/Goswami/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/" + z + "/"
                            shutil.copy2(file, temp)
                image_concat = []
                temp1 = "/home/soumyananda/Dropbox/Goswami/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/" + z + "/"
                os.chdir(temp1)
                image_list = glob.glob('*.fits')
                number_files = len(image_list)
                for p in range(0, number_files):
                    hdul = fits.open(str(image_list[p]))
                    image_concat.append(hdul[0].data)
                    hdul.close()
                final_image = np.zeros(shape=image_concat[0].shape)
                for image in image_concat:
                    final_image += image
                hdu = fits.PrimaryHDU(final_image)
                s = "stack_galnuv6as_" + str(i) + ".fits"
                s1 = "stack_galnuv6as_" + str(i) + ".png"
                os.makedirs('/home/soumyananda/Dropbox/Goswami/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/STACKED_IMAGES/', exist_ok=True)
                os.chdir("/home/soumyananda/Dropbox/Goswami/DATA_FITS_KIDS_GAMA_VST/GALEX_NUV_FITS_6AS/STACKED_IMAGES/")
                hdu.writeto(s, overwrite=True)
                image_data = fits.getdata(s, ext=0)
                print(image_data.shape)
                plt.imshow(image_data, cmap='gray')
                tempstr="BY_MSRB"+str(resl)+"_"+str(resu)
                plt.title(tempstr)
                plt.savefig(s1)
                mrc.close()


fp.close()
