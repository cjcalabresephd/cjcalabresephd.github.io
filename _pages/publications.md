---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## Journal Articles

{% assign pubs = site.publications | where:"category","journal" %}
{% for post in pubs %}
  {% include archive-single.html %}
{% endfor %}

---

## Articles in Progress

{% assign pubs = site.publications | where:"category","inprogress" %}
{% for post in pubs %}
  {% include archive-single.html %}
{% endfor %}
