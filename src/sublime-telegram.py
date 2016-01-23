import sublime, sublime_plugin
from pytg import Telegram
import sys
from pytg.sender import Sender
from pytg.receiver import Receiver

reload(sys)
sys.setdefaultencoding('utf-8')

class TelegramCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print("alala")
    connect_to_telegram()

  def connect_to_telegram(self):
    receiver = Receiver(host="localhost", port=9091)
    sender = Sender(host="localhost", port=9091)

    sender.send_msg(u'USERNAME', u'Hello World!')
    list = sender.contacts_list() 
    print(list)
