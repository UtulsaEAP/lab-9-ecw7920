def feet_to_steps(user_feet):
   #write your code here
   steps = user_feet / 2.5
   return int(steps)

if __name__ == '__main__':
    #take input feet steps here
    user_feet = float(input())
    #store it into the function
<<<<<<< HEAD
    steps = user_feet / 2.5
    #print your steps here
    print(int(steps))
=======
    steps = feet_to_steps(user_feet)
    
    #print your steps here
    print(steps)
>>>>>>> refs/remotes/origin/main
    feet_to_steps(5280)