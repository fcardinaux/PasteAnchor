# The “Paste Anchor” Plugin

## for Sublime Text

* Author: François Cardinaux, CH 1207 Genève
* Creation date: 2013-06-14, last updated on 2013-06-16

## Description

This [Sublime Text](http://www.sublimetext.com/) plugin allows you to get an anchor with a text when you paste an URL to a Markdown or HTML file. The text corresponds to the page title.

For instance, if you paste the link "http://www.sublimetext.com/docs/2/api_reference.html" to a Markdown file, you get this:

    [API Reference - Sublime Text 2 Documentation](http://www.sublimetext.com/docs/2/api_reference.html)

If you paste the same URL to an HTML file, you get this:

    <a href="http://www.sublimetext.com/docs/2/api_reference.html">API Reference - Sublime Text 2 Documentation</a>

### Pasting URLs of Hacker News threads

When you paste a link to a thread on Hacker News or on a similar site, you get two anchors: one to the thread itself, and one to the related article. For instance, if you paste the link "https://news.ycombinator.com/item?id=1834305" to a Markdown file, you get this:

    [NewsBlur](http://www.newsblur.com) via [Hacker News](https://news.ycombinator.com/item?id=1834305)

If you paste the same URL to an HTML file, you get this:

    <a href="http://www.newsblur.com">NewsBlur</a> via <a href="https://news.ycombinator.com/item?id=1834305">Hacker News</a>

The syntax "anchor 1 via anchor 2" is configured in the [PasteAnchor.sublime-settings](PasteAnchor.sublime-settings) file and can be easily modified.

## Dependency

You need to install the [BeautifulSoup for Sublime Text](https://github.com/ivanchaer/beautiful-soup-sublime) plugin.

## How to run the command

Copy or cut the URL, and paste it by pressing the following keys:

* ctrl + alt + v on Windows and Linux
* cmd + alt + v on Mac OSX

You may also run the command from the Sublime Text Console:

    view.run_command("paste_anchor")

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
          <li><b>url-regexp</b>: the regular expression to use in order to detect the Hacker-News-like site</li>
          <li><b>title-anchor-selector</b>: the css selector to use in order to locate the anchor of the page title</li>
          <li><b>site-name</b>: the name of the Hacker-News-like site</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## License

This software is released under the GNU General Public License (GPL) version 3.

Copyright: François Cardinaux &copy; 2013
