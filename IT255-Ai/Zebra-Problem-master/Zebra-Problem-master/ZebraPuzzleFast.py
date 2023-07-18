import Constraints
import tree
from copy import deepcopy
from time import time

def process_each(parentNode):-  allVars1 = parentNode.get_data()
    for x in range (5):
        for y in range (5):
    #       only split domain that are not satisfied 
            if not Constraints.is_satisfied(allVars1[x][y]):
                new_domains = allVars1[x][y].getDomains()
                for i in range (len(new_domains)):
                    allVars2 = deepcopy(allVars1)
                    redDomain = []
                    redDomain.append(new_domains[i])
                    allVars2[x][y].setDomains(redDomain)
                    Constraints.Go_Through_Constraints(allVars2)
                    #check to see if any are empty
                    if not Constraints.is_any_empty(allVars2):                        
                        new_node = tree.Node(allVars2)
                        parentNode.add_child(new_node)
                        process_each(new_node)
                
def any_Answers(parentNode):
    answers = []
    if parentNode.children == []:
        allvars = parentNode.get_data()
        if Constraints.is_all_satisfied(allvars):
            possible_answers = Constraints.print_domainResults(allvars)
            for i in range (len(possible_answers)):
                answers.append(possible_answers[i])
    else:
        for i in range (len(parentNode.children)):
            possible_answers = any_Answers(parentNode.children[i])
            if possible_answers != None:
                for i in range (len(possible_answers)):
                    answers.append(possible_answers[i])
    return answers
    

timetaken = 0
ts = time()
                     
allVars1 = Constraints.set_up_Variables()

print("Start")
Constraints.print_all(allVars1)
print("_______________________________________________")


print("_______________________________________________")
print("Please bear with us as we try to solve the puzzle")
print("_______________________________________________")
print("_______________________________________________")

Constraints.Go_Through_Constraints(allVars1)    # fill the initial constraints
parentNode = tree.Node(allVars1)          # make the first go through the parent node.
process_each(parentNode)                        # process_each(parentNode, 0)

#Go through tree and find the correct answers
Answers = any_Answers(parentNode)
answer_list = []
full_answer_list = []
for i in range(0,len(Answers), 5):
    answer_list = Answers[i] + Answers[i+1] + Answers[i+2] + Answers[i+3] + Answers[i+4]
    full_answer_list.append(answer_list)

answer_set = list(set(full_answer_list)) #get unique answers
print("")
print("The possible solutions to the puzzle are: ")
print("")
for i in range(len(answer_set)):
    print(answer_set[i])
    print("_______________________________________________")

timetaken = format(time()-ts)
print ("Total Time: ", timetaken)
