---
layout: default
title: AI Productivity Blog
---

# Welcome to AI Productivity Blog!

This blog explores AI tools, automation strategies, and productivity hacks.

## Recent Posts:
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}

