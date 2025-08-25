class PrimeNumberChecker:
    def __init__(self, value):
        self.value = value

    def is_prime(self):
        if self.value < 2:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True

if __name__ == "__main__":
    prime_number_checker = PrimeNumberChecker(29)
    print(prime_number_checker.is_prime())

    prime_number_checker = PrimeNumberChecker(15)
    print(prime_number_checker.is_prime())

    prime_number_checker = PrimeNumberChecker(7)
    print(prime_number_checker.is_prime())
