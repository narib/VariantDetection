# detectCAPVariant.exe

*This script takes in two input in order to run successfully.Its output in csv format (can be open in notepad) will be in the same directory name as QuickDetection{8 digits Run Date}-{6 digits - Run Time}. The script may run in any window DOS environment in a directory where it resides.*
	
> ***Command format:*** detectCAPVariant.exe -b somebedfile.bed -v someVariantfile.txt
>
> ***input example:***	detectCAPVariant.ext -b st222_ROI.bed -v 2022NGSST_submission_form.txt
>	
> ***output example:***	QuickDetection20220826-113059.csv
			
# DOS demo
*Say you copy the files inside a Drive: I:\AMDL\dist\, type the command ***dir/w*** , will list out all files and folders in the ***dist*** directory.*

		I:\AMDL\dist>dir/w
		 Volume in drive I is WORKS
		 Volume Serial Number is 0C43-101F

		 Directory of I:\AMDL\dist

		[.]                               [..]                              2022B_NGSST_submission_form.txt
		detectCAPvariant.exe              README.md                         st222_ROI.bed
					   4 File(s)     39,462,175 bytes
					   2 Dir(s)  179,949,092,864 bytes free

*See detectCAPvariant.exe is in the directory, two input files st222_ROI.bed and 2022B_NGSST_submission_form.txt (which is prepared earlier from an excel). Now you use the command in the form as detectCAPVariant.exe -b somebedfile.bed -v someVariantfile.txt*

		I:\AMDL\dist>detectCAPvariant.exe -b st222_ROI.bed -v 2022B_NGSST_submission_form.txt
		Bed file is " st222_ROI.bed
		Variant file is " 2022B_NGSST_submission_form.txt


*The command ran successfully, check the output QuickDetection20220829-100407.csv is created.*

		I:\AMDL\dist>dir/w
		 Volume in drive I is WORKS
		 Volume Serial Number is 0C43-101F

		 Directory of I:\AMDL\dist

		[.]                                 [..]                                2022B_NGSST_submission_form.txt
		detectCAPvariant.exe                QuickDetection20220829-100407.csv   README.md
		st222_ROI.bed
					   5 File(s)     39,476,434 bytes
					   2 Dir(s)  179,949,076,480 bytes free

# Input file format requirement:
### For bed file:
*All bed files (hg19) are available from Pillar found in NAS. The current format is good fit as input, no further manipulation needed.*

### For the variant file:

	1. The field headers must follows the given convention. Only two fields, separated by tab, as shown below: 
> ***"Start POS (If any, otherwise same)"***  \{tab\}		***"End POS (If any, otherwise same)"***

	2. all entries in subsequent lines ARE HG19 corodiantes, 1st field is the start pos, 2nd field is the ending position, separated by tab, 2nd field is optional, may be blank in case of snp

	3. The variant file may be prepared/cleansed using excel functions "find and replace" or "SUB", and output as txt or csv. 
	
> ***For Example:*** In the given directory, it contains a CAP variant file in excel with all variants' coordinates in the column of ***"Genomic Description (hg19)"***
	
> *One may copy all the column's entries in new worksheet, and work on data cleansing.*
> 
> 1.	In Excel pressing ***"Ctrl-H"*** on your keyboard can replace all unnnecessary characters e.g. chr*: or the like
> 
>> under find textbox, typing:

>>> ***chr****: *to replace all prefixing chromosome location*
>>>		
>>> ***del**** *to replace all suffixing deletion notation in deletion{ACGT}*
>>>
>>> ***ins**** *to replace all suffixing insetion notation ins\{ACGT\}*
>>>
>>> ***?>**** *to replace all suffixing substition notation  ?\>\{ACGT\}*
>>>
>>> ***dup**** *to replace all suffixing duplication notation ?\>\{ACGT\}*
>	
> 2. For those containing two coordinates, Excel function LEFT() & RIGHT() helps separates based on  "_"/ "-" into the two coordiantes under two cells 
>
>		=LEFT(CELL, LEN(CELL)-FIND("_",CELL)) or =RIGHT(CELL, LEN(CELL)-FIND("-",CELL))
>
>		=RIGHT(CELL, LEN(CELL)-FIND("_",CELL)) or =RIGHT(CELL, LEN(CELL)-FIND("-",CELL))
>>	
>>		For example, if B4 cell with entry: 140453136_140453137   	
>>	
>>>
>>>		B5 =LEFT(B4, LEN(B4)-FIND("_",B4))		= 140453136
>>>
>>>		B6 =RIGHT(B4, LEN(B4)-FIND("_",B4))		= 140453137
>
>3. 	Export selected rows in tab separated text in excel, add the required header as mentioned above
		
	
	

		
	
	
	
	
