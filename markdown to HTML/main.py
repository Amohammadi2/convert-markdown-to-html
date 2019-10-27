import os
import eel
import translator
eel.init("web")
@eel.expose
def handleMarkdown(markdownData:str,outpuFileName:str):
    data = translator.translate(markdownData,outpuFileName)
    return data
@eel.expose
def openOutputDirectory():
    currentPath = os.getcwd()
    targetPath = "\\web\\out"
    os.startfile(currentPath + targetPath)
eel.start("index.html",size=(1000,500))
