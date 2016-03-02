import sublime, sublime_plugin
class ToggleVintagePackageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        setts = sublime.load_settings("Global.sublime-settings")
        ipacks = setts.get('ignored_packages')
    
        if not ipacks: ipacks = []
        if "Vintage" in ipacks:
            ipacks.pop(ipacks.index("Vintage"))
        else:
            ipacks.append("Vintage")
        
        setts.set('ignored_packages', ipacks)
        sublime.save_settings("Global.sublime-settings")
#Keymaps
#[{ "keys": ["ctrl+alt+v"], "command": "toggle_vintage_package" }]
