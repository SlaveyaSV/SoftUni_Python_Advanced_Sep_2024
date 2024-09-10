from collections import deque

words = deque(input().split())

colours = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"}
}

colours_found = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ""

    for colour in (first_word + second_word, second_word + first_word):
        if colour in colours:
            colours_found.append(colour)
            break
    else:
        for word in (first_word[:-1], second_word[:-1]):
            if word:
                words.insert(len(words)//2, word)

for s_colour, m_colours in secondary_colors.items():
    if s_colour in colours_found:
        if not m_colours.issubset(colours_found):
            colours_found.remove(s_colour)

print(colours_found)
