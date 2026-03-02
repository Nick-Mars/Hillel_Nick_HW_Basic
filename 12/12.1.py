import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = ""
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
            continue
        elif char == '>':
            inside_tag = False
            continue
        if not inside_tag:
            cleaned_text += char

    lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
    cleaned_text_final = '\n'.join(lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text_final)


delete_html_tags(r'C:\Users\My comp\PycharmProjects\PythonProject\12\draft.html',
                 r'C:\Users\My comp\PycharmProjects\PythonProject\12\cleaned.txt')