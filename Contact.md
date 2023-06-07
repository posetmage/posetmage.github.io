---
layout: page
title: Contact
permalink: /Contact/
redirect_from:
  - /contact/
---

<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <style>
  .contact-form {
      width: 100%;
  }

  .contact-form input[type="text"],
  .contact-form input[type="email"],
  .contact-form textarea {
      width: 100%;
  }
  </style>
</head>

{% include social.html %}


<form action="https://formspree.io/f/xayzglbq" method="POST">
    <label for="name">Your Name:</label><br>
    <input type="text" id="name" name="name" required><br>
    <label for="email">Your Email:</label><br>
    <input type="email" id="email" name="_replyto" required><br>
    <label for="message">Your Message:</label><br>
    <textarea id="message" name="message" required></textarea><br>
    <input type="submit" value="Submit">
</form>