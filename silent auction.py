import os

def find_winner(bidder_details): #{karthi:100,siva:200}
    highest_bid = 0
    winner=""
    for bidder in bidder_details: #karthi
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(bidder_details)
    print(f"The winner is {winner} with the bid value of {highest_bid}!")
bidder_data={}
end_of_bidding = False
while not end_of_bidding:
    name=input("Enter your Name : ")
    price=int(input("Enter your Bid price : "))
    bidder_data[name] = price
    more_bidders=input("Are there more bidders? type 'yes' or 'no' :").lower()
    if more_bidders == 'no':
        end_of_bidding = True
        find_winner(bidder_data)
    elif more_bidders == "yes":
        os.system('cls')
