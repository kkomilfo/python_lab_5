import string
import langdetect

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Знаходимо перше речення
            first_sentence = text.split('.')[0]
            print("Перше речення:", first_sentence)

            # Видаляємо знаки пунктуації
            text_cleaned = text.translate(str.maketrans('', '', string.punctuation))

            # Розбиваємо на слова
            words = text_cleaned.split()

            # Розділяємо слова за мовами
            ukrainian_words = []
            english_words = []
            other_words = []

            for word in words:
                try:
                    lang = langdetect.detect(word)
                    if lang == 'uk':
                        ukrainian_words.append(word.lower())
                    elif lang == 'en':
                        english_words.append(word.lower())
                    else:
                        other_words.append(word.lower())
                except langdetect.lang_detect_exception.LangDetectException:
                    pass  # Якщо неможливо визначити мову, пропускаємо слово


            # Сортуємо українські та англійські слова
            ukrainian_words_sorted = sorted(ukrainian_words)
            english_words_sorted = sorted(english_words)
            other_words_sorted = sorted(other_words)

            # Виводимо відсортовані слова
            if ukrainian_words_sorted:
                print("\nУкраїнські слова (по алфавіту):", ukrainian_words_sorted)
            if english_words_sorted:
                print("\nАнглійські слова (по алфавіту):", english_words_sorted)
            if other_words_sorted:
                print("\nOthers слова (по алфавіту):", other_words_sorted)

            # Виводимо загальну кількість слів
            print("\nКількість слів у тексті:", len(words))

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")


# Приклад використання програми
file_path = 'file.txt'  # Вкажіть шлях до вашого файлу
read_first_sentence(file_path)
