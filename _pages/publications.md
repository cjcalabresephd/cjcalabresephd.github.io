---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign pubs_by_year = site.publications | sort: 'date' | reverse %}

{% assign current_year = nil %}

{% for pub in pubs_by_year %}
  {% assign year = pub.date | date: "%Y" %}

  {% if year != current_year %}
    {% assign current_year = year %}
    <h2 class="archive__subtitle">{{ current_year }}</h2>
  {% endif %}

  <div class="list__item">
    <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
      
      <h3 class="archive__item-title" itemprop="headline">
        <a href="{{ pub.permalink }}" rel="permalink">{{ pub.title }}</a>
      </h3>

      {% if pub.venue %}
        <p class="archive__item-excerpt">{{ pub.venue }}</p>
      {% endif %}

      {% if pub.citation %}
        <p class="archive__item-excerpt">
          {{ pub.citation | truncatewords: 20 }}
        </p>
      {% endif %}

      {% if pub.paperurl %}
        <p>
          <a href="{{ pub.paperurl }}">DOI</a>
        </p>
      {% endif %}

    </article>
  </div>
{% endfor %}
