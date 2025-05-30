## Arithmetic Arranger – Python Function to Format Arithmetic Problems

This project implements a Python function that arranges and formats a list of simple arithmetic problems vertically and side-by-side, optionally displaying the answers. It was created as part of freeCodeCamp’s Scientific Computing with Python Certification.

## Features:

- Takes a list of arithmetic problems (addition and subtraction only)
- Validates input format and size limits (max 5 problems, numbers up to 4 digits)
- Aligns operands and operators vertically and horizontally for neat display
- Optionally calculates and shows the answers
- Returns helpful error messages on invalid input
## Usage

Call the function:
```python
arithmetic_arranger(problems, show_answers=False)
```
```problems```: list of strings, each string an arithmetic problem like "32 + 698"

```show_answers```: boolean, optional, set to True to display answers
## Example
```python
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
```
## Output
```python
    3      988
+ 855    +  40
-----    -----
  858     1028
```
