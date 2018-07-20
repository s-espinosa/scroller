from lib.scrolling_message import ScrollingMessage
from lib.projector import Projector

sm = ScrollingMessage("here is a message")
p  = Projector(sm)
p.animate()
