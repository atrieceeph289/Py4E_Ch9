name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
names = dict()
for line in handle:
    if not line.startswith('From '): continue 
    words = line.split()
    for word in words:
        if word == words[1]:
            names[word] = names.get(word, 0) + 1

count = None
email = None

for k,v in names.items():
    if count is None or v > count:
        count = v
        email = k
print(email,count)

