import csv
import os

#file to load
file_to_load = os.path.join("election_data.csv")

#declaring variables to store data

candidate_list = {}
winner = ""
winner_count = []

county_list = []
voter_list = []
#reading the csv
 
vote_count = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    #skip the header row
    header = next(reader)
    print(header)
    for row in reader:
        try:
            candidate_list[row[2]]+= 1
        except:
            candidate_list[row[2]]= 1
        #breaking down each column
        vote_count += 1

print(f'voter count is {vote_count}')
print(candidate_list['Correy'])
