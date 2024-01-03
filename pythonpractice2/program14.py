def pig_latin_converter(sentence):
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word.isalpha():
            pig_latin_word = word[1:] + word[0] + "ay" if word else word
            pig_latin_words.append(pig_latin_word)
        else:
            pig_latin_words.append(word)

    pig_latin_sentence = " ".join(pig_latin_words)
    return pig_latin_sentence

# Example usage:
input_sentence = "Hello world"
pig_latin_result = pig_latin_converter(input_sentence)
print(pig_latin_result)