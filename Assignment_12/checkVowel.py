def checkVowel(char):
  vowelList = ['a','e','i','o','u','A','E','I','O','U']
  if char in vowelList:
    return True
  else:
    return False 

def main():
  no = input("Enter a char : ")
  ret = checkVowel(no)
  if(ret == True):
    print("Vowel")
  else:
    print("Not a vowel")
    
if __name__ == '__main__':
  main()
