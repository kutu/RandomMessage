import sublime, sublime_plugin
from urllib2 import urlopen

class RandomMessageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		data = urlopen('http://whatthecommit.com/index.txt')
		if not data:
			return
		message = data.read().strip()
		for region in self.view.sel():
			self.view.replace(edit, region, message)
