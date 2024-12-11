def fibonacci(n):
    
    #write your code here
    if start_num < 0:
        return -1
<<<<<<< HEAD
    
    if start_num == 0:
=======
    elif start_num == 0:
>>>>>>> refs/remotes/origin/main
        return 0
    elif start_num == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, start_num + 1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')