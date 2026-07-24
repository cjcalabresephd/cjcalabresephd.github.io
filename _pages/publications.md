---
layout: single
title: "Publications"
permalink: /publications/
author_profile: false
---

<div class="publications-page">
<div class="page-hero">
  <p class="page-label">Research Output</p>
  <h1>Publications</h1>
  <div class="page-intro">
    My research examines communication interventions, digital information environments, and health decision-making. Below is a selected list of peer-reviewed publications.
  </div>

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