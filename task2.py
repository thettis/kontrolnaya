import re
from collections import Counter

GLAS = set("аеёиоуыэюяaeiouy")

def count_words(text):
    words = re.findall(r"[а-яёa-z]+", text.lower())
    glasni = 0
    sogl = 0
    for w in words:
        if w[0] in GLAS:
            glasni += 1
        else:
            sogl += 1
    return glasni, sogl

def most_frequent_word(text):
    words = re.findall(r"[а-яёa-z]+", text.lower())
    if not words:
        return None, 0
    word, freq = Counter(words).most_common(1)[0]
    return word, freq

def rep(text):
    result: list[str] = []
    for ch in text:
        if not result or ch != result[-1]:
            result.append(ch)
    return "".join(result)

def is_anagram(text1, text2):
    letters1 = sorted(ch.lower() for ch in text1 if ch.isalpha())
    letters2 = sorted(ch.lower() for ch in text2 if ch.isalpha())
    return bool(letters1) and letters1 == letters2

def quotes(text):
    matches = re.findall(r"«([^»]*)»|\"([^\"]*)\"", text)
    return [m[0] if m[0] != "" else m[1] for m in matches]

def bulls_and_cows(secret, guess):
    if len(secret) != len(guess):
        return None

    bulls = 0
    rem_secret: list[str] = []
    rem_guess: list[str] = []

    for s_ch, g_ch in zip(secret, guess):
        if s_ch == g_ch:
            bulls += 1
        else:
            rem_secret.append(s_ch)
            rem_guess.append(g_ch)

    c_secret = Counter(rem_secret)
    c_guess = Counter(rem_guess)
    cows = sum(min(c_secret[ch], c_guess[ch]) for ch in c_secret)
    return bulls, cows

def main():
    text = input("Введите текст: ")
    second_text = input("Введите вторую строку для проверки на анаграмму: ")
    print("Для игры «Быки и коровы» введите две строки одинаковой длины:")
    bc_first = input("Строка 1: ")
    bc_second = input("Строка 2: ")

    glas_cnt, consonants_cnt = count_words(text)
    print(f"\nСлов с гласной: {glas_cnt} | с согласной: {consonants_cnt}")

    top_word, freq = most_frequent_word(text)
    if top_word is not None:
        print(f"Самое частое слово: «{top_word}» (встречается {freq} раз(а))")
    else:
        print("Слова в тексте не найдены.")

    squeezed = rep(text)
    print(f"После сжатия повторов: {squeezed}")

    print(
        "Является ли анаграммой второй строки:",
        "Да" if is_anagram(text, second_text) else "Нет",
    )

    quoted = quotes(text)
    print(f"Подстроки в кавычках: {quoted}")

    bc_res = bulls_and_cows(bc_first, bc_second)
    if bc_res is None:
        print("Быки и коровы: строки должны быть одинаковой длины.")
    else:
        bulls, cows = bc_res
        print(
            f"Быки и коровы для «{bc_first}» и «{bc_second}»: "
            f"быки={bulls}, коровы={cows}"
        )
main()