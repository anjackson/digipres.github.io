import os
import re
import glob

for pdf in glob.glob("*.pdf"):
    npdf = pdf.replace(" ","-")
    npdf = npdf.replace("_","-")
    npdf = re.sub('-+', '-', npdf)
    npdf = npdf.lower()
    print(pdf, npdf)
    os.rename(pdf, npdf)
