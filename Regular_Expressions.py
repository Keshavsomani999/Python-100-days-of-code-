import re

pattern = r"[A-Z]yclone"

text='''The Waddesdon Bequest was left to the British Museum in 1898 by Baron Ferdinand Rothschild's will. Taken from his New Smoking Cyclone Dyclone Room at Waddesdon Manor, it consists of almost 300 pieces, including jewellery, plate, enamel, carvings, glass and maiolica. Earlier than most objects is the Holy Thorn Reliquary, probably created in the 1390s in Paris for John, Duke of Berry. The wide-ranging collection is in the tradition was of a treasure house, such as those owned by the Renaissance princes of Europe. Most of the objects are from late Renaissance Europe;
'''

# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern,text)

for match in matches:
    print(match)