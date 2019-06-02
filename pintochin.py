import re

def convert_numpin_to_regpin(numpin_text: str) -> str:
    converted_text = numpin_text
    numpin_iter = re.finditer(".\d", converted_text)
    
    for match in numpin_iter:
        converted_char = "({})".format(match.group())
        converted_text = converted_text[match.start():match.end()]
    
    return converted_text

if __name__ == "__main__":
    print(convert_numpin_to_regpin("ni3 ji1ao fu2 bu4 yi3ra1ng"))