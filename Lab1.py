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
    performs bitwise AND operation on 2 binary strings
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

def bitwise_xor(str1, str2):
    """
    performs bitwise XOR operation on 2 binary strings
    returns '1' if bits are different, else returns '0'
    """
    result = ""
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            result += '1'
        else:
            result += '0'
    return result

def main():
    '''
    main function that takes 2 binary strings and outputs their 
    results of and, or, and xor operations
    '''
    # Get first binary string
    binary_str1 = get_binary_string()

    # Get second binary string
    binary_str2 = get_binary_string()

    # Ensure both strings are of the same length
    if len(binary_str1) != len(binary_str2):
        print("Binary strings must be of the same length. Please try again.")
        return
    
    # Perform bitwise operations
    and_result = bitwise_and(binary_str1, binary_str2)
    or_result = bitwise_or(binary_str1, binary_str2)
    xor_result = bitwise_xor(binary_str1, binary_str2)

    # Print results
    print(f"Bitwise AND: {and_result}")
    print(f"Bitwise OR: {or_result}")
    print(f"Bitwise XOR: {xor_result}")