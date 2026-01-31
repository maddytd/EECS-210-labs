# Name: Maddy Dang
# KUID: 3159243
# LAB Session: Monday 4:30-6:20pm
# LAB Assignment: 01
# Description: This program takes implements bitwise AND, OR, and XOR. The program must take command line
# input at runtime. The program takes as input two bit strings, each of length n. The program produces as
# output the bitwise AND, bitwise OR, and bitwise XOR of those strings.
# Collaborators / Sources: Claude.Ai

def get_binary_string():
    """
    Function to get a valid binary string from user input.
    Returns a string containing only '0' and '1' characters.
    """
    x = input("Enter a binary string: ")
    x = x.strip()
    
    # Check if the string contains only '0' and '1'
    if x.replace("1", "").replace("0", ""):
        print("Invalid characters, please try again")
        return get_binary_string()  # Recursively call until valid input
    
    return x

def bitwise_and(str1, str2):
    """
    performs bitwise AND operation on 2 binary srtings
    returns '1' only if both bits are '1', else returns '0'
    """
    result = ""
    for i in range(len(str1)):
        if str1[i] == '1' and str2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result

def bitwise_or(str1, str2):
    """
    performs bitwise OR operation on 2 binary strings
    returns '1' if at least one bit is '1', else returns '0'
    """
    result = ""
    for i in range(len(str1)):
        if str1[i] == '1' or str2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result