# -*- coding: utf-8 -*-

import re                 
def slugfy(string):
    table = {u'а':u'a',
                 u'б':u'b',
                 u'в':u'v',
                 u'г':u'g',
                 u'д':u'd',
                 u'е':u'e',
                 u'ё':u'e',
                 u'ж':u'j',
                 u'з':u'z',
                 u'и':u'i',
                 u'к':u'k',
                 u'л':u'l',
                 u'м':u'm',
                 u'н':u'n',
                 u'о':u'o',
                 u'п':u'p',
                 u'р':u'r',
                 u'с':u's',
                 u'т':u't',
                 u'у':u'u',
                 u'ф':u'f',
                 u'х':u'h',
                 u'ц':u'c',
                 u'ч':u'ch',
                 u'ш':u'sh',
                 u'щ':u'ch',
                 u'ъ':u'',
                 u'ы':u'i',
                 u'ь':u'',
                 u'э':u'e',
                 u'ю':u'yu',
                 u'я':u'ya',
                 ' ':u'_'}
    s = string.lower()
    print s
    r = ''
    for ch in s:
        if table.has_key(ch):
            r+=table[ch]
        else:
            r+=ch
    
    r = re.sub(r'[^0-9a-z _]','',r) #
    return r

