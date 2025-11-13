from flask import Flask, render_template, request, jsonify
from main import AllPrograms

app = Flask(__name__)
programs = AllPrograms()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Map operation names to their methods
operation_map = {
    "prime": "_prime_checker",
    "factorial": "_factorial",
    "factorial_recursion": "_factorial_rec",
    "reverse_string": "_reverse_string",
    "palindrome_check": "_is_palindrome",
    "fibonacci_sequence": "_fibonacci_sequence",
    "sum_digits": "_sum_digits",
    "gcd": "_gcd",
    "check_leap_year": "_is_leap_year",
    "power": "_power",
    "reverse_words": "_reverse_words",
    "count_vowels": "_count_vowels",
    "armstrong_check": "_is_armstrong",
    "sum_squares": "_sum_squares",
    "decimal_to_binary": "_decimal_to_binary",
    "binary_to_decimal": "_binary_to_decimal",
    "second_largest_number": "_second_largest",
    "largest_number": "_largest",
    "sum_list": "_sum_list",
    "remove_duplicates": "_remove_duplicates",
    "intersection_list": "_intersection",
    "merge_sorted_lists": "_merge_sorted_lists",
    "sorted_list": "_is_sorted",
    "missing_consecutive_num": "_missing_number",
    "reverse_integer": "_reverse_integer",
    "longest_word": "_longest_word",
    "num_power": "_is_power_of_two",
    "flatten": "_flatten",
    "find_pairs": "_find_pairs",
    "rotation_checker": "_is_rotation",
    "tuple_dict": "_tuple_to_dict",
    "median": "_median",
    "sorted_dict": "_sort_dict_by_value",
    "list_prime_numbers": "_prime_numbers",
    "subsequence_list": "_is_subsequence",
    "common_elements_list": "_common_three_lists",
    "swapping_numbers": "_swap_numbers",
    "remove_occurrence": "_remove_nth_char",
    "first_non_repeated_character": "_first_non_repeated_character",
    "digits_checks": "_digits_only",
    "anagram": "_is_anagram",
    "generate_subsets": "_generate_subsets",
    "count": "_char_frequency",
    "frequency_word": "_word_frequency_file"
}

@app.route('/operation/<op_name>', methods=['POST'])
@app.route('/operation/<op_name>', methods=['POST'])
def operation(op_name):
    if op_name not in operation_map:
        return jsonify({"error": "Operation not found"}), 404

    method_name = operation_map[op_name]
    method = getattr(programs, method_name)

    data = request.get_json() or {}

    try:
        # Define operation types
        string_ops = ["reverse_string","palindrome_check","reverse_words",
                      "count_vowels","longest_word","rotation_checker",
                      "digits_checks","first_non_repeated_character",
                      "anagram","count","binary_to_decimal","tuple_dict"]

        list_ops = ["sum_list","remove_duplicates","intersection_list",
                    "merge_sorted_lists","flatten","generate_subsets",
                    "common_elements_list","subsequence_list"]

        dict_ops = ["sorted_dict"]

        # Prepare arguments
        args = []
        for k,v in data.items():
            if op_name in string_ops:
                args.append(str(v))
            elif op_name in list_ops:
                args.append(v if isinstance(v,list) else eval(v))
            elif op_name in dict_ops:
                args.append(v if isinstance(v,dict) else eval(v))
            else:
                args.append(int(v))  # Default numeric

        # Call the method
        result = method(*args)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5003, debug=True)
