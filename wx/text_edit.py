#!/usr/bin/env python
import wx


class MyFrame(wx.Frame):
    """derived class for our GUI"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        fmenu = wx.Menu()
        about_item = fmenu.Append(wx.ID_ANY, "&About",
                              " Information about this program")
        fmenu.AppendSeparator()
        open_item = fmenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        fmenu.Append(wx.ID_ANY, "Test&1", "this item uses id = wx.ID_ANY")
        fmenu.Append(-1, "Test&2", "this item uses id = -1")
        fmenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.on_open, open_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)

        tim_menu = wx.Menu()
        tim_menu.Append(-1, "Diller", " About me")
        tim_menu.AppendSeparator()
        tim_menu.Append(-1, "wife", " is Hannah")

        menu_bar = wx.MenuBar()
        menu_bar.Append(fmenu, "&File")
        menu_bar.Append(tim_menu, "Tim Diller")
        self.SetMenuBar(menu_bar)

        tool_bar = wx.ToolBar(self, wx.ID_ANY)
        tool_bar.AddCheckTool(-1, wx.ITEM_CHECK, wx.EmptyBitmap(10,10))
        self.SetToolBar(tool_bar)
        self.Show(True)

    def on_about(self, event):
        """ Here's what to do when the About menu item is selected"""
        dlg = wx.MessageDialog(self, """This is a small text editor.
        Written by Tim Diller as a way to learn
        wx interface programming.""", "About Text Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def on_open(self, event):
        """Open a file"""
        from os import path
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file",
                            self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


def main():
    """main"""
    app = wx.App(False)
    frame = MyFrame(None, "Simple wx text editor")
    app.MainLoop()

if __name__ == "__main__":
    main()
