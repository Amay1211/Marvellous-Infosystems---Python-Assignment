minimunLength = lambda str : len(str) >= 5

def main():
  data = ["sdadsf","SADfsaf","Df","DFs", "SDFsadf","DSfasf","Fsafsdf"]

  ret = list(filter(minimunLength,data))
  print(f"string with length is more than 5 is {ret}")

if __name__ == '__main__':
  main()
