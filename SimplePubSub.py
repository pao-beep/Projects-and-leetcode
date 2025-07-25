class PubSub(object):
    topics ={}

    def __init__(self):
        self.topics = {}

    def suscribe(self,topic, callBack):
        if topic in self.topics:
            self.topics[topic].append(callBack)
        else:
            self.topics[topic] = []
            self.topics[topic].append(callBack)

    def publish(self,topic, message):
        if topic not in self.topics:
            return "topic not found"
        for callback in self.topics[topic]:
            callback(message)

    def unsuscribe(self,topic,callback):
        if self.topics[topic] and (callback in self.topics[topic]):
            self.topics[topic].remove(callback)

def handle_message1(message):
        print(f"Handler 1 received: {message}")

def handle_message2(message):
        print(f"Handler 2 received: {message}")

pubsub = PubSub()

pubsub.subscribe("news", handle_message1)
pubsub.subscribe("news", handle_message2)
pubsub.subscribe("events", lambda msg: print(f"Event: {msg}"))

pubsub.publish("news", "Breaking news: A new library is born!")
pubsub.publish("events", "Annual meeting next week.")

pubsub.unsubscribe("news", handle_message1)
pubsub.publish("news", "Another news item")  # only handle_message2 will be called

