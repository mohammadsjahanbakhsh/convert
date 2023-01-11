import os 

# if the name of the features is with extra quotation marks
def DelCot(column_name):
    temp2=''
    for i in column_name:
        if i.isalnum():
            temp2= temp2+i

    return temp2

def toCsv(text):
    data = False
    header = ""
    new_content = []
    for line in text:
        if not data:
            if "@ATTRIBUTE" in line or "@attribute" in line:
                attributes = line.split()
                if("@attribute" in line):
                    attri_case = "@attribute"
                else:
                    attri_case = "@ATTRIBUTE"

                column_name = attributes[attributes.index(attri_case) + 1]
                
 #If the name of the features has extra quotes, remove the following function from the comment
               
               #column_name= DelCot(column_name)
               
                header = header + column_name + ","
                
            elif "@DATA" in line or "@data" in line:
                data = True
                header = header[:-1]
                header += '\n'
                new_content.append(header)
        else:
            new_content.append(line)
    return new_content


# write data to a csv file

with open(r"YOUR_FILE_PATH.arff" , "r") as inFile:
    content = inFile.readlines()
    name, ext = os.path.splitext(inFile.name)
    
    new = toCsv(content)
    with open(name+'2' + ".csv", "w") as outFile:
        outFile.writelines(new)
            
            
    