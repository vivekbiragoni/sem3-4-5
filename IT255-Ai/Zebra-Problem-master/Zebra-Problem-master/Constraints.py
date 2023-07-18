import variable 
from copy import deepcopy

#--------------------------------------#
#        set up the constraints        #
#--------------------------------------#
def Constraint_equality_var_cons(Category, toChange, setHouse):
    #reduce this domain to the last house
    setHouseList = [setHouse]
    changed1 = toChange.setDomains(setHouseList)
    
    #reduce all the other variable in the category 
    changed2 = Constraint_NoSet_variable_Match(Category)
    return changed1 == True or changed2 == True

def Constraint_equality(var1, var2):
    #reduce this domain to the last house
    return var1.domains == var2.domains

def Constraint_toRight_of(leftVar, rightVar):
    changed = False
    for x in range (6):        
        if (x in leftVar.getDomains()) and (x+1 in rightVar.getDomains()):
            continue
        else:
            changed1 = leftVar.domains.domainReduction(x)
            changed2 = rightVar.domains.domainReduction(x+1)
            if changed1 or changed2:
                changed = True
    return changed

def Constraint_Nextto(var1, var2):
    '''Check if either house only has 1 domain left and set the other domain to be next to it'''
    changed = False
    var1Domains = var1.getDomains()
    var2Domains = var2.getDomains()
    for x in range (6):
        change1, change2 = False, False
        if x-1 not in var1Domains and x+1 not in var1Domains:
            change1 = var2.domains.domainReduction(x)
            var2Domains = var2.getDomains()
        elif x-1 not in var2Domains and x+1 not in var2Domains:
            change2 = var1.domains.domainReduction(x)
            var1Domains = var1.getDomains()
        if change1 or change2:
                changed = True
    return changed

def Constraint_NoSet_variable_Match(varCategory):
    '''check if any of the variables is satisfied if so reduce all other variables by this'''
    changed = False
    setChanged = False
    for x in range(5):
        if varCategory[x].domains.is_satisfied():
            LastDomain = varCategory[x].getDomains()
            for i in range (5):
                if x != i:
                    setChanged = varCategory[i].domains.domainReduction(LastDomain[0])
                if setChanged == True:
                    changed = True
    return changed

def Constraint_Last_Available(varCategory):
    ''' check to see if any domain only has one possibility left'''
    changed = False
    altered = False
    for i in range(1,6):    #cycle through the domain values
        counter = 0
        for x in range(5):      #cycle through the variables
            if i in varCategory[x].getDomains():
                counter += 1
                isInVar = x
                lastRemaining = i
        if counter == 1 and len(varCategory[isInVar].getDomains())>1:
            altered = Constraint_equality_var_cons(varCategory, varCategory[isInVar], lastRemaining)
        if altered == True:
            changed = True
    return changed   
       
def print_all(allvars):
    for x in range (5):
        for i in range(5):
            allvars[x][i].PrintVariable()

def get_available_By_house(varCategory): 
    myList = ["","","","","", 0 , False] 
    for x in range(5):
        remaining = varCategory[x].getDomains()
        for i in range (1,6):
            if i in remaining:
                myList[i-1] += (varCategory[x].name) + " "
        if varCategory[x].domains.is_satisfied():
            myList[5] += 1
        if varCategory[x].domains.is_empty():
            myList[6] = True
    return myList

def is_all_satisfied(allvars):
    no_satisfied = 0 
    for x in range(5):
        for i in range (5):
            if allvars[x][i].is_satisfied():
                no_satisfied += 1
    return no_satisfied == 25

def is_satisfied(elem):
    return elem.is_satisfied()

def is_any_empty(allvars):
    any_empty = False 
    for x in range(5):
        for i in range (5):
            if allvars[x][i].is_empty():
                any_empty = True
    return any_empty
    
def print_domainResults(allVars):
    #what I want:
    # House 1: norwegian | Coffee | Cluedo | Pet | Colour
    allSatisfied = 0
    anyEmpty = False
    nat = get_available_By_house(allVars[0]) 
    bev = get_available_By_house(allVars[1])
    gam = get_available_By_house(allVars[2])
    pet = get_available_By_house(allVars[3])
    col = get_available_By_house(allVars[4])
    
    allSatisfied = nat[5] + bev[5] + gam[5] + pet[5] + col[5]
    if nat[6] or bev[6] or gam[6] or pet[6] or col[6]:
        anyEmpty = True   
    return_string = []
    for x in range (5):
        make_string = "house: " + str(x+1)+  " : "+ nat[x]+ " | "+ bev[x]+ " | "+ gam[x]+ " | "+ pet[x]+ " | "+ col[x]+ "\n"
        return_string.append(make_string)
    return return_string
            
