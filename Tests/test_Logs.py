import sys
sys.path.append('../Utilities/')
import Log
log_path = "../Logs/"

try:
    Log.warning("Warning test success!",log_path)
    Log.error("Error test success!", log_path)
except Exception as e:
    print("Logging Test Failed")
    print(e)
