const operationSelect = document.getElementById('operation');
const inputsContainer = document.getElementById('inputs');
const computeBtn = document.getElementById('computeBtn');
const resultBox = document.getElementById('result');

// Define inputs needed per operation
const operationInputs = {
    "prime": ["number"],
    "factorial": ["number"],
    "factorial_recursion": ["number"],
    "reverse_string": ["string"],
    "palindrome_check": ["string"],
    "fibonacci_sequence": ["n"],
    "sum_digits": ["number"],
    "gcd": ["a", "b"],
    "check_leap_year": ["year"],
    "power": ["base", "exp"],
    "reverse_words": ["string"],
    "count_vowels": ["string"],
    "armstrong_check": ["number"],
    "sum_squares": ["n"],
    "decimal_to_binary": ["number"],
    "binary_to_decimal": ["binary"],
    "second_largest_number": ["list"],
    "largest_number": ["list"],
    "sum_list": ["list"],
    "remove_duplicates": ["list"],
    "intersection_list": ["list1", "list2"],
    "merge_sorted_lists": ["list1", "list2"],
    "sorted_list": ["list"],
    "missing_consecutive_num": ["list", "diff"],
    "reverse_integer": ["number"],
    "longest_word": ["string"],
    "num_power": ["number"],
    "flatten": ["list"],
    "find_pairs": ["list", "target"],
    "rotation_checker": ["string1", "string2"],
    "tuple_dict": ["list"],
    "median": ["list"],
    "sorted_dict": ["dict"],
    "list_prime_numbers": ["n"],
    "subsequence_list": ["large", "small"],
    "common_elements_list": ["list1", "list2", "list3"],
    "swapping_numbers": ["a", "b"],
    "remove_occurrence": ["string", "pos", "char"],
    "first_non_repeated_character": ["string"],
    "digits_checks": ["string"],
    "anagram": ["string1", "string2"],
    "generate_subsets": ["list"],
    "count": ["string"],
    "frequency_word": ["filename"]
};

// Function to render input fields
function renderInputs() {
    const selectedOp = operationSelect.value;
    const inputs = operationInputs[selectedOp] || [];
    inputsContainer.innerHTML = '';

    inputs.forEach(name => {
        const input = document.createElement('input');
        input.type = name === "list" || name.startsWith("list") || name === "dict" ? "text" : "text";
        input.placeholder = `Enter ${name}`;
        input.id = name;
        input.style.margin = "5px 0";
        input.className = "dynamic-input";
        inputsContainer.appendChild(input);
    });
}

// Initial render
renderInputs();
operationSelect.addEventListener('change', renderInputs);

// Handle compute button
computeBtn.addEventListener('click', async () => {
    const selectedOp = operationSelect.value;
    const inputs = operationInputs[selectedOp] || [];
    let data = {};

    inputs.forEach(name => {
        const val = document.getElementById(name).value;
        if (val) {
            // Convert to list or dict if needed
            if (name === "list" || name.startsWith("list")) {
                data[name] = val.split(',').map(item => item.trim());
            } else if (name === "dict") {
                try {
                    data[name] = JSON.parse(val);
                } catch (e) {
                    data[name] = {};
                }
            } else if (name === "binary") {
                data[name] = val.trim(); // <-- make sure binary is string
            } else {
                data[name] = val;
            }

        }
    });

    try {
        const response = await fetch(`/operation/${selectedOp}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        if (result.error) {
            resultBox.innerText = `Error: ${result.error}`;
        } else {
            resultBox.innerText = `Result: ${JSON.stringify(result.result)}`;
        }
    } catch (err) {
        resultBox.innerText = `Error: ${err.message}`;
    }
});
