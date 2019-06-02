import re

NUMPIN_PINYIN_DICT = {
    "a1":u"01ce",
}

def convert_numpin_to_regpin(numpin_text: str) -> str:
    converted_text = numpin_text
    numpin_iter = re.finditer(".\d", converted_text)
    numpin_iter_set = set([i.group() for i in list(numpin_iter)])
    print(numpin_iter_set)
    
    for numpin in numpin_iter_set:
        converted_char = "({})".format(numpin)
        converted_text = re.sub(numpin, converted_char, converted_text)
    
    return converted_text

if __name__ == "__main__":
    print(convert_numpin_to_regpin("ni3 ji1ao fu2 bu4 yi3ra1ng"))