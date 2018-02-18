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

#-----------------------------------------------------------------------------#
#1.6 String Compression: Basic string Compression using counts of repeated characters
# Example 'aabcccccaaa' to 'a2b1c5a3'
# My Solution
import copy
def stringCompression(text):
    """ Complexity O(n) - Travesing over the loop
        better to join string from list instead of conactenation
    """
    repeat_count = 1
    compressed_text_list = []
    prev_c = ""
    text += ";"
    for c in text:
        if(c == prev_c):
            repeat_count += 1
        elif(c != prev_c and prev_c != ""):
            compressed_text_list.append(prev_c + str(repeat_count))
            repeat_count = 1
        prev_c = copy.deepcopy(c)

    compressed_text = "".join(compressed_text_list)
    if(len(compressed_text) >= len(text)):
        compressed_text = text[:-1]

    return compressed_text

print("String Compression ", stringCompression("aabcccccaaa"))

#-----------------------------------------------------------------------------#
#1.7 Rotate matrix: Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate matrix by 90 degrees
# My Solution

def rotateMatrix(m):
    rotated_m = [[m[len(m[i]) -1 - j][i] for j in range(len(m[i]))] for i in range(len(m))]
    for row in rotated_m:
        print(row)

print("Rotated matrix \n ", rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))


#-----------------------------------------------------------------------------#
#1.8 ZERO matrix: Write an algorithm such that if an element in an MxN matrix is 0
# its entire row and column are set to 0
#Solution
def nullifyRow(mat,row):
    for j in range(len(mat[0])):
        mat[row][j] = 0

def nullifyCol(mat,col):
    for i in range(len(mat)):
        mat[i][col] = 0

def zeroMatrix(mat):
    #Row and col to mantain 0s
    row = [False] * len(mat)
    col = [False] * len(mat[0])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if(mat[i][j] == 0):
                row[i] = True
                col[j] = True
    for i in range(len(row)):
        if(row[i]):
            nullifyRow(mat,i)
    for j in range(len(col)):
        if(col[j]):
            nullifyCol(mat,j)
    return mat

#Zero matrix test
print("Zero Matrix: ", zeroMatrix([[1,2,3,0],[4,0,6,7],[7,8,9,8]]))

#-----------------------------------------------------------------------------#
#1.9 String Rotation: Assume you have mathod isSubstring which checks one is sub strings
#of the other, write a code to check if s2 is rotation of s1 using only one call
#to isSubstring
#Solution

def isSubstring(s1,s2):
    if s2 in s1:
        return True
    return False

def isStringRotation(s1,s2):
    #check equal length and non empty
    if(len(s1) == len(s2) and len(s1) > 0):
        s1s1 = s1 + s1
        return isSubstring(s1s1,s2)
    return False

print("String Rotation: ", isStringRotation("waterbottle","erbottlewat"))
