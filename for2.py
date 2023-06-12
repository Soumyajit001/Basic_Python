# Search for lost car key in home and
# when found stop searching

key_location = "chair"
locations = ["garage", "bed room", "dinning table", "closet", "chair", "table"]
for i in locations:
    if i == key_location:
        print("key is found in", i)
        break
    else:
        print("key is not found in", i)
