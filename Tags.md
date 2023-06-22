---
layout: page
title: Tags
permalink: /tags/
redirect_from:
  - /tags/
---

{% raw %}
{% for tag in site.tags %}
  <h2 id="{{ tag[0] }}">{{ tag[0] }}</h2>
  <ul>
    {% for post in tag[1] %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
{% endfor %}
{% endraw %}
