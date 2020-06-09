#load csv
import os
import csv

#Path to collect data
election_data_csv="C:/Users/Keke/git/python_challenge/PyPoll/Resources/election_data.csv"

#define variables
totalvotes= 0
#define column 3 as a dict to refer to occurence number of votes
candidates={}
#define value in column 3 as a list to cross reference to values
candidate= []

percentage=0

#read csv file
with open(election_data_csv)as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #skip header row
    csv_header = next(csvfile)


    print(f"Election Results")
    print("\n------------------------------------")  


    for row in csv.reader(csvfile):
        #total casts
        totalvotes += 1

        candidate = row[2]
        #voterid=row[0]

        #calculate each candidate votes,if candidate name is not in the list
        if candidate not in candidates:
            #then the candidate will equal to it's name only
        
            candidates[candidate]=1
        else:
            #otherwise each appearance will add to next appearance of the same candidate name
            candidates[candidate]+=1

    print(f"Total Votes:{totalvotes}")
    print("\n------------------------------------")  
    #print(f"{candidates}")

    # vote%= votes/totalvotes *100
    for candidate in candidates:
        #define a shorter name to refer in below function
        votes=candidates[candidate]
         
        #percentage= float(votes)/ float(totalvotes) * 100
    for key in candidates:
        percentage= candidates[key]/totalvotes*100 
        
        #print(key +':'+ str("{0:.3f}%".format(percentage))+'('+str(candidates[key])+')')
        #print(f"{percentage:,.3f}%".format(percentage))
        print(f"{key}:{percentage:,.3f}% ({str(candidates[key])})")
    
    #the highest votes
    Winner= max(candidates,key=candidates.get)

    print("\n------------------------------------") 
    print(f"Winner:{Winner}")  
    print("\n------------------------------------") 

text =(

    f"Election Results\n"
    f"------------------------------------\n"
    f"Total Votes:{totalvotes}\n"
    f"------------------------------------\n")

#set a new STRING variable to loop different names in the list ''is to including numbers, text,etcs
stringer=''
#set a new for statement to search for string of names

for key in candidates:   
    percentage= candidates[key]/totalvotes*100
    stringer+= f"{key}:{percentage:,.3f}% ({str(candidates[key])})\n"
   
  
text2 =(
    f"------------------------------------\n"
    f"Winner:{Winner}\n"
    f"------------------------------------\n")
#split the answer into 2 parts and combine at the end
Finaltext=text+stringer+text2

# Export the results to text file
Final= open('C:/Users/Keke/git/python_challenge/PyPoll/analysis/Final.text', 'w')
#the final answer should be output into the text file
Final.write(Finaltext)
Final.close()




