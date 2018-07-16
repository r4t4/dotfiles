# config.load_autoconfig()

c.fonts.completion.category = '10pt monospace'
c.fonts.completion.entry = '10pt monospace'
c.fonts.messages.error = '10pt monospace'
c.fonts.messages.info = '10pt monospace'
c.fonts.messages.warning = '10pt monospace'
c.fonts.monospace = 'Inconsolata'
c.fonts.prompts = '10pt monospace'
c.fonts.statusbar = '10pt monospace'
c.fonts.tabs = '8pt monospace'
c.fonts.hints = '12pt monospace'
c.fonts.web.size.default = 16

c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(25, 47, 33, 0.75), stop:1 rgba(55, 97, 66, 0.5))'
c.colors.hints.fg = '#f3f4e8'
c.colors.hints.match.fg = '#f22815'
c.colors.tabs.selected.even.bg = '#3a1819'
c.colors.tabs.selected.even.fg = '#c2ccc1'
c.colors.tabs.selected.odd.bg = '#3a1819'
c.colors.tabs.selected.odd.fg = '#c2ccc1'
c.colors.tabs.even.fg = '#c2ccc1'
c.colors.tabs.even.bg = '#6e747b'
c.colors.tabs.odd.fg = '#c2ccc1'
c.colors.tabs.odd.bg = '#50555d'
c.colors.tabs.bar.bg = '#171a1f'
c.colors.tabs.indicator.error = '#8f7373'
c.colors.tabs.indicator.start = '#bdb2a0'
c.colors.tabs.indicator.stop = '#536a52'

c.hints.uppercase = False 
c.hints.chars = 'poi' 
c.hints.border = '1px dashed #eaa4b2' 

c.tabs.background = True
c.tabs.favicons.scale = 0.75
c.tabs.favicons.show = 'never'
c.tabs.indicator.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 1 }
c.tabs.last_close = 'blank'
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 2, 'right': 10 }
c.tabs.show = 'always'
c.tabs.wrap = False
c.tabs.position = 'left'
c.tabs.width = '8%'
c.tabs.mousewheel_switching = False

c.completion.shrink = True
c.completion.show = 'always'
c.completion.cmd_history_max_items = 50
c.completion.web_history_max_items = 50

c.content.javascript.alert = False
c.content.plugins = False

c.statusbar.padding = {'top': 2, 'bottom': 2, 'left': 2, 'right': 2 }
c.statusbar.hide = False
c.statusbar.position = 'bottom'
c.statusbar.widgets = [ "url" ]

c.window.title_format = '{perc}{title}'

c.messages.timeout = 500

c.zoom.default = '80%'

c.url.start_pages = 'about:blank'
c.url.searchengines = { 'DEFAULT': 'https://duckduckgo.com/?q={}', 
                         'g': 'https://www.google.com/search?q={}',
                         'i': 'https://www.google.com/search?q={}&dcr=0&tbm=isch'
                       }
config.unbind('d')
config.bind('dd', 'tab-close')
