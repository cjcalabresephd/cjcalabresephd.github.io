---
title: "Research Lab"
permalink: /research-lab/
layout: single
---

Welcome to the **Health Communication and Digital Innovation Research Group** at Clemson University!  
Our research focuses on understanding how media messaging and persuasive technologies influence human behaviors, particularly in the context of health.

---

{% assign roles = "Faculty,External Collaborator,Masters Student" | split: "," %}

{% for role in roles %}

{% if role == "Faculty" %}
## Faculty
{% elsif role == "External Collaborator" %}
## External Collaborators
{% elsif role == "Masters Student" %}
## Master's Students
{% else %}
## {{ role }}s
{% endif %}

<div class="lab-grid">

{% for member in site.data.lab_members %}
{% if member.role == role and member.alumni != true %}

<div class="lab-card">

<img src="{{ member.image }}" alt="{{ member.name }}">

<h3>{{ member.name }}</h3>

<p class="lab-role">{{ member.role }}</p>

{% if member.affiliation %}
<p class="lab-affiliation">{{ member.affiliation }}</p>
{% endif %}

<p>{{ member.bio }}</p>

<div class="lab-links">
{% if member.website %}<a href="{{ member.website }}" target="_blank">🌐</a>{% endif %}
{% if member.scholar %}<a href="{{ member.scholar }}" target="_blank">🎓</a>{% endif %}
{% if member.github %}<a href="https://github.com/{{ member.github }}" target="_blank">💻</a>{% endif %}
{% if member.email %}<a href="mailto:{{ member.email }}">✉️</a>{% endif %}
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
{% if member.alumni %}

<div class="lab-card">

<img src="{{ member.image }}" alt="{{ member.name }}">

<h3>{{ member.name }}</h3>

<p class="lab-role">{{ member.role }}</p>

{% if member.affiliation %}
<p class="lab-affiliation">{{ member.affiliation }}</p>
{% endif %}

<p>{{ member.bio }}</p>

<div class="lab-links">
{% if member.website %}<a href="{{ member.website }}" target="_blank">🌐</a>{% endif %}
{% if member.scholar %}<a href="{{ member.scholar }}" target="_blank">🎓</a>{% endif %}
{% if member.github %}<a href="https://github.com/{{ member.github }}" target="_blank">💻</a>{% endif %}
{% if member.email %}<a href="mailto:{{ member.email }}">✉️</a>{% endif %}
</div>

</div>

{% endif %}
{% endfor %}

</div>
