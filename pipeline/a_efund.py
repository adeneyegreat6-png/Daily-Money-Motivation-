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
def clank():
    n=int(0.3*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*420*tt)+0.7*np.sin(2*np.pi*1130*tt)+0.4*np.sin(2*np.pi*2290*tt))*np.exp(-tt*16)
TB,T0,T1,END=3.4,5.4,14.6,15.4; NM=40; MT=(T1-T0)/NM
add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6)
for tt in (1.2,1.6): add(ping(1175),tt,0.11)
for tt in (2.0,2.4): add(ping(1568),tt,0.12)
add(whoosh(0.4),TB-0.2,0.5); add(thud(),TB,1.0); add(clank(),TB+0.05,0.25); add(clank(),TB+0.25,0.18)
add(whoosh(0.6),TB+0.6,0.5)
for m in range(NM):
    st=T0+m*MT+0.03
    add(clank(),st,0.04); add(ping(1760 if m%2 else 1568),st+0.02,0.05)
add(thud(),T1,0.9); add(whoosh(0.5),T1,0.5)
for f_ in (1046,1318,1568): add(ping(f_),T1+0.1,0.14)
add(whoosh(0.6),END,0.6); add(thud(),END+0.3,0.5)
add(ping(2093),END+1.2,0.2); add(ping(2637),END+2.4,0.25)
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('efund.wav',SR,(st*32767).astype(np.int16))
print('ok')
