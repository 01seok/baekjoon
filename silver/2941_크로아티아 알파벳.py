word = input()
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for ca in croatian_alphabets:
    word = word.replace(ca, ' ') # 크로아티아 알파벳을 공백으로 치환

print(len(word))