exec(open('a_compound.py').read().split('T0,T1,END')[0])
OPEN=[3.8,5.0,6.2,7.4,8.6]; PLUG=[10.4,11.2,12.0,12.8,13.6]; T1,END=14.4,15.4
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6); add(ping(1318),0.35,0.1)
for k in range(30): add(clank(),0.2+k*0.11+0.4,0.012)      # coins dropping into barrel
for o in OPEN:
    add(thud(),o,0.5); add(whoosh(0.3),o,0.25); add(ping(880),o+0.05,0.08)
for i,p in enumerate(PLUG):
    add(clank(),p,0.12); add(ping(1318+i*110),p+0.05,0.14)
add(thud(),T1,0.9); add(whoosh(0.5),T1,0.5)
for f_ in (1046,1318,1568): add(ping(f_),T1+0.15,0.14)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25); add(ping(3136),END+3.0,0.2)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('leaks.wav',SR,(st*32767).astype(np.int16))
print('ok')
