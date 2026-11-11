(()=>{const $=s=>document.querySelector(s);
const b=$('#burger'),l=$('#links');
if(b){b.onclick=()=>{const o=l.classList.toggle('open');b.setAttribute('aria-expanded',o)}}
const dd=$('.dd-btn');
if(dd){dd.onclick=()=>{const p=dd.parentElement,o=p.classList.toggle('open');dd.setAttribute('aria-expanded',o)}}
document.addEventListener('keydown',e=>{if(e.key==='Escape'){l&&l.classList.remove('open');b&&b.setAttribute('aria-expanded','false');const p=$('.dd.open');if(p){p.classList.remove('open');dd.setAttribute('aria-expanded','false');dd.focus()}}});
const f=$('#form');if(!f)return;
const CONFIG={email:'mensaweb@mensaweb.com',endpoint:'https://formbold.com/s/3qXr1'}; // Formbold form endpoint (form ID is public by design)
const st=$('#status'),v=n=>f.elements[n].value.trim();
const bad=(n,m)=>{$('#e-'+n).textContent=m;f.elements[n].setAttribute('aria-invalid',!!m);return !m};
const check=()=>{const a=bad('name',v('name').length<2?'Please enter your full name.':''),
c=bad('email',/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('email'))?'':'Please enter a valid email address.'),
d=bad('message',v('message').length<10?'Please describe your project (at least 10 characters).':'');
if(!(a&&c&&d))f.querySelector('[aria-invalid=true]').focus();return a&&c&&d};
['name','email','message'].forEach(n=>f.elements[n].addEventListener('input',()=>{if(f.elements[n].getAttribute('aria-invalid')==='true')check()}));
f.onsubmit=async e=>{e.preventDefault();if(f.elements.website.value)return;if(!check())return;
const data={name:v('name'),email:v('email'),phone:v('phone'),organisation:v('org'),service:v('service'),budget:v('budget'),message:v('message')};
if(CONFIG.endpoint){const btn=$('#send');btn.disabled=true;
try{const r=await fetch(CONFIG.endpoint,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(data)});if(!r.ok)throw 0;
st.className='ok';st.textContent='Thank you. Your enquiry has been sent.';f.reset()}catch{st.className='bad';st.textContent='Sending failed. Please try again or email '+CONFIG.email+'.'}btn.disabled=false}
else{const body=Object.entries(data).map(([k,x])=>k+': '+(x||'n/a')).join('\n');
st.className='ok';st.innerHTML='Your enquiry is ready. This site has no form service connected yet, so it will be sent from your own email app: <a class="btn btn-p" style="margin-top:10px" href="mailto:'+CONFIG.email+'?subject='+encodeURIComponent('Project enquiry: '+data.service)+'&body='+encodeURIComponent(body)+'">Open email to send</a>'}
st.setAttribute('tabindex','-1');st.focus()}})();
