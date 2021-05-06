import re
import pandas as pd
import datetime
import sys
import numpy as np

doc = []
with open('dates.txt', 'r') as file:
    for line in file:
        doc.append(line)


df = pd.Series(doc)

#df.index = range(1,len(df)+1)
#df
#df = np.arange(1, len(d) + 1)



first = df.str.extract(r'((?:\d{1,2})(?:(?:\/|-)\d{1,2})(?:(?:\/|-)\d{2,4}))')

second = df.str.extract(r'((?:\d{,2}\s)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*(?:-|\.|\s|,)\s?\d{,2}[a-z]*(?:-|,|\s)?\s?\d{2,4})')

third = df.str.extract(r'((?:\d{1,2}(?:-|\/))?\d{4})')

dates = (second.fillna(first).fillna(third).replace('Marc', 'March', regex=True).replace('Decemeber','December',regex=True).replace('Janaury','January',regex=True).replace('Marchh','March',regex=True))


dates.loc[123] = '2/1998'

dates_format = pd.to_datetime(dates(0))


print(dates_format.to_string())


#sys.stdout = open("LHS712-Assg1-SEREENK.txt","wt")
#print(final_output)
