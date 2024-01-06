import json
 
inpf = open("C:\KLA alum data\Input data\level0.json")
 
# returns JSON object as 
# a dictionary
idata = json.load(inpf)
print(type(idata))
# Iterating through the json
# list
for k,v in idata.items():
    print(k,"        ",v,"\n")
 
# Closing file
inpf.close()


print("\n\noutput sample for level 0\n\n")

outf = open("C:\KLA alum data\Sampleoutput\level0_output.json")
 
# returns JSON object as 
# a dictionary
odata = json.load(outf)
print(type(odata))
# Iterating through the json
# list
for k,v in odata.items():
    print(k,"        ",v,"\n")
 
# Closing file
outf.close()


## starting

print("idata:                         \n\n",idata)
num_neighbours = idata["n_neighbourhoods"]

for i,v in idata.items():
    if i=="restaurants":
        restaurant_dist = []
        for x,z in v.items():
            for x2,z2 in z.items():
                if x2=="neighbourhood_distance":
                    #restaurant_dist.append(z2)
                    restaurant_dist = z2

    if i=="neighbourhoods":
        neighbour_dist=[]
        
        for i1,v2 in v.items():
            for i3,v3 in v2.items():

                if(i3=="distances"):
                    neighbour_dist.append(v3)
                
#print(neighbour_dist)

print("r0 -->",restaurant_dist)

for i,n in enumerate(neighbour_dist):
    print(i,"--->",n,"\n")

visited=[]

first_visit = restaurant_dist.index(min(restaurant_dist))
print(first_visit)






