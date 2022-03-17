def is_prime(n):
    """Function that recognizes if a single integer number is prime"""
    
    for i in range(2,n):
        if(n % i) == 0:
            print("False")
            break
    else:
        print("True")
