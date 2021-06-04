s=input()
for i in '+-':
    for j in '+-':
        for k in '+-':
            eq=f'{s[0]}{i}{s[1]}{j}{s[2]}{k}{s[3]}'
            if eval(eq)==7:
                print(eq+'=7')
                exit()