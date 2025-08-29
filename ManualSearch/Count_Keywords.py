import pandas as pd
from collections import Counter
import config

ms = pd.read_csv(config.master_list,keep_default_na=False)
kwds=list()
for k in ms["C2B2_keywords"]:
  ks = k.lower().split(";")
  kss = [x.strip(' ') for x in ks] 
  kwds.extend(kss)
kwds = [x for x in kwds if x]
kwds.sort()
#print(kwds)


counts = Counter(kwds)
for l in counts.keys():
  print(l + ": %i" % counts[l])
  
