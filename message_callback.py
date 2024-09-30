def on_message(topic, message):
    # Perform desired actions based on the subscribed topic and response
    print('Received message on topic:', topic)
    print('Response:', message)
    if message in {b'cooling', b'heating', b'idle'}:
        print('Response:', message)
    else:
        print('Unknown command')
        return None
    return message
