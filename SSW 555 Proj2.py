#open file
data = open('proj02test.ged' , 'r')
cocao = open('My-Family-Project01.txt')

#set variables
global tag_key #list of possible keys
global level #assingment of level
global sentence #the line that we are analyzing
global reas #is the array valid???!?!?!?!?
global tag #the tag... that we are checking

#function for validation
def valival(array, tag_key): #put array in vali or just tag?
    if len(array) > 2:
        if array[1] in tag_key:
            if array[1] == "FAM" or array[1] == "INDI":
                reas = "N"
            else:
                reas = "Y"
        elif array[2] in tag_key:
            reas = "Y"
            array[1],array[2] = array[2],array[1] #put tag in proper place
        else:
            reas = "N"
    else:
        if array[1] in tag_key:
            if array[1] == "FAM" or array[1] == "INDI":
                reas = "N"
            else:
                reas = "Y"
        else:
            reas = "N"
    return(reas, array)

#function for switch
def caseyCase(array):
    level = array[0] #i am initializing everything for debugging purposes but maybe delete later
    tag = array[1]
    arg = array[2:]
    reas = "N"
    
    if level == "0":
        tag_key = ["HEAD", "TRLR", "NOTE", "INDI", "FAM"]
        x, y = valival(array, tag_key)
        
        print(str(level) + " " + str(array[1]) + " " + str(' '.join(array[2:])))
        print(str(level) + "|" + str(array[1]) + "|" + str(x) + "|" + str(' '.join(array[2:])))
    elif level == "1":
        tag_key = ["NAME", "SEX", "MARR", "BIRT", "DEAT", "FAMC", "FAMS", "HUSB", "WIFE", "CHIL", "DIV"]
        x, y = valival(array, tag_key)
        
        print(str(level) + " " + str(tag) + " " + str(' '.join(arg)) , sep = " ")
        print(str(level) + "|" + str(tag) + "|" + str(x) + "|" + str(' '.join(arg)))
    elif level == "2":
        tag_key = ["DATE"]
        x, y = valival(array, tag_key)
        
        print(str(level) + " " + str(tag) + " " + str(' '.join(arg)))
        print(str(level) + "|" + str(tag) + "|" + str(x) + "|" + str(' '.join(arg)))
    else:
        arg = array[2:]
        
        print(str(level) + " " + str(tag) + " " + str(' '.join(arg)))
        print(str(level) + "|" + str(tag) + "|" + str(reas) + "|" + str(' '.join(arg)))
 
#dissect into arrays and solve each
def arrayify(file):
    datarray = file.read().splitlines()
    for line in datarray:
        array = line.split(" ")
        caseyCase(array)
        
arrayify(data)