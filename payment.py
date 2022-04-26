class Payment(object):
    chat_id = None
    send = None
    product = None

    def __init__(self, row):
        self.chat_id = row["chat_id"]
        self.send = row["send"]
        self.product = row["product"]
