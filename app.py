import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import  alpaca_trade_api as tradeapi
import fire
import questionary
# from MCForecastTools import MCSimulation

load_dotenv("api.env")

alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

# Global Variables
user_name = ""
favorited_stocks = []


# User intro functionality
def user_intro():
    print("\nWelcome to your portfolio planner.\n")
    print("Here our goal is to help you search, learn, and choose stock that will diversify your future.\n")
    print("Please follow the prompts and answer our very important questions. Your answers will help us get all the important portfolio data you will need to for making promising financial investment choices.\n")

    name = questionary.text("What name should we call you by?").ask()
    user_name = name

    print(f"\nHello {user_name}! Welcome to your portfolio planner!\n")
    

# Sharpe ratio functionality
def get_sharpe_ratio(ticker):
    
    # Api dat information inputs
    timeframe = "1Day"
    start_date = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2023-05-03", tz="America/New_York").isoformat()
    
    # Api data to dataframe
    df = alpaca.get_bars(
    ticker,
    timeframe,
    start=start_date,
    end=end_date
    ).df
    
    # Data return computations
    daily_returns = df['close'].pct_change().dropna()
    annual_average_return = daily_returns.mean() * 1260
    annual_standard_deviation = daily_returns.std() * np.sqrt(1260)
    sharpe_ratio = annual_average_return / annual_standard_deviation
    
    print(f"Sharpe ratio for {ticker} is {sharpe_ratio : .02f}.")


# Application run functionality    
def run():
    if user_name == "":
        user_intro()
    
    cruddy_cli_running = True
    
    # Dictionary with provided stock names and ticker symbols
    stocks = {
        "Apple Inc" : "AAPL",
        "Amazon.com Inc" : "AMZN",
        "Tesla Inc" : "TSLA",
        "Johnson & Johnson" : "JNJ",
        "Pfizer Inc" : "PFE",
        "Morgan Stanley" : "MS",
        "Coinbase Gllobal Inc" : "COIN",
        "Visa Inc" : "V",
        "American Express Company" : "AXP",
        "Paypal Holding Inc" : "PYPL",
        "General Electric Company" : "GE",
        "Delta Air Lines Inc" : "DAL",
        "Exxon Mobil Corp" : "XOM"
    }

    while cruddy_cli_running:
        choice = questionary.select(
            "Where would you like to continue?",
            choices=["Research Stocks", "Run Monte Carlo Simulation", "Favorites List", "Quit"]
        ).ask()
        
        if choice == "Research Stocks":
            print("\nHere you can choose a stock to research\n")
            print("If you are satisfied with the data you can add it to your favorites or move on to the next module\n")
            
            continue_answer = questionary.select("Shall we continue?\n", choices = ["Yes", "No"]).ask()
            if continue_answer == "No":
                cruddy_cli_running = False
                print("\nThank you for using the CRUDdy CLI! Goodbye!")
                break
                                                 
            choice = questionary.select(
                f"{user_name} what stocks would you like to review?", 
                choices = [ 
                    "Apple Inc",
                    "Amazon.com Inc",
                    "Tesla Inc",
                    "Johnson & Johnson",
                    "Pfizer Inc",
                    "Morgan Stanley",
                    "Coinbase Gllobal Inc",
                    "Visa Inc",
                    "American Express Company",
                    "Paypal Holding Inc",
                    "General Electric Company",
                    "Delta Air Lines Inc",
                    "Exxon Mobil Corp",
                    "QUIT - not stock :("
                ]).ask()
            
            if choice != "QUIT - not stock :(":
                get_sharpe_ratio(stocks[choice])
                favorite_stock = questionary.select("\nWould you like to add to favorites?\n", choices = ["Yes", "No"]).ask()
                
                # Add stock to favorites list
                if favorite_stock == "Yes":
                    if stocks[choice] not in favorited_stocks:
                        favorited_stocks.append(stocks[choice])
                    else:
                        print("stock is already in favorites\n")
                
            else:
                cruddy_cli_running = False
                print("\nThank you for using the CRUDdy CLI! Goodbye!")
        
        elif choice == "Favorites List":
            if favorited_stocks == []:
                print("Favorites list is empty\n")
            else:
                for stock in favorited_stocks:
                    print(stock)
            
        else:
            cruddy_cli_running = False
            print("\nThank you for using the CRUDdy CLI! Goodbye!")
        
                                                 
                                                 
