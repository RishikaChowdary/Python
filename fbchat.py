from fbchat import Client
from fbchat.models import Message
#credentials
username = "rishikapotturu@gmail.com"
password = "sourish1"
#login
client = Client(username,password)
#logout
client.logout()

#sending message to single user
client.send(Message(text='<message>'),thread_id='<user id>',thread_type=ThreadType.USER)
#sending message to a group
client.send(Message(text='<message>'),thread_id='<group id>',thread_type=ThreadType.GROUP)

#reacting to a message
message_id = client.send(Message(text='message'),thread_id=thread_id,thread_type=threadtype)
client.reactToMessage(message_id,MessageReaction.LOVE)

users=client.searchForUsers('<name of user>')
user=users[0]

#printing searched information
print("User's id: {}".format(user.uid))
print("User's name: {}".format(user.name))
print("User's profile picture url: {}".format(user.photo))
print("User's main url: {}".format(user.url))
