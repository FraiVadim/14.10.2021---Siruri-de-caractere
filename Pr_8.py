s='ABCDEFGH JKLMNOPZ'
a=''
for i in range (0,len(s)):
    if ord(s[i])!=32 and ord(s[i])!=90:
        a+=chr(ord(s[i])+1)
print('– fiecare literă de la ’A’ până la ’Y’ se înlocuieşte prin următoarea literă din alfabet:') 
print(a) 
a=s
print('– fiecare literă ’Z’ se înlocuieşte prin litera ’A’:')
print(a.replace('Z','A'))
a=''
for i in range (0,len(s)):
    if ord(s[i])==32:
        a+=chr(ord('-'))
    else :
        a+=s[i]
print('– fiecare spaţiu se înlocuieşte prin ’-’:')
print(a)