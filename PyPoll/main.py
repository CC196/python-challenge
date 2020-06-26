import os
import csv
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    total_cast = 0
    candidate_dic = {}
    for row in reader:
        total_cast += 1
        candidate = row[2]
        if candidate not in candidate_dic:
            candidate_dic[candidate] = 1
        else:
            candidate_dic[candidate] += 1

print("Election Results\n----------------------------")
print(f"Total Votes: {total_cast}\n----------------------------")            

candidate_percent = {}

for candidate in candidate_dic:
    percentage = candidate_dic[candidate]/total_cast*100
    candidate_percent[candidate] = percentage
    print(f"{candidate}: {round(percentage,3)}% ({candidate_dic[candidate]})")

winner = max(candidate_dic, key = candidate_dic.get)
print("----------------------------")
print(f"Winner: {winner}\n----------------------------")

filepath = "analysis/analysis.txt"
with open(filepath, 'w') as analysis:
    analysis.write("Election Results\n----------------------------\n")
    analysis.write(f"Total Votes: {total_cast}\n----------------------------\n")
    for candidate in candidate_dic:
        analysis.write(f"{candidate}: {round(candidate_percent[candidate],3)}% ({candidate_dic[candidate]})\n")
    analysis.write("----------------------------\n")
    analysis.write(f"Winner: {winner}\n----------------------------")
