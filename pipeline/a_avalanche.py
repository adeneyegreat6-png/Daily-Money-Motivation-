exec(open('a_low.py').read().split('# SFX')[0])
def ping(f=1760):
    n=int(0.45*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*f*tt)+0.6*np.sin(2*np.pi*f*1.5*tt)+0.3*np.sin(2*np.pi*f*2.01*tt))*np.exp(-tt*9)
def whoosh(d=0.6):
    n=int(d*SR); x=np.random.RandomState(3).randn(n)
    x=np.convolve(x,np.ones(40)/40,'same'); e=np.sin(np.pi*np.arange(n)/n)
    return x*e
def thud():
    n=int(0.5*SR); tt=np.arange(n)/SR
    return np.sin(2*np.pi*(60+60*np.exp(-tt*20))*tt)*np.exp(-tt*6)
def tick():
    n=int(0.08*SR); tt=np.arange(n)/SR
    return np.sin(2*np.pi*1900*tt)*np.exp(-tt*60)
T0=3.8; MON=0.33; MONTHS=28; T1=T0+MONTHS*MON; END=15.6
add(thud(),0.05,0.8); add(whoosh(0.5),0.5,0.5); add(whoosh(0.5),1.0,0.5)
add(ping(1318),1.2,0.1)
add(whoosh(0.4),T0-0.4,0.4)
for m in range(MONTHS): add(tick(),T0+m*MON,0.12)
# payoffs: snowball loan m7, card m23, car m28; avalanche loan+card m22, car m28
for m,f_ in ((7,1568),(23,1760),(22,1318)): add(ping(f_),T0+m*MON,0.2)
add(whoosh(0.3),T0+7*MON,0.25)
add(thud(),T1,0.9); add(whoosh(0.5),T1+0.3,0.5)
for f_ in (1046,1318,1568): add(ping(f_),T1+0.35,0.14)
add(ping(1760),T1+0.8,0.15)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('avalanche.wav',SR,(st*32767).astype(np.int16))
print('ok')
