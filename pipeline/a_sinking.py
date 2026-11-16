exec(open('a_compound.py').read().split('T0,T1,END')[0])
T0,MT,DROP,END=4.6,0.8,0.7,15.8; T1=T0+12*MT
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6); add(ping(1318),0.35,0.1)
add(whoosh(1.2),0.9,0.35)                                         # track builds
for i in range(6): add(clank(),1.0+i*0.45,0.04)
add(thud(),1.7,0.6); add(ping(330),1.75,0.08)                      # last Christmas on card
add(whoosh(0.4),T0-0.4,0.4)
for m in range(1,13):                                              # monthly £50: chime up for fund, low clank for card
    tt=T0+m*MT-0.1
    add(ping(880+m*45),tt,0.09); add(clank(),tt+0.05,0.05)
    if m>=3: add(ping(392),tt+0.18,0.035)                          # interest biting back
for k in range(int(12*MT/0.2)): add(clank(),T0+k*0.2,0.015)        # coaster clatter
add(whoosh(0.8),T1,0.7); add(thud(),T1+DROP,0.9)                   # the Christmas drop
for f_ in (1046,1318,1568): add(ping(f_),T1+DROP+0.1,0.14)
add(ping(262),T1+DROP+0.15,0.12); add(ping(247),T1+DROP+0.4,0.1)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25); add(ping(3136),END+3.0,0.2)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('sinking.wav',SR,(st*32767).astype(np.int16))
print('ok')