#-------------------------------#
#   set up variables            #
#-------------------------------#
def set_up_Variables():

    Norwegian = variable.Variable("Norwegian", "N01")
    English = variable.Variable("English", "N02")
    Spanish = variable.Variable("Spanish", "N03")
    Ukrainian = variable.Variable("Ukrainian", "N04")
    Japanese = variable.Variable("Japanese", "N05")
    Nationality = [Norwegian, English, Spanish, Ukrainian, Japanese]
    
    Water = variable.Variable("Water", "B01")
    Coffee = variable.Variable("Coffee", "B02")
    Tea = variable.Variable("Tea", "B03")
    Milk = variable.Variable("Milk", "B04")
    OJ = variable.Variable("Orange Juice", "B05")
    Beverages = [Water, Coffee, Tea, Milk, OJ]
    
    Backgammon = variable.Variable("Backgammon", "G01")
    Snakes = variable.Variable("Snakes & Ladders", "G02")
    Cluedo = variable.Variable("Cluedo", "G03")
    Pictionary = variable.Variable("Pictionary", "G04")
    Travel = variable.Variable("Travel the World", "G05")
    Games = [Backgammon, Snakes, Cluedo, Pictionary, Travel]
    
    Zebra = variable.Variable("Zebra", "A01")
    Dog = variable.Variable("Dog", "A02")
    Snail = variable.Variable("Snail", "A03")
    Fox = variable.Variable("Fox", "A04")
    Horse = variable.Variable("Horse", "A05")
    Animals = [Zebra, Dog, Snail, Fox, Horse]
    
    Blue = variable.Variable("Blue", "C01")
    Red = variable.Variable("Red", "C02")
    Green = variable.Variable("Green", "C03")
    Ivory = variable.Variable("Ivory", "C04")
    Yellow = variable.Variable("Yellow", "C05")
    colours = [Blue, Red, Green, Ivory, Yellow]
    
    AllVars = [Nationality, Beverages,Games, Animals, colours]
    return AllVars

def Go_Through_Constraints(allVars):
    changed = True
    while(changed == True):
        changed = False
        c15_c24 = False
        c1 = Constraint_equality(allVars[0][1], allVars[4][1])      #(English, Red)
        c2 = Constraint_equality(allVars[0][2], allVars[3][1])      #(Spanish, Dog)
        c3 = Constraint_equality(allVars[1][1], allVars[4][2])      #(Coffee, Green)
        c4 = Constraint_equality(allVars[0][3], allVars[1][2])      #(Ukrainian, Tea)
        c5 = Constraint_toRight_of(allVars[4][3], allVars[4][2])    #(Ivory, Green)
        c6 = Constraint_equality(allVars[2][1], allVars[3][2])      #(Snakes, Snail)
        c7 = Constraint_equality(allVars[2][2], allVars[4][4])      #(Cluedo, Yellow)
        c8 = Constraint_equality_var_cons(allVars[1], allVars[1][3], 3)      #(Beverages, Milk, 3)
        c9 = Constraint_equality_var_cons(allVars[0], allVars[0][0], 1)    #(Nationality, Norwegian, 1)
        c10 = Constraint_equality(allVars[2][4], allVars[1][4])     #(Travel, OJ)
        c11 = Constraint_equality(allVars[0][4], allVars[2][0])     #(Japanese, Backgammon)
        c12 = Constraint_Nextto(allVars[2][3], allVars[3][3])       #(Pictionary, Fox)
        c13 = Constraint_Nextto(allVars[2][2], allVars[3][4])       #(Cluedo, Horse)
        c14 = Constraint_Nextto(allVars[0][0], allVars[4][0])       #(Norwegian, Blue)
        for x in range(5):
            c15 = Constraint_NoSet_variable_Match(allVars[x])   #(category)
            c20 = Constraint_Last_Available(allVars[x])          #(category)
            if c15 or c20:
                c15_c24 = False
        
        if c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8 or c9 or c10 or c11 or c12 \
        or c13 or c14 or c15_c24:
            changed = True
    
    