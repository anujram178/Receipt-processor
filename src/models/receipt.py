from models.item import Item


class Receipt:
    def __init__(self, receiptPayload):
        self.retailer = receiptPayload["retailer"]
        self.purchaseDate = receiptPayload["purchaseDate"]
        self.purchaseTime = receiptPayload["purchaseTime"]
        self.items = [Item(i) for i in receiptPayload["items"]]
        self.totalAmount = float(receiptPayload["total"])

