from pyparsing import Word, OneOrMore, Or
import re


def parse_operator(code_text):
    elements = dict()
    keywords = [
        "+",
        "-",
        "*",
        "/",
        "%",
        "**",
        "==",
        "!=",
        ">",
        "<",
        ">=",
        "<=",
        "<=>",
        "||",
        "!",
        "=",
        "+=",
        "-=",
        "*=",
        "/=",
        "%=",
        "**=",
        ".",
        "::",
        "&&",
        "+=",
        "-=",
        "&",
        "|",
        "^",
        "~",
        "<<",
        ">>",
        "===",
        "??",
        "[]",
        "?:",
        # "for",
        # "while",
        # "until",
        # "if",
        # "else",
        # "elsif",
        # "case",
        # "when",
        # "do",
        # "begin",
        # "end",
        # "break",
        # "next",
        # "redo",
        # "retry",
        # "return",
        # "yield",
        # "puts",
    ]

    keyword_expressions = [Word(keyword) for keyword in keywords]

    or_expression = Or(keyword_expressions)

    grammar = OneOrMore(or_expression)

    matches = grammar.searchString(code_text)

    elements = {
        keyword: len([match for match in matches if match[0] == keyword])
        for keyword in keywords
    }

    elements = {keyword: count for keyword, count in elements.items() if count != 0}

    regex = r"\((.*?)\)"

    matches = re.findall(regex, code_text)

    count = 0

    arithmetic_operators = r"[\+\-\*/%]"
    for match in matches:
        if re.search(arithmetic_operators, match):
            count += 1

    if count > 0:
        elements["()"] = count

    ################ name.name_method()
    regex = r"\b\w+\.\w+(?=\(|\?)"

    matches = re.findall(regex, code_text)
    for match in matches:
        method = match.split(".")[1]  # Извлекаем имя метода из строки
        if method in elements:
            elements[method] += 1
        else:
            elements[method] = 1

    ########### funcs
    regex = r"(?:^|\s)(\w+)(?=\()"

    matches = re.findall(regex, code_text)
    for match in matches:
        if match not in elements:
            elements[match] = 1
        else:
            elements[match] += 1

    ########### keywords
    regex = r"\b(for|while|until|if|else|elsif|case|when|do|begin|end|break|next|redo|retry|return|yield|in)\b"

    matches = re.findall(regex, code_text)
    for match in matches:
        if match not in elements:
            elements[match] = 1
        else:
            elements[match] += 1

    total_count = 0

    for key in elements:
      total_count += elements[key]



    return elements, total_count
