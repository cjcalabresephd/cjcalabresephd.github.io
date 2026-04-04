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
  {% include archive-single.html %}
{% endfor %}

---

## Articles in Review

{% assign review = site.publications 
  | where: "category", "review" 
  | sort: "date" 
  | reverse %}

{% for post in review %}
  {% include archive-single.html %}
{% endfor %}

---

## Articles in Progress

{% assign progress = site.publications 
  | where: "category", "inprogress" 
  | sort: "date" 
  | reverse %}

{% for post in progress %}
  {% include archive-single.html %}
{% endfor %}
