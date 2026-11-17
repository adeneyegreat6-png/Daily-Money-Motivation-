exec(open('a_compound.py').read().split('T0,T1,END')[0])
T_FLOW,T0,T1,END=3.6,7.6,14.0,15.4; MT=(T1-T0)/12
LEFTOVER=[50,0,30,0,80,0,20,0,60,0,0,40]
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6)
for b in range(2): add(whoosh(0.35),0.4+b*0.25,0.25)
for b in range(2): add(thud(),2.3+b*0.2,0.45); add(ping(1318),2.35+b*0.2,0.1)   # envelopes land
for f in range(3):
    for b in range(2): add(ping([1568,1318,1046][f] if b==1 else [1046,1318,880][f]),T_FLOW+0.2+f*1.0+b*0.15,0.11)
add(ping(330),T_FLOW+2.4,0.1)                                     # only £50 left
add(whoosh(0.4),T0-0.3,0.4)
for m in range(12):
    st=T0+m*MT
    add(ping(1760),st+0.08,0.09); add(clank(),st+0.12,0.04)       # save-first +£250
    if LEFTOVER[m]>0: add(ping(988),st+0.2,0.05)
    else: add(ping(262),st+0.2,0.04)
add(thud(),T1+0.1,0.9); add(whoosh(0.5),T1+0.1,0.5)
for f_ in (1046,1318,1568): add(ping(f_),T1+0.25,0.14)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25); add(ping(3136),END+3.0,0.2)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('payfirst.wav',SR,(st*32767).astype(np.int16))
print('ok')
