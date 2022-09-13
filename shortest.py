import sys

def shortest():
    sentence = sys.argv[1]
    shortest_word = min(sentence.split(), key=len)

    print(f'The shortest word is {shortest_word.upper()}')

shortest()