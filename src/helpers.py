from models.receipt import Receipt
from datetime import datetime
import math

def calculatePoints(receipt: Receipt):
    points = 0

    for ch in receipt.retailer:
        if ch.isalpha():
            points += 1
    print(points)
    
    totalAmount = receipt.totalAmount
    # 50 points if the total amount of the receipt is a round dollar number without cents
    if totalAmount // 1 == totalAmount:
        points += 50
    
    # 25 points if total amount is a multiple of 0.25 
    if totalAmount % 0.25 == 0:
        points += 25
    
    # 5 points for each item pair
    items = receipt.items
    numItemPairs = len(items) // 2
    points += (5 * numItemPairs)

    # If the trimmed length of item description is a multiple of 3, add 0.2 * price of the item to points
    for item in items:
        trimmedItemDescription = item.description.strip()
        if len(trimmedItemDescription) % 3 == 0:
            points += math.ceil(0.2 * item.price)
    
    # 6 points if the day in the purchase date is odd
    purchaseDate = datetime.fromisoformat(receipt.purchaseDate)
    if purchaseDate.month % 2 == 1:
        points += 6
    
    # 10 points if the purchase time is after 2pm and before 4pm
    purchaseTime = receipt.purchaseTime
    if purchaseTime > "14:00" and purchaseTime < "16:00":
        points += 10

    return points


    

