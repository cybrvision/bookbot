def count_words_in_text(text) -> int:
    return len(text.split())


def count_characters_in_text(text) -> dict:
    chars_dict = {}
    for ch in text:
        c = ch.lower()
        if c in chars_dict:
            chars_dict[c] += 1
        else:
            chars_dict[c] = 1
    return chars_dict


def sort_list_of_characters(char_dict:dict) -> list[dict]:
    def count_sort(c):
        return c['count']

    chars_list = []
    for c_dict in char_dict:
        chars_list.append({
            "character":c_dict,
            "count":char_dict[c_dict]
        })
    chars_list.sort(reverse=True, key=count_sort)
    return chars_list 




