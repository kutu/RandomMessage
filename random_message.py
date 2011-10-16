import sublime, sublime_plugin, re
from urllib2 import urlopen

class RandomMessageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		data = urlopen('http://whatthecommit.com/')
		if not data:
			return
		m = re.match(r'.*<p>\s*(.+?)\s*</p>', data.read(), re.S)
		if not m:
			return
		message = m.group(1)
		for region in self.view.sel():
			self.view.replace(edit, region, message)
