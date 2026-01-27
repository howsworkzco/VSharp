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
