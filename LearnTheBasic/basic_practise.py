class BasicPractise:
    def __init__(self):
        self.input = None

    def get_input(self):
        try:
            self.input = int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            self.get_input()

    def print_input(self):
        print(f"The input you entered is: {self.input}")

    @staticmethod
    def compare_numbers(first_number : int, second_number : int) -> str:
        if first_number==second_number:
            return "equal"
        elif first_number>second_number:
            return "greater"
        else:
            return "lesser"


if __name__ == "__main__":
    basic_practise = BasicPractise()

    basic_practise.get_input()
    basic_practise.print_input()
    print(basic_practise.compare_numbers(3, 5))
