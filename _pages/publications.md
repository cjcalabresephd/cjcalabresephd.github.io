---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign pubs_by_year = site.publications | sort: 'date' | reverse %}

{% assign current_year = "" %}

{% for pub in pubs_by_year %}
  {% assign pub_year = pub.date | date: "%Y" %}

  {% if pub_year != current_year %}
    {% unless forloop.first %}</div>{% endunless %}
    <h2 class="pub-year-heading">{{ pub_year }}</h2>
    <div class="pub-year-group">
    {% assign current_year = pub_year %}
  {% endif %}

  <div class="pub-card">
    <div class="pub-title">
      <a href="{{ pub.permalink }}">{{ pub.title }}</a>
    </div>
    {% if pub.venue %}
      <div class="pub-journal">{{ pub.venue }}</div>
    {% endif %}
    {% if pub.citation %}
      <div class="pub-authors">{{ pub.citation | truncatewords: 12 }}</div>
    {% endif %}
    {% if pub.paperurl %}
      <a class="pub-doi" href="{{ pub.paperurl }}">DOI</a>
    {% endif %}
  </div>

  {% if forloop.last %}
    </div>
  {% endif %}
{% endfor %}
