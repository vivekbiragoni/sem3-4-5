class HouseDomain(object):
    """ A Class representing Houses in the puzzle"""
    def __init__(self):
        self.__houses = [1,2,3,4,5]
                
    def domainReduction(self, house):
        #return true is domain changed
        if house in self.__houses:
            whichIndex = self.__houses.index(house)
            if whichIndex != -1:
                self.__houses.pop(whichIndex)
                return True
            else:
                return False
        
    def printDomain(self):
        print(self.__houses)
        
    def splitDomain(self):
        # split the domain in two and return two new domains
        half = int(len(self.__houses)/2)
        first_domain = self.__houses[0:half]
        second_domain = self.__houses[half:]
        return [first_domain, second_domain]
    
    def remainingDomains(self):
        return self.__houses
    
    def setDomain(self, myList):
        if len(self.__houses) == len(myList):
            for i in range(len(self.__houses)):
                if self.__houses[i] == myList[i]:
                    continue
                else:
                    self.__houses = []
                    self.__houses = list(myList)
                    return True
        else:
            self.__houses = []
            self.__houses = list(myList)
            return True
        return False
    
    def __eq__(self, otherDomain):
        '''compare two domains and make them equal each other'''
        changed = False
        for x in range (1, 6):
            if (x in self.remainingDomains()) and (x in otherDomain.remainingDomains()):
                continue
            else:
                if x in self.remainingDomains():
                    self.domainReduction(x)
                    changed = True
                elif x in otherDomain.remainingDomains():
                    otherDomain.domainReduction(x)
                    changed = True
        return changed
    
    def is_empty(self):
        return len(self.__houses) == 0
                
    def is_satisfied(self):
        '''check if there is only 1 possibility'''
        return len(self.__houses) == 1
         