if __name__ == "__main__":
    fire.Fire(run)
    
    
    
    
    
# import pandas as pd
# import sqlalchemy as sql
# import os
# import alpaca_trade_api as tradeapi
# from dotenv import load_dotenv
# import questionary
# import fire

# # MVP APPLICATION MODEL****

# # Start application

# def portfolio_app():
#     user_name = ""
	
    
#     # User intro functionality
#     def user_intro():
#         print("\nWelcome to your portfolio planner.\n")
#         print("Here our goal is to help you search, learn, and choose stock that will diversify your future.\n")
#         print("Please follow the prompts and answer our very important questions. Your answers will help us get all the important portfolio data you will need to for making promising financial investment choices.\n")
        
#         name = questionary.text("What's your first name").ask()
#         user_name = name
        
#         print(f"Hello {user_name}! Welcome to your portfolio planner!")
        
#         module = questionary.select("Would you like to enter Module 1 and find out current data or enter Module 2 and forecast for relevent data", choices=["Module 1", "Module 2", "Exit App"]).ask()
        
#         if module == "Module 1":
#             module_one()
#         else:
#             module_two()
       
    
#     # Module 1 functionality
#     def module_one():
        
#         # Prompt stock choices
#         stock_choice = questionary.select("Which stocks would you like to explore?", choices = ["TSLA", "AMZN"])ask()
    
    
#     # API functionality
#     def call_api(tick, time, date_one, date_two):
#         # Load .env environment variables
#         load_dotenv('api.env')

#         # Set Alpaca API key and secret
#         alpaca_api_key = os.getenv("ALPACA_API_KEY")
#         alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

#         # Create the Alpaca API object
#         alpaca = tradeapi.REST(
#             alpaca_api_key,
#             alpaca_secret_key,
#             api_version="v2")

#         # Get required user inputs
#         tickers = tick
#         timeframe = time
#         start_date = pd.Timestamp(date_one, tz="America/New_York").isoformat()
#         end_date = pd.Timestamp(date_two, tz="America/New_York").isoformat()

#         # Get Data From Alpaca
#         alpaca_data = alpaca.get_bars(
#             tickers,
#             timeframe,
#             start = start_date,
#             end = end_date
#         )

# # Prompt to user - "Hello welcome to app"
# # table_name = questionary.text("What stock do you want to choose to see Sharpe Ratio?").ask()


# # Propt user actions 
# 	# option 1 - sharpe ratio module name (prompt only 5 stocks for simplicity)
# 		# check for correct stock input (is stock input correct) choose from list of stock
# 	#  
# 	# option 2 monte carlo simulation module

# # Condtional statement
# 	# if user chooses option 1
# 		# prompt user for ticker symbol ( Print ticker symbols for user )
# 		# run ratio and show metric results (** user will be able to weigh risk vs. reward **)
# 		# At end of module prompt user for another ticker ratio (**DO YOU WANT TO LOOK UP ANOTHER STOCK **
# 			# if yes, loop over option 1
# 			#  if no, prompt user to add stock to a list, then send back to module 1 - prompt user actions 

# 			# **** if MVP met then we will implement stock comparing model ****


# 	# if user chose option 2
# 		# run function monte carlo ( Print ticker symbols user chose and all metric inputs in order to run simulation )
# 			# Parameters inputs = initial investment, number of years/days, stocks, weight of stocks, investor goals

# 			# conditional statement  
# 			# prompt user if choices specified are correct
# 			# show results of simulations 

# 			# conditional statement
# 				# Prompt user - 'your investor goals are above or below results?' , 
# 				# 'do you want change inputs and re-run simulation?' 
# 					# if yes, send back to beginning of monte carlo simulation
# 					# if no, 'Oh glad youre happy with results,
					
# 					# conditional statement
# 						# do you want to add to your portfolio?'
# 						# if yes, print 'thank you for using our application, bye bye'
# 						# if no, 'try again later, thank you :)'




    
# if __name__ == '__main__':
# 	fire.Fire(portfolio_app)