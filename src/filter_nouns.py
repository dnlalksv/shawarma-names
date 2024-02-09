import pymorphy2
morph = pymorphy2.MorphAnalyzer()

with open('ma.txt', 'r') as fin:
    words = [x.strip() for x in fin.readlines()]

nouns = set()
for word in words:
    anas = morph.parse(word)
    for ana in anas:
        tag = ana.tag
        if (tag.POS in {'NOUN', 'ADJ'}) and 'nomn' in tag and 'sing' in tag:
            nouns.add(f"\t'{word.lower()}',")
            break

new_line = '\n'
with open('../ma.js', 'w') as fout:
    fout.write("const NOUNS = [\n" + f"{new_line.join(nouns)}" + '\n]')
