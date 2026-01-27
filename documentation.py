""" --RegEx-- """
'''
Keyword_Hierachy =
"
[
create_keyword="create";
="";
]
Command_keywords = 
"
[
"Let's capture {{data}},{{data}},{{data}},"=data_capture;

]
general_prog_functions = 
"
[

]

'''
def keywords(test_keyword):'
  test_keyword = "test"
  return test_keyword

local_test_val = keywords(test_keyword)

print(local_test_val)

'''--import--'''
import re
TOKEN_TYPES = [
    ('NUMBER',  r'\d+(\.\d*)?'), # Matches integers or floats
    ('PLUS',    r'\+'),
    ('MINUS',   r'-'),
    ('MULTIPLY',r'\*'),
    ('DIVIDE',  r'\/'),
    ('WHITESPACE', r'\s+'), # Matches one or more whitespace characters
    ('MISMATCH', r'.'),    # Matches any single character not matched by previous rules
]
def lexer(source_code):
    tokens = []
    position = 0
    # Compile the patterns for efficiency
    token_patterns = [(name, re.compile(pattern)) for name, pattern in TOKEN_TYPES]

    while position < len(source_code):
        match = None
        for token_name, pattern in token_patterns:
            # Try to match from the current position
            match = pattern.match(source_code, position)
            if match:
                value = match.group(0)
                if token_name != 'WHITESPACE':
                    tokens.append((token_name, value))
                position = match.end(0)
                break
        
        if not match:
            # Handle errors for unmatched characters
            raise Exception(f"Illegal character at position {position}: {source_code[position]}")

    return tokens

# Example usage:
code = "10 + 5 * 2"
my_tokens = lexer(code)
print(my_tokens)




