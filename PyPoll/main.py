# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import string
import csv
import array as my_array

#definig the input and output file paths. 
#due to runtime error, I had to use absoulte addressing than the prefferred relative one

file_to_load = "c:/Users/elija/Desktop/Class_Room/Python-challenge/Python-challenge/PyPoll/Resources/election_data.csv"
file_to_output = os.path.join("c:/Users/elija/Desktop/Class_Room/Python-challenge/Python-challenge/PyPoll/Analysis", "Election_result.txt")

Total_votes_number=0
array_len=0
candidates_list=[]
total_vote_by_candidate=[]
candidate_name=0
vote_by_candidate=[[],[]]
a=0

#section to load the input data from the csv file
with open (file_to_load) as election_data:
    reader=csv.reader(election_data)
    next(reader) #code to skip the header
    
    for row in reader:
        #counting the number of votes adn appending a list the names of candidates
        Total_votes_number=Total_votes_number + 1 
        candidates_list.append(str(row[2]))
        array_len=len(candidates_list)

#sorting the candidate makes it to remove the duplication       
candidates_list.sort()
array_len=len(candidates_list)
j=0

while j<array_len:
   
    if j==(array_len-1):
        break
    else:
        if candidates_list[j+1] == candidates_list[j]:
           candidates_list.pop(j+1)
        else:
           j=j+1
    array_len=len(candidates_list)

#section to calculate the total vote by candidate
total_vote=0   
for i in range(0,array_len):
    with open (file_to_load) as election_data:
       reader=csv.reader(election_data)
       next(reader) #code to skip the header
       total_vote=0
       for row in reader:   
           if row[2]==candidates_list[i]:
               total_vote=total_vote + 1
    
    total_vote_by_candidate.append(total_vote)

#two dimensional list to hold both Candidate name and their respective total vote
for k in range(0,array_len):
    vote_by_candidate[0].append(candidates_list[k])
    vote_by_candidate[1].append(total_vote_by_candidate[k])

index=0
winner_1_name=vote_by_candidate[0][0]
winner_1_vote=vote_by_candidate[1][0]
winner_1_vote_percent=0
for k in range(0,array_len):
    if vote_by_candidate[1][k]>winner_1_vote:
        winner_1_vote=vote_by_candidate[1][k]
        winner_1_name=vote_by_candidate[0][k]
        index=k

vote_by_candidate[1][index]=0   
winner_1_vote_percent=round((winner_1_vote/Total_votes_number)*100,3)

index=0
winner_2_name=vote_by_candidate[0][0]
winner_2_vote=vote_by_candidate[1][0]
winner_2_vote_percent=0
for l in range(0,array_len):
    if vote_by_candidate[1][l]>winner_2_vote:
        winner_2_vote=vote_by_candidate[1][l]
        winner_2_name=vote_by_candidate[0][l]
        index=l

vote_by_candidate[1][index]=0      
winner_2_vote_percent=round((winner_2_vote/Total_votes_number)*100,3)      

index=0
winner_3_name=vote_by_candidate[0][0]
winner_3_vote=vote_by_candidate[1][0]
winner_3_vote_percent=0
for k in range(0,array_len):
    if vote_by_candidate[1][k]>winner_3_vote:
        winner_3_vote=vote_by_candidate[1][k]
        winner_3_name=vote_by_candidate[0][k]
        index=k

vote_by_candidate[1][index]=0       
winner_3_vote_percent=round((winner_3_vote/Total_votes_number)*100,3)     

index=0
winner_4_name=vote_by_candidate[0][0]
winner_4_vote=vote_by_candidate[1][0]
winner_4_vote_percent=0
for k in range(0,array_len):
    if vote_by_candidate[1][k]>winner_4_vote:
        winner_4_vote=vote_by_candidate[1][k]
        winner_4_name=vote_by_candidate[0][k]
        index=k
vote_by_candidate[1][index]=0      
winner_4_vote_percent=round((winner_4_vote/Total_votes_number)*100,3)     

print("Election Results")
print("..............................")
print(f"Total Votes: {str(Total_votes_number)}")    
print(f"Total Candidates: {str(array_len)}")
print("..............................")
print(f"{winner_1_name}: {winner_1_vote_percent}% ({winner_1_vote})")
print(f"{winner_2_name}: {winner_2_vote_percent}% ({winner_2_vote})")
print(f"{winner_3_name}: {winner_3_vote_percent}% ({winner_3_vote})")
print(f"{winner_4_name}: {winner_4_vote_percent}% ({winner_4_vote})")
print("..............................")
print(f"Winner: {winner_1_name}")
print("..............................")


#section to write the result analysis to a text file
with open(file_to_output, "w") as pyfile:
    pyfile.write("Election Results\n")
    pyfile.write("..............................\n")
    pyfile.write(f"Total Votes: {str(Total_votes_number)}\n")    
    pyfile.write("..............................\n")
    pyfile.write(f"{winner_1_name}: {winner_1_vote_percent}% ({winner_1_vote})\n")
    pyfile.write(f"{winner_2_name}: {winner_2_vote_percent}% ({winner_2_vote})\n")
    pyfile.write(f"{winner_3_name}: {winner_3_vote_percent}% ({winner_3_vote})\n")
    pyfile.write(f"{winner_4_name}: {winner_4_vote_percent}% ({winner_4_vote})\n")
    pyfile.write("..............................\n")
    pyfile.write(f"Winner: {winner_1_name}\n")
    pyfile.write("..............................")
