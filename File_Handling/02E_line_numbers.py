with open('text.txt') as text_file:
    with open('output_2.txt', 'w') as output_file:
        for i, line in enumerate(text_file):
            len_line = len([x for x in line if x.isalnum()])
            punct_count = len([x for x in line if x in "-,.'!?"])
            output_file.write(f'Line {i + 1}: {line[:-1]} ({len_line})({punct_count})\n')
