n=int(input('Dati numarul de elemente din vector='))
z=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
if n<10:
    for i in range(0,n):
        x=int(input('Dati elementul='))
        z.extend([x])
    print(z)
    print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
    print(z[:5])
    print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
    b=z
    print(b[::-1])
    print('c)  sortează componentele tabloului în ordine descrescătoare;')
    c=sorted(z)
    c.sort(reverse=True)
    print(c)
    print('d)  afişează pe ecran doar componentele pare;')
    d=[]
    for i in range(0,len(z)):
        if z[i]%2==0:
            y=z[i]
            d.extend([y])
    print(d)
    print('e)  afişează pe ecran media aritmetică a componentelor pare;') 
    s=sum(d)/len(d)
    print(s)
    print('f)  afişează pe ecran doar componentele impare;')
    f=[]
    for i in range(0,len(z)):
        if z[i]%2!=0:
            y=z[i]
            f.extend([y])
    print(f)
    print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
    g=[]
    x=int(input('dati valoare lui x='))
    y=int(input('dati valoare lui y='))
    g=[]
    for i in range(0,len(z)):
        if ((z[i]>x) and (z[i]%y!=0)):
            r=z[i]
            g.extend([r])
    print(g)
    print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
    q=int(input('valoarea x= '))
    q1=int(input('valoarea y= '))
    h=[]
    for i in range(0,len(z)):
        if ((z[i]>x) and (z[i]<y)):
            s=z[i]
            h.extend([s])
    print(h)
    print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
    for i in z:
        if i < 0 and i%2==1:
            print(z.index(i))
    print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
    for i in z:
        if (i < 100 and i>9) or (i > -100 and i<-9):
            print(z.index(i))
    print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
    k=z
    randomvar=z[0]
    ind = z.index(min(z))
    k[:1]=[min(k)]
    print(k)
    print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
    k[ind]=randomvar   
    print(k)
    print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
    m = []
    for i in z:
        if i%2==0:
            m.append(i)
    print(m)
    print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
    n = []
    for i in z:
        if i%3==0:
            n.append(i)
    print(n)
    print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')
    o=[]
    for i in z:
        counter = 0
        for t in range(1,i):
            if i%t==0:
             counter+=1
        if counter < 5:
            o.append(i)
    print(o)