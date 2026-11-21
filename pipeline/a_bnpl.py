exec(open('a_compound.py').read().split('T0,T1,END')[0])
TP=[2.0,4.4,6.8]; TTOT=9.0; T0=10.2; PT=1.2; T1=T0+4*PT; END=15.6
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6); add(ping(1318),0.35,0.1)
for i in range(10): add(clank(),0.6+i*0.08,0.03)                 # saver's pot stacks up
for i,tp in enumerate(TP):                                        # each "easy" purchase
    add(ping(1046+i*130),tp,0.11); add(ping(1568),tp+0.08,0.06)
    for j in range(4): add(clank(),tp+0.1+j*0.12,0.045)            # owed stack grows
add(whoosh(0.6),TP[0],0.3); add(ping(1760),TP[0]+0.2,0.09)        # saver pays in full
for tp in TP[1:]: add(ping(2093),tp+0.25,0.1)                     # "ONLY £x!"
add(ping(523),TTOT,0.12); add(ping(392),TTOT+0.15,0.1)            # £180 due every 2 weeks
add(whoosh(0.4),T0-0.4,0.4)
for k in range(4):                                                 # four payments
    tt=T0+k*PT
    add(thud(),tt+0.1,0.55); add(ping(330-k*20),tt+0.15,0.1); add(whoosh(0.35),tt+0.2,0.15)
    add(ping(1568),tt+0.35,0.05)                                   # saver: £0 due
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
for f_ in (1046,1318,1568): add(ping(f_),END+0.5,0.1)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('bnpl.wav',SR,(st*32767).astype(np.int16))
print('ok')
