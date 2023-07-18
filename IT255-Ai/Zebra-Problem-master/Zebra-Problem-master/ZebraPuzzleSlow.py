import Constraints
import tree
from copy import deepcopy
from time import time

# this program can take up to an hour to run. It's incredably slow and I'm not sure why.

def process_each(parentNode, parentNodeNO, childnode_no):
    allVars1 = parentNode.get_data()
    answers = []
    for x in range (5):
        for y in range (5):
    #       only split domain that are not satisfied 
            if not Constraints.is_satisfied(allVars1[x][y]):
                new_domains = allVars1[x][y].split_doimain()
                allVars2 = deepcopy(allVars1)
                allVars2[x][y].setDomains(new_domains[0])
                allVars3 = deepcopy(allVars1)
                allVars3[x][y].setDomains(new_domains[1])
                
                Constraints.Go_Through_Constraints(allVars2)
                Constraints.Go_Through_Constraints(allVars3)
                
                #check to see if any are empty
                if not Constraints.is_any_empty(allVars2):
                    new_node = tree.Node(allVars2)
                    new_child = parentNode.add_child(new_node)
                # work on the other option for the domain
                if not Constraints.is_any_empty(allVars3):
                    new_node = tree.Node(allVars3)
                    new_child = parentNode.add_child(new_node)
            #Process nodes just added
    print("here", parentNodeNO, "-", childnode_no)
    child_no = 0
    parentNodeNO +=1
    for child_node in (parentNode.children):
        child_no +=1
        possible_answers = child_node.get_data()
        if Constraints.is_all_satisfied(possible_answers):
            return_answers = Constraints.print_domainResults(possible_answers)
            for i in range (len(return_answers)):
                answers.append(return_answers[i])
        elif not Constraints.is_any_empty(possible_answers):
            process_each(child_node, parentNodeNO, child_no)
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
Constraints.print_all(allVars1)
print("_______________________________________________")

parentNode = tree.Node(allVars1)          # make the first go through the parent node.
Answers = process_each(parentNode, 0, 0)                

#Go through tree and find the correct answers
# Answers = any_Answers(parentNode)
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