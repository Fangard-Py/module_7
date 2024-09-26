class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = [word.strip(',.:!?;- ').lower() for word in file.read().split()]
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('O Captain!.txt',
                      'Rudyard Kipling.txt',
                      'Mondays Child.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('the'))  # 3 слово по счёту
print(finder2.count('the'))  # 4 слова teXT в тексте всего
