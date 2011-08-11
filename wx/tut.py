#!/usr/bin/env python
import wx

#  wx.App is the application object in wx
app = wx.App(False)

#  wx.Frame(parent, id, title) is a top-level window 
frame = wx.Frame(None, wx.ID_ANY, "Hello, World!")

#  make the frame visible
frame.Show(True)

#  start the event loop
app.MainLoop()
