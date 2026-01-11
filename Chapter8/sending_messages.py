messages = ['hello', 'how are you', 'i have been living in italy now', 
            'i miss you', 'i\'ll be coming back home soon', 'wanna hang out'
            ' like in the old times?']

sent_messages=[]

def send_message(messages, sent_messages):
    while messages:
        print(messages[0])
        sent_messages.append(messages[0])
        messages.pop(0)

send_message(messages, sent_messages)
print(messages)
print(sent_messages)