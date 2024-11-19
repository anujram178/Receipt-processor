class Item:
    def __init__(self, item):
        self.description = item["shortDescription"]
        self.price = float(item["price"])