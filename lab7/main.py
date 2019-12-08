txt_26 = open("26.txt", "rt", encoding="cp1251")
content = txt_26.read()
txt_26.close()

sentences = list(content.split("."))
length = len(sentences)

filtered_sentences = []     # без пустых предложений

for i in range(length):
    sentences[i] = ' '.join(sentences[i].split())
    if sentences[i] != "":
        filtered_sentences.append(sentences[i])

filt_len = len(filtered_sentences)  # длина списка без пустых
final_text = []

for j in range(filt_len):
    filtered_sentences[j] = list(filtered_sentences[j].split(" "))
    new_sentece = []
    for k in range(len(filtered_sentences[j])):
        if filtered_sentences[j][k] != "":
            new_sentece.append(filtered_sentences[j][k])
    final_text.append(new_sentece)


fin = len(final_text)
for i in range(fin):
    for j in range(len(final_text[i])):
        if j % 2 != 0 and (j+2)<len(final_text[i]):
            r = set(final_text[i][j]) | set(final_text[i][j+2])
            final_text[i][j] = r

new_content = ""
for sentence in final_text:
    for word in sentence:
        w = " ".join(word)
        w = w.replace(" ", "")
        new_content += w+" "
    new_content = new_content.rstrip() + ".\n"


txt_261 = open(r"261.txt", "w")
txt_261.write(new_content)
txt_261.close()

txt_26_byte = open(r"26.txt", "r", encoding="cp1251")
content_2 = txt_26_byte.read()
cont = list(content_2)
txt_26_byte.close()

symbol_codes_array = []
for i in range(len(cont)):
    new_symbol = ord(cont[i]) + 2
    symbol_codes_array.append(new_symbol)

symbol_text = ""
for j in symbol_codes_array:
    symbol_text += chr(j)

txt_262 = open(r"262.txt", "w", encoding="utf8")
txt_262.write(symbol_text)
txt_262.close()
