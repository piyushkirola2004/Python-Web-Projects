class AllPrograms:

    # ---------------- Math Operations ----------------

    # 1. Prime Check
    def _prime_checker(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_checker(self):
        try:
            num = int(input("Enter the number: "))
            print(f"{num} is {'prime' if self._prime_checker(num) else 'not prime'}")
        except Exception as e:
            print(e)

    # 2. Factorial
    def _factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def factorial(self):
        try:
            num = int(input("Enter a number: "))
            print(f"Factorial of {num} is {self._factorial(num)}")
        except Exception as e:
            print(e)

    # 3. Reverse String
    def _reverse_string(self, s):
        return s[::-1]

    def reverse_string(self):
        try:
            s = input("Enter a string: ")
            print(f"Reversed string: {self._reverse_string(s)}")
        except Exception as e:
            print(e)

    # 4. Palindrome Check
    def _is_palindrome(self, s):
        return s == s[::-1]

    def palindrome_check(self):
        try:
            s = input("Enter a string: ")
            print(
                f"'{s}' is {'palindrome' if self._is_palindrome(s) else 'not palindrome'}"
            )
        except Exception as e:
            print(e)

    # 5. Fibonacci Sequence
    def _fibonacci_sequence(self, n):
        seq = []
        a, b = 0, 1
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        return seq

    def fibonacci_sequence(self):
        try:
            n = int(input("Enter number of terms: "))
            print(f"Fibonacci sequence: {self._fibonacci_sequence(n)}")
        except Exception as e:
            print(e)

    # 6. Sum of Digits
    def _sum_digits(self, n):
        return sum(int(d) for d in str(abs(n)))

    def sum_digits(self):
        try:
            n = int(input("Enter a number: "))
            print(f"Sum of digits: {self._sum_digits(n)}")
        except Exception as e:
            print(e)

    # 7. Factorial Using Recursion
    def _factorial_rec(self, n):
        if n <= 1:
            return 1
        return n * self._factorial_rec(n - 1)

    def factorial_recursion(self):
        try:
            n = int(input("Enter a number: "))
            print(f"Factorial (recursion) of {n} is {self._factorial_rec(n)}")
        except Exception as e:
            print(e)

    # 8. GCD (Euclidean)
    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcd(self):
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"GCD: {self._gcd(a, b)}")
        except Exception as e:
            print(e)

    # 9. Check Leap Year
    def _is_leap_year(self, year):
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        return False

    def check_leap_year(self):
        try:
            year = int(input("Enter a year: "))
            print(
                f"{year} is {'a leap year' if self._is_leap_year(year) else 'not a leap year'}"
            )
        except Exception as e:
            print(e)

    # 10. Power Without **
    def _power(self, base, exp):
        result = 1
        for _ in range(exp):
            result *= base
        return result

    def power(self):
        try:
            base = int(input("Enter base: "))
            exp = int(input("Enter exponent: "))
            print(f"{base}^{exp} = {self._power(base, exp)}")
        except Exception as e:
            print(e)

    # 11. Reverse Words in a Sentence
    def _reverse_words(self, s):
        return " ".join(s.split()[::-1])

    def reverse_words(self):
        try:
            s = input("Enter a sentence: ")
            print(f"Reversed words: {self._reverse_words(s)}")
        except Exception as e:
            print(e)

    # 12. Count Vowels
    def _count_vowels(self, s):
        return sum(1 for ch in s if ch.lower() in "aeiou")

    def count_vowels(self):
        try:
            s = input("Enter a string: ")
            print(f"Vowels count: {self._count_vowels(s)}")
        except Exception as e:
            print(e)

    # 13. Armstrong Number Check
    def _is_armstrong(self, n):
        digits = [int(d) for d in str(abs(n))]
        return sum(d**3 for d in digits) == n

    def armstrong_check(self):
        try:
            n = int(input("Enter number: "))
            print(f"{n} is {'Armstrong' if self._is_armstrong(n) else 'not Armstrong'}")
        except Exception as e:
            print(e)

    # 14. Sum of Squares
    def _sum_squares(self, n):
        return sum(i**2 for i in range(1, n + 1))

    def sum_squares(self):
        try:
            n = int(input("Enter a number: "))
            print(f"Sum of squares up to {n}: {self._sum_squares(n)}")
        except Exception as e:
            print(e)

    # 15. Decimal to Binary
    def _decimal_to_binary(self, n):
        return bin(n)[2:]

    def decimal_to_binary(self):
        try:
            n = int(input("Enter a decimal number: "))
            print(f"Binary: {self._decimal_to_binary(n)}")
        except Exception as e:
            print(e)

    # 16. Binary to Decimal
    def _binary_to_decimal(self, b):
        return int(b, 2)

    def binary_to_decimal(self):
        try:
            b = input("Enter binary number: ")
            print(f"Decimal: {self._binary_to_decimal(b)}")
        except Exception as e:
            print(e)

    # 17. Second Largest Number
    def _second_largest(self, lst):
        unique = sorted(set(lst))
        return unique[-2] if len(unique) >= 2 else None

    def second_largest_number(self):
        try:
            lst = list(map(int, input("Enter numbers separated by space: ").split()))
            result = self._second_largest(lst)
            print(
                f"Second largest: {result if result is not None else 'Not enough elements'}"
            )
        except Exception as e:
            print(e)

    # 18. Largest Number
    def _largest(self, lst):
        return max(lst)

    def largest_number(self):
        try:
            lst = list(map(int, input("Enter numbers separated by space: ").split()))
            print(f"Largest number: {self._largest(lst)}")
        except Exception as e:
            print(e)

    # 19. Sum of List
    def _sum_list(self, lst):
        return sum(lst)

    def sum_list(self):
        try:
            lst = list(map(int, input("Enter numbers: ").split()))
            print(f"Sum of list: {self._sum_list(lst)}")
        except Exception as e:
            print(e)

    # 20. Remove Duplicates
    def _remove_duplicates(self, lst):
        return list(dict.fromkeys(lst))

    def remove_duplicates(self):
        try:
            lst = list(map(int, input("Enter numbers: ").split()))
            print(f"Without duplicates: {self._remove_duplicates(lst)}")
        except Exception as e:
            print(e)

    # 21. Intersection of Two Lists
    def _intersection(self, lst1, lst2):
        return [x for x in lst1 if x in lst2]

    def intersection_list(self):
        try:
            lst1 = list(map(int, input("List 1: ").split()))
            lst2 = list(map(int, input("List 2: ").split()))
            print(f"Intersection: {self._intersection(lst1, lst2)}")
        except Exception as e:
            print(e)

    # 22. Merge Two Sorted Lists
    def _merge_sorted_lists(self, lst1, lst2):
        return sorted(lst1 + lst2)

    def merge_sorted_lists(self):
        try:
            lst1 = list(map(int, input("List 1: ").split()))
            lst2 = list(map(int, input("List 2: ").split()))
            print(f"Merged: {self._merge_sorted_lists(lst1, lst2)}")
        except Exception as e:
            print(e)

    # 23. Check if List is Sorted
    def _is_sorted(self, lst):
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

    def sorted_list(self):
        try:
            lst = list(map(int, input("Enter numbers: ").split()))
            print(f"List is {'sorted' if self._is_sorted(lst) else 'not sorted'}")
        except Exception as e:
            print(e)

    # 24. Find Missing Number in Consecutive List
    def _missing_number(self, lst, diff):
        lst.sort()
        missing = []
        for i in range(len(lst) - 1):
            current = lst[i] + diff
            while current < lst[i + 1]:
                missing.append(current)
                current += diff
        return missing

    def missing_consecutive_num(self):
        try:
            lst = list(map(int, input("Enter numbers: ").split()))
            diff = int(input("Enter common difference: "))
            print(f"Missing numbers: {self._missing_number(lst, diff)}")
        except Exception as e:
            print(e)

    # 25. Reverse Integer
    def _reverse_integer(self, n):
        sign = -1 if n < 0 else 1
        n = abs(n)
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return rev * sign

    def reverse_integer(self):
        try:
            n = int(input("Enter number: "))
            print(f"Reversed integer: {self._reverse_integer(n)}")
        except Exception as e:
            print(e)

    # 26. Longest Word in a Sentence
    def _longest_word(self, sentence):
        words = sentence.split()
        return max(words, key=len) if words else None

    def longest_word(self):
        try:
            sentence = input("Enter sentence: ")
            print(f"Longest word: {self._longest_word(sentence)}")
        except Exception as e:
            print(e)

    # 27. Check if Number is Power of 2
    def _is_power_of_two(self, n):
        return n > 0 and (n & (n - 1)) == 0

    def num_power(self):
        try:
            n = int(input("Enter number: "))
            print(
                f"{n} is {'power of 2' if self._is_power_of_two(n) else 'not power of 2'}"
            )
        except Exception as e:
            print(e)

    # 28. Flatten Nested List
    def _flatten(self, lst):
        result = []
        for i in lst:
            if isinstance(i, list):
                result.extend(self._flatten(i))
            else:
                result.append(i)
        return result

    def flatten(self):
        try:
            nested = eval(input("Enter nested list: "))
            print(f"Flattened list: {self._flatten(nested)}")
        except Exception as e:
            print(e)

    # 29. Find Pairs with Given Sum
    def _find_pairs(self, lst, target):
        return [
            (lst[i], lst[j])
            for i in range(len(lst))
            for j in range(i + 1, len(lst))
            if lst[i] + lst[j] == target
        ]

    def find_pairs(self):
        try:
            lst = list(map(int, input("Enter list: ").split()))
            target = int(input("Enter target sum: "))
            print(f"Pairs: {self._find_pairs(lst, target)}")
        except Exception as e:
            print(e)

    # 30. Check if Two Strings are Rotations
    def _is_rotation(self, str1, str2):
        return len(str1) == len(str2) and str2 in str1 * 2

    def rotation_checker(self):
        try:
            str1 = input("Enter first string: ")
            str2 = input("Enter second string: ")
            print(
                f"Strings are {'rotations' if self._is_rotation(str1, str2) else 'not rotations'}"
            )
        except Exception as e:
            print(e)

    # 31. Convert List of Tuples to Dictionary
    def _tuple_to_dict(self, lst):
        return dict(lst)

    def tuple_dict(self):
        try:
            lst = eval(input("Enter list of tuples: "))
            print(f"Dictionary: {self._tuple_to_dict(lst)}")
        except Exception as e:
            print(e)

    # 32. Find Median
    def _median(self, lst):
        lst_sorted = sorted(lst)
        n = len(lst_sorted)
        if n % 2:
            return lst_sorted[n // 2]
        else:
            return (lst_sorted[n // 2 - 1] + lst_sorted[n // 2]) / 2

    def median(self):
        try:
            lst = list(map(int, input("Enter numbers: ").split()))
            print(f"Median: {self._median(lst)}")
        except Exception as e:
            print(e)

    # 33. Sort Dictionary by Value
    def _sort_dict_by_value(self, d):
        return dict(sorted(d.items(), key=lambda x: x[1]))

    def sorted_dict(self):
        try:
            d = eval(input("Enter dictionary: "))
            print(f"Sorted dict: {self._sort_dict_by_value(d)}")
        except Exception as e:
            print(e)

    # 34. Prime Numbers up to n (Sieve)
    def _prime_numbers(self, n):
        primes = []
        for num in range(2, n + 1):
            if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
                primes.append(num)
        return primes

    def list_prime_numbers(self):
        try:
            n = int(input("Enter n: "))
            print(f"Primes: {self._prime_numbers(n)}")
        except Exception as e:
            print(e)

    # 35. Check Subsequence in List
    def _is_subsequence(self, large, small):
        it = iter(large)
        return all(x in it for x in small)

    def subsequence_list(self):
        try:
            large = list(map(int, input("Enter large list: ").split()))
            small = list(map(int, input("Enter small list: ").split()))
            print(f"Subsequence exists: {self._is_subsequence(large, small)}")
        except Exception as e:
            print(e)

    # 36. Find Common Elements in Three Lists
    def _common_three_lists(self, lst1, lst2, lst3):
        return [x for x in lst1 if x in lst2 and x in lst3]

    def common_elements_list(self):
        try:
            lst1 = list(map(int, input("List 1: ").split()))
            lst2 = list(map(int, input("List 2: ").split()))
            lst3 = list(map(int, input("List 3: ").split()))
            print(f"Common elements: {self._common_three_lists(lst1,lst2,lst3)}")
        except Exception as e:
            print(e)

    # 37. Swap Two Numbers
    def _swap_numbers(self, a, b):
        return b, a

    def swapping_numbers(self):
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            a, b = self._swap_numbers(a, b)
            print(f"After swap: a={a}, b={b}")
        except Exception as e:
            print(e)

    # 38. Remove Nth Occurrence of Character
    def _remove_nth_char(self, s, pos, char):
        words = s.split()
        if 0 < pos <= len(words):
            words[pos - 1] = words[pos - 1].lstrip(char)
        return " ".join(words)

    def remove_occurrence(self):
        try:
            s = input("Enter string: ")
            pos = int(input("Enter word position: "))
            char = input("Enter character to remove: ")
            print(f"Modified: {self._remove_nth_char(s,pos,char)}")
        except Exception as e:
            print(e)

    # 39. First Non-Repeated Character
    def _first_non_repeated(self, s):
        for ch in s:
            if s.count(ch) == 1:
                return ch
        return None

    def first_non_repeated_character(self):
        try:
            s = input("Enter string: ")
            print(f"First non-repeated character: {self._first_non_repeated(s)}")
        except Exception as e:
            print(e)

    # 40. Check if String Contains Only Digits
    def _digits_only(self, s):
        return s.isdigit()

    def digits_checks(self):
        try:
            s = input("Enter string: ")
            print(f"Contains only digits: {self._digits_only(s)}")
        except Exception as e:
            print(e)

    # 41. Generate All Subsets
    def _subsets(self, lst):
        res = [[]]
        for num in lst:
            res += [curr + [num] for curr in res]
        return res

    def generate_subsets(self):
        try:
            lst = list(map(int, input("Enter list: ").split()))
            print(f"All subsets: {self._subsets(lst)}")
        except Exception as e:
            print(e)

    # 42. Count Frequency of Characters in String
    def _char_frequency(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        return freq

    def count(self):
        try:
            s = input("Enter string: ")
            print(f"Character frequency: {self._char_frequency(s)}")
        except Exception as e:
            print(e)

    # 43. Count Frequency of Words in File
    def _word_frequency_file(self, filename):
        freq = {}
        with open(filename, "r") as f:
            for word in f.read().split():
                freq[word.lower()] = freq.get(word.lower(), 0) + 1
        return freq

    def frequency_word(self):
        try:
            filename = input("Enter filename: ")
            print(f"Word frequency: {self._word_frequency_file(filename)}")
        except Exception as e:
            print(e)

    # 44. First Non-Repeated Character
    def _first_non_repeated_character(self, string):
        for ch in string:
            if string.count(ch) == 1:
                return ch
        return None


    def first_non_repeated_character(self):
        try:
            string = input("Enter the string: ")
            result = self._first_non_repeated_character(string)
            if result:
                print(f"The first non-repeated character is: {result}")
            else:
                print("No non-repeated character found")
        except Exception as e:
            print(e)


    # 45. Check if String Contains Only Digits
    def _digits_only(self, string):
        return string.isdigit()

    def digits_checks(self):
        try:
            string = input("Enter any string: ")
            if self._digits_only(string):
                print("Input string contains only digits")
            else:
                print("Input string does not contain only digits")
        except Exception as e:
            print(e)

    # 46. Anagram Check
    def _is_anagram(self, s1, s2):
        return sorted(s1) == sorted(s2)

    def anagram(self):
        try:
            s1 = input("Enter string 1: ")
            s2 = input("Enter string 2: ")
            print(f"Anagram: {self._is_anagram(s1,s2)}")
        except Exception as e:
            print(e)

    # 47. Generate All Subsets of a Set
    def _generate_subsets(self, numbers):
        subsets = [[]]
        for num in numbers:
            subsets += [curr + [num] for curr in subsets]
        return subsets


    def generate_subsets(self):
        try:
            numbers = list(map(int, input("Enter numbers for the list: ").split()))
            result = self._generate_subsets(numbers)
            print(f"All subsets: {result}")
        except Exception as e:
            print(e)
