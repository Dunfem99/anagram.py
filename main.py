# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

str1 = "Elbow"
str2 = "Below"

    
str1 = str1.lower()
str2 = str2.lower()

def find_anagram(str1,str2):
    # [assignment] Add your code here
    

    
    if(len(str1) == len(str2)):

   
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)

   
        if(sorted_str1 == sorted_str2):
            print("True")
        else:
            print("False")

    else:
        print("False")

print(find_anagram(str1,str2))      

