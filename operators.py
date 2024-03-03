from pyparsing import Word, OneOrMore, Or
import re


def parse_operator(code_text):
 
  elements=dict()
  keywords = ["+", "-", "*", "/", "%", "**", "==", "!=", ">", "<", ">=", "<=", "<=>",
                "||","!", "=", "+=", "-=", "*=", "/=", "%=", "**=",".", "::",  "&&",
               "+=", "-=", "&", "|", "^", "~", "<<", ">>", "===", "??", "[]",  "?:"]

  keyword_expressions = [Word(keyword) for keyword in keywords]

  or_expression = Or(keyword_expressions)
  
  grammar = OneOrMore(or_expression)
    
  matches = grammar.searchString(code_text)

  elements = {keyword: len([match for match in matches if match[0] == keyword]) for keyword in keywords}

  elements = {keyword: count for keyword, count in elements.items() if count != 0}


  return elements


