from lib.scrolling_message import ScrollingMessage
from lib.projector import Projector

sm = ScrollingMessage("HELLO WORLD <")
p  = Projector(sm)
p.animate()
