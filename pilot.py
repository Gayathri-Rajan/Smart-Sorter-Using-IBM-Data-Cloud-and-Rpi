#Initialising the ibm data classification part

import json
from watson developer cloud import VisualRecognitionV3
visual recognition = VisualRecognitionV3(
version=’2018-03-19’, #this version number can be retrieved from ibm
iam apikey=’API KEY’ #insert your API Key from IBM
)
with open(’./fruitbowl.jpg’, ’rb’) as images file: 
classes = visual recognition.classify(
images file,
threshold=’0.6’, #change the threshold value according to the result
classifier ids=’DefaultCustomModel 'YourModelNumber'’).get result() #Custom Model Will be different for each users
print(json.dumps(classes, indent=2))