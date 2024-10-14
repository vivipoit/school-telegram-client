print('generic imports')

import os
import json

print('telethon imports')

from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

print('start function')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    
    string = os.environ.get('SESSION_STRING')
    api_id = os.environ.get('API_ID')
    api_hash = os.environ.get('API_HASH')
    # print("environment: " + string + ", " + api_id + ", " + api_hash)
    
    body = json.loads(event['body'])
    course = body['course']
    course_id_string = str(course['id'])
    group_title = course['subject'] + " with " + course['teacher_email_address'] + " (#" + course_id_string + ")"
    print("group_title: " + group_title)
    
    with TelegramClient(StringSession(string), api_id, api_hash) as client:
        invited_users = client(CreateChatRequest([], group_title))
        chat = invited_users.updates.chats[0]
        # print("chat: " + chat.stringify())
        chat_invite_exported = client(ExportChatInviteRequest(peer=chat, title="join-course-" + course_id_string))
        invite_link = chat_invite_exported.link
        print("invite_link: " + invite_link)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "course": body['course'],
            "group": {
                "title": group_title,
                "invite_link": chat_invite_exported.link
            }
        })
    }