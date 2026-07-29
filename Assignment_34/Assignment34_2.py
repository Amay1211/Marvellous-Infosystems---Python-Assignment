# 1.Design automation script which display information of running processes as its name, PID,
# Username.
# Usage : ProcInfo.py

import os
import sys
import psutil
import time
import schedule

def processScan():
  listProcess = []

  for proc in psutil.process_iter():
    info = proc.as_dict(attrs=["name","pid", "status"])
    listProcess.append(info)
  return listProcess

def procInfo(folderName, ProcessName):
  BORDER = "-" * 50
  ret = False
  ret = os.path.exists(folderName)

  if ret == True:
    ret = os.path.isdir(folderName)
    if(ret == False):
      print("Unable to process as directory name is exist not its not a directory")
      return
  else:
    os.mkdir(folderName)
    print("Directory for log file gets created successfully")

  timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
  fileName = os.path.join(folderName,"Marvellous_%s.log" %timeStamp)
  fobj = open(fileName,"w")
  print(f"Log file gets created sucessfully with name {fileName}")

  fobj.write(BORDER + "\n")
  fobj.write("----Marvellous Platform Survillence System----\n")
  fobj.write(f"Log file gets created : {timeStamp}\n")
  fobj.write(BORDER + "\n\n")

  data = processScan()
  runnigProcess = list(filter(lambda data: data["name"] == ProcessName, data))
  for info in runnigProcess:
    fobj.write("PID: %s\n" %info.get("pid"))
    fobj.write("Name: %s\n" %info.get("name"))
    fobj.write("Status: %s\n" %info.get("status"))
    fobj.write(BORDER + "\n\n")

  fobj.write("-------------------------System Report------------------------\n")
  fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n")
  fobj.write(BORDER + "\n\n")
  fobj.write("-------------------------End of log fle-----------------------\n")
  fobj.write(BORDER + "\n\n")

  fobj.close()

def main():
  BORDER = "-" * 50
  print(BORDER)
  print("----Welcome to proc info system")
  print(BORDER)

  if(len(sys.argv) == 2):
    if sys.argv[1] == "--h" or sys.argv[1] == "--H":
      print("This automation script is use to perform")
      print("1 : It fetch the information of running processes")
      print("2 : it maintain all recorsd in to log file")
      print("3 :  it send log file through main periodically")
    elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
      print("Use the automation script as : ")
      print(f"python {sys.argv[0]} timeInterval folderName processName")
      print("timeIntval :  Time interval in minutes for periodic execution")
      print("folderName : Name of log file folder")
      print("ProcessName : Name of process")
    else:
      print("Unable to proceed as there is not maching args")
    pass
  # actual project code
  elif(len(sys.argv) == 4):
    print("Schedular started sucessfully")
    print("Press ctrl + C to abort the automation script")
    procInfo(sys.argv[2], sys.argv[3])
    schedule.every(int(sys.argv[1])).minutes.do(procInfo,sys.argv[2], sys.argv[3])
    while True:
      schedule.run_pending()
      time.sleep(1)

  else:
    print("Invalid number of arguments")
    print("Unable to proceed as argument are not maching")
    print("Please use --u or --h flag for more getting information")

  print(BORDER)
  print("----Thank you for using our automation system")
  print(BORDER)
  

if __name__ == "__main__":
  main()