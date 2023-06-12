exp = [2340, 2500, 2100, 3020, 2980, 3990]
# item = exp[0] = 2340
# total = total + item that is total=total+exp[0]
# i.e. at first total=0 therefore for exp[0], total=0+2340
# Now,total=2340
# item = exp[1]
# total = total + item that is total=total+exp[1]
# i.e. for exp[1], total= 2340(total of prev.)+2500
# Now,total=4840
total = 0
for item in exp:
    total = total + item
print(total)

# // Another method
# exp = [2340, 2500, 2100, 3020, 2980, 3990]
# total = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
# print(total)
