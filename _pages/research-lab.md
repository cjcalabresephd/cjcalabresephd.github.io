---
title: "Research Lab"
permalink: /research-lab/
layout: single
---

## Our Research Lab

Welcome to the Health Communication and Digital Innovations Research Group! Our research focuses on understanding the effects and processes 
through which media messaging and persuasive technologies influence human behaviors, particularly in the context of health.

---

## Lab Members

{% for member in site.data.lab_members %}
### {{ member.name }}

**Role:** {{ member.role }}

{{ member.bio }}

{% endfor %}

