with open('data/data.json','w') as f:
    import json
    json.dump({},f)
with open('data/date.json','w') as f:
    import json
    json.dump({},f)

import glob
import os
for i in glob.glob('*.png'):
    os.remove(i)