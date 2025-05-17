CasosDeTeste = int(input())

for i in range(CasosDeTeste):
    string = input()

dict_contador = {}
for char in string:
    if 'a' <= char <= 'z':
        if char in dict_contador:
            dict_contador[char] += 1
        else:
            dict_contador[char] = 1

max_freq = max(dict_contador.values(), default=0)
max_chars = [char for char, freq in dict_contador.items() if freq == max_freq]

print(sum(dict_contador.values()), max_freq, dict_contador)
      