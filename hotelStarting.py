import json
 
inpf = open("C:\KLA alum data\Input data\level0.json")
 
# returns JSON object as 
# a dictionary
data = json.load(inpf)
print(type(data))
# Iterating through the json
# list
for k,v in data.items():
    print(k,"        ",v,"\n")
 
# Closing file
inpf.close()


print("\n\noutput sample for level 0\n\n")

outf = open("C:\KLA alum data\Sampleoutput\level0_output.json")
 
# returns JSON object as 
# a dictionary
data = json.load(outf)
print(type(data))
# Iterating through the json
# list
for k,v in data.items():
    print(k,"        ",v,"\n")
 
# Closing file
outf.close()
