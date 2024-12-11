def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   
   return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__':   
   user_val1 = int(input())
   user_val2 = int(input())
   user_val3 = int(input())
   user_val4 = int(input())
   #store output for every input here
   #print those output
   swapped_values = swap_values(user_val1, user_val2, user_val3, user_val4)
   print(swapped_values)

 