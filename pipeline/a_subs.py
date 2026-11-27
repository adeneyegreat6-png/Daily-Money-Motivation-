exec(open('a_compound.py').read().split('T0,T1,END')[0])
TR=[1.6,3.2,4.5,5.8,7.1]; TTOT=8.6; T0=10.0; MT=0.45; T1=T0+12*MT; END=15.8
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6); add(ping(1318),0.35,0.1)
add(ping(1046),TR[0],0.1)                                          # the one used subscription
for i,tr in enumerate(TR[1:]):                                     # each unused sub appears, then gets cancelled
    add(ping(523-i*30),tr,0.1); add(clank(),tr+0.05,0.04)
    add(whoosh(0.3),tr+0.4,0.2); add(ping(1568+i*120),tr+0.5,0.1)
add(ping(392),TTOT,0.12); add(ping(1760),TTOT+0.12,0.1)            # £46.96 a month
add(whoosh(0.4),T0-0.4,0.4)
for k in range(12):                                                 # twelve months
    tt=T0+k*MT
    add(clank(),tt+0.05,0.05); add(ping(330),tt+0.08,0.05); add(ping(1318+k*40),tt+0.12,0.06)
add(thud(),T1,0.6); add(ping(2093),T1+0.05,0.15)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
for f_ in (1046,1318,1568): add(ping(f_),END+0.5,0.1)
add(ping(2093),END+2.0,0.2); add(ping(2637),END+2.6,0.25)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('subs.wav',SR,(st*32767).astype(np.int16))
print('ok')
