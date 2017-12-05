n this problem you will learn to use the
csv
(comma separated values) module to read a
data set detailing administrative fines from the past 15 years of elections.
This data can be downloaded from the course website (AdminFineAction.csv).  It should
be possible to open this file with any standard text editor.  Beware that if you open this
with Excel and save changes, it may modify the delimiters.  A more detailed description
of the fields described by this data can be found here
http://www.fec.gov/finance/disclosure/metadata/MetadataforAdministrativeFines.shtml
(a)  In
analyze
fines.py
, write a function
readCSV(filename)
that can read csv files
formatted in the same way as AdminFineAction.csv, and returns a tuple
com
name,
rep
year, fine
amt
:
•
com
name
is a list of strings containing the committee name
•
rep
year
is a 1D numpy array of ints containing the year of the reports that let
to fines
•
fine
amt
is a 1D numpy array of floats containing the fine amounts (with no
dollar sign or commas allowed)
1
Hints:
com
name[i]
,
rep
year[i]
and
fine
amt[i]
should all correspond to the
same row of AdminFineAction.csv.  This file uses tabs to mark changes in fields, so
you can use
’
\
t’
as the delimiter option in the csv reader.  Some fines are missing
the fine amount, so you can input 0.0 as the fine for any missing fine amount.
(b)  In
analyze
fines.py
, write a function
finesHist(fine
amt, outfile)
that makes
a histogram of the number of fines in multiple ranges and saves it in outfile.  You can
decide what ranges you want to plot (should have at least 8 ranges of fine values)
and if you want a linear or log scale for either axis.  Label your axes and include a
title.
(c)  In
analyze
fines.py
,  write  a  function
finesPerYear(rep
year, outfile)
that
makes a plot of the number of fines in each year included in
rep
year
,  saves that
plot in
outfile
, and returns a dictionary containing the years as keys and the number
of fines per year as values.  Your plot should have axes labeled and a title.
(d)  In
analyze
fines.py
, write a function
writeSummary(com
name, rep
year, fine
amt,
finesPerYearOutfile, finesHistOutfile, outfile)
that  prints  text  in  a  for-
mat like this into outfile (note, the numbers will be different for the real data set):
Number of fines:  3210
The distribution of fine amounts is plotted in myFinesHistOutfile
Fines per year plotted in myFinesPerYearOutfile
Table of fines per year:
2000:  113
2002:  341
2004:  51
2005:  12
2006:  95
