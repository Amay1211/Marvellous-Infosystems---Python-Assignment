import sys

def main():
  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation script is use to travel the directory")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py DirectoryName")
      print("Directory name should be absoulte path")
    else:
      directory = sys.argv[1]
      print("Directory name is : ", directory)
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")


if __name__ == "__main__":

  main()