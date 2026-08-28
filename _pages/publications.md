---
layout: single
title: "Publications"
permalink: /publications/
description: "Browse publications by CJ Calabrese on health communication, digital media, misinformation, persuasion, and artificial intelligence."
author_profile: false
---

<div class="publications-page">
<div class="page-hero">
  <p class="page-label">Research Output</p>
  <h1>Publications</h1>

  <p class="page-intro">
    My research reflects a theory-driven research program examining the processes through which communication interventions influence human behavior and decision-making in digital information environments. I use multiple methods, such as experiments, surveys, and computational methods, across health and science contexts.</p>

<p class="page-intro">

    Below is a chronological list of peer-reviewed publications.
  </p>

</div>

<div class="page-section">

  {% assign current_year = "" %}

  {% for pub in site.data.publications %}

    {% unless pub.year == current_year %}
      {% assign current_year = pub.year %}
      <h2 class="pub-year">{{ current_year }}</h2>
    {% endunless %}

    <article class="publication">
      <h3 class="publication-title">{{ pub.title }}</h3>


      <div class="publication-meta">
        <span class="publication-journal">{{ pub.venue }}</span>

        {% if pub.url %}
          <a href="{{ pub.url }}" target="_blank" rel="noopener">Read Article →</a>
        {% endif %}
      </div>

      <p class="publication-authors">
        {{ pub.authors | replace: "Calabrese, C.", "<strong>Calabrese, C.</strong>" }}
      </p>
    </article>

  {% endfor %}

</div>
</div>