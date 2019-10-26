from markdown2 import markdown
import fileio
def translate(inp:str="# header",outputFileName:str=None)->str:
    print(inp)
    output = markdown(inp)
    if outputFileName:
       fileio.writeToFile("web/out/"+outputFileName,output)
    return output


if __name__ == "__main__":
    markdownInput = input("enter a markdown statement : ")

    if input("do you want to write result into a file ? (y,n) : ") == "y":
        filename = input("so enter your file name : ")
        data = translate(markdownInput,filename)
        print("the data written into the file was this : \n\n")
        print(data)
    else:
        print("we don't write your data into file but the data is this : \n\n\a")
        data = translate(markdownInput)
        print(data)
    