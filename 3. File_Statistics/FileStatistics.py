text = open("input.txt", "r").read()

c_lines = text.count("\n")+1
c_words = text.count(" ")+c_lines
c_symbols = len(text)

print(f"Riadkov:{c_lines}, Slov:{c_words}, Znakov:{c_symbols}")