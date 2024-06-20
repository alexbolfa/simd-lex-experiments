import random

def gen(n):
    """
    Generates synthetic C code of n lines with a maximum indentation of 80 characters
    """
    code = []
    indentation_level = 0
    max_indentation = 3

    variable_names = []

    def generate_variable():
        variable_type = random.choice(['int', 'float', 'double', 'char'])
        variable_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(1, 5)))
        if variable_type == 'char':
            value = f'"{random.choice(["hello", "world", "test", "string"])}"'
        else:
            value = random.randint(0, 100)
        variable_names.append(variable_name)
        return f"{variable_type} {variable_name} = {value};"

    def generate_if_statement():
        condition = random.choice(variable_names + ['a', 'b', 'c', 'd'])  # Placeholder condition for simplicity
        return f"if ({condition}) {{"

    def generate_while_loop():
        condition = random.choice(variable_names + ['x < 10', 'y != 0', 'i <= 5'])  # Placeholder condition for simplicity
        return f"while ({condition}) {{"

    def generate_function():
        return_type = random.choice(['void', 'int', 'float', 'double'])
        function_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(3, 8)))
        parameters = ', '.join(f"{random.choice(['int', 'float', 'double'])} {chr(97 + i)}" for i in range(random.randint(1, 3)))
        return f"{return_type} {function_name}({parameters}) {{\n    // Function body\n}}"

    def generate_block_comment():
        comment_lines = []
        num_lines = random.randint(2, 5)
        for _ in range(num_lines):
            comment_lines.append('    ' * indentation_level + f"// {random.choice(['TODO:', 'FIXME:', 'NOTE:'])} {random.choice(['Implement this', 'Fix this', 'Consider this'])}")
        return "/*\n" + "\n".join(comment_lines) + "\n" + '    ' * indentation_level + "*/"

    def generate_arithmetic_operation():
        if not variable_names:
            return generate_variable()
        var1 = random.choice(variable_names)
        var2 = random.choice(variable_names)
        operation = random.choice(['+', '-', '*', '/'])
        return f"{var1} = {var1} {operation} {var2};"

    def generate_non_declaration_line():
        if not variable_names:
            return generate_variable()
        var = random.choice(variable_names)
        operation = random.choice([
            f"{var}++;",
            f"{var}--;",
            f"printf(\"%d\", {var});",
            f"{var} = {random.randint(0, 100)};"
        ])
        return operation

    for _ in range(n):
        choice = random.choices(
            [generate_variable, generate_if_statement, generate_while_loop, generate_function, generate_block_comment, generate_arithmetic_operation, generate_non_declaration_line],
            weights=[1, 3, 3, 1, 1, 3, 5],  # Adjust weights to reduce variable declarations and increase logic
            k=1
        )[0]

        line = choice()

        # Ensure that the line respects the maximum indentation width of 80 characters
        if len('    ' * indentation_level + line) > 80:
            indentation_level = max(0, indentation_level - 1)

        if line.endswith(" {"):
            code.append('    ' * indentation_level + line)
            if indentation_level < max_indentation:
                indentation_level += 1
        elif line.startswith("}") or line.endswith("};") or line.startswith("/*"):
            if indentation_level > 0:
                indentation_level -= 1
            code.append('    ' * indentation_level + line)
        else:
            code.append('    ' * indentation_level + line)

    return "\n".join(code)

# Example usage:
num_lines = 50
generated_code = gen(num_lines)
print(generated_code)
