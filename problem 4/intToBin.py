def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    #while num1 > 0:
        #write your code
    while num1 > 0:
        binary_val += str(num1 % 2)
        num1 = num1 // 2

    return binary_val;


def string_reverse(input_string): 
    reverse_input = ''
    
   #write your for loop here
    
    return input_string[::-1]

if __name__ == '__main__':
    user_input = int(input())
    
    reversed_binary = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(reversed_binary))
    
    print(binary_string)