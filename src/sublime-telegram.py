import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    sel = view.sel()[0]
    print(sel)
    line_pos = view.line(sel)
    print(line_pos)
    lala = self.view.substr(line_pos)
    print(lala)
