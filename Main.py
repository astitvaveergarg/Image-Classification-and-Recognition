import Encodings

All_Names=[]
All_Results = []
Name_Results =[]
Final=[]

path = input("Give The Image File Path: ")
All_Names,All_Results= Encodings.main(path)

for i in All_Results:
    if i==True:
        index1 = All_Results.index(i)
        All_Results.remove(All_Results[index1])
        Name_Results.append(All_Names[index1])
        continue

for i in Name_Results:
    if i==Name_Results[0:len(Name_Results)]:
        print("There is an Issue")
        break
    else:
        if i not in Final:
            Final.append(i)
        else:
            continue


if i in Final:
    print("The Person Is: " + Final[0])