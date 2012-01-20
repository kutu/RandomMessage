import sublime, sublime_plugin
import threading
import urllib2

class RandomMessageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		thread = WhatTheCommitCallThread(self.view, edit)
		thread.start()
		self.handle_thread(thread)

	def handle_thread(self, thread):
		if thread.is_alive():
			sublime.set_timeout(lambda: self.handle_thread(thread), 100)
			return
		if thread.result:
			for region in thread.view.sel():
				thread.view.replace(thread.edit, region, thread.result)
		if thread.error:
			sublime.status_message('%s: %s' % (__name__, thread.error))

class WhatTheCommitCallThread(threading.Thread):
	def __init__(self, view, edit):
		self.view = view
		self.edit = edit
		self.result = None
		self.error = None
		super(WhatTheCommitCallThread, self).__init__()

	def run(self):
		try:
			req = urllib2.Request('http://whatthecommit.com/index.txt',
				headers={'User-Agent': 'Sublime Text 2 - Random Message'})
			res = urllib2.urlopen(req, timeout=5)
			self.result = res.read().strip()
		except Exception, e:
			self.error = e
			raise
