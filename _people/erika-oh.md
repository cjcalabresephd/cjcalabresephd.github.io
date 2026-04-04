---

name: Yoo Jung (Erika) Oh, PhD
lastname: Oh
role: External Collaborator
affiliation: Michigan State University
image: /images/lab/erikaoh.jpg
scholar: https://scholar.google.com/citations?user=kZAz0c8AAAAJ&hl=en
website: https://comartsci.msu.edu/our-people/yoo-jung-erika-oh
alumni: false
layout: single

---

Dr. Oh specializes in artificial intelligence (AI) dialogue systems, commonly referred to as AI chatbots.



## Publications

{% assign mypubs = site.publications 
   | where_exp:"item","item.authors contains 'erika-oh'" %}

### Journal Articles

{% assign journal = mypubs 
   | where:"category","journal" 
   | sort:"date" 
   | reverse %}

{% for post in journal %}
  {% include archive-single.html %}
{% endfor %}

---
