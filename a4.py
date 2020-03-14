#a4.py

#class repersent a  Definite Clauses knowledge base and possible acctions 
# all function expected to accept "funcName.(self, aurgs)", aurgs = ["a","b",...]
class knowledgeBase:

    #data
    atoms = [] #{"atom1": True, ....}
    rules = {} #{"atomN": ["atomX","atomY",...]}

    #load knowledge base
    def load(self, aurgs):

        #check aurguments
        if len(aurgs) != 1:
            raise AurgError("load needs one input")

        if aurgs[0][-4:] != ".txt":
            raise AurgError("input to load must end with \".txt\"")
        
        #load KB
        try:
            fileKB = open(aurgs[0],"r")
        except FileNotFoundError:
            raise AurgError("No such file or directory: \""+aurgs[0]+"\"")

        ruleCounter = 0
        tempRules = {}
        for line in fileKB:
            if line != "\n":
                #print("  ",line, end="")
                lineSplit = line.split()

                i = 0
                for token in lineSplit:
                    #checks rule format, toekn type 
                    if ((i%2 == 0) and not self._is_atom(token)) or (i == 1 and token != "<--") or (i%2 == 1 and i != 1 and token != "&"):
                        raise AurgError(aurgs[0] + " is not a valid knowledge base, rule " + str(ruleCounter + 1) + " token \""+ token +"\" is invalid")
                    i += 1

                #checks rule format, correct number of tokens ie trailing operator
                if len(lineSplit) % 2 != 1:
                    raise AurgError(aurgs[0] + " is not a valid knowledge base, rule " + str(ruleCounter + 1) + " is invalid, trailing operator not allowed")

                tempRules[lineSplit[0]]= lineSplit[2::2]    
                ruleCounter += 1

        self.rules = tempRules
        self.atoms = []

        #print results
        print("  ",ruleCounter, "new rule(s) added\n")
        for h in self.rules.keys():
            print("  ", h, "<-- ", end='')
            for atom in self.rules[h]:
                print(atom, end='')
                if atom != self.rules[h][-1]:
                    print(" & ", end='')
                else:
                    print("\n", end='')
        print("\n", end='')

        
    #tell, set variable(s) to true 
    def tell(self, aurgs):

        #check aurgments 
        if len(aurgs) < 1:
            raise AurgError("tell needs atleast one atom")

        for atom in aurgs:
            if not self._is_atom(atom):
                raise AurgError("\""+atom +"\" is not a valid atom" )

        #Check kb loaded
        if self.rules == {}:
            raise AurgError("No knowledge base has been loaded")

        #Remove duliactes
        aurgs = list(dict.fromkeys(aurgs))

        #Do asssingment 
        for atom in aurgs:
            if atom in self.atoms:
                print("  atom \""+atom+"\" already know to be true")
            else:
                self.atoms.append(atom)    
                print("  \""+atom+"\" added to KB")
        print("\n", end='')
        
    #infer all possible values and print 
    def infer_all(self, aurgs):

        #check aurguments
        if len(aurgs) != 0:
            raise AurgError("infer_all takes no input")

        #infer all 
        newAtoms = []
        
        while(1):
            foundNewAtom = False 
            h_open = [x for x in self.rules.keys() if x not in self.atoms]
            for h in h_open:
                conditions = self.rules[h]
                if all(elem in self.atoms for elem in conditions):
                    newAtoms.append(h)
                    self.atoms.append(h)
                    foundNewAtom = True
                    break
            if(not foundNewAtom):
                break
        
        #print results
        print("  Newly inferrd atoms:\n      ", end ='')
        if newAtoms == []:
            print("<none>", end='')
        else:
            for atom in newAtoms:
                print(atom, end ='')
                if atom != newAtoms[-1]:
                    print(", ", end ='')
        print("\n  Atoms already known to be true:\n      ", end='')
        oldAtoms = [x for x in self.atoms if x not in newAtoms]
        if oldAtoms == []:
            print("<none>", end='')
        else:
            for atom in oldAtoms:
                print(atom, end ='')
                if atom != oldAtoms[-1]:
                    print(", ", end='')
        print("\n")
                
    #remove told values
    def clear_atoms(self, aurgs):

        #check aurguments 
        if len(aurgs) != 0:
            raise AurgError("clear_atoms takes no input")

        #remove told atoms
        self.atoms = []
        print("  All atoms cleared\n")

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
    if len(inputSplit) == 0:
        cmd = ""
    else:
        cmd = "KB." + inputSplit[0] + "(["
        for i in inputSplit[1:]:
            cmd = cmd + "\"" + i + "\"" 
            if inputSplit[1:].index(i) < len(inputSplit[1:]) -1:
                cmd = cmd + ","
        cmd = cmd  + "])"

    # calls appropriate function 
    try:

        #check cmd
        generalValidChars = "_abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        startingValidChars = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if cmd == "":
            pass
        elif (not all(elem in generalValidChars for elem in inputSplit[0])) or not (inputSplit[0][0] in startingValidChars):
            raise AurgError("Invalid command charaters \"" + inputSplit[0] + "\"")
        else:
            eval(cmd)

    except AurgError as e:
        print("Error:", e.message)
    except AttributeError as e:
        print("Error: unknown command \"", inputSplit[0],"\"", sep = '')
    # except TypeError as e: #should remove
    #     print("Error: unknown command \"", inputSplit[0],"\"", sep = '')
    #     print(e)
