exec(open('a_compound.py').read().split('T0,T1,END')[0])
T_FLOW,T0,T1,END=4.3,8.0,14.4,15.4; MT=(T1-T0)/12
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6)
for f in range(3): add(whoosh(0.35),0.5+f*0.25,0.25)
for f in range(3): add(thud(),2.6+f*0.2,0.45); add(ping(1318),2.65+f*0.2,0.1)
for f in range(3):
    for i in range(3): add(ping([1568,1318,1046][f]+i*110),T_FLOW+f*0.75+i*0.25,0.11)
add(whoosh(0.4),T0-0.3,0.4)
for m in range(12):
    st=T0+m*MT
    add(ping(1760),st+0.08,0.09)      # top floor +400
    add(clank(),st+0.12,0.04)
add(thud(),T1+0.1,0.9); add(whoosh(0.5),T1+0.1,0.5)
for f_ in (1046,1318,1568): add(ping(f_),T1+0.25,0.14)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('payday.wav',SR,(st*32767).astype(np.int16))
print('ok')
