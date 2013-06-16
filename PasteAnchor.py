# Sublime Text 2 - Paste Anchor
#
# Author: Francois Cardinaux
# Date: 2013-06-14
import sublime, sublime_plugin, urllib, re, os.path
from bs4 import BeautifulSoup

class Paste_anchorCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selectedRegion = self.view.sel()[0]
    assumedUrl = sublime.get_clipboard().strip()

    anchor = assumedUrl

    try:
      settings = sublime.load_settings("PasteAnchor.sublime-settings")
      config = settings.get("paste-anchor")

      fileName, fileExtension = os.path.splitext( self.view.file_name() )
      if fileExtension in config["extensions"]:
        anchorType = config["extensions"][fileExtension]
        anchorSyntax = config["anchor-syntaxes"][anchorType]

        soup = self.serveTheSoup(assumedUrl)

        # Build the Markdown URL
        title = soup.title.string.strip()

        # Find out if HN-like site
        isHNLike = False
        extUrlREComp = re.compile('^https?://')
        for site in config["hn-like-sites"]:

          if None == re.match(site["regexp"], assumedUrl):
            continue

          mainUrl = soup.select(site['title-anchor'])[0]['href'].strip()
          if None == extUrlREComp.match(mainUrl):
            # A local link
            anchor = anchorSyntax.format(assumedUrl, title)

          else:
            # An external link
            mainSoup = self.serveTheSoup(mainUrl)
            title = mainSoup.title.string.strip()

            target = anchorSyntax.format(mainUrl, title)
            source = anchorSyntax.format(assumedUrl, site['via-title'])
            fullLink = config["hn-like-site-syntax"].format(target, source)
            anchor = fullLink

          isHNLike = True
          break

        if not isHNLike:
          anchor = anchorSyntax.format(assumedUrl, title)
    except Exception, excp:
      # print str(excp)
      anchor = assumedUrl

    self.view.replace(edit, selectedRegion, anchor)

  def serveTheSoup(self, url):
      doc = urllib.urlopen(url)
      # http://stackoverflow.com/a/51550/2403326
      return BeautifulSoup(doc)
