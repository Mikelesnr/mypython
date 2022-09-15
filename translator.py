from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        transalation = translator.translate(text)
        print(transalation)
except:
    print('check your file path')
