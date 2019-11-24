

import pandas as pd
import csv
import os



#path
csv_path ='budget_data.csv'



#read csv
py_bank_df = pd.read_csv(csv_path)

py_bank_df.head()



#get total months
month_count = py_bank_df['Date'].count()
month_count



#total revenue(profit/loss)
total_profit_loss = py_bank_df['Profit/Losses'].sum()
total_profit_loss



#average change of profit
Profit_Loss_Diff = py_bank_df["Profit/Losses"].diff().mean()

Profit_Loss_Diff


#greatest increase and decrease 

greatest_increase = py_bank_df["Profit/Loss Diff"].max()
greatest_decrease = py_bank_df["Profit/Loss Diff"].min()

greatest_increase_row = py_bank_df.loc[py_bank_df["Profit/Loss Diff"]==greatest_increase,"Date"]
greatest_decrease_row = py_bank_df.loc[py_bank_df["Profit/Loss Diff"]==greatest_decrease,"Date"]

greatest_decrease_date = greatest_decrease_row.iloc[0]
greatest_increase_date = greatest_increase_row.iloc[0]

print(greatest_decrease_date, greatest_increase_date)



print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_profit_loss}")
print(f"Average Revenue Change: ${Profit_Loss_Diff}")
print(f"Greatest Increase: {greatest_increase}({greatest_increase_date})")
print(f"Greatest Decrease: {greatest_decrease}({greatest_decrease_date})")

