from typing import List
from math import ceil

def hexColorToLedziak(HTMLColor:str) -> int:
    HTMLColor = HTMLColor.replace('#', '')
    splitted:List[str] = [HTMLColor[2*i:2*i+2] for i in range(3)]
    print(splitted)
    for i in range(len(splitted)):
        splitted[i] = int(splitted[i], base=16)
    
    print(splitted)
    # (rrrgggbb)
    return ((ceil((splitted[0]*7)/255) << 5)  +  (ceil((splitted[1]*7)/255) << 3) + ceil((splitted[2]*3)/255))


def depolonizator3000(slowo:str):
    return slowo.lower().replace('ź', 'z').replace('ż', 'z').replace('ś', 's').replace('ń', 'n').replace('ł', 'l').replace('ó', 'o').replace('ą', 'a').replace('ć', 'c').replace('ę', 'e').upper()