# //Write a prog. that asks user to enter dish name
# //and it should print which cuisine is that dish.

indian = ["mutton", "samosa", "katla"]
chinese = ["fried rice", "chilly chicken", "noodles"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print("Indian dishes are very much delicious")
elif dish in chinese:
    print("chinese dishes are delicious like their sweet nature")
elif dish in italian:
    print("Italian dishes are delicious like their fabulous football")
else:
    print("Based on little knowledge I have I don't know which cuisine is", dish, ".")
