c.content.javascript.alert = False
config.set('content.javascript.enabled', True, 'file://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')
c.content.plugins = True
c.completion.cmd_history_max_items = 50
c.completion.show = 'always'
c.completion.shrink = True
c.completion.web_history_max_items = 50
c.hints.border = '1px dashed #eaa4b2'
c.hints.chars = 'poi'
c.hints.uppercase = False
c.messages.timeout = 500
c.statusbar.hide = False
c.statusbar.padding = {'top': 2, 'bottom': 2, 'left': 2, 'right': 2}
c.statusbar.position = 'bottom'
#   - url: Current page URL.
#   - scroll: Percentage of the current page position like `10%`.
#   - scroll_raw: Raw percentage of the current page position like `10`.
#   - history: Display an arrow when possible to go back/forward in history.
#   - tabs: Current active tab, e.g. `2`.
#   - keypress: Display pressed keys when composing a vi command.
#   - progress: Progress bar for the current page loading.
c.statusbar.widgets = ['tabs', 'progress', 'url', 'scroll']

c.tabs.favicons.scale = 0.75
c.tabs.favicons.show = 'never'
c.tabs.last_close = 'blank'
c.tabs.mousewheel_switching = False
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 2, 'right': 10}
c.tabs.position = 'left'
#   - always: Always show the tab bar.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'
# Type: PercOrInt
c.tabs.width = '8%'
c.tabs.indicator.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 1}
c.tabs.wrap = True

c.url.searchengines = {'d': 'https://duckduckgo.com/?q={}',
                       'DEFAULT': 'https://www.google.com/search?q={}',
                       'i': 'https://www.google.com/search?q={}&dcr=0&tbm=isch',
                       'w': 'https://en.wikipedia.org/w/index.php?search={}&go=Go',
                       'a': 'https://wiki.archlinux.org/index.php?search={}&go=Go'}

c.url.start_pages = 'about:blank'
c.window.title_format = '{perc}{title}'
c.zoom.default = '80%'
c.colors.hints.fg = '#f3f4e8'
c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(25, 47, 33, 0.75), stop:1 rgba(55, 97, 66, 0.5))'
c.colors.hints.match.fg = '#f22815'
c.colors.tabs.bar.bg = '#171a1f'
c.colors.tabs.indicator.start = '#bdb2a0'
c.colors.tabs.indicator.stop = '#536a52'
c.colors.tabs.indicator.error = '#8f7373'
c.colors.tabs.odd.fg = '#c2ccc1'
c.colors.tabs.odd.bg = '#50555d'
c.colors.tabs.even.fg = '#c2ccc1'
c.colors.tabs.even.bg = '#6e747b'
c.colors.tabs.selected.odd.fg = '#c2ccc1'
c.colors.tabs.selected.odd.bg = '#3a1819'
c.colors.tabs.selected.even.fg = '#c2ccc1'
c.colors.tabs.selected.even.bg = '#3a1819'
c.fonts.monospace = 'Ubuntu Mono'
c.fonts.completion.entry = '9pt monospace'
c.fonts.completion.category = '10pt monospace'
c.fonts.hints = '12pt monospace'
c.fonts.messages.error = '10pt monospace'
c.fonts.messages.info = '10pt monospace'
c.fonts.messages.warning = '10pt monospace'
c.fonts.prompts = '10pt monospace'
c.fonts.statusbar = '10pt monospace'
c.fonts.tabs = '8pt monospace'
c.fonts.web.size.default = 16
c.fonts.web.family.sans_serif = 'Ubuntu Regular'
c.fonts.web.family.serif = 'URW Bookman Light'
c.fonts.web.family.standard = 'Ubuntu Regular'
c.fonts.web.family.fixed = 'Ubunutu Mono'

config.bind('d', None)
config.bind('dd', 'tab-close')
