import pandas as pd

skip= [x for x in range(0, 4)]

skip+= [x for x in range(9, 76)]

for x in [13,14,18,19]:
    skip.remove(x)

data = pd.read_csv('data.txt', 
                    sep=" ", 
                    header=None,
                    skiprows=skip)

data.to_html('output.html')