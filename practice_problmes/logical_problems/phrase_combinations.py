
# Given a lists of words, print all combinations of phrases that can be formed by picking one word from each list.

# Input:
# lists =
# [
#  ['John', 'Emma'],
#  ['Plays', 'Hates', 'Watches'],
#  ['Cricket', 'Soccer', 'Chess']
# ]

# Output:
#  'John Plays Cricket',
#  'John Plays Soccer',
#  'John Plays Chess',
#  'John Hates Cricket',
#  'John Hates Soccer',
#  'John Hates Chess',
#  'John Watches Cricket',
#  'John Watches Soccer',
#  'John Watches Chess',
#  'Emma Plays Cricket',
#  'Emma Plays Soccer',
#  'Emma Plays Chess',
lists = [
    ['John', 'Emma'],
    ['Plays', 'Hates', 'Watches'],
    ['Cricket', 'Soccer', 'Chess']
]
phrases = []

for word1 in lists[0]:
    for word2 in lists[1]:
        for word3 in lists[2]:
            phrases.append(word1 + ' ' + word2 + ' ' + word3)

for phrase in phrases:
    print(phrase)

#
lists = [
    ['John', 'Emma'],
    ['Plays', 'Hates', 'Watches'],
    ['Cricket', 'Soccer', 'Chess']
]

phrases = [word1 + ' ' + word2 + ' ' + word3
           for word1 in lists[0]
           for word2 in lists[1]
           for word3 in lists[2]]

for phrase in phrases:
    print(phrase)

