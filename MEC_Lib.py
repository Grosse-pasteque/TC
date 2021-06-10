def text2bin(t): return ' '.join([bin(b) for b in bytearray(t, 'utf-8')]).replace('b', '')
def bin2text(b): return ''.join([chr(int(t, 2)) for t in b.split()])

def text2oct(t): return ' '.join([oct(b) for b in bytearray(t, 'utf-8')]).replace('o', '')
def oct2text(o): return ''.join([chr(int(t, 8)) for t in o.split()])

def text2hex(t): return ' '.join([hex(b) for b in bytearray(t, 'utf-8')]).replace('x', '')
def hex2text(h): return ''.join([chr(int(t, 16)) for t in h.split()])

def hex2rgb(h): return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def base_infos(): print('-'*60, "\nBinary:\t\tbase = 2\tpython-func: bin()\nOctal:\t\tbase = 8\tpython-func: oct()\nHexa:\t\tbase = 16\tpython-func: hex()\n", '-'*60)