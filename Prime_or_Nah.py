number = int(input("Enter a number: "))

def prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

is_prime = prime(number)

if is_prime is True:
    print(f"NICE! {number} is prime!")
else:
    print(f"Oh no! {number} is not prime!")
