---
layout: default
title: AI Productivity Blog
---

## Welcome to the AI Productivity Blog!

### Recent Posts:
<ul>
  {% for post in site.posts %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
