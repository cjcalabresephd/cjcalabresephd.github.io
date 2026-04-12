---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign pubs_by_year = site.publications | sort: 'date' | reverse %}

{% for pub in pubs_by_year %}
<div class="pub-card">
  <div class="pub-year">{{ pub.date | date: "%Y" }}</div>
  <div class="pub-title"><a href="{{ pub.permalink }}">{{ pub.title }}</a></div>
  {% if pub.venue %}<div class="pub-journal">{{ pub.venue }}</div>{% endif %}
  {% if pub.citation %}<div class="pub-authors">{{ pub.citation | truncatewords: 12 }}</div>{% endif %}
  {% if pub.paperurl %}<a class="pub-doi" href="{{ pub.paperurl }}">DOI</a>{% endif %}
</div>
{% endfor %}
