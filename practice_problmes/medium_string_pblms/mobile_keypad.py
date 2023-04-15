# Find all possible combinations of words formed from the mobile keypad
# Input: [2, 3, 4]
# output
# ADG BDG CDG AEG BEG CEG AFG BFG CFG ADH BDH CDH AEH BEH CEH AFH BFH CFH ADI BDI CDI AEI BEI CEI AFI BFI CFI
def keypad_words(input_numbers):
    keypad = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ"
    }
    if not input_numbers:
        return [""]

    words = [""]
    for i in range(len(input_numbers)):
        first = str(input_numbers[i])
        new_words = []
        for char in keypad[first]:
            for word in words:
                new_words.append(word + char)
        words = new_words

    return words


input_numbers = [2, 3, 4]
print(keypad_words(input_numbers))


# using list comprehension
def keypad_words(input_numbers):
    keypad = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ"
    }
    if not input_numbers:
        return [""]

    words = [""]
    for i in range(len(input_numbers)):
        first = str(input_numbers[i])
        words = [word + char for word in words for char in keypad[first]]

    return words


input_numbers = [2, 3, 4]
print(keypad_words(input_numbers))

