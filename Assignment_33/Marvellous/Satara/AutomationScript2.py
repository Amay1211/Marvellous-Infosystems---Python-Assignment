import sys
import os

def main():
  if(len(sys.argv) == 2):
    directory = sys.argv[1]
    print("Directory name is : ", directory)
  else:
    print("Invalid number of arguments")


if __name__ == "__main__":
  main()