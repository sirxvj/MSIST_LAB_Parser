from operands import parse_operands
from operators import parse_operator
#print('и операторы и операнды будем делать в своих файликах что бы не было конфликтов и отдельно кути добавим')

code = None

with open("Example.rb", "r") as file:
    code = file.read()

parse_operator(code)
parse_operands(code)