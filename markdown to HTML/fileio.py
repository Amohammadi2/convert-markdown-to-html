def writeToFile(fileName:str,data:str):
    with open(fileName, "w") as file:
        file.write(data)
        file.close()
def readFromFile(fileName:str)->str:
    with open(fileName, "r") as file:
        return file.read()

def appendToFile(fileName:str,data:str):
    with open(fileName, "a") as file:
        file.write(data)
