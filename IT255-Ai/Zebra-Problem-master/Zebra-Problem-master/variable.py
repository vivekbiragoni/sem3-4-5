import houseDomains

class Variable(object):
    """ A Class representing variables in the puzzle"""
    def __init__(self, name, code):
        self.name = name
        self.__ID = code
        self.domains = houseDomains.HouseDomain()
        
    def PrintVariable(self):
        print("Name: ", self.name, " ID: ", self.__ID, " Domains: ", self.getDomains())
        
    def VariableDetails(self):
        return([self.name, self.__ID, self.getDomains])
        
    def getDomains(self):
        return self.domains.remainingDomains()
        
    def setDomains(self, myList):
        return self.domains.setDomain(myList)
    
    def is_satisfied(self):
        return self.domains.is_satisfied()
    
    def is_empty(self):
        return self.domains.is_empty()
    
    def split_doimain(self):
        return self.domains.splitDomain()