words = ['cat', 'window', 'defenstrate']

for w in words:
    print(w, len(w))



users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' equals ', x, ' * ', n // x)
            break
    else: 
            print(n, ' is a prime number')

for i in range(2, 10):
    if i % 2 == 0:
        print(i, ' is an even number')
        continue
    print(i, ' is an add number')