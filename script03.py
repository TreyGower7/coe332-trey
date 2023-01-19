import names

fivenames = []

#store names
for x in range(5):
    fivenames.append(names.get_full_name())


#print names (could have also printed as I went)
for i in range(len(fivenames)):
    print("Name: " + fivenames[i] + "/length of name: " + str(len(fivenames[i])))
