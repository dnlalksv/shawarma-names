import pymorphy2
morph = pymorphy2.MorphAnalyzer()

with open('ma.txt', 'r') as fin:
    words = [x.strip() for x in fin.readlines()]

nouns = set()
for word in words:
    anas = morph.parse(word)
    for ana in anas:
        tag = ana.tag
        if tag.POS == 'NOUN' and 'nomn' in tag and 'sing' in tag:
            nouns.add(word.lower())
            break

with open('ma_nouns.txt', 'w') as fout:
    fout.write('\n'.join(nouns))
