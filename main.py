# 1 - misol
sonlar = [1, 2, 3, 6, 9, 12, 15, 4, 5, 8]
natija = list(filter(lambda x: x % 3 == 0 and x > 5, sonlar))
print(natija)

# 2 - misol
sozlar = ["radar", "salom", "level", "python", "kayak"]
natija = list(filter(lambda x: x == x[::-1], sozlar))
print(natija)

# 3 - misol
elementlar = [10, 20, 30, 40, 50, 60]
natija = list(filter(lambda x: elementlar.index(x) % 2 != 0, elementlar))
print(natija)

# 4 - misol
sozlar = ["Salom", "dunyo", "Python", "kod", "Apple"]
natija = list(filter(lambda x: x[0].isupper(), sozlar))
print(natija)

# 5 - misol
sonlar = [-3, 2, 5, 6, 7, -8]
natija = list(filter(lambda x: x > 0 and x % 2 != 0, sonlar))
print(natija)
