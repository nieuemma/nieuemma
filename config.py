# Call autoconfig
config.load_autoconfig()

# set qutebrowser colors
gray = "#0a0c10"
red = "#ff9492"
green = "#26cd4d"
yellow  = "#f0b72f"
blue = "#71b7ff"
purple = "#cb9eff"
turq = "#39c5cf"
white = "#d9dee3"
grayb = "#0d1117"
redb = "#ffb1af"
greenb = "#4ae168"
yellowb = "#f7c843"
blueb = "#91cbff"
purpleb = "#dbb7ff"
turqb = "#56d4dd"
whiteb = "#ffffff"

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = white

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = grayb

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = gray

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = green

# Background color of the completion widget category headers.
c.colors.completion.category.bg = gray

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = gray

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = gray

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = green

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = blue

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = blue

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = blue

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = greenb

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = greenb

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = grayb

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = gray

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = grayb

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = gray

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = gray

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  white

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = blue

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = green

# Background color for the download bar.
c.colors.downloads.bar.bg = gray

# Color gradient start for download text.
c.colors.downloads.start.fg = gray

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = gray

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = gray

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = grayb

# Text color for the keyhint widget.
c.colors.keyhint.fg = grayb

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = grayb

# Background color of the keyhint widget.
c.colors.keyhint.bg = gray

# Foreground color of an error message.
c.colors.messages.error.fg = gray

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = gray

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = grayb

# Background color of an info message.
c.colors.messages.info.bg = gray

# Border color of an info message.
c.colors.messages.info.border = gray

# Foreground color for prompts.
c.colors.prompts.fg = grayb

# Border used around UI elements in prompts.
c.colors.prompts.border = gray

# Background color for prompts.
c.colors.prompts.bg = gray

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = green

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = grayb

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = greenb

# Background color of the statusbar.
c.colors.statusbar.normal.bg = gray

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = gray

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base0D

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = gray

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base0C

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = gray

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base01

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = grayb

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = gray

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = grayb

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = gray

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = gray

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base0E

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = gray

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base0D

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = grayb

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = grayb

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0C

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = greenb

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = gray

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = grayb

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = grayb

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = grayb

# Background color of unselected even tabs.
c.colors.tabs.even.bg = gray

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0C

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = whiteb

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = greenb

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = whiteb

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = green

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = grayb

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = green

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = grayb

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = grayb

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = green

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = grayb

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = green

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = gray
