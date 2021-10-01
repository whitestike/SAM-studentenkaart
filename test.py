import pusher

def InitPusher():

    pusher_client = pusher.Pusher(
        app_id='1275452',
        key='92353ee8426715c5cc4f',
        secret='c5e4a1a431e5d39cdc8d',
        cluster='eu',
        ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})


InitPusher()