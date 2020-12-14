#Creating logging functionality for Warnings & Errors
import sys 
import datetime

CSI=u"\u001b"
output = CSI+"[38;5;{color}m"+ "{stdout}" + CSI + "[0m"

def warning(warning, path):
    __write_to_file(path+"Warnings", warning, 220)
    print(output.format(color=220,stdout=warning))

def error(error, path):
    __write_to_file(path+"Errors", error, 160)
    print(output.format(color=160,stdout=error))

def __write_to_file(file, log, code):
    sys.stderr = open(file+".txt", "a+")
    now = datetime.datetime.now().strftime("%b-%d-%G @ %I:%M%p")
    file_out = log + " - " + now
    sys.stderr.write(file_out +"\n")
    sys.stderr.close()   
