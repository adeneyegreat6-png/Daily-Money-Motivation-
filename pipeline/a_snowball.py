exec(open('a_compound.py').read().split('T0,T1,END')[0])
T0,MT=5.0,0.5; PAID=[3,12,18]; T1,END=T0+18*MT,15.4
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6); add(ping(1318),0.35,0.1)
for i in range(3): add(thud(),1.2+i*0.35,0.45); add(ping(220*(i+2)),1.25+i*0.35,0.06)
add(ping(660),1.6,0.08); add(ping(520),2.2,0.08)                 # minimums-only warning
add(whoosh(0.4),T0-0.4,0.4)
k=0; t=T0
while t<T1:
    tg=sum(1 for p in PAID if T0+p*MT<=t)
    add(clank(),t+0.35,0.03+0.015*tg); k+=1; t+=0.18
for i,p in enumerate(PAID):
    tt=T0+p*MT; add(thud(),tt,0.9); add(whoosh(0.4),tt,0.4)
    for j,f_ in enumerate((1046,1318,1568)[:i+1+ (1 if i<2 else 0)]): add(ping(f_),tt+0.05+j*0.07,0.14)
for f_ in (1046,1318,1568,2093): add(ping(f_),T1+0.3,0.12)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25); add(ping(3136),END+3.0,0.2)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('snowball.wav',SR,(st*32767).astype(np.int16))
print('ok')
