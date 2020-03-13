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
            raise AurgError("input must be a .txt file")

    #tell, set variable(s) to true 
    def tell(self, aurgs):

        #helper functions
        # returns True if, and only if, string s is a valid variable name
        def is_atom(s):
            if not isinstance(s, str):
                return False
            if s == "":
                return False
            return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

        def is_letter(s):
            return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"  

        #check aurgments 
        if len(aurgs) < 1:
            raise AurgError("tell needs atleast one input")

        for atom in aurgs:
            if not is_atom(atom):
                raise AurgError("\""+atom +"\" is not a valid atom" )

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
    # cmd = "funcName.(["a","b",....])""
    inputSplit = userInput.split()
    cmd = inputSplit[0] + "(["
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
    except TypeError as e: #should remove
        print("Error: unknown command \"", inputSplit[0],"\"", sep = '')
        print(e)
