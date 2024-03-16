# Number Combination and Calculation Python Script

This Python script generates 5 single-digit numbers, 1 two-digit number (a multiple of 10), and 1 three-digit number (the target number). It then generates all possible combinations using these 6 numbers and the 4 basic arithmetic operations. The script iterates through each combination and evaluates them. Regardless of the order of operations, it prints the closest result found along with the combination of numbers used and the operations performed. It calculates the absolute difference between the found result and the target result, assigning a score based on the difference: 10 points if the difference is 0, 0 points if the difference is greater than 9, or a score based on the difference otherwise. Additionally, it prints the execution time of the script.

## Usage

1. Ensure you have Python installed on your system.
2. Run the script using a Python interpreter.

```bash
python number_combination_calculator.py
```


## Note

This script efficiently explores all possible combinations of numbers and operations to find the closest result to the target number, disregarding operator precedence. It calculates a score based on the closeness of the found result to the target result, providing an indication of the effectiveness of the combination.
