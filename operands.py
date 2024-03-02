from pyparsing import *
import re
def parse_operands(code_text):
    elements = dict()
    match = re.findall(r'[\w+._]+\s?[+-=]+\s?[\w+._^ ]+(?:\([\w+]\))?', code_text)
    match += re.findall(r'\([\w+._]+[ ,)]]', code_text)
    match += re.findall(r'[\w+._]+ ?\)]', code_text)
    for el in match:
        lrvalue = el.replace(' ','').split('=')
        for el2 in lrvalue:
            if(len(el2) == 0 or (el2[0] !='(' and '(' in el2)):
                continue;
            if el2 in elements:
                elements[el2]+=1
            else:
                elements[el2]=1
    return elements
