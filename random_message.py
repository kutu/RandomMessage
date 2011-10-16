import sublime, sublime_plugin, re
from urllib2 import urlopen

class RandomMessageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		data = urlopen('http://whatthecommit.com/index.tx')
		if not data:
			return
		message = data.read()
		for region in self.view.sel():
			self.view.replace(edit, region, message)
