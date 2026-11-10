const cv=document.getElementById('c'),W=cv.width,H=cv.height,g=cv.getContext('2d');
const F='Inter';
const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v));
const eOut=t=>1-Math.pow(1-t,3);
const eIn=t=>t*t*t;
const back=t=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2);};
const gbp=v=>(v<0?'-':'')+'£'+Math.round(Math.abs(v)).toLocaleString('en-GB');
function rand(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function rr(x,y,w,h,r){r=Math.min(r,w/2,h/2);g.beginPath();g.moveTo(x+r,y);g.arcTo(x+w,y,x+w,y+h,r);g.arcTo(x+w,y+h,x,y+h,r);g.arcTo(x,y+h,x,y,r);g.arcTo(x,y,x+w,y,r);g.closePath();}
function text(s,x,y,size,color,{weight=900,align='center',stroke=0,sc='#111',base='middle',shadow=false,spacing=0,alpha=1}={}){
  g.save();g.globalAlpha*=alpha;g.font=`${weight} ${size}px ${F}`;g.textAlign=align;g.textBaseline=base;
  if('letterSpacing' in g) g.letterSpacing=spacing+'px';
  if(shadow){g.fillStyle='rgba(0,0,0,.45)';g.fillText(s,x,y+size*0.07);}
  if(stroke){g.lineJoin='round';g.lineWidth=stroke;g.strokeStyle=sc;g.strokeText(s,x,y);}
  g.fillStyle=color;g.fillText(s,x,y);g.restore();
}
function pill(s,x,y,size,fg,bg,border){
  g.save();g.font=`900 ${size}px ${F}`;const w=g.measureText(s).width+size*1.1,h=size*1.7;
  g.fillStyle=bg;rr(x-w/2,y-h/2,w,h,h/2);g.fill();if(border){g.strokeStyle=border;g.lineWidth=4;rr(x-w/2,y-h/2,w,h,h/2);g.stroke();}
  g.restore();text(s,x,y+1,size,fg);
}
function bubble(s,x,y,a){ // speech bubble, tail pointing down-left
  if(a<=0)return;g.save();g.globalAlpha=clamp(a);const sc=0.7+0.3*back(clamp(a*1.4));
  g.translate(x,y);g.scale(sc,sc);g.font=`900 34px ${F}`;const w=g.measureText(s).width+48,h=66;
  g.fillStyle='#fff';g.strokeStyle='#111';g.lineWidth=5;rr(-w/2,-h/2,w,h,16);g.fill();g.stroke();
  g.beginPath();g.moveTo(-18,h/2-3);g.lineTo(-34,h/2+26);g.lineTo(6,h/2-3);g.closePath();g.fill();
  g.beginPath();g.moveTo(-18,h/2);g.lineTo(-34,h/2+26);g.lineTo(6,h/2);g.stroke();
  g.restore();text(s,x,y+1,34*(0.7+0.3*back(clamp(a*1.4))),'#111',{alpha:clamp(a)});
}
function coin(x,y,r=16,rot=0){
  g.save();g.translate(x,y);g.scale(Math.max(0.25,Math.abs(Math.cos(rot))),1);
  g.fillStyle='#b8860b';g.beginPath();g.arc(0,2,r,0,7);g.fill();
  g.fillStyle='#ffd23f';g.beginPath();g.arc(0,0,r,0,7);g.fill();
  g.fillStyle='rgba(255,255,255,.55)';g.beginPath();g.arc(-r*.3,-r*.3,r*.28,0,7);g.fill();
  g.restore();
}
function pop(s,x,y,age,color,size=40){
  if(age<0||age>1)return;const a=age<0.15?age/0.15:1-clamp((age-0.6)/0.4);
  text(s,x,y-age*50,size*(0.8+0.2*back(clamp(age/0.25))),color,{stroke:8,sc:'#111',alpha:a});
}
// ---- stick figure (thick rounded limbs) ----
// opts: col, acc ('cap'|'beanie'|'tie'), armL/armR angle from straight down (rad, +ve = toward figure's right/forward),
// legs spread, slump (0..1), face ('meh'|'happy'|'shock'|'cool'), look (-1..1), scale
function stick(x,feet,o={}){
  const {col='#f1f1f1',acc=null,armL=0.15,armR=0.15,spread=0.16,slump=0,face='meh',look=0,scale=1,bob=0,limb='#ececec',outline='#16171b',hold=null}=o;
  g.save();g.translate(x,feet+bob);g.scale(scale,scale);g.lineCap='round';g.lineJoin='round';
  const lw=24,hip=-150+slump*25,neck=-300+slump*50,hx=slump*22,nx=slump*40;
  const limbPath=(pts,c)=>{for(const [w,cc] of [[lw+8,outline],[lw,c]]){g.strokeStyle=cc;g.lineWidth=w;g.beginPath();g.moveTo(pts[0][0],pts[0][1]);for(let k=1;k<pts.length;k++)g.lineTo(pts[k][0],pts[k][1]);g.stroke();}};
  const L=150;
  limbPath([[hx-8,hip],[hx-8-Math.sin(spread)*L,hip+Math.cos(spread)*L]],limb);
  limbPath([[hx+8,hip],[hx+8+Math.sin(spread)*L,hip+Math.cos(spread)*L]],limb);
  limbPath([[hx,hip],[nx,neck]],col);
  if(acc==='tie'){g.fillStyle='#f5c542';g.beginPath();g.moveTo(nx-7,neck+8);g.lineTo(nx+7,neck+8);g.lineTo(nx+9,neck+70);g.lineTo(nx,neck+84);g.lineTo(nx-9,neck+70);g.closePath();g.fill();}
  const A=125,sy=neck+18;
  // armL = back arm (left of screen), armR = front arm (right of screen); angle 0 = down, PI/2 = horizontal outwards
  const hl=[nx-Math.sin(armL)*A,sy+Math.cos(armL)*A], hr=[nx+Math.sin(armR)*A,sy+Math.cos(armR)*A];
  limbPath([[nx,sy],hl],limb);limbPath([[nx,sy],hr],limb);
  if(hold)hold(hr[0],hr[1]);
  // head
  const hy=neck-46,R=44,ex=look*8;
  g.fillStyle='#f6f6f6';g.strokeStyle=outline;g.lineWidth=6;g.beginPath();g.arc(nx,hy,R,0,7);g.fill();g.stroke();
  g.fillStyle=outline;g.strokeStyle=outline;g.lineWidth=5;
  if(face==='cool'){rr(nx-30+ex,hy-14,26,15,6);g.fill();rr(nx+4+ex,hy-14,26,15,6);g.fill();g.fillRect(nx-6+ex,hy-10,12,4);
    g.beginPath();g.arc(nx+ex+2,hy+14,10,0.25,Math.PI-0.25);g.stroke();}
  else if(face==='shock'){g.beginPath();g.arc(nx-13+ex,hy-6,7,0,7);g.fill();g.beginPath();g.arc(nx+15+ex,hy-6,7,0,7);g.fill();
    g.beginPath();g.ellipse(nx+ex+1,hy+20,9,12,0,0,7);g.fill();}
  else if(face==='happy'){g.beginPath();g.arc(nx-13+ex,hy-4,8,Math.PI*1.1,Math.PI*1.9);g.stroke();g.beginPath();g.arc(nx+15+ex,hy-4,8,Math.PI*1.1,Math.PI*1.9);g.stroke();
    g.beginPath();g.arc(nx+ex+1,hy+10,13,0.2,Math.PI-0.2);g.stroke();}
  else if(face==='sad'){g.beginPath();g.arc(nx-13+ex,hy-4,5,0,7);g.fill();g.beginPath();g.arc(nx+15+ex,hy-4,5,0,7);g.fill();
    g.beginPath();g.arc(nx+ex+1,hy+26,11,Math.PI+0.4,-0.4);g.stroke();}
  else { // meh: half-lidded
    for(const ox of [-13,15]){g.beginPath();g.arc(nx+ox+ex,hy-4,7,0,Math.PI);g.fill();g.beginPath();g.moveTo(nx+ox+ex-10,hy-5);g.lineTo(nx+ox+ex+10,hy-5);g.stroke();}
    g.beginPath();g.moveTo(nx+ex-6,hy+20);g.lineTo(nx+ex+10,hy+18);g.stroke();}
  if(acc==='cap'){g.fillStyle='#e8394f';g.beginPath();g.arc(nx,hy-8,R+2,Math.PI*1.02,-0.02);g.fill();rr(nx-R-36,hy-16,46,13,6);g.fill();}
  if(acc==='beanie'){g.fillStyle='#2fbf9b';g.beginPath();g.arc(nx,hy-6,R+3,Math.PI,0);g.fill();g.fillStyle='#24997c';rr(nx-R-4,hy-16,2*R+8,16,6);g.fill();g.fillStyle='#2fbf9b';g.beginPath();g.arc(nx,hy-R-10,10,0,7);g.fill();}
  if(acc==='tie'){g.fillStyle=outline;g.beginPath();g.arc(nx,hy-6,R+1,Math.PI*1.08,-0.08);g.fill();}
  g.restore();
}
