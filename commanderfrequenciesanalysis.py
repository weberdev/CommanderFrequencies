import csv
file_path = "commanderfrequencies.csv"

#the first thing to do is compress data so that partner commanders are only tracked by color identity
#we make the sacrifice of accuracy by assuming that, for example:
#The Tenth Doctor // Rose Tyler decks and The Tenth Doctor // Jo Grant decks are the same archetype
compressed_data = {}
#then we compress it further
#The Tenth Doctor // Rose Tyler and The Tenth Doctor // Martha Jones decks are now the same archetype as well
#I'll avoid giving an opinion on which is better because I'd like to keep my job.
name_only_compressed_data = {}

#We open the nicely processed CSV file
with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    #we read the CSV file into a list
    for row in csv_reader:
        if len(row) == 3:
            color_identity, commander_name, deck_frequency = row
            try:
                deck_frequency = int(deck_frequency)
                #basic data compression for color identiy and name
                key = (color_identity, commander_name)
                if key in compressed_data:
                    compressed_data[key] += deck_frequency
                else:
                    compressed_data[key] = deck_frequency

                #secondary data compression solely for name
                #partner makes this far more complicated than it needs to be
                #I'll say that I don't like it
                #because I might be a magic boomer now
                #I started in Zendikar
                if commander_name in name_only_compressed_data:
                    name_only_compressed_data[commander_name] += deck_frequency
                else:
                    name_only_compressed_data[commander_name] = deck_frequency
            except ValueError:
                print(f"Invalid number format in row: {row}")

#Dictinaries are moved back to lists
compressed_commander_data = [(color, commander, freq) for (color, commander), freq in compressed_data.items()]
name_only_compressed_data_list = [(commander, freq) for commander, freq in name_only_compressed_data.items()]

#not that commander data
#this is not what peak performance looks like
sorted_commander_data = sorted(compressed_commander_data, key=lambda x: x[2], reverse=True)
num_decks = 0
# Print the sorted data with consistent double quotes
for color, commander, freq in sorted_commander_data:
    print(f"\"{color}\", \"{commander}\", {freq}")
    num_decks += freq

print(num_decks)
average_num_decks = num_decks / len(sorted_commander_data)
print(average_num_decks)
print()

#Solely getting frequency of commanders now
#More interesting from a uniqueness perspective, maybe not from a gameplay perspective
#I honestly don't know
#If I could get better data on partner frequency I could do more.
#I'll do that later.
sorted_name_only_data = sorted(name_only_compressed_data_list, key=lambda x: x[1], reverse=True)
num_decks_name_only = 0
for commander, freq in sorted_name_only_data:
    print(f"\"{commander}\", {freq}")
    num_decks_name_only += freq

average_num_decks_name_only = num_decks_name_only / len(sorted_name_only_data)
print(num_decks_name_only)
print(average_num_decks_name_only)
