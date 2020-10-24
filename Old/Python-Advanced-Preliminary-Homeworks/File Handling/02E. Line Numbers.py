symbols = ["-", ",", ".", "!", "?", "'", "\""]
output_file = open('output.txt', 'w')

with open('text.txt', 'r') as text_file:
    for i, line in enumerate(text_file):
        letters = 0
        punctuation_marks = 0
        for char in line:
            if char.isalpha():
                letters += 1
            elif char in symbols:
                punctuation_marks += 1
        line_to_add = f'Line {i + 1}: {line[:-2]} ({letters})({punctuation_marks})\n'
        output_file.write(line_to_add)

output_file.close()
