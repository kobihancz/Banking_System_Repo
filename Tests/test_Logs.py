import sys
sys.path.append('../Utilities/')
import Log
log_path = "../Logs/"

try:
    Log.warning("Warning test success!",log_path)
    Log.error("Error test success!", log_path)
except:
    print("Logging Test Failed")
