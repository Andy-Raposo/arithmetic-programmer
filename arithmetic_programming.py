def input_length(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    return None


def input_error(problem):
    parts = problem.split()
    if len(parts) != 3:
        return 'Error: Problem format is invalid.'

    operand1, operator, operand2 = parts

    if operator not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."

    if not operand1.isdigit() or not operand2.isdigit():
        return 'Error: Numbers must only contain digits.'

    if len(operand1) > 4 or len(operand2) > 4:
        return 'Error: Numbers cannot be more than four digits.'

    return None


def calculation(operand1, operand2, operator):
    if operator == '+':
        return str(int(operand1) + int(operand2))
    elif operator == '-':
        return str(int(operand1) - int(operand2))


def arithmetic_arranger(problems, show_answers=False):
    error = input_length(problems)
    if error:
        return error

    row1, row2, row3, row4 = [], [], [], []

    for problem in problems:
        error = input_error(problem)
        if error:
            return error

        operand1, operator, operand2 = problem.split()
        width = max(len(operand1), len(operand2)) + 2

        operand1_aligned = f'{operand1:>{width}}'
        operand2_aligned = f'{operator} {operand2:>{width - 2}}'
        dash = '-' * width

        row1.append(operand1_aligned)
        row2.append(operand2_aligned)
        row3.append(dash)

        if show_answers:
            result = calculation(operand1, operand2, operator)
            row4.append(f'{result:>{width}}')

    arranged_problems = '    '.join(row1) + '\n' + '    '.join(row2) + '\n' + '    '.join(row3)
    if show_answers:
        arranged_problems += '\n' + '    '.join(row4)

    return arranged_problems

arithmetic_arranger(["3 + 855", "988 + 40"], True)
