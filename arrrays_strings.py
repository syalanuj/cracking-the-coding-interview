"""
Cracking the coding interview
Chapter 1: Arrays and Strings
@author - anujsyal
"""
#-----------------------------------------------------------------------------#
#1.1 Implement algo to determine if a string has all unique characters? What if
# you cannot use an additional data structure

#Answer: Solution 1 with additional ds
def checkUniqueCharacters_1(text):
    """ Checks if text has unique characters
        Time Complexity:
        converting string to set =  O(n)
        len of text = O(1)
        Total = O(n)
    """
    if(len(text) == len(set(text))):
        return True
    else:
        return False

#Test
print(checkUniqueCharacters_1("asd"))

#Anser: Solution2 without ds
def checkUniqueCharacters_2(text):
    """ Checks unique characters by mantaining an array of boolean values for
        each int ascii values of an integer, which will have 128 ascii values
        Time Complexity:
        Iteration over string : O(n) but it will be constant as there are only
                                128 characters
        Total O(n)
    """
    if(len(text) > 128):
        return False
    char_set = [False] * 128
    for char in text:
        if(char_set[ord(char)] == True):
            return False
        char_set[ord(char)] = True
    return True
#Test
print("unique characters: ", checkUniqueCharacters_2("abca"))

#This can also be comparing all characters to each other at O(n^2)
#also can sort and then compare side values O(nlog(n))
#-----------------------------------------------------------------------------#
#1.2 Given two strings, write a method to decide if one is a permutation of other
#My Solution which looks wrong
def checkPermutation(text,text2):
    """Check permutation of two strings
    Complexity - O(nlogn) - sorting
    """
    if (sorted(text) == sorted(text2)):
        return True
    return False
#Test
print("Permutation: ",checkPermutation("abc", "cb"))

#-----------------------------------------------------------------------------#
#1.3 URLify: Write a method to replace all spaces in a string with "%20"
# Solution 1
def urlify(text):
    """ urlify json using python ds
        Complexity - O(n) split iterates over all the characters and join as well
    """
    text = " ".join(text.split())
    text = text.replace(" ", "%20")
    return text

#Test
print("URLify: ", urlify("     Mr        Smith       "))


#-----------------------------------------------------------------------------#
#1.4 Palindrome Permutation: Given a string, check if it is permutation of Palindrome
# To be a permutation of a palindrome , a string can have no more than one characters
# that is odd
# To be done

#sum(v % 2 for v in Counter("Tact Coa").values()) <= 1

#-----------------------------------------------------------------------------#
#1.5 One Away: There are three type of edits: insert a character; remove a char;
# or replace a character. Check if the strings are zero or one edit away
# Solution 1

def oneAway(text1,text2):
    """ One Away json using python ds
        Complexity - O(n) split iterates over all the characters
    """
    isOneAway = False
    if(checkOneReplace(text1,text2) == True):
        isOneAway = True
    elif(checkOneInsert(text1,text2) == True):
        isOneAway = True
    elif(checkOneRemove(text1,text2) == True):
        isOneAway = True

    return isOneAway

def checkOneReplace(text1,text2):
    if(len(text1) == len(text2)):
        diff_count = 0
        for i,c in enumerate(text1):
            if(text1[i] != text2[i]):
                diff_count += 1
                if(diff_count == 2):
                    return False
        return True
    else:
        return False

def checkOneInsert(text1,text2):
    if (len(text1) - len(text2) == 1):
        for i,c in enumerate(text2):
            if(text1[i] != text2[i]):
                fixed_text2 = text2[:i] + text1[i] + text2[i:]
                if(fixed_text2 == text1):
                    return True
            if(i == len(text2) - 1):
                fixed_text2 = text2 + text1[i+1]
                if(fixed_text2 == text1):
                    return True
    return False

def checkOneRemove(text1,text2):
    if (len(text1) - len(text2) == -1):
        for i,c in enumerate(text1):
            if(text1[i] != text2[i]):
                fixed_text2 = text2[:i] + text2[i+1:]
                if(fixed_text2 == text1):
                    return True
    return False



#Test case
print("One Away", oneAway("pale","bake"))
