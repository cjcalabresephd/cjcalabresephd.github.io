---

name: Emma G. Cox
lastname: Cox
role: External Collaborator
affiliation: Cornell University
image: /images/lab/emmacox.jpg
scholar: https://scholar.google.com/citations?user=iHTKCOsAAAAJ&hl=en
website: https://cals.cornell.edu/people/emma-cox 
alumni: true
layout: single

---

Emma is a PhD student at Cornell University focusing on media effects, persuasion, and health communication.


## Publications

{% assign mypubs = site.publications 
   | where_exp:"item","item.authors contains 'emma-cox'" %}

### Journal Articles

{% assign journal = mypubs 
   | where:"category","journal" 
   | sort:"date" 
   | reverse %}

{% for post in journal %}
  {% include archive-single.html %}
{% endfor %}

---
