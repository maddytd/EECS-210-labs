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
    main function that takes 2 binary strings and outputs 
    their results of and, or, and xor operations

    program continues unlesss user decides to exit
    '''

    # Loop to keep program running
    while True:
        # Get first binary string from user
        binary_str1 = get_binary_string()
        
        # Get second binary string from user
        binary_str2 = get_binary_string()

        # Check if both strings have the same length
        if len(binary_str1) != len(binary_str2):
            print(f"Error: Bit strings must have the same length!")
            print(f"First string has {len(binary_str1)} bits, second string has {len(binary_str2)} bits.")
            print("Please restart and try again.")
            print()  # Blank line for readability
            continue  # Restart the loop to get new inputs
        
        # Perform bitwise operations
        and_result = bitwise_and(binary_str1, binary_str2)
        or_result = bitwise_or(binary_str1, binary_str2)
        xor_result = bitwise_xor(binary_str1, binary_str2)
        
        # Display results (keeping leading zeros as specified)
        print(f"AND: {and_result}")
        print(f"OR: {or_result}")
        print(f"XOR: {xor_result}")
        print()  # Blank line for readability
        
        # Ask user if they want to continue
        continue_choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        
        # Exit loop if user says no
        if continue_choice in ['no', 'n']:
            print("Thank you for using the bitwise operations program!")
            break
        
        print()  # Blank line between runs

#run program
if __name__ == "__main__":
    main()