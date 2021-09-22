zi=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
with open('venit.txt','r') as f:
    v=list(eval(f.read()))
print(sum(v))
print(sum(v)/7)
max=v.index(max(v))
min=v.index(min(v))
print(zi[max],'are venit maxim de',v[max])
print(zi[min],'are venit minim de',v[min])