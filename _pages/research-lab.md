---
title: "Research Lab"
permalink: /research-lab/
layout: single
---

Welcome to the **Health Communication and Digital Innovation Research Group** at Clemson University. Our research focuses on how media messaging and persuasive technologies influence human behavior, particularly in health contexts.

---

{% assign roles = "Faculty Collaborator,External Collaborator,Masters Student" | split: "," %}

{% for role in roles %}

{% if role == "Faculty Collaborator" %}
## Faculty Collaborators
{% elsif role == "External Collaborator" %}
## External Collaborators
{% elsif role == "Masters Student" %}
## Master's Students
{% endif %}

<div class="lab-grid">

{% assign sorted_people = site.people | sort: "lastname" %}
{% for person in sorted_people %}
{% if person.role == role and person.alumni != true %}

<div class="lab-card">

<a href="{{ person.url }}">
<img src="{{ person.image }}" alt="{{ person.name }}">
</a>

<h3><a href="{{ person.url }}">{{ person.name }}</a></h3>

<p class="lab-role">{{ person.role }}</p>

{% if person.affiliation %}
<p class="lab-affiliation">{{ person.affiliation }}</p>
{% endif %}

<p>{{ person.content | strip_html | truncate: 120 }}</p>

<div class="lab-links">

{% if person.website %}
<a href="{{ person.website }}" target="_blank"><i class="fas fa-globe"></i></a>
{% endif %}

{% if person.scholar %}
<a href="{{ person.scholar }}" target="_blank"><i class="fas fa-graduation-cap"></i></a>
{% endif %}

{% if person.github %}
<a href="https://github.com/{{ person.github }}" target="_blank"><i class="fab fa-github"></i></a>
{% endif %}

{% if person.email %}
<a href="mailto:{{ person.email }}"><i class="fas fa-envelope"></i></a>
{% endif %}

</div>

</div>

{% endif %}
{% endfor %}

</div>

{% endfor %}

---

## Alumni

<div class="lab-grid">

{% assign sorted_people = site.people | sort: "lastname" %}
{% for person in sorted_people %}
{% if person.alumni == true %}

<div class="lab-card">

<a href="{{ person.url }}">
<img src="{{ person.image }}" alt="{{ person.name }}">
</a>

<h3><a href="{{ person.url }}">{{ person.name }}</a></h3>

<p class="lab-role">{{ person.role }}</p>

{% if person.affiliation %}
<p class="lab-affiliation">{{ person.affiliation }}</p>
{% endif %}

<p>{{ person.content | strip_html | truncate: 120 }}</p>

</div>

{% endif %}
{% endfor %}

</div>
