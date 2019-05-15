sites = ["string","list","char","int"]
for site in sites:
    if site == "int":
        print("iterator end")
        break
    print("site is " + site)
print("iterator ok")

for i in range(1,11):
    print(i)

for i in range(len(sites)):
    print(i,sites[i])

l = list(range(-1, -10, -2))
print(l)

print(sum(range(101)))