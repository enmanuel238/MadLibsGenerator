from encodings import utf_8
import json
import os

class MadLibs:
    def __init__(self, word_descriptions, template):
        self.word_descriptions = word_descriptions
        self.template = template

    @classmethod
    def get_template(name, path="./templates"):
        fpath = os.path.join(path, name)
        with open (fpath, "r", encoding="utf_8") as f:
            data = json.load(f)
        return MadLibs.get_template()

def get_words_from_user(word_descriptions):
    words = []
    print("Ingrese las palabras por favor: ")
    for desc in word_descriptions:
        user_input = input(desc + ": ")
        words.append(user_input)
    
    return words

def build_story(template, words):
    story = template.format(*words)
    print (story)


temp_name = "lechera.json"
get_template(temp_name)

# template = "hola {} {}"
# words = get_words_from_user(["nouns", "verb"])
# build_story(template, words)

def main():
    pass


if __name__ == '__main__':
    main()
