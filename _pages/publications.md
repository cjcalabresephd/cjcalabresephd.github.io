---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## Journal Articles
{% assign journal = site.publications 
  | where: "category", "journal" 
  | sort: "date" 
  | reverse %}
{% for post in journal %}
  {% include archive-single.html show_excerpt=false %}
{% endfor %}
---
