

import os

entries = os.listdir("file")

for file in entries:
    with open(f"./file/{file}", 'r') as f:
        text = f.read()
        words = text.split(' ')
        words_num = len(words)
        print(f"{file} : {len(words)}")
        with open("counted.txt", "a") as w:
            w.write(f"{file} : {words_num} \n")