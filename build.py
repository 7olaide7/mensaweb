#!/usr/bin/env python3
"""Static site generator for MensaWeb ICT. Run: python3 build.py  (outputs pages as /<slug>/index.html)"""
import os, json
SITE = "https://mensaweb.com"  # domain supplied by owner (not live yet)
EMAIL, PHONE, PHONE_DISPLAY = "mensaweb@mensaweb.com", "+2349054409479", "+234 905 440 9479"
SERVICES = [
 ("website-design-development","Website Design & Development","Professional, responsive websites that communicate your brand, present your services and give your business a credible online presence."),
 ("ecommerce-development","E-commerce Development","Online stores designed to help businesses showcase products, manage their online operations and provide customers with a convenient shopping experience."),
 ("web-application-development","Web Application Development","Custom browser-based applications that help businesses automate processes, manage information and provide specialised online services."),
 ("custom-software-development","Custom Software Solutions","Purpose-built software and application solutions developed around specific requirements, workflows and operational challenges."),
 ("website-maintenance-support","Website Maintenance & Support","Ongoing technical assistance, updates, improvements and maintenance to help keep websites secure, functional and performing as intended.")]
NAV=[("/","Home"),("/about/","About"),("SERVICES",""),("/how-we-work/","How We Work"),("/why-choose-us/","Why Choose Us"),("/contact/","Contact")]

def header(cur):
    li=""
    for h,t in NAV:
        if h=="SERVICES":
            sub="".join(f'<li><a href="/services/{s}/">{n}</a></li>' for s,n,_ in SERVICES)
            li+=f'<li class="dd"><button class="dd-btn" aria-expanded="false" aria-haspopup="true" aria-controls="services-submenu">Services &#9662;</button><ul class="sub-menu" id="services-submenu"><li><a href="/services/">All Services</a></li>{sub}</ul></li>'
        else:
            c=' aria-current="page"' if h==cur else ''
            li+=f'<li><a href="{h}"{c}>{t}</a></li>'
    return f'''<a class="skip" href="#main">Skip to content</a><header><div class="wrap"><nav aria-label="Main"><a href="/" class="logo" aria-label="MensaWeb ICT home"><span class="mark" aria-hidden="true">M</span>MensaWeb ICT</a><button class="burger" id="burger" aria-expanded="false" aria-controls="links" aria-label="Menu">&#9776;</button><ul class="links" id="links">{li}<li><a href="/contact/" class="btn btn-p">Discuss Your Project</a></li></ul></nav></div></header>'''

def footer():
    sv="".join(f'<li><a href="/services/{s}/">{n.replace(" Design &","").replace(" Solutions","").replace(" & Support","").replace(" & Technical Support","")}</a></li>' for s,n,_ in SERVICES)
    return f'''<footer><div class="wrap"><div class="fgrid">
<div><a href="/" class="logo"><span class="mark" aria-hidden="true">M</span>MensaWeb ICT</a><p style="margin-top:14px">Professional website development, custom applications and practical digital solutions for individuals and businesses.</p><p>Based in Nigeria. Serving clients worldwide.</p></div>
<div><h2 class="fh">Company</h2><ul><li><a href="/about/">About Us</a></li><li><a href="/why-choose-us/">Why Choose Us</a></li><li><a href="/how-we-work/">How We Work</a></li><li><a href="/contact/">Contact</a></li></ul></div>
<div><h2 class="fh">Services</h2><ul>{sv}</ul></div>
<div><h2 class="fh">Resources</h2><ul><li><a href="/faq/">Frequently Asked Questions</a></li></ul></div>
<div><h2 class="fh">Contact</h2><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li></ul></div></div>
<div class="fbot"><span>Professional technology solutions. Personal attention. Dependable execution.</span><span>&copy; 2026 MensaWeb ICT. All rights reserved.</span></div></div></footer>'''

def page(slug,title,desc,body,cur="",noindex=False,crumbs=None,schema=None):
    url=f"{SITE}/{slug}/" if slug else f"{SITE}/"
    ld=[{"@context":"https://schema.org","@type":"Organization","name":"MensaWeb ICT","url":SITE+"/","email":EMAIL,"areaServed":"Worldwide","address":{"@type":"PostalAddress","addressCountry":"NG"}}]
    if not slug: ld.append({"@context":"https://schema.org","@type":"WebSite","name":"MensaWeb ICT","url":SITE+"/"})
    if schema: ld.append(schema)
    if crumbs: ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+u} for i,(n,u) in enumerate(crumbs)]})
    robots='<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">{robots}
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="MensaWeb ICT"><meta property="og:image" content="{SITE}/assets/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}/assets/og-image.png"><meta name="theme-color" content="#0A1424">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css"><script type="application/ld+json">{json.dumps(ld)}</script></head>
<body>{header(cur)}<main id="main">{body}</main>{footer()}<script src="/assets/site.js" defer></script></body></html>'''

def cta(h,p,b1,b2=None):
    s2=f'<a class="btn btn-o" href="/contact/">{b2}</a>' if b2 else ''
    return f'<section class="deep cta"><div class="wrap"><h2>{h}</h2><p class="sub">{p}</p><div class="actions"><a class="btn btn-p" href="/contact/">{b1}</a>{s2}</div></div></section>'

def home():
    icons={'website-design-development': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 9h18M7 7h.01M10 7h.01"/>', 'ecommerce-development': '<path d="M5 7h15l-1.5 8H7L5 4H3"/><circle cx="9" cy="19" r="1.3"/><circle cx="17" cy="19" r="1.3"/>', 'web-application-development': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16M13 9h5M13 13h5"/>', 'custom-software-development': '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>', 'website-maintenance-support': '<path d="M14.5 6.5a4 4 0 0 0-5 5L4 17l3 3 5.5-5.5a4 4 0 0 0 5-5l-2.5 2.5-2-2z"/>'}
    val={'website-design-development': ("A website that doesn't reflect the quality of your business.", 'Professional, responsive websites that build credibility and make it easy for visitors to get in touch.'), 'ecommerce-development': ('Selling online without a clear, manageable store.', 'Online stores to showcase products, take orders and manage your online sales.'), 'web-application-development': ("Manual processes that a standard website or tool can't handle.", 'Custom browser-based applications that automate processes and manage information.'), 'custom-software-development': ("Specialised requirements that off-the-shelf tools don't meet.", 'Purpose-built software designed around your workflows and operational challenges.'), 'website-maintenance-support': ('A website that is neglected after launch.', 'Updates, fixes and improvements that keep your website secure, functional and performing.')}
    cards="".join(f'<article class="card"><svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icons[s]}</svg><h3>{n}</h3><p class="prob">{val[s][0]}</p><p>{val[s][1]}</p><a href="/services/{s}/">Learn more<span class="sr"> about {n}</span> &rarr;</a></article>' for s,n,_ in SERVICES)
    ctasec=cta("Have a project in mind? Let's talk about it.","Tell us what you need and we will discuss a practical way forward. No commitment to enquire.","Start a Conversation","Request a Project Quote")
    return f'''<section class="deep hero"><div class="wrap"><div><h1>Digital Solutions Built Around Your Business.</h1>
<p class="lead">We design and develop professional websites, web applications and practical software that help businesses operate, connect and grow, built around your actual needs.</p>
<div class="actions"><a class="btn btn-p" href="/contact/">Discuss Your Project</a><a class="btn btn-o" href="/services/">Explore Our Services</a></div>
<p class="tag">Based in Nigeria. Working with individuals and businesses worldwide.</p></div>
<div class="mock" role="img" aria-label="Conceptual preview of a modern business website interface">
<div class="mock-top"><span class="mock-dots"><i></i><i></i><i></i></span><span class="mock-url">yourbusiness.com</span><span class="mock-label">WEB EXPERIENCE</span></div>
<div class="mock-body"><div class="mock-copy"><span class="mock-eyebrow">BUILT AROUND YOUR BUSINESS</span><b>Make a stronger first impression.</b><i></i><i></i><em>Explore services <span>↗</span></em></div>
<div class="mock-art"><div class="art-panel"><div class="art-nav"><b></b><span></span><span></span><span></span></div><div class="art-content"><div class="art-lines"><i></i><i></i><i></i></div><div class="art-blocks"><b></b><b></b><b></b></div></div></div><div class="mock-note"><span>01</span><b>Plan. Design. Build.</b></div></div></div>
<p class="cap">Conceptual interface preview — not a client project.</p></div></div></section>
<section class="trust" aria-label="Why clients can rely on us"><div class="wrap"><ul>
<li>Independent and Nigeria-based<span>Open to clients worldwide</span></li>
<li>Direct communication<span>With the person doing the work</span></li>
<li>Agreed scope and quotation<span>Before development begins</span></li>
<li>Remote collaboration<span>Organised, clear, accessible</span></li></ul></div></section>
<section class="paper light"><div class="wrap"><p class="kick">What we build</p><h2>Practical solutions for real business problems.</h2>
<div class="cards">{cards}<div class="card tile"><h3>Not sure what you need?</h3><p>Describe the problem. We will help you work out the right approach, even if that means something simpler.</p><a href="/contact/">Start a conversation &rarr;</a></div></div></div></section>
<section class="light"><div class="wrap split"><div><p class="kick">Why MensaWeb ICT</p><h2>A more direct, considered approach.</h2><div class="actions"><a class="btn btn-o" href="/why-choose-us/">More about how we work with clients</a></div></div>
<ul class="rows" style="border-top-color:#C3CCD7">
<li><div><h3>Direct communication</h3></div><div><p>You deal with the person who plans, builds and delivers your project.</p></div></li>
<li><div><h3>Fair pricing</h3></div><div><p>A lean, independent structure keeps costs reasonable without cutting corners.</p></div></li>
<li><div><h3>Efficient execution</h3></div><div><p>Clear scope and priorities, with no unrealistic promises on turnaround.</p></div></li>
<li><div><h3>Integrity</h3></div><div><p>Honest conversations and respect for every commitment we make.</p></div></li></ul></div></section>
<section class="dark"><div class="wrap"><p class="kick">How we work</p><h2>From first conversation to finished solution.</h2><ol class="steps">
<li><h3>Understand</h3><p>We discuss your requirements, objectives and expectations.</p></li><li><h3>Plan</h3><p>We agree scope, approach, quotation and timeline.</p></li><li><h3>Develop</h3><p>We design and build the agreed solution.</p></li><li><h3>Refine</h3><p>We review, test and make agreed adjustments.</p></li><li><h3>Deliver</h3><p>We complete the project and arrange deployment or handover.</p></li></ol>
<div class="actions"><a class="btn btn-o" href="/how-we-work/">See the full process</a></div></div></section>
'''+ctasec


def contact():
    opts='<option value="">Select a service (optional)</option>'+"".join(f"<option>{n}</option>" for _,n,_ in SERVICES)+"<option>Other / Not Sure Yet</option>"
    return f'''<section class="deep" style="padding-bottom:56px"><div class="wrap"><p class="kick">Contact</p><h1>Tell Us What You're Looking to Build.</h1><p class="lead">Have a website project, an application idea or a digital challenge you would like to solve? We would be pleased to hear from you. Get in touch with MensaWeb ICT, share your requirements and let's discuss how we can help.</p></div></section>
<section><div class="wrap split"><div><h2>Contact information</h2><ul class="bullets"><li><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li><li><strong>Phone:</strong> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li><li><strong>Location:</strong> Nigeria.</li><li><strong>Availability:</strong> Working with individuals and organisations in Nigeria and internationally.</li></ul>
<h3 style="margin-top:32px">Prefer email?</h3><p>You can also contact us directly at <a href="mailto:{EMAIL}" style="text-decoration:underline">{EMAIL}</a>.</p></div>
<div><h2>Let's start with a conversation.</h2><p class="sub" style="margin-bottom:24px">Tell us a little about your project. The more information you provide, the easier it will be for us to understand your requirements and respond appropriately. You do not need to have every detail figured out before getting in touch.</p>
<form id="form" novalidate><div class="hp" aria-hidden="true"><label>Leave blank<input name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="row"><div><label for="name">Full Name *</label><input id="name" name="name" autocomplete="name" required aria-describedby="e-name"><div class="err" id="e-name"></div></div><div><label for="email">Email Address *</label><input id="email" name="email" type="email" autocomplete="email" required aria-describedby="e-email"><div class="err" id="e-email"></div></div></div>
<div class="row"><div><label for="phone">Phone Number (Optional)</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div><div><label for="org">Business or Organisation (Optional)</label><input id="org" name="org" autocomplete="organization"></div></div>
<div class="row"><div><label for="service">Service you are interested in (optional)</label><select id="service" name="service">{opts}</select></div><div><label for="budget">Estimated Project Budget (Optional)</label><input id="budget" name="budget" placeholder="e.g. ₦500,000 or $1,000"></div></div>
<div><label for="message">Project Description *</label><textarea id="message" name="message" required aria-describedby="e-message" placeholder="Describe what you want to build, improve or achieve. Include any important requirements you already have."></textarea><div class="err" id="e-message"></div></div>
<button class="btn btn-p" type="submit" id="send">Send Project Enquiry</button><div id="status" role="status" aria-live="polite"></div>
<p class="fine">Your enquiry will be used to understand your project and respond to your request. We will not ask you to commit to a project simply by making an enquiry.</p></form></div></div></section>
'''+cta("Wherever you are, let's make your next digital project happen.","We welcome enquiries from Nigeria and around the world. Tell us what you need and let's explore the best way forward.","Email Us Directly").replace('href="/contact/">Email Us Directly',f'href="mailto:{EMAIL}">Email Us Directly')

def nf():
    return '<section class="deep" style="min-height:60vh;display:grid;align-items:center"><div class="wrap"><p class="kick">Error 404</p><h1>That page could not be found.</h1><p class="lead">The page may have moved or the address may be mistyped. These links should help.</p><div class="actions"><a class="btn btn-p" href="/">Back to Home</a><a class="btn btn-o" href="/services/">Our Services</a><a class="btn btn-o" href="/contact/">Contact Us</a></div></div></section>'


# ---------- helpers ----------
def crumbs_html(items): return '<p class="crumbs">'+" / ".join(f'<a href="{u}">{n}</a>' for n,u in items[:-1])+(" / " if len(items)>1 else "")+items[-1][0]+'</p>'
def hero(h1,lead,crumbs=None):
    c=crumbs_html(crumbs) if crumbs else ""
    return f'<section class="deep" style="padding-bottom:56px"><div class="wrap">{c}<h1 style="max-width:20ch">{h1}</h1><p class="lead">{lead}</p></div></section>'
def ps(l): return "".join(f"<p>{x}</p>" for x in l)
def ul(l): return '<ul class="bullets">'+"".join(f"<li>{x}</li>" for x in l)+"</ul>"
def block(cls,kick,h2,body): return f'<section class="{cls}"><div class="wrap split">'+f'<div><p class="kick">{kick}</p><h2>{h2}</h2></div><div>{body}</div></div></section>'
def rowlist(cls,kick,h2,items,intro=""):
    r="".join(f"<li><div><h3>{t}</h3></div><div>{ps(p)}</div></li>" for t,p in items)
    return f'<section class="{cls}"><div class="wrap"><p class="kick">{kick}</p><h2>{h2}</h2>{intro}<ul class="rows" style="margin-top:32px">{r}</ul></div></section>'

# ---------- About ----------
def about():
    return hero("Technology Solutions With a More Personal Approach.","Professional digital development built around understanding, collaboration and doing the work properly.",[("Home","/"),("About","/about/")])+\
    block("","Who we are","An independent ICT and digital solutions business.",ps(["MensaWeb ICT is an independent ICT and digital solutions business based in Nigeria, providing website development, application development and related technology services to individuals and organisations locally and internationally.","We help clients establish their online presence, improve existing digital platforms and develop software solutions that address specific needs.","Our approach is centred on a simple idea: technology should be useful, accessible and built with a clear understanding of the people who will depend on it.","We do not believe in recommending complicated solutions where simpler ones will do. Nor do we believe that professional digital development should come at an unnecessarily high cost.","Instead, we focus on understanding the problem, identifying an appropriate solution and executing the work with care and accountability."]))+\
    block("dark","What drives us","Making technology work for real business needs.",ps(["A website should do more than look attractive. It should communicate clearly, represent the business professionally and make it easier for people to engage with it.","An application should do more than provide features. It should solve a genuine problem, improve a process or make an important task easier.","This understanding influences how we approach every project. We consider the purpose behind the technology, the people who will use it and the outcomes the client expects.","Our objective is to develop solutions that are not only technically appropriate but also meaningful and practical."]))+\
    block("paper light","Our independent approach","Direct involvement. Greater accountability. A more focused experience.",ps(["MensaWeb ICT operates independently, allowing us to maintain a direct relationship with clients throughout the project. Rather than introducing unnecessary layers of communication, we keep the relationship straightforward.","You communicate directly with the person responsible for your project, making it easier to discuss requirements, exchange feedback and make decisions.","This operating model also allows us to maintain a lean structure, helping us offer competitive pricing without the additional overheads associated with larger agency operations.","For clients, this means a more personal working relationship and a focused approach to getting things done."]))+\
    rowlist("deep","What we stand for","Four principles we work by.",[("Integrity over empty promises.",["We believe in being honest about what a project requires, what is achievable and what clients should expect."]),("Quality over unnecessary complexity.",["We aim to build solutions that are appropriate, dependable and fit for their intended purpose."]),("Value over inflated costs.",["We work towards making professional digital development accessible through reasonable pricing and efficient operations."]),("Collaboration over guesswork.",["We listen, ask questions and work with clients to ensure that the final solution reflects their requirements."])])+\
    block("","Who we work with","Projects of different shapes and sizes.",ul(["Individuals looking to establish a professional online presence.","Entrepreneurs turning business ideas into digital products.","Startups building their first websites or applications.","Small and medium-sized businesses improving their operations.","Established organisations requiring website development or specialised digital solutions.","Businesses seeking ongoing technical assistance and website improvements."])+"<p style='margin-top:18px'>We welcome projects of different sizes, provided they align with our capabilities and working arrangements.</p>")+\
    cta("Let's build a productive working relationship.","If you value direct communication, reasonable pricing and a responsible approach to technology, we would be pleased to hear about your project.","Get in Touch")

# ---------- Services overview ----------
SVC_DETAIL={
"website-design-development":(["Your website is often one of the first places potential customers encounter your business. It should communicate professionalism, make information easy to find and give visitors a clear understanding of what you offer.","We design and develop websites that combine thoughtful presentation, practical functionality and responsive performance."],"Deliverables may include","Business and corporate websites.|Professional service-based websites.|Personal and portfolio websites.|Startup and landing page websites.|Website redesigns and modernisation.|Responsive layouts.|Content management functionality.|Performance and technical optimisation.","A professional digital presence that helps your business communicate with confidence and connect with its audience."),
"ecommerce-development":(["Take your products and services online with an e-commerce platform designed around your business model.","We develop online stores that make it easier for customers to explore products, place orders and interact with your business."],"Features may include","Online store design.|Product catalogues.|Shopping cart and checkout.|Payment gateway integration, subject to provider availability.|Order management.|Customer accounts.|Shipping configuration.|Store administration.","A convenient online shopping experience and a structured platform for managing online sales."),
"web-application-development":(["When a standard website is not enough, a custom web application can provide the functionality your business actually needs."],"Potential solutions include","Customer portals.|Administrative dashboards.|Booking systems.|Inventory management.|Business management applications.|Membership platforms.|Reporting systems.|Workflow automation.","A digital application designed around your requirements rather than forcing your operations into a generic solution."),
"custom-software-development":(["Some business requirements call for specialised software that goes beyond conventional websites and standard applications."],"Potential solutions include","Specialised business applications.|Internal operational tools.|Data management systems.|Business process automation.|Software integrations.|Custom application features.|Purpose-built digital tools.","Software that addresses specific requirements and supports the way your organisation works."),
"website-maintenance-support":(["A website needs attention after launch."],"Support may include","Website updates.|Content and image changes.|Bug investigation and fixes.|Plugin and software updates.|Backup configuration and checks.|Performance optimisation.|Technical troubleshooting.|Ongoing development assistance.","Continued technical attention that helps protect your investment and keep your website useful.")}
def services():
    out=hero("Digital Services Designed Around What You Need.","From professional business websites to custom applications, we provide practical technology solutions that help individuals and organisations establish, improve and manage their digital operations. Whether you have a clearly defined project or need help determining the right approach, we are ready to have the conversation.",[("Home","/"),("Services","/services/")])
    for i,(s,n,_) in enumerate(SERVICES):
        p,lab,items,ben=SVC_DETAIL[s]; dark=i%2==0
        body=ps(p)+f"<h3 style='margin-top:22px'>{lab}</h3>"+ul(items.split("|"))+f'<p class="benefit"><strong>Benefit:</strong> {ben}</p><div class="actions"><a class="btn btn-o" href="/services/{s}/">Explore {n}</a></div>'
        cls="dark" if dark else "paper light"
        out+=f'<section class="{cls}"><div class="wrap split{" rev" if i%2 else ""}"><div><p class="kick">0{i+1}</p><h2>{n}</h2></div><div>{body}</div></div></section>'
    return out+cta("Let's find the right solution for your project.","Every project begins with understanding what you need. Start a conversation with MensaWeb ICT and let's explore the possibilities.","Discuss Your Project")

# ---------- How we work ----------
STAGES=[("Initial conversation","First, we listen.",["Every successful project begins with understanding what the client needs.","We invite you to explain your idea, business objectives, challenges and expectations.","You do not need to have all the technical details figured out. We can help clarify the requirements through discussion."]),
("Requirements and project scope","Establishing what needs to be done.",["Once we understand the general requirements, we work towards defining the project's scope.","This includes identifying the required features, functionality, deliverables and relevant technical considerations.","A clear scope helps both parties understand what the project involves and reduces the possibility of misunderstandings."]),
("Proposal and agreement","Clear expectations before development begins.",["We provide a quotation or proposal based on the agreed requirements.","The proposed arrangement should establish the work involved, expected deliverables, estimated timeline and relevant payment terms.","Development begins once the necessary details have been discussed and agreed upon."]),
("Design and development","Turning requirements into a working solution.",["We work through the agreed design and functionality, keeping the project aligned with its objectives.","Communication remains important throughout this stage, and we provide opportunities for review at appropriate milestones."]),
("Feedback, testing and refinement","Reviewing the details before delivery.",["We review the developed solution, test relevant functionality and address agreed adjustments.","Your feedback helps us identify areas requiring clarification or refinement.","Any changes outside the original agreed scope can be discussed and assessed separately."]),
("Delivery and deployment","Completing the project and preparing it for use.",["Once the agreed requirements have been completed and reviewed, we arrange the appropriate deployment, handover or delivery.","The specific handover arrangements depend on the nature of the project."]),
("Ongoing support","Support beyond the initial delivery.",["Where required, we can discuss ongoing maintenance, technical assistance and further improvements.","This provides an opportunity to continue developing your digital platform as your requirements change."])]
def how():
    tl="".join(f'<li><span class="n">Stage {i+1}</span><h2 class="st">{t}</h2><h3 class="tg">{h}</h3>{ps(p)}</li>' for i,(t,h,p) in enumerate(STAGES))
    return hero("A Clear Process. Direct Communication. Work Done Properly.","We believe technology projects should be organised, transparent and collaborative. Our process is designed to make working with MensaWeb ICT straightforward, from the initial conversation to final delivery.",[("Home","/"),("How We Work","/how-we-work/")]).replace('class="deep"','class="deep"',1)+\
    f'<section class="deep" style="padding-top:40px"><div class="wrap"><ol class="tl">{tl}</ol></div></section>'+\
    block("paper light","Our commitment","Our commitment throughout the process.",ul(["Clear and respectful communication.","Agreed project expectations.","Responsible handling of requirements.","Constructive collaboration.","Efficient execution.","Accountability for agreed deliverables."]))+\
    cta("Have a project you would like to get started?","Tell us what you have in mind and let's take the first step.","Start a Conversation")

# ---------- Why choose us ----------
WHY=[("Direct access to the person handling your project",["You communicate directly with the person responsible for your project's development.","This makes it easier to discuss ideas, clarify requirements, exchange feedback and make decisions without unnecessary communication layers."]),
("Competitive and reasonable pricing",["We operate with a focused, independent structure. This helps us maintain competitive pricing without the additional overheads that can accompany larger agency operations.","Our focus is on providing genuine value rather than competing solely on the lowest price."]),
("Personal attention",["Your project is not simply another item moving through a large production system.","We take the time to understand its purpose, requirements and expected outcomes."]),
("A commitment to agreed deliverables",["We believe professional relationships depend on clear expectations.","We work to establish what is included in a project before development begins and remain focused on delivering the agreed requirements."]),
("Efficient execution",["A focused working structure allows us to approach projects without unnecessary complexity.","We plan around the agreed scope, prioritise important requirements and work towards efficient delivery. We do not promise unrealistic turnaround times."]),
("Solutions built around your needs",["Every business has different requirements. We avoid assuming that one standard solution is suitable for everyone.","Instead, we consider your objectives and recommend an approach appropriate to the actual problem."]),
("Flexible collaboration",["We welcome input from clients throughout the development process.","Whether you have a detailed specification or only an initial idea, we are prepared to discuss your requirements and work towards defining a suitable solution."]),
("Accessible from anywhere",["Although based in Nigeria, MensaWeb ICT works with clients internationally.","Remote communication and organised project coordination make it possible to collaborate across different locations."])]
def why():
    return hero("Professional Technology Services. Without Unnecessary Complexity.","Finding the right technology partner is about more than technical ability. You need someone who listens, understands your requirements, communicates clearly and takes responsibility for the work. That is the approach we bring to MensaWeb ICT.",[("Home","/"),("Why Choose Us","/why-choose-us/")])+\
    rowlist("paper light","Eight reasons","What working with us looks like.",WHY)+\
    cta("The right technology partner makes a difference.","If our approach aligns with what you expect from a professional working relationship, let's discuss your project.","Work With MensaWeb ICT")

# ---------- FAQ ----------
FAQ=[("General questions",[("What types of projects does MensaWeb ICT handle?",["We work on a range of digital projects, including business websites, corporate websites, e-commerce platforms, custom web applications, specialised software solutions, website redesigns and ongoing website maintenance.","If you have a specific requirement that is not listed, you are welcome to contact us to discuss it."]),("Do you work with international clients?",["Yes. MensaWeb ICT is based in Nigeria but welcomes projects from individuals and organisations in other countries.","We use remote communication and collaboration to discuss requirements, coordinate development and manage projects across geographical boundaries."]),("Can I hire you to build a custom web application?",["Yes. We undertake custom web application projects based on defined requirements.","Examples include booking platforms, customer portals, management dashboards, inventory systems and workflow applications. The scope and technical approach depend on the functionality required."]),("Do you work with individuals and small businesses?",["Yes. Our services are available to individuals, entrepreneurs, startups, small businesses and established organisations."])]),
("Pricing and timelines",[("How much does website development cost?",["The cost depends on the type of website, number of pages, design requirements, functionality, integrations and overall project complexity.","A straightforward business website will generally require a different investment from a large corporate platform or an e-commerce website. Contact us with your requirements for a project-specific quotation."]),("How long does a typical website project take?",["The timeline depends on the project's size, complexity, content readiness and required functionality.","A relatively straightforward website may take considerably less time than a complex e-commerce platform or custom application. We discuss estimated timelines during the planning stage before development begins."]),("Do you require an upfront payment?",["Payment arrangements are discussed and agreed upon before development starts.","Depending on the project, payments may be structured around an initial payment and agreed development milestones. The specific arrangement will be communicated in the project proposal or agreement."]),("Are domain registration and hosting included?",["Domain registration and hosting can be discussed as part of your project requirements.","Whether these services are included in a quotation depends on the agreed scope and the hosting arrangements selected."])]),
("Development and collaboration",[("Can I request changes during development?",["Yes. Client feedback is an important part of our process. We provide opportunities to review the work and request adjustments at appropriate stages.","Changes that fall within the agreed scope are handled as part of the project. Significant additions or changes to the original requirements may require a revised quotation or timeline."]),("Will my website work on mobile phones?",["Responsive design is considered an important part of modern website development.","Websites are developed with appropriate layouts for mobile phones, tablets and desktop devices, depending on the project requirements."]),("Will I be able to update my website myself?",["Where appropriate, we can develop websites with content management functionality that allows clients to make selected updates without requiring technical assistance.","The exact level of control depends on the website's platform and agreed functionality."]),("Do you provide website redesign services?",["Yes. We can help modernise existing websites by improving their presentation, navigation, responsiveness, functionality and overall user experience.","The first step is reviewing your current website and understanding what you would like to improve."]),("Do you provide maintenance after completing a project?",["Yes. We offer website maintenance and technical support arrangements that can be discussed according to your needs.","The nature and frequency of support are agreed separately based on the website and the services required."])]),
("Getting started",[("How do I get started?",["Simply contact us through the website enquiry form or email mensaweb@mensaweb.com.","Tell us what you need, and we will discuss your requirements and the appropriate next steps."]),("What if I have an idea but no technical knowledge?",["That is perfectly fine. You do not need to know how to build a website or develop software to discuss your idea.","Explain the problem you want to solve or the outcome you want to achieve. We can help explore the technical requirements and possible approaches."]),("Can you improve an existing application or website?",["Yes. We can discuss existing websites and applications that need redesigning, additional functionality, troubleshooting or technical improvements.","The project will first need to be assessed to understand its current condition and requirements."]),("How do we communicate during an international project?",["Communication arrangements are agreed at the beginning of the project.","Email and other suitable online communication channels can be used to discuss requirements, share progress and coordinate feedback."]),("Do I have to commit to anything when requesting a quotation?",["No. Making an enquiry allows us to understand your requirements and discuss a possible project.","Any actual development work begins only after the project scope, quotation and relevant terms have been discussed and agreed upon."])])]
def faq():
    out=hero("Frequently Asked Questions","Answers to common questions about our services, pricing, process and working arrangements.",[("Home","/"),("FAQ","/faq/")])
    out+='<section class="paper light"><div class="wrap">'
    for cat,qs in FAQ:
        out+=f'<h2 style="margin-top:44px;font-size:1.5rem">{cat}</h2><div class="faq">'+"".join(f'<details><summary>{q}</summary><div class="a">{ps(a)}</div></details>' for q,a in qs)+'</div>'
    return out+'</div></section>'+cta("Still have a question?","We are happy to discuss your requirements and clarify anything you would like to know before starting a project.","Contact MensaWeb ICT")
def faq_ld():
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":" ".join(a)}} for _,qs in FAQ for q,a in qs]}

# ---------- Individual service pages ----------
def R(*pairs): return [(t,[d]) for t,d in pairs]
SP={}
SP["website-design-development"]=dict(h1="Websites That Represent Your Business Properly.",
 lead="A professional website should do more than occupy a space on the internet. It should communicate your value, build confidence and make it easy for visitors to take the next step. We design and develop modern, responsive websites for individuals, businesses and organisations looking for a credible and effective online presence.",
 title="Website Design & Development Services | MensaWeb ICT",
 desc="Professional, responsive business, portfolio and landing page websites, plus redesigns, from MensaWeb ICT. Built around your audience and goals.",
 secs=[("paras","A website built with purpose","Your website plays an important role in how people perceive your business.",["Visitors often form an impression of your business from the first few moments on your website.","An outdated design, confusing navigation or poorly presented information can make it harder for visitors to understand what you offer.","We approach website development by considering your business, audience, objectives and the experience you want visitors to have.","The result should be a website that looks professional, communicates clearly and supports your objectives."]),
 ("rows","What we develop","Websites for different needs.",R(("Business and corporate websites","Professional websites for businesses that need to present their services, establish credibility and communicate with customers and stakeholders."),("Small business websites","Practical, attractive websites that help smaller businesses compete online without unnecessary complexity."),("Portfolio and personal websites","Well-structured websites for professionals, creatives and individuals who want to showcase their work, experience or services."),("Landing pages","Focused web pages designed around a specific service, product, campaign or conversion objective."),("Website redesigns","Modernisation of existing websites to improve their presentation, usability, responsiveness and overall functionality."))),
 ("bullets","What your website can include","Features, defined by your project scope.",["Customised visual design.","Mobile-responsive layouts.","Clear navigation.","Contact forms.","Service and product presentation.","Search engine optimisation foundations.","Social media integration.","Content management capabilities.","Performance optimisation.","Relevant third-party integrations.","<em>All features are discussed and defined according to the project scope.</em>"]),
 ("paras","Our development approach","Understand first, then design and build.",["We begin by understanding your business and what you expect your website to accomplish.","We then establish the structure, content requirements and design direction before moving into development.","Throughout the process, we encourage feedback and review so that the finished website reflects your expectations and agreed requirements.","Before delivery, we check the website's functionality, presentation and responsiveness."]),
 ("bullets","Who is this service for?","Who benefits most.",["Businesses establishing their first website.","Organisations improving existing websites.","Entrepreneurs launching new ventures.","Professionals building a personal brand.","Companies seeking a more credible online presence."])],
 cta=("Your next customer could be looking for you online.","Give your business a professional platform that communicates what you do and makes it easier for people to connect with you.","Start Your Website Project"))
SP["ecommerce-development"]=dict(h1="Take Your Business Beyond the Traditional Storefront.",
 lead="Reach customers online with an e-commerce website designed to showcase your products, simplify ordering and support your business operations. We develop online stores that combine professional presentation with practical shopping and management functionality.",
 title="E-commerce Website Development | MensaWeb ICT",
 desc="Online stores with product catalogues, checkout, payment integration and order management, built around your business model by MensaWeb ICT.",
 secs=[("paras","Sell online with greater convenience","An effective online store should make shopping straightforward.",["A successful store needs to make the buying journey simple for customers while giving owners practical tools to manage the business behind it.","Customers should be able to discover products, understand their options, place orders and complete purchases without unnecessary complications.","At the same time, business owners need a manageable way to maintain products, monitor orders and administer their store.","We develop e-commerce solutions with both experiences in mind."]),
 ("rows","E-commerce functionality","What your store can do.",R(("Product management","Organise products, descriptions, images, categories, variations and pricing."),("Shopping cart and checkout","Give customers a structured process for reviewing purchases and completing orders."),("Payment integration","Integrate supported payment gateways according to your target market, business requirements and provider availability."),("Order management","Manage incoming orders and monitor their status through the store administration system."),("Customer accounts","Provide account functionality where appropriate."),("Delivery configuration","Set up shipping and delivery options according to your operational arrangements."),("Store administration","Manage important aspects of your online store through an accessible administration interface."))),
 ("paras","Built around your business model","Not every online store operates in the same way.",["The structure of an online store should reflect what it sells and how it fulfils orders.","A fashion retailer may require product variations and size options. An electronics store may need detailed specifications. A wholesale business may require different pricing arrangements.","We consider these differences when planning your store."]),
 ("bullets","Who can benefit?","Stores for different kinds of business.",["Retail businesses.","Fashion and clothing brands.","Electronics and accessories sellers.","Beauty and lifestyle businesses.","Manufacturers and distributors.","Entrepreneurs launching online stores.","Existing retailers expanding into online sales."])],
 cta=("Ready to make your products available online?","Let's discuss your products, customers and business requirements and develop an online store that makes sense for your operation.","Request an E-commerce Quote"))
SP["web-application-development"]=dict(h1="Custom Web Applications for the Way Your Business Works.",
 lead="When standard websites and off-the-shelf tools cannot meet your requirements, a custom web application can provide a more suitable solution. We develop browser-based applications designed to solve specific problems, improve workflows and make business processes more manageable.",
 title="Custom Web Application Development | MensaWeb ICT",
 desc="Custom portals, dashboards, booking and inventory systems and workflow applications built around your requirements by MensaWeb ICT.",
 secs=[("paras","More than a conventional website","A website presents information. A web application lets users act.",["A website primarily presents information and enables communication.","A web application goes further by allowing users to interact with data, perform tasks, manage information and access specialised functionality through a browser."]),
 ("rows","What we can build","Applications for specific problems.",R(("Business management platforms","Applications that bring selected business operations and information together in one accessible system."),("Customer portals","Private online spaces where customers can access information, manage accounts or interact with your services."),("Booking and reservation systems","Applications that allow users to view availability, submit bookings and manage appointments."),("Inventory management systems","Tools for recording, monitoring and managing stock and related information."),("Administrative dashboards","Centralised interfaces for viewing important information, managing users and performing administrative tasks."),("Membership platforms","Systems that support registration, user accounts, restricted content and membership-related functionality."),("Workflow applications","Custom tools that organise processes, automate selected tasks and reduce repetitive administrative work."))),
 ("bullets","Our development considerations","Every application begins with a clear understanding of its purpose.",["Who will use the application?","What tasks should it perform?","What information needs to be stored?","What different user roles are required?","What existing systems need to connect to it?","What level of security and access control is appropriate?","How should the application grow as requirements evolve?"]),
 ("paras","A collaborative development process","Refining ideas as the project takes shape.",["Custom application development often involves refining ideas as the project takes shape.","We work with clients to establish requirements, agree on functionality and review the application at appropriate stages."])],
 cta=("Have an application idea that needs a technical partner?","Tell us what you want the application to accomplish. We can discuss the requirements and explore an appropriate development approach.","Discuss Your Web Application"))
SP["custom-software-development"]=dict(h1="Software Designed Around Your Specific Requirements.",
 lead="Not every business challenge has an off-the-shelf solution. When standard tools do not provide the functionality or flexibility you need, custom software can offer a more appropriate way forward. MensaWeb ICT helps clients explore and develop specialised software and application solutions based on defined requirements.",
 title="Custom Software Development Services | MensaWeb ICT",
 desc="Internal tools, data systems, workflow automation and integrations built around defined requirements. Custom software from MensaWeb ICT.",
 secs=[("paras","Software that addresses real operational needs","Technology for an identifiable need.",["Businesses often develop processes around their unique products, services and ways of working.","As operations become more complex, existing tools may become insufficient.","Custom software can help by providing functionality specifically designed around those processes.","The objective is not to introduce technology for its own sake. It is to develop a practical solution that addresses an identifiable need."]),
 ("bullets","Areas of custom development","Where custom software can help.",["Internal business management tools.","Data processing and management applications.","Automated business workflows.","Customer and administrative systems.","Custom reporting solutions.","Third-party system integrations.","Specialised application functionality.","Bespoke digital platforms."]),
 ("rows","How we approach custom software projects","Five steps from problem to delivery.",R(("Understand the problem","We first examine the operational challenge or requirement the software is expected to address."),("Define the requirements","We identify the essential features, users, workflows and technical considerations."),("Establish the scope","We agree on what the solution should include, how it should function and what constitutes successful delivery."),("Develop and refine","We build the agreed functionality and review progress with client input."),("Test and deliver","We assess the solution against its requirements before arranging deployment or handover."))),
 ("paras","Is custom software right for your business?","Custom development is not always necessary.",["A bespoke solution is not automatically the best solution for every problem.","Sometimes an existing platform, a simpler web application or a configuration of available tools will provide better value.","We believe in discussing the actual requirements before recommending a development approach."])],
 cta=("Let's explore what the right software could do for your business.","Share your requirements with us and let's discuss a practical way to approach your project.","Request a Software Consultation"))
SP["website-maintenance-support"]=dict(h1="Your Website Needs Attention Beyond Launch Day.",
 lead="Keep your website updated, functional and aligned with your business needs through ongoing technical maintenance and support. We help clients maintain and improve their websites through practical technical assistance and agreed support arrangements.",
 title="Website Maintenance & Technical Support | MensaWeb ICT",
 desc="Website updates, troubleshooting, software updates, backups, performance and security-related maintenance from MensaWeb ICT.",
 secs=[("paras","Why ongoing website maintenance matters","A website is not a finished product.",["A website is not a finished product that should be ignored after launch.","Content changes, software updates, technical issues and evolving business requirements can all affect how a website functions over time.","Regular maintenance helps identify problems, maintain compatibility and keep your website aligned with its intended purpose."]),
 ("rows","Our maintenance and support services","What support can cover.",R(("Website updates","Make agreed content, image, page and functionality changes."),("Technical troubleshooting","Investigate website errors, unexpected behaviour and technical problems."),("Software and plugin updates","Assist with relevant updates to the website's underlying software and extensions."),("Backup assistance","Configure or review backup arrangements to support recovery where needed."),("Performance improvements","Identify opportunities to improve loading performance and overall website efficiency."),("Security-related maintenance","Assist with appropriate security updates and routine technical checks."),("Ongoing improvements","Make agreed changes as your business requirements evolve."))),
 ("paras","Flexible support arrangements","Different websites need different levels of attention.",["Different websites require different levels of attention.","Some clients need occasional technical assistance, while others require more regular maintenance.","We can discuss the nature of your website, your support requirements and an appropriate arrangement before work begins."])],
 cta=("Need someone dependable to look after your website?","Tell us about your existing website and the type of assistance you require.","Request Technical Support"))

def service_page(slug):
    d=SP[slug]; name=[n for s,n,_ in SERVICES if s==slug][0]
    out=hero(d["h1"],d["lead"],[("Home","/"),("Services","/services/"),(name,f"/services/{slug}/")])
    cyc=["light","dark","paper light"]
    for i,(typ,kick,h2,c) in enumerate(d["secs"]):
        cls=cyc[i%3]
        if typ=="paras": out+=block(cls,kick,h2,ps(c))
        elif typ=="bullets": out+=block(cls,kick,h2,ul(c))
        else: out+=rowlist(cls,kick,h2,c)
    rel="".join(f'<li><a href="/services/{s}/" style="text-decoration:underline">{n}</a></li>' for s,n,_ in SERVICES if s!=slug)
    out+=block("deep","Related services","Other ways we can help.",f'<ul class="bullets">{rel}</ul>')
    return out+cta(*d["cta"])
SCHEMAS={}
for _s,_n,_d in SERVICES:
    SCHEMAS["services/"+_s]={"@context":"https://schema.org","@type":"Service","name":_n,"description":_d,"url":f"{SITE}/services/{_s}/","provider":{"@type":"Organization","name":"MensaWeb ICT","url":SITE+"/"},"areaServed":"Worldwide"}

# ---------- output modes ----------
# default (portable): relative links to .../index.html and CSS/JS inlined, so pages work from file://, any host, any subfolder.
# `python3 build.py --clean`: root-absolute clean URLs + external assets, for hosting at the domain root (production).
import sys, re as _re
CLEAN="--clean" in sys.argv
_page=page
def page(slug,*a,**k):
    html=_page(slug,*a,**k)
    if CLEAN: return html
    root_dir=os.path.dirname(os.path.abspath(__file__))
    css=open(root_dir+"/assets/style.css",encoding="utf-8").read(); js=open(root_dir+"/assets/site.js",encoding="utf-8").read()
    html=html.replace('<link rel="stylesheet" href="/assets/style.css">',"<style>"+css+"</style>")
    html=html.replace('<script src="/assets/site.js" defer></script>',"<script>"+js+"</script>")
    if slug=="404": return html   # 404 is served from arbitrary paths, keep root-absolute links
    depth=slug.count("/")+1 if slug else 0
    pre="../"*depth
    def fix(m):
        p=m.group(2)
        t="index.html" if p=="/" else p[1:]+("index.html" if p.endswith("/") else "")
        return f'{m.group(1)}="{pre}{t}"'
    return _re.sub(r'(href|src)="(/(?!/)[^"]*)"',fix,html)

PAGES=[("", "MensaWeb ICT | Website & Software Development","MensaWeb ICT is an independent Nigeria-based provider of website development, web applications and practical software solutions for clients worldwide.",home(),"/",None),
("about","About MensaWeb ICT | Independent Technology Solutions","Learn about MensaWeb ICT, an independent Nigeria-based technology provider offering direct collaboration, fair pricing and dependable execution.",about(),"/about/",[("Home","/"),("About","/about/")]),
("services","Our Services | Website, E-commerce & Software Development","Website design, e-commerce, web applications, custom software and website maintenance from MensaWeb ICT, built around what your business needs.",services(),"/services/",[("Home","/"),("Services","/services/")]),
("how-we-work","Our Development Process | MensaWeb ICT","See how MensaWeb ICT works, from the first conversation and scoping through development, testing, delivery and ongoing support.",how(),"/how-we-work/",[("Home","/"),("How We Work","/how-we-work/")]),
("why-choose-us","Why Choose MensaWeb ICT | Professional Digital Solutions","Direct communication, personal attention and fair pricing. See why clients in Nigeria and abroad choose MensaWeb ICT for digital projects.",why(),"/why-choose-us/",[("Home","/"),("Why Choose Us","/why-choose-us/")]),
("faq","Frequently Asked Questions | MensaWeb ICT","Answers about MensaWeb ICT services, international projects, pricing, timelines, changes, maintenance, hosting, payment and getting started.",faq(),"/faq/",[("Home","/"),("FAQ","/faq/")]),
("contact","Contact MensaWeb ICT | Discuss Your Project","Contact MensaWeb ICT to discuss a website, e-commerce, web application or software project. Enquiries welcome from Nigeria and worldwide.",contact(),"/contact/",[("Home","/"),("Contact","/contact/")])]
for _s,_n,_d in SERVICES:
    PAGES.append(("services/"+_s,SP[_s]["title"],SP[_s]["desc"],service_page(_s),"/services/",[("Home","/"),("Services","/services/"),(_n,f"/services/{_s}/")]))
root=os.path.dirname(os.path.abspath(__file__))
def w(path,txt):
    os.makedirs(os.path.dirname(path),exist_ok=True);open(path,"w",encoding="utf-8").write(txt)
for slug,t,d,b,cur,cr in PAGES: w(f"{root}/{slug}/index.html" if slug else f"{root}/index.html",page(slug,t,d,b,cur,crumbs=cr,schema=faq_ld() if slug=='faq' else SCHEMAS.get(slug)))
w(f"{root}/404.html",page("404","Page Not Found | MensaWeb ICT","The page you were looking for could not be found.",nf(),noindex=True))
slugs=[p[0] for p in PAGES]
w(f"{root}/sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}/{s+'/' if s else ''}</loc></url>" for s in slugs)+"</urlset>")
w(f"{root}/robots.txt",f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("built",len(PAGES)+1,"pages")
