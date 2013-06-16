# Paste Anchor - Readme

* Author: François Cardinaux, CH 1207 Genève
* Creation date: 2013-06-14, last updated on 2013-06-16

Copyright: François Cardinaux (CH 1207 Genève) 2013

## Description

This plugin allows you to get an anchor when you paste an URL to a Markdown file.

For instance, if you paste the link "http://www.sublimetext.com/docs/2/api_reference.html" to a Markdown file, you get this:

    [API Reference - Sublime Text 2 Documentation](http://www.sublimetext.com/docs/2/api_reference.html)

The text of the anchor is automatically taken from the TITLE tag of the target page.

### Pasting links to Hacker News or similar sites

When you paste a link to a thread on Hacker News or on a similar site, you get two anchors: one to the thread itself, and one to the related article. For instance, if you paste the link "https://news.ycombinator.com/item?id=1834305", you get this:

    [NewsBlur](http://www.newsblur.com) via [Hacker News](https://news.ycombinator.com/item?id=1834305)

## Dependency

You need to install the [BeautifulSoup for Sublime Text](https://github.com/ivanchaer/beautiful-soup-sublime) plugin.

## How to run

To run:

    view.run_command("paste_anchor")

To use the cmd + alt + v shortcut:

* Go to Preferences > Key Bindings - User
* Add the following binding: { "keys": ["super+alt+v"], "command": "paste_anchor" }
