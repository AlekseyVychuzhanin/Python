from string import punctuation
my_str = 'АБВ ылоажы фыыдлх? абв Зщышф вабвв ффлжв абВ'
res = []

x = 'абв'
for c in punctuation:
    my_str = my_str.replace(c, ' ' + c + ' ')
data = my_str.split()
print(data)

for item in data:
    if not x.lower() in item.lower():
        res.append(item)
res = ' '.join(res)
for c in punctuation:
    res = my_str.replace(' ' + c, c)
print(res)