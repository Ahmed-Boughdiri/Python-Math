
class Compose:
    def __init__(self,equation):
        self.equation = equation
    def start(self):
        result = []
        operations = {
            "+": "PLUS",
            "-": "MIN",
            "*": "MULT",
            "/": "DIV"
        }
        start_char = 0
        end_char = -1
        while(end_char != None):
            end_char += 1
            if(self.equation[end_char] in "0123456789"):
                end_char += 1
                if(end_char == (len(self.equation) - 1)):
                    end_char = None
            elif(self.equation[end_char] in "+-*/"):
                variable = self.equation[start_char:end_char]
                if("." in variable):
                    try:
                        variable = float(variable)
                    except:
                        # Return An Error
                        return "Error"
                else:
                    try:
                        variable = int(variable)
                    except:
                        # Return An Error
                        return "Error"
                result.append(variable)
                result.append(operations[self.equation[end_char]])
            else:
                # Return An Error
                return "Error"
        return result        
