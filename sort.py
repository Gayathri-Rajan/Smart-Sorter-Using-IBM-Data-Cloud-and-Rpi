#Run this code to sort the wastes

import subprocess
import os
import time
for i in range(0,100):
os.system(”raspistill -o fruitbowl.jpg”)
cat = subprocess.check output(”python ./pilot.py —grep BIO”,shell = True)
if ”non” in cat :
print(”pushing garbage towards left”)
os.system(’python nonbio.py’)
else:
print(”pushing garbage towards right”)
os.system(’python bio.py’)
print(”finish”)