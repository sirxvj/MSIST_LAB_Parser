from pyparsing import *
import re
def parse_operands(code_text):
    elements = dict()
    keywords = ["BEGIN", "END", "alias", "and", "begin", "break", "case", "class", "def", "defined?", "do", "else", "elsif", "end", "ensure", "false", "for", "if", "in", "module", "next", "nil", "not", "or", "redo", "rescue", "retry", "return", "self", "super", "then", "true", "undef", "unless", "until", "when", "while", "yield"]
    match = re.findall(r'[\w._]+\s*[-+=<>/*]', code_text)
    match += re.findall(r'[-<>+=/*]\s*[\w._]+[\s.]', code_text)
    match += re.findall(r'[(\[][\w._]+[-+<>=/*,)\]]', code_text)
    match += re.findall(r'[-<>+=/*,]\s*[\w._]+[)\]]', code_text)
    match += re.findall(r'return\s*[\w._]+\s', code_text)
    match += re.findall(r'if\s+[\w._]+\?\s', code_text)

    for el in match:
        lrvalue = (el.replace(' ','').replace('<','').replace('*','').replace('/','')
        .replace('(','').replace('[','').replace(']','').replace(')','').replace('=','').replace(',','').replace('?','')
                   .replace('>','').replace('+','').replace('-','').replace('\n','').split('.'))


        for el2 in lrvalue:#result_value:
            if (len(el2) == 0 or el2 in keywords):
                continue;
            if(el2[0] =='i' and el2[1]=='f'):
                el2 = el2[2:len(el2)]
            if(el2.startswith('return')):
                el2 = el2.replace('return','')

            if el2 in elements:
                elements[el2]+=1
            else:
                elements[el2]=1
    return elements
