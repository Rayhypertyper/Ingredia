from thefuzz import fuzz, process

s1 = "Lay's classic"
s2 = ["Chips classiche-plastica Lay's-30", "Family Size Classic Potato Chips-Lay's-235 g", "Potato chips classic lightly salted-Lay's-219.7 g", "Classic Potato Chips - Lay's -28 g",
      "Classic-Lay's-226.8 gr"]

# best_match = process.extractOne(s1, s2)
# print(best_match)
highest = 0
best_match = s2[0]
for i in s2:
    if fuzz.token_sort_ratio(s1, i) > highest:
        highest = fuzz.token_sort_ratio(s1,i)
        print(f"The best one is : {i}")
        best_match = i
