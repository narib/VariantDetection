'''
# Given a csv with list of genomic variant coordinate in hg19,
# predict if it may be detected by a given panel bed file of Pillar
# modified on 30 Oct 22
'''

import pandas as pd
import sys, getopt
import os
import time

def main(argv):
    bedFile = ''
    variantFile = ''

    try:
        opts, args = getopt.getopt(argv,"hv:b:",["bfile=","vfile="])
    except getopt.GetoptError:
        print('detectCAPvariant.exe -b <bedfile> -v <variantfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('detectCAPvariant.exe -b <bedfile> -v <variantfile>')
            sys.exit()
        elif opt in ("-b", "--bfile"):
            bedFile = arg
        elif opt in ("-v", "--vfile"):
            variantFile = arg

    print('Bed file is "', bedFile)
    print('Variant file is "', variantFile)
    print('Hello there")
    print("HEllow World")

    timestr = time.strftime("%Y%m%d-%H%M%S")
    Output_Filename = "QuickDetection" + timestr + '.csv'
    Output_directory = os.getcwd()
    Output_path = os.path.join(Output_directory, Output_Filename)
    sys.stdout = open(Output_path, "w")
    df_bed = pd.read_csv(bedFile, sep="\t")
    df_bed_name = os.path.splitext(os.path.basename(bedFile))[0].split("_")[0]
    df_Cap_Variant = pd.read_csv(variantFile, sep="\t")


    total_count = 0
    for index_input, row_input in df_Cap_Variant.iterrows():
        var_Start_pos = row_input['Start POS']
        var_End_pos = row_input['End POS']
        print(f'For CAP Variant ({var_Start_pos},{var_End_pos})')
        count = 0
        for index_bed, row_bed in df_bed.iterrows():
            bed_start_pos = row_bed['Start(0-based)']
            bed_end_pos = row_bed['End']
            chromo_no = row_bed['#Chrom']
            bed_detect_name = row_bed['Name']

            if variant_detect(var_Start_pos, var_End_pos, bed_start_pos, bed_end_pos):
                print(f'It should be detected by {df_bed_name} Name: {bed_detect_name}({bed_start_pos}, {bed_end_pos}) in {chromo_no} ')
                count += 1

        if count == 0:
            print(f'Maybe no detection in panel ({df_bed_name})\n')
            continue
        total_count += count
        print(f'Total detection(s) for panel {df_bed_name} : {count}\n')

    print(f'Final Total detection(s) for panel {df_bed_name} : {total_count}\n')


def variant_detect(startPos, endPos, bedStartPos, bedEndPos):
    if (startPos>= bedStartPos and startPos <= bedEndPos):
        return True
    elif (endPos <= bedEndPos and endPos >= bedStartPos):
        return True
    else:
        return False

if __name__ == "__main__":
    main(sys.argv[1:])