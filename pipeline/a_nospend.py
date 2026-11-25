exec(open('a_compound.py').read().split('T0,T1,END')[0])
T0,MT,END=4.6,0.32,15.8; T1=T0+30*MT
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6); add(ping(1318),0.35,0.1)
add(whoosh(1.2),0.9,0.35)                                          # tracks build
for i in range(6): add(clank(),1.0+i*0.45,0.04)
for j in range(3): add(ping(660-j*60),1.8+j*0.5,0.09); add(clank(),1.8+j*0.5,0.05)   # extras list
add(ping(523),3.3,0.08)                                            # £10 / £17.50 line
add(ping(1568),2.2,0.08)                                           # no-spend rider: bills paid, no extras
add(whoosh(0.4),T0-0.4,0.4)
for d in range(30):                                                # every day
    tt=T0+d*MT; we=(d%7 in (5,6))
    add(ping(880+d*25),tt+0.03,0.07 if not we else 0.1)            # savings pot grows (rising pitch)
    add(clank(),tt+0.12,0.03 if not we else 0.06)                  # usual: money out
    if we: add(whoosh(0.25),tt+0.1,0.08)
for k in range(int(30*MT/0.2)): add(clank(),T0+k*0.2,0.012)        # coaster clatter
add(thud(),T1+0.05,0.9); add(whoosh(0.6),T1,0.5)
for f_ in (1046,1318,1568): add(ping(f_),T1+0.15,0.14)
add(ping(262),T1+0.2,0.12); add(ping(247),T1+0.45,0.1)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25); add(ping(3136),END+3.0,0.2)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('nospend.wav',SR,(st*32767).astype(np.int16))
print('ok')
