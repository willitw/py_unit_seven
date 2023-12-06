def half_slice(word):

    midpoint = len(word) // 2

    first_half = word[:midpoint]
    second_half = word[midpoint:]

    new_word = second_half + first_half

    return new_word

def no_first_last(some_str):
  pass


def longest(phrase):
   pass



def title_case(sentence):
    words = sentence.split()
    title_case_words = []
    for word in words:
        capitalized_word = word[0].upper() + word[1:]
        title_case_words.append(capitalized_word)
    title_case_sentence = " ".join(title_case_words)
    return title_case_sentence


print(half_slice("bread"))

user_input = input("Enter a sentence: ")
result = title_case(user_input)
print(result)