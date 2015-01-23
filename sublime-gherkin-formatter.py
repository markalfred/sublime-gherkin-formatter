import sublime, sublime_plugin

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.formatter import ViewFormatter


class FormatGherkinCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    ViewFormatter(sublime, self.view).format_view(edit)

class FormatGherkinOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    settings = sublime.load_settings('GherkinFormatter.sublime-settings')
    if settings.get('format_on_save'):
      view.run_command('format_gherkin')
