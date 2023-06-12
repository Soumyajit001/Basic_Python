# Print square of no. btw 1 to 5 (except even nos.)

for i in range(6):
    if i % 2 == 0:
        print("Skipped Even nos. are ", i)
        continue
    print(i*i)
