# Import os module
import os

def clear():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

import time

again = 'y'
while again == 'y':
   clear()

   print("Welcome to our secret BLIND AUCTION program")
   print('''                         ___________
                      \         /
                       )_______(
                       |"""""""|_.-._,.---------.,_.-._
                       |       | | |               | | ''-.
                       |       |_| |_             _| |_..-'
                       |_______| '-' `'---------'` '-'
                       )"""""""(
                      /_________\    
                      `'-------'`
                    .-------------.
                   /_______________\ \n''') 
   auction = {} # creating an empty dictionary to hold auctioneer and their bids for every new auction

   another = 'y' # for another auctioneer

   while another == 'y':
      name = input("What's your name? ").upper()
      bid = int(input("And what's your bid? "))

      auction[name] = bid
     
      another = input("Is there another bidder? Type 'Y' for YES | ANYTHING ELSE for NO: ").lower()
      clear()

   # most basic way
   """
   largest_name = ""

   for name in auction:
      if auction[name] > largest_bid:
         largest_name = name
   """
   # more elaborate, and shortcut
   max_name = max(auction, key = auction.get)
   
   print("All the bidders have placed their bids!\nAnd the winner is...")
   time.sleep(1)
   print(3)
   time.sleep(1)
   print(2)
   time.sleep(1)
   print(1)
   time.sleep(1)

   #print(f"\n{largest_name}!!! Congratulation {largest_name} with the winning bid for ${auction[largest_name]}") # easiest
   
   print(f"\n{max_name}!!! Congratulation {max_name} with the winning bid for ${auction[max_name]}")
   time.sleep(2)    
 
   again = input("\nThe auction has ended! Would you like to continue with another one? Type 'Y' for YES | ANYTHING ELSE for NO: ").lower()
