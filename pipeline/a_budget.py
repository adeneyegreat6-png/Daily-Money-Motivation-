import numpy as np
from scipy.io import wavfile
SR=44100; DUR=20.0; N=int(SR*DUR)
t=np.arange(N)/SR
mix=np.zeros(N)
bpm=96; beat=60/bpm; bar=beat*4

def add(sig,start,gain=1.0):
    i=int(start*SR); j=min(N,i+len(sig))
    if i<N: mix[i:j]+=sig[:j-i]*gain

def env(n,a=0.01,r=0.3):
    e=np.ones(n); ai=int(a*SR); e[:ai]=np.linspace(0,1,ai)
    e*=np.exp(-np.arange(n)/SR/r); return e

def note(f,dur,shape='sine'):
    n=int(dur*SR); tt=np.arange(n)/SR
    s=np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt)+0.12*np.sin(2*np.pi*3*f*tt)
    return s

# chords (Am7, Fmaj7, Cmaj7, G6) - soft pad
mid=lambda m:440*2**((m-69)/12)
chords=[[48,52,55,59],[53,57,60,64],[57,60,64,67],[55,59,62,65]]
pos=0.0;ci=0
while pos<DUR:
    for m in chords[ci%4]:
        n=int(bar*SR)
        s=note(mid(m),bar)
        e=np.minimum(1,np.arange(n)/(0.25*SR))*np.minimum(1,(n-np.arange(n))/(0.3*SR))
        add(s*e,pos,0.035)
    # bass
    b=chords[ci%4][0]-12
    for k in [0,2.5]:
        n=int(beat*1.2*SR); s=np.sin(2*np.pi*mid(b)*np.arange(n)/SR)*env(n,0.005,0.35)
        add(s,pos+k*beat,0.22)
    # piano-ish arpeggio
    for k,m in enumerate([chords[ci%4][1]+12,chords[ci%4][2]+12,chords[ci%4][3]+12,chords[ci%4][2]+12]):
        n=int(beat*SR); s=note(mid(m),beat)*env(n,0.005,0.25)
        add(s,pos+k*beat+beat*0.5,0.05)
    pos+=bar;ci+=1

# drums
def kick():
    n=int(0.35*SR); tt=np.arange(n)/SR
    f=50+90*np.exp(-tt*30); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-tt*9)
def snap():
    n=int(0.2*SR); tt=np.arange(n)/SR
    return np.random.RandomState(1).randn(n)*np.exp(-tt*28)*0.6+np.sin(2*np.pi*190*tt)*np.exp(-tt*30)*0.4
def hat():
    n=int(0.05*SR); x=np.random.RandomState(2).randn(n); x=np.diff(np.concatenate([[0],x]))
    return x*np.exp(-np.arange(n)/SR*90)
k=0;p=0.0
while p<DUR:
    b=k%4
    if b in (0,2): add(kick(),p,0.55)
    if b in (1,3): add(snap(),p,0.18)
    add(hat(),p,0.06); add(hat(),p+beat/2,0.04)
    p+=beat;k+=1

# SFX
def ping(f=1760):
    n=int(0.45*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*f*tt)+0.6*np.sin(2*np.pi*f*1.5*tt)+0.3*np.sin(2*np.pi*f*2.01*tt))*np.exp(-tt*9)
def whoosh(d=0.6):
    n=int(d*SR); x=np.random.RandomState(3).randn(n)
    # simple low-pass by cumulative average
    x=np.convolve(x,np.ones(40)/40,'same'); e=np.sin(np.pi*np.arange(n)/n)
    return x*e
def thud():
    n=int(0.5*SR); tt=np.arange(n)/SR
    return np.sin(2*np.pi*(60+60*np.exp(-tt*20))*tt)*np.exp(-tt*6)

add(thud(),0.05,0.8); add(whoosh(0.5),0.0,0.6)
for k in range(10): add(ping(1568+(k%3)*200),3.0+k*0.2,0.07)
per=9.6/12
for m in range(12):
    add(ping(1760+(m%4)*110),5.0+m*per+0.05,0.12)
    add(whoosh(0.25),5.0+m*per+0.65*per,0.25)
for f_ in (1318,1568,2093): add(ping(f_),14.6,0.16)
add(whoosh(0.7),15.2,0.7); add(thud(),15.45,0.6)
add(ping(2093),16.4,0.2); add(ping(2637),17.7,0.25)
# master: fade in/out, normalise
fade=np.ones(N); fi=int(0.3*SR); fo=int(1.2*SR)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
mix*=fade
mix/=np.max(np.abs(mix))*1.12
st=np.stack([mix,mix],1)
wavfile.write('budget.wav',SR,(st*32767).astype(np.int16))
print('ok')
