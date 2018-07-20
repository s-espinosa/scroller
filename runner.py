from lib.scrolling_message import ScrollingMessage
from lib.projector import Projector
from lib.message_service import MessageService
import time

def play(duration):
    ms   = MessageService()
    text = ms.text()
    sm   = ScrollingMessage(text)
    p    = Projector(sm)
    p.animate(duration)
    play(duration)

play(10)
