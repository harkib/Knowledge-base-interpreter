#a4.py
def test(x):
    if x == []:
        raise AurgError("Test needs one input")
    print("test good: ", x )


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class AurgError(Error):

    def __init__(self, message):
        self.message = message

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
