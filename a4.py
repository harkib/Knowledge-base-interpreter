#a4.py

#class repersent a  Definite Clauses knowledge base and possible acctions 
# all function expected to accept "funcName.(self, aurgs)", aurgs = ["a","b",...]
class knowledgeBase:

    #data
    atoms = {} #{"atom1": True, ....}
    rules = {} #{"atomN": ["atomX","atomY",...]}

    #load knowledge base
    def load(self, aurgs):

        #check aurguments
        if len(aurgs) != 1:
            raise AurgError("load needs one input")

        if aurgs[0][-4:] != ".txt":
            raise AurgError("input must repersent a .txt file")
        
        #load KB
        fileKB = open(aurgs[0],"r")
        ruleCounter = 0
        tempRules = {}
        for line in fileKB:
            if line != "\n":
                print("  ",line, end="")
                lineList = line.split()
                i = 0
                for token in lineList:
                    #checks rule format, what about trailing "&"
                    if ((i%2 == 0) and not self._is_atom(token)) or (i == 1 and token != "<--") or (i%2 == 1 and i != 1 and token != "&"):
                        raise AurgError(aurgs[0] + " is not a valid knowledge base, rule " + str(ruleCounter + 1) + " is invalid")
                    i += 1

                tempRules[lineList[0]]= lineList[2::2]    
                ruleCounter += 1

        self.rules = tempRules
        print("\n")
        print("  ",ruleCounter, "new rule(s) added")
        
        
    #tell, set variable(s) to true 
    def tell(self, aurgs):

        #check aurgments 
        if len(aurgs) < 1:
            raise AurgError("tell needs atleast one input")

        for atom in aurgs:
            if not self._is_atom(atom):
                raise AurgError("\""+atom +"\" is not a valid atom" )

        #Check kb loaded

        #Do asssingment 

    #infer all possible values and print 
    def infer_all(self, aurgs):

        #check aurguments
        if len(aurgs) != 0:
            raise AurgError("infer_all takes no input")

    #remove told values
    def clear_atoms(self, aurgs):

        #check aurguments 
        if len(aurgs) != 0:
            raise AurgError("clear_atoms takes no input")

    #helper functions
    # returns True if, and only if, string s is a valid variable name
    def _is_atom(self,s):
        if not isinstance(s, str):
            return False
        if s == "":
            return False
        return self._is_letter(s[0]) and all(self._is_letter(c) or c.isdigit() for c in s[1:])

    def _is_letter(self, s):
        return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"          

#base python error class
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

#simple message containing error class
class AurgError(Error):

    def __init__(self, message):
        self.message = message

#parsing and error test functions
def test(x):
    if len(x) != 1:
        raise AurgError("Test needs one input")
    print("test good: ", x )

def test2(x):
    if len(x) != 0:
        raise AurgError("Test2 takes no input")
    print("test2..." )


#initalize  KB
KB = knowledgeBase()

#interpeter running    
while(1):
    # print interpertor name and take input
    userInput = input("kb>")


    # parse input and form cmd
    # inputSplit = ["funcName", "a","b",...]
    # cmd = "KB.funcName.(["a","b",....])""
    inputSplit = userInput.split()
    cmd = "KB." + inputSplit[0] + "(["
    for i in inputSplit[1:]:
        cmd = cmd + "\"" + i + "\"" 
        if inputSplit[1:].index(i) < len(inputSplit[1:]) -1:
            cmd = cmd + ","
    cmd = cmd  + "])"

    # calls appropriate function 
    try:
        eval(cmd)
    except AurgError as e:
        print("Error:", e.message)
    except NameError as e:
        print("Error: unknown command \"", inputSplit[0],"\"", sep = '')
    # except TypeError as e: #should remove
    #     print("Error: unknown command \"", inputSplit[0],"\"", sep = '')
    #     print(e)
