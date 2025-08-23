class Palindrome:
    def __init__(self, input):
        self.input = input

    def is_palindrome(self):
        left_pointer = 0
        right_pointer = len(self.input) - 1

        while left_pointer < right_pointer:
            if self.input[left_pointer] != self.input[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True


# Main program
if __name__ == "__main__":

    palindrome_checker = Palindrome("kayak")
    print(palindrome_checker.is_palindrome())

    palindrome_checker = Palindrome("abba")
    print(palindrome_checker.is_palindrome())

    palindrome_checker = Palindrome("hello")
    print(palindrome_checker.is_palindrome())

    palindrome_checker = Palindrome("a")
    print(palindrome_checker.is_palindrome())


