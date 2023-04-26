# Write a sorting function that takes in a list of names and sorts them by last name either alphabetically (ASC) or
# reverse-alphabetically (DESC).
#
# Examples
# sort_contacts([
#   "John Locke",
#   "Thomas Aquinas",
#   "David Hume",
#   "Rene Descartes"
# ], "ASC") ➞ [
#   "Thomas Aquinas",
#   "Rene Descartes",
#   "David Hume",
#   "John Locke"
# ]
#
# # Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)
#
# sort_contacts([
#   "Paul Erdos",
#   "Leonhard Euler",
#   "Carl Gauss"
# ], "DESC") ➞ [
#   "Carl Gauss",
#   "Leonhard Euler",
#   "Paul Erdos"
# ]
#
# # Gauss (G) > Erdos (ER) > Euler (EU)
#
# sort_contacts([], "DESC") ➞ []
#
# sort_contacts(None, "DESC") ➞ []
def sort_contacts(names, direction):
    if names is None:
        return []
    if len(names) == 0:
        return names

    # it will split each name into first and last names, and store  it in a tuple
    name_list = [(name.split()[0], name.split()[-1]) for name in names]

    # here sort the list of tuples by last name (the second element in each tuple)
    for i in range(len(name_list)):
        for j in range(i + 1, len(name_list)):
            if direction == "ASC":
                if name_list[j][1] < name_list[i][1]:
                    temp=name_list[j]
                    name_list[j]=name_list[i]
                    name_list[i]=temp
                    # name_list[j], name_list[i] = name_list[i], name_list[j]
            else:
                if name_list[j][1] > name_list[i][1]:
                    # name_list[j], name_list[i] = name_list[i], name_list[j]
                    temp=name_list[j]
                    name_list[j]=name_list[i]
                    name_list[i]=temp

    # combine the sorted first and last names into a list of full names
    sorted_names = [" ".join(name) for name in name_list]

    return sorted_names


names = ["John Locke", "Thomas Aquinas", "David Hume", "Rene Descartes"]
direction = "ASC"

sorted_names = sort_contacts(names, direction)
print(sorted_names)
