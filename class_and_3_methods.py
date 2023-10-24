class MyClasses:
    def sum_two_numbers(self, num1, num2):
        return num1 + num2

    def is_palindrome(self, word):
        word = word.lower()
        reversed_word = word[::-1]
        return word == reversed_word

    def reversed_string(self, string):
        return string[::-1]


mc = MyClasses()

print(mc.sum_two_numbers(5, 5))
print(mc.is_palindrome("house"))
print(mc.is_palindrome("radar"))
print(mc.reversed_string("Python"))
