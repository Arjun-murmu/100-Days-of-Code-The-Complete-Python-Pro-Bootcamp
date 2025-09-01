sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_word = sentence.split()
sentence_len = {len(word) for word in sentence_word}
# print(sentence_len)
# print(sentence_word)
result = {word:len(word) for word in sentence_word}
print(result)
