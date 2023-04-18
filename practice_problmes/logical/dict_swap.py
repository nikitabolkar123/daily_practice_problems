# Problem: Write a program that takes a dictionary as input and returns a new dictionary with the keys and values
# swapped.

# Problem: Write a program that takes a string as input and returns a new string with all the vowels removed.

def swap_dict_keys_values(input_dict):
    return {value: key for key, value in input_dict.items()}


my_dict = {"apple": 3, "banana": 7, "cherry": 2}
swapped_dict = swap_dict_keys_values(my_dict)
print(swapped_dict)
