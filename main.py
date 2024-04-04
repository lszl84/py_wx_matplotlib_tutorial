import wx
import numpy as np
import matplotlib.figure
import matplotlib.backends.backend_wxagg

from utils import ensure_hdpi

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Sine Wave Plot in wxPython")

        self.panel = wx.Panel(self)

        self.figure = matplotlib.figure.Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = matplotlib.backends.backend_wxagg.FigureCanvasWxAgg(self.panel, -1, self.figure)

        frequency_label = wx.StaticText(self.panel, label="Frequency")

        frequency_slider = wx.Slider(self.panel, value=2, minValue=1, maxValue=20, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        frequency_slider.Bind(wx.EVT_SLIDER, self.on_frequency_change)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, self.FromDIP(5))
        sizer.AddSpacer(self.FromDIP(10))
        sizer.Add(frequency_label, 0, wx.ALIGN_CENTER)
        sizer.Add(frequency_slider, 0, wx.EXPAND | wx.ALL, self.FromDIP(5))
        sizer.AddSpacer(self.FromDIP(10))

        self.panel.SetSizer(sizer)

        self.SetSize(self.FromDIP((800, 600)))
        self.update_plot(frequency_slider.GetValue())


    def update_plot(self, frequency):
        AMPLITUDE = 2

        self.axes.clear()  # Clear existing plot

        t = np.linspace(0, 2, 1000)
        y = AMPLITUDE * np.sin(2 * np.pi * frequency * t)
        
        self.axes.plot(t, y, label=f'{AMPLITUDE} * sin(2π * {frequency}t)')
        self.axes.set_title('Sine Wave')
        self.axes.set_xlabel('Time (seconds)')
        self.axes.set_ylabel('Amplitude')
        self.axes.axhline(0, color='black', linewidth=0.5)
        self.axes.axvline(0, color='black', linewidth=0.5)
        self.axes.grid(color='gray', linestyle='--', linewidth=0.5)
        self.axes.legend(loc='upper right')
        
        self.canvas.draw()


    def on_frequency_change(self, event):
        frequency = event.GetInt()
        self.update_plot(frequency)


if __name__ == "__main__":
    app = wx.App(False)
    ensure_hdpi()

    frame = MainFrame()
    frame.Show()
    app.MainLoop()

