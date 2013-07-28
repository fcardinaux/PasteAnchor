# The _Paste Anchor_ Plugin for Sublime Text 2

* Author: François Cardinaux, CH 1207 Genève
* Creation date: 2013-06-14, last updated on 2013-07-28

## Description

This [Sublime Text](http://www.sublimetext.com/) plugin allows you to get an anchor with a text when you paste an URL to a Markdown or HTML file. The text corresponds to the page title.

For instance, if you paste the link "http://www.sublimetext.com/docs/2/api_reference.html" to an HTML or Markdown file, you get this link:
“[API Reference - Sublime Text 2 Documentation](http://www.sublimetext.com/docs/2/api_reference.html)”.

The exact Markdown syntax is:

    [API Reference - Sublime Text 2 Documentation](http://www.sublimetext.com/docs/2/api_reference.html)

If you paste the same URL to an HTML file, you get this:

    <a href="http://www.sublimetext.com/docs/2/api_reference.html">API Reference - Sublime Text 2 Documentation</a>

### Pasting URLs of [Hacker News](https://news.ycombinator.com/) threads

When you paste a link to a thread on Hacker News or on a similar site, you get two anchors: one to the thread itself, and one to the related article. For instance, if you paste the link "https://news.ycombinator.com/item?id=4161610" to an HTML or Markdown file, you get this link:
“[Sublime Blog » Sublime Text 2.0 Released](http://www.sublimetext.com/blog/articles/sublime-text-2-0-released) via [Hacker News](https://news.ycombinator.com/item?id=4161610)”.

The exact Markdown syntax is:

    [Sublime Blog » Sublime Text 2.0 Released](http://www.sublimetext.com/blog/articles/sublime-text-2-0-released) via [Hacker News](https://news.ycombinator.com/item?id=4161610)

If you paste the same URL to an HTML file, you get this:

    <a href="http://www.sublimetext.com/blog/articles/sublime-text-2-0-released">Sublime Blog » Sublime Text 2.0 Released</a> via <a href="https://news.ycombinator.com/item?id=4161610">Hacker News</a>

The syntax "anchor 1 via anchor 2" is configured in the [PasteAnchor.sublime-settings](PasteAnchor.sublime-settings) file and can be easily modified.

Note that the same system works for the following sites as well:

* [Lobste.rs](https://lobste.rs)
* [EchoJS.com](http://www.echojs.com)
* [Inbound.org](http://www.inbound.org)
* [LamerNews.com](http://www.lamernews.com)
* [LuserNews.com](http://www.lusernews.com)
* [Hackful.com](http://hackful.com)
* [MetaFilter.com](http://www.metafilter.com)

## Installation

Go to your _Sublime Text_ package directory and clone [the present repository](https://github.com/fcardinaux/PasteAnchor).

### Linux (untested, copied from [joneshf/sublime-chaplinjs](https://github.com/joneshf/sublime-chaplinjs/blob/master/README.md))

```
$ cd ~/.config/sublime-text-2/Packages
$ git clone https://github.com/fcardinaux/PasteAnchor
```

### Macosx

```
$ cd "~/Library/Application Support/Sublime Text 2/Packages"
$ git clone https://github.com/fcardinaux/PasteAnchor
```

### Windows (untested, copied from [joneshf/sublime-chaplinjs](https://github.com/joneshf/sublime-chaplinjs/blob/master/README.md))

```
$ cd "%APPDATA%\Sublime Text 2"
$ git clone https://github.com/fcardinaux/PasteAnchor
```

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
      <td style="border: 1px solid black;">default-title</td>
      <td style="border: 1px solid black;">This default title is used if the link isn't a valid URL, or if anything else goes wrong.</td>
    </tr>
    <tr>
      <td style="border: 1px solid black;">inaccessible-sites</td>
      <td style="border: 1px solid black;">A list of url patterns that are known not to be accessible for Paste Anchor. To each pattern is associated a replacement title:
        <ul>
          <li><b>url-regexp</b>: the regular expression to use in order to identify the inaccessible site</li>
          <li><b>title</b>: the text to put in the anchor</li>
        </ul>
      </td>
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
