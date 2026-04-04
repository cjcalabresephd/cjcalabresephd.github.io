---

name: Muhammad Ehab Rasul, PhD
lastname: Rasul
role: External Collaborator
affiliation: National University of Singapore
image: /images/lab/muhammadrasul.jpg
scholar: https://scholar.google.com/citations?user=cuvLPmQAAAAJ&hl=en
alumni: false
layout: single

---

Dr. Rasul's research lies at the intersection of digital and new media, political communication, mis/disinformation, and media effects.


## Publications

{% assign mypubs = site.publications 
   | where_exp:"item","item.authors contains 'muhammad-rasul'" %}

### Journal Articles

{% assign journal = mypubs 
   | where:"category","journal" 
   | sort:"date" 
   | reverse %}

{% for post in journal %}
  {% include archive-single.html %}
{% endfor %}

---

