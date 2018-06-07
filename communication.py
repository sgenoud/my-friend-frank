import twitter

api = twitter.Api(
    consumer_key="XXXX",
    consumer_secret="XXXX",
    access_token_key="XXXX",
    access_token_secret="XXXX"
)


def say(message):
    api.PostUpdate(status=message)
    return "ok"


def reply(message, to):
    api.PostUpdate(status=message, in_reply_to_status_id=to, auto_populate_reply_metadata=True)
    return "ok"


def listen(since):
    return ((message.id, message.text.replace("@ProtoSwiss", "").strip())
            for message in api.GetMentions(since_id=since))
