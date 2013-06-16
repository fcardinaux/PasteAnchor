# Sublime Text 2 - Paste Anchor
#
# Author: Francois Cardinaux
# Date: 2013-06-14
import sublime, sublime_plugin, urllib, re
from bs4 import BeautifulSoup

pmu_settings = sublime.load_settings("PasteAnchor.sublime-settings")

class Paste_anchorCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    config = pmu_settings.get("paste-anchor")

    selectedRegion = self.view.sel()[0]
    # Note that to get the cursor position:
    cursorPos = selectedRegion.begin()

    assumedUrl = sublime.get_clipboard().strip()
    try:
      soup = self.serveTheSoup(assumedUrl)

      # Build the Markdown URL
      title = soup.title.string.strip()
      mdurl = self.makeUrl(title, assumedUrl)

      # Find out if HN-like site
      isFound = False
      extUrlREComp = re.compile('^https?://')
      for site in config["hn-like-sites"]:

        if None == re.match(site["regexp"], assumedUrl):
          continue

        mainUrl = soup.select(site['title-anchor'])[0]['href'].strip()
        if None == extUrlREComp.match(mainUrl):
          # A local link
          self.view.replace(edit, selectedRegion, mdurl)

        else:
          # An external link
          mainSoup = self.serveTheSoup(mainUrl)
          title = mainSoup.title.string.strip()

          target = self.makeUrl(title, mainUrl)
          source = '[' + site['via-title'] + '](' + assumedUrl + ')'
          fullLink = config["hn-like-site-syntax"].format(target, source)
          self.view.replace(edit, selectedRegion, fullLink)

        isFound = True
        break

      if not isFound:
        self.view.replace(edit, selectedRegion, mdurl)
    except Exception, excp:
      print str(excp)
      self.view.replace(edit, selectedRegion, assumedUrl)

  def makeUrl(self, title, url):
    return ''.join(["[", title, "](", url, ")"])

  def serveTheSoup(self, url):
      doc = urllib.urlopen(url)
      # http://stackoverflow.com/a/51550/2403326
      return BeautifulSoup(doc)
