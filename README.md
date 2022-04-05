# pdfbatchmerge

Goal:  Merge pdf's that start with the same site name (e.g. "site00123_1.pdf", "site00123_2.pdf", "site00123_3.pdf") and output using the site name (e.g. "site00123.pdf").  All site pdf's are located in a single folder.  The naming scheme is "siteXXXXX.pdf".

Steps:\
Identify unique site names in folder (append to a list?)\
Gather pdf's with same site name (append to a list?)\
Merge pdf's with same site name, and name the output pdf with the site name.


Examples:
https://stackoverflow.com/questions/3444645/merge-pdf-files
https://stackoverflow.com/questions/63758510/merging-pdf-files-starting-with-similar-names-in-a-directory


PyPDF2:  https://pypi.org/project/PyPDF2/

in Commannd line:  pip install PyPDF2  \
check:  pip list

