---
layout: page
title: Tags
permalink: /Tags/
redirect_from:
  - /tags/
---

<style>
.archive-item h6 {
  margin: 0;
  line-height: 1;
}
</style>


<div id="archives">
{% for tag in site.tags %}
  <div class="archive-group">
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <div id="#{{ tag_name | slugize }}"></div>
    <p></p>

    <h3 class="tag-head">{{ tag_name }}</h3>
    <a name="{{ tag_name | slugize }}"></a>
    {% assign posts = site.tags[tag_name] %}
    {% for post in posts %}
    <article class="archive-item">
      <h6>\t{% if forloop.last %}└{% else %}├{% endif %} <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h6>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>
