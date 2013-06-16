# Paste Anchor - Readme

* Author: François Cardinaux, CH 1207 Genève
* Creation date: 2013-06-14, last updated on 2013-06-16

Copyright: François Cardinaux 2013

## Description

This plugin allows you to get an anchor when you paste an URL to a Markdown or HTML file.

For instance, if you paste the link "http://www.sublimetext.com/docs/2/api_reference.html" to a Markdown file, you get this:

    [API Reference - Sublime Text 2 Documentation](http://www.sublimetext.com/docs/2/api_reference.html)

The text of the anchor is automatically taken from the TITLE tag of the target page.

If you paste it to an HTML file, you get this:

    <a href="http://www.sublimetext.com/docs/2/api_reference.html">API Reference - Sublime Text 2 Documentation</a>

### Pasting URLs of Hacker-News-like threads

When you paste a link to a thread on Hacker News or on a similar site, you get two anchors: one to the thread itself, and one to the related article. For instance, if you paste the link "https://news.ycombinator.com/item?id=1834305" to a Markdown file, you get this:

    [NewsBlur](http://www.newsblur.com) via [Hacker News](https://news.ycombinator.com/item?id=1834305)

If you paste it to an HTML file, you get this:

    <a href="http://www.newsblur.com">NewsBlur</a> via <a href="https://news.ycombinator.com/item?id=1834305">Hacker News</a>

## Dependency

You need to install the [BeautifulSoup for Sublime Text](https://github.com/ivanchaer/beautiful-soup-sublime) plugin.

## How to run the command

To run the command, type this in the Sublime Text Console:

    view.run_command("paste_anchor")

To use the cmd + alt + v shortcut:

* Go to Preferences > Key Bindings - User
* Add the following binding: { "keys": ["super+alt+v"], "command": "paste_anchor" }

## Configuration

Here is a description of the parameters in the PasteAnchor.sublime-settings file:

<table style="border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid black;">Setting name</th>
      <th style="border: 1px solid black;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black;">extensions</td>
      <td style="border: 1px solid black;">A dictionary of recognized extensions, with the types they correspond to</td>
    </tr>
    <tr>
      <td style="border: 1px solid black;">anchor-syntaxes</td>
      <td style="border: 1px solid black;">The syntax of each extension type</td>
    </tr>
    <tr>
      <td style="border: 1px solid black;white-space: nowrap;">hn-like-site-syntax</td>
      <td style="border: 1px solid black;">The syntax to use for Hacker-News-like sites. You may want to replace the value with a text in your language, e.g. "{0} depuis {1}" in French</td>
    </tr>
    <tr>
      <td style="border: 1px solid black;">hn-like-sites</td>
      <td style="border: 1px solid black;">A list of Hacker-News-like sites, with the following settings:
        <ul>
          <li><b>regexp</b>: the regular expression to use in order to detect the Hacker-News-like site</li>
          <li><b>title-anchor</b>: the css selector to use in order to locate the anchor of the page title</li>
          <li><b>via-title</b>: the name to use to represent the Hacker-News-like site</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## License

This software is released under the GNU General Public License (GPL) version 3.

## Todo

* Encode the URLs and the anchor texts.
