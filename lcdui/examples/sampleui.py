import sys
sys.path.append('..')

from lcdui.devices import Generic, CrystalFontz, MatrixOrbital
from lcdui.ui import frame
from lcdui.ui import ui
from lcdui.ui import widget
import time

# device = Generic.MockCharacterDisplay(rows=2, cols=20)
# device = CrystalFontz.CFA635Display(port='/dev/ttyUSB0')
device = MatrixOrbital.MatrixOrbitalDisplay(port='/dev/ttyUSB0', baudrate=19200, rows=2, cols = 16)

device.ClearScreen()
device.BacklightEnable(True)

l = [
  '0b10001',
  '0b11111',
  '0b10001',
  '0b10001',
  '0b01010',
  '0b00100',
  '0b01010',
  '0b10001'
]

device.DefineChar('\x00', "".join("%c" % int(x,0) for x in l))

ui = ui.LcdUi(device)

f = ui.FrameFactory(frame.Frame)

line1 = f.BuildWidget(widget.LineWidget, row=0, col=0)
line1.set_contents("Hello, world! \x00")

line2 = f.BuildWidget(widget.LineWidget, row=1, col=10, span=6)
line2.set_contents("cutoffXXX")

ui.PushFrame(f)
ui.Repaint()

time.sleep(5)

f = ui.FrameFactory(frame.MenuFrame)

f.setTitle('example menu')
f.addItem(1, 'first choice')
f.addItem(2, 'second choice')
f.addItem(3, 'another choice')

f.addItem(4, 'last choice')

ui.PushFrame(f)
ui.Repaint()

for i in xrange(6):
  f.scrollDown()
  ui.Repaint()
  time.sleep(0.2)

for i in xrange(6):
  f.scrollUp()
  ui.Repaint()
  time.sleep(0.2)

f = ui.FrameFactory(frame.MultiFrame)

f1 = ui.FrameFactory(frame.Frame)
line1 = f1.BuildWidget(widget.LineWidget, row=0, col=0, contents="Page 1")

f2 = ui.FrameFactory(frame.Frame)
line2 = f2.BuildWidget(widget.LineWidget, row=0, col=0, contents="Page 2")

f.AddFrame(f1, 5)
f.AddFrame(f2, 2)

ui.PushFrame(f)

for i in xrange(15):
  ui.Repaint()
  time.sleep(1)
