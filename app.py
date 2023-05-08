import pandas as pd
import sqlalchemy as sql
import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import questionary
import fire

# MVP APPLICATION MODEL****

# Start application

# Prompt to user - "Hello welcome to app"

# Propt user actions 
	# option 1 - sharpe ratio module name (prompt only 5 stocks for simplicity)
		# check for correct stock input (is stock input correct) choose from list of stock
	#  
	# option 2 monte carlo simulation module

# Condtional statement
	# if user chooses option 1
		# prompt user for ticker symbol ( Print ticker symbols for user )
		# run ratio and show metric results (** user will be able to weigh risk vs. reward **)
		# At end of module prompt user for another ticker ratio (**DO YOU WANT TO LOOK UP ANOTHER STOCK **
			# if yes, loop over option 1
			#  if no, prompt user to add stock to a list, then send back to module 1 - prompt user actions 

			# **** if MVP met then we will implement stock comparing model ****


	# if user chose option 2
		# run function monte carlo ( Print ticker symbols user chose and all metric inputs in order to run simulation )
			# Parameters inputs = initial investment, number of years/days, stocks, weight of stocks, investor goals

			# conditional statement  
			# prompt user if choices specified are correct
			# show results of simulations 

			# conditional statement
				# Prompt user - 'your investor goals are above or below results?' , 
				# 'do you want change inputs and re-run simulation?' 
					# if yes, send back to beginning of monte carlo simulation
					# if no, 'Oh glad youre happy with results,
					
					# conditional statement
						# do you want to add to your portfolio?'
						# if yes, print 'thank you for using our application, bye bye'
						# if no, 'try again later, thank you :)'







def run_crud(message="Hello, we can suggest you next stocks: AAPL, TSLA"):
	print(message)
if __name__ == '__main__':
	fire.Fire(run_crud)
    
table_name = questionary.text("What stock do you want to choose to see Sharpe Ratio?").ask()
                              
print(table_name)