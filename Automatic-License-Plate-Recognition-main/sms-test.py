

from twilio.rest import Client

accountSID = 'AC5ccaffc385de1769ae92daf29d7b34fc'
token = '1c86b06aa20213bac6727c1fd9c9d42d'

client = Client(accountSID, token)

message = client.messages.create(body='Test SMS hahah', from_='+12313891114', to='+251933019593')

print("The license plate is:",message.sid)