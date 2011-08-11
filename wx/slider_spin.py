import wx

FRAME_TITLE = "Demo"
FRAME_SIZE  = (300,200)

class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__( self,
                          None, -1, FRAME_TITLE,
                          size=FRAME_SIZE,
                          style=wx.DEFAULT_FRAME_STYLE )
        self.sizer = wx.BoxSizer( wx.VERTICAL )

        # put stuff into sizer

        # apply sizer
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.Show(1)

app = wx.PySimpleApp()
frame = AppFrame()
app.MainLoop()
