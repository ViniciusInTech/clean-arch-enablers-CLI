import re

from variables import filter_package_java, filter_java


def split_words(string):
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+|[a-zA-Z0-9]+', string)
    return [word.lower() for word in words]


def upper_case_first(words):
    words_first_upper = []
    for word in words:
        words_first_upper.append(word.capitalize())
    return words_first_upper


def join_words(words):
    word_complete = ''
    for word in words:
        word_complete += word
    return word_complete


def to_snake_case(words):
    snake_case_string = "_".join(words).lower()
    return snake_case_string


def to_pascal_case(input_list):
    pascal_case_string = "".join(word.capitalize() for word in input_list)
    return pascal_case_string


def to_camel_case(input_list):
    camel_case_string = "".join(word.capitalize() if index > 0 else word for index, word in enumerate(input_list))
    return camel_case_string


def to_package_format(path):
    parts = path.split(filter_package_java, filter_java)
    if len(parts) > filter_java:
        return parts[filter_java].replace("\\", ".")
    else:
        return path


def remove_after_string(original_string, target_string):
    parts = original_string.split(target_string, 1)
    if len(parts) > 1:
        result = parts[0] + target_string
        return result
    return original_string