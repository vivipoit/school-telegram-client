import os

string = os.environ.get('SESSION_STRING')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

print("environment: " + string + ", " + api_id + ", " + api_hash)

from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

with TelegramClient(StringSession(string), api_id, api_hash) as client:
  invited_users = client(CreateChatRequest([], 'test group'))
  chat = invited_users.updates.chats[0]
  print(chat.stringify())
  chat_invite_exported = client(ExportChatInviteRequest(peer=chat, title="join-test-group"))
  print(chat_invite_exported.link)
