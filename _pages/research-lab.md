---
title: "Research Lab"
permalink: /research-lab/
layout: single
---

## Health Communication and Digital Innovation Research Group

Welcome to the Health Communication and Digital Innovation Research Group! Our research focuses on understanding the effects and processes 
through which media messaging and persuasive technologies influence human behaviors, particularly in the context of health.

---

{% assign roles = "Faculty,Collaborator,Masters Student" | split: "," %}

{% for role in roles %}

## {{ role }}

<div class="lab-grid">

{% for member in site.data.lab_members %}
{% if member.role == role and member.alumni != true %}

<div class="lab-card">

<img src="{{ member.image }}" alt="{{ member.name }}">

<h3>{{ member.name }}</h3>

<p class="lab-role">{{ member.role }}</p>

<p>{{ member.bio }}</p>

<div class="lab-links">

{% if member.website %}
<a href="{{ member.website }}">🌐</a>
{% endif %}

{% if member.scholar %}
<a href="{{ member.scholar }}">🎓</a>
{% endif %}

{% if member.github %}
<a href="https://github.com/{{ member.github }}">💻</a>
{% endif %}

{% if member.email %}
<a href="mailto:{{ member.email }}">✉️</a>
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

{% for member in site.data.lab_members %}
{% if member.alumni == true %}

<div class="lab-card">

<img src="{{ member.image }}" alt="{{ member.name }}">

<h3>{{ member.name }}</h3>

<p class="lab-role">{{ member.role }}</p>

<p>{{ member.bio }}</p>

</div>

{% endif %}
{% endfor %}

</div>
