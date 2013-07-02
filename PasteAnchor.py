# Sublime Text 2 - Paste Anchor
#
# Author: Francois Cardinaux
# Date: 2013-06-14
import sublime, sublime_plugin, urllib, re, os.path

class Paste_anchorCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    if not hasattr(self, 'BeautifulSoup'):
      # Importing BeautifulSoup at the beginning of the script prevents this package from being loaded.
      # This is very probably because dependency constraints cannot be expressed, at least with the current version
      # of Sublime Text or Package Control.
      # This solution is from: http://stackoverflow.com/a/4481762
      try:
        from bs4 import BeautifulSoup
      except ImportError:
        self.BeautifulSoup = None
      else:
        self.BeautifulSoup = BeautifulSoup

    print "running command now..."
    selectedRegion = self.view.sel()[0]
    assumedUrl = sublime.get_clipboard().strip()

    anchor = assumedUrl

    try:
      # Read the configuration
      settings = sublime.load_settings("PasteAnchor.sublime-settings")
      config = settings.get("paste-anchor")

      fileName, fileExtension = os.path.splitext( self.view.file_name() )
      if fileExtension in config["extensions"]:

        # Determine the anchor syntax from the file type
        anchorType = config["extensions"][fileExtension]
        anchorSyntax = config["anchor-syntaxes"][anchorType]

        # Get the BeautifulSoup object
        soup = self.serveTheSoup(assumedUrl)

        if not soup:

          anchor = "You should install the BeautifulSoup package"

        else:

          # Build the Markdown URL
          title = soup.title.string.strip()

          # Find out if HN-like site
          isHNLike = False
          re_comp_externalURL = re.compile('^https?://')
          for site in config["hn-like-sites"]:

            if None == re.match(site["url-regexp"], assumedUrl):
              continue

            mainUrl = soup.select(site['title-anchor-selector'])[0]['href'].strip()
            if None == re_comp_externalURL.match(mainUrl):
              # A local link
              anchor = anchorSyntax.format(assumedUrl, title)

            else:
              # An external link
              mainSoup = self.serveTheSoup(mainUrl)
              title = mainSoup.title.string.strip()

              target = anchorSyntax.format(mainUrl, title)
              source = anchorSyntax.format(assumedUrl, site['site-name'])
              fullLink = config["hn-like-site-syntax"].format(target, source)
              anchor = fullLink

            isHNLike = True
            break

          if not isHNLike:
            anchor = anchorSyntax.format(assumedUrl, title)

    except Exception, excp:
      print str(excp)
      anchor = assumedUrl

    self.view.replace(edit, selectedRegion, anchor)

  # Load the specified URL and return the BeautifulSoup object
  def serveTheSoup(self, url):
    if not self.BeautifulSoup:
      return False

    doc = urllib.urlopen(url)
    return self.BeautifulSoup(doc)
