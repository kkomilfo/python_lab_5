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
                        ukrainian_words.append(word)
                    elif lang == 'en':
                        english_words.append(word)
                    else:
                        other_words.append(word)
                except langdetect.lang_detect_exception.LangDetectException:
                    pass  # Якщо неможливо визначити мову, пропускаємо слово


            all = ukrainian_words + english_words + other_words
            sorted_all = sorted(all, key=str.lower)
            print("\nOthers слова (по алфавіту):", sorted_all)

            # Виводимо загальну кількість слів
            print("\nКількість слів у тексті:", len(words))

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")


# Приклад використання програми
file_path = 'file.txt'  # Вкажіть шлях до вашого файлу
read_first_sentence(file_path)
