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


# first and second have been removed from the sample code

second = df.str.extract(r'((?:\d{,2}\s)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*(?:-|\.|\s|,)\s?\d{,2}[a-z]*(?:-|,|\s)?\s?\d{2,4})')

dates = (second.fillna(first).fillna(third).replace('Marc', 'March', regex=True).replace('Decemeber','December',regex=True).replace('Janaury','January',regex=True).replace('Marchh','March',regex=True))
