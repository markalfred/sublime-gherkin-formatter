import sublime, sublime_plugin

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.formatter import ViewFormatter

def is_gherkin(view=None):
  if view is None:
    view = sublime.active_window().active_view()
  if 'text.gherkin' in view.scope_name(0):
    return True
  if os.path.splitext(view.file_name())[1] == '.feature':
    return True
  return False

class FormatGherkinCommand(sublime_plugin.TextCommand):
  def is_enabled(self):
    return is_gherkin(self.view)

  def run(self, edit):
    ViewFormatter(sublime, self.view).format_view(edit)

class FormatGherkinOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    settings = sublime.load_settings('GherkinFormatter.sublime-settings')
    if settings.get('format_on_save'):
      view.run_command('format_gherkin')
