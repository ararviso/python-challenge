
import pandas as pd



#path
csv_path ='election_data.csv'


#read csv
py_poll_df = pd.read_csv(csv_path)

py_poll_df.head()



#The total number of votes cast
vote_counts = py_poll_df["Voter ID"].count()
vote_counts



#A complete list of candidates who received vote
candidate = py_poll_df["Candidate"].unique()
candidate



#The total number of votes each candidate won
candidate_counts = py_poll_df["Candidate"].value_counts()
candidate_counts.head()



#percentage votes for each candidate
#percent_of_votes = {candidate_counts}/{vote_counts} * 100
#print(f"{candidate}: {int(percent_of_votes)}% {votes_counts}")



#The winner of the election based on popular vote
winner = py_poll_df["Candidate"].max()
winner



print("Election Results")
print("-------------------------")
print(f"Total Votes:{vote_counts}")
print("-------------------------")
print(f"candidate:{candidate_counts}")
print(f"Winner: {winner}")
print("--------------------------")

