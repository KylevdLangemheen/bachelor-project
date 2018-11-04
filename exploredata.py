import readdata

dataLocation = "HA_t_complete_human.fasta"
dataobj = readdata.readData(dataLocation,["host","fasta"])
dataobj.cleanHost()
x,y = dataobj.sepDataLabels()

mammal = ["Sea_Mammal","Human","Swine","Dog","Domestic_Cat","Large_Cat","Civet","Bat","Donkey","Equine","Horse","Ferret","Flat_Faced_Bat",
"Sloth","Panda","Lion","little_yellow_shouldered_bat","mink","Mink","Weasel","Muskrat","Rat","Pika","Plateau_Pika","Raccoon_Dog","Skunk",
"sloth_bear","tiger","Camel"]

bird = ["Adelie_Penguin","African_Starling","African_Stonechat","American_Black_Duck","American_Coot","Coot","Avian","Green_Winged_Teal",
"American_Green_Winged_Teal", "Eurasian_Teal","Mallard","Oystercatcher","American_White_Pelican","American_Wigeon","American_Widgeon",
"Northern_Pintail","Green_Winged_Teal_","Cinnamon_Teal","Blue_Winged_Teal_","Blue_Winged_Teal","Duck","Goose","Waterfowl","Crane",
"Aquatic_Bird","Bird","Grey_Heron","Australian_Shelduck","Pochard","Baikal_Teal","Bald_Eagle","Bantam","Bar_Headed_Goose","Barn_Swallow",
"Barnacle_Goose","Bewick's_Swan","Bewick'S_Swan","Chicken","Black_Duck","Black_Headed_Gull","Black_Scoter","Skimmer","Swan","Black_Billed_Magpie",
"Heron","Gull","Black_Legged_Kittiwake","Black_Neck_Crane","Black_Necked_Grebe","Black_Necked_Stilt","Godwit","Blackbird","Flycatcher",
"Finch","Breeder_Duck","Broiler_Duck","Brown_Headed_Gull","Budgerigar","Bufflehead","Bulbul","Common_Buzzard","California_gull",
"Canada_Goose","Canvasback","Crow","Teal","Pigeon","Silky_Chicken","Yellow_Billed_Teal","Chinese_Francolin","Babbler","Chinese_Pond_Heron",
"Penguin","Chukar","Common_Coot","Cormorant","Common_Eider","Common_Goldeneye","Mew_Gull","Common_Iora_","Kestrel","Moorhen","Common_Murre",
"Common_Myna","Common_Pochard","Common_Scoter","Shelduck","Condor","Parrot","Hawk","Eagle","Crested_Myna","Whooper_Swan","Mute_Swan",
"Cygnus_Olor","Double_Crested_Cormorant","Dove","Muscovy_Duck","Dunlin","Eagle_Owl","Eastern_Buzzard","Egret","Tern","Emu","Eurasian_Coot",
"Curlew","Eurasian_Eagel_Owl","Eurasian_Wigeon","European_Herring_Gull","Fairy_Bluebird","Falcon","Feral_Pigeon","Fowl","Franklin's_Gull",
"Gadwall","Garganey","Guineafowl","Glaucous_Gull","Golden_Pheasant","Common_Merganser","Goshawk","Plover","Gray_Teal","Grey_Crowned_Crane",
"Great_Barbet","Great_Black_Headed_Gull","Great_Crested_Grebe","Grebe","Great_Horned_Owl","Greater_Scaup","Greater_White_Fronted_Goose",
"Green_Peafowl","Spot_Billed_Duck","Grey_Faced_Buzzard","Greylag_Goose","Guillemot","Guinea_Fowl","Guinea","Helmeted_Guineafowl","Herring_Gull",
"Myna","Black_Winged_Stilt","Hooded_Merganser","Horned_Puffin","Houbara_Bustard","House_Crow","Iceland_Gull","Peafowl","Japanese_Quail",
"Quail","Japanese_White_Eye","Kalij_Pheasant","Kelp_Gull","Knot","Laughing_Gull","Least_Sandpiper","Lesser_Kestrel","Lesser_Scaup",
"Lesser_Snow_Goose","Snow_Goose","Little_Egret","Little_Grebe","Little_Tern","Long_Tailed_Duck","Macaw","Magpie_Robin","Mallard_Duck",
"Mallard_Black_Duck_Hybrid","Stork","Smew","Murre","Loriinae","Northern_Shoveler","Northern_Shov","Openbill_Stork","Ostrich","Owl",
"Pacific_Golden_Plover","Parakeet","Partridge","Peacock","Pekin_Robin","Pelican","Peregrine_Falcon","Pheasant","Magpie","Pink_Footed_Goose",
"Pintail","Pintail_Duck","Poultry","Red_Crested_Pochard","Red_Knot","Red_Billed_Teal","Red_Necked_Stint","Redhead_Duck","Redhead","Rhea",
"Ring_Necked_Duck","Ring_Billed_Gull","Rook","Rosy_Billed_Pochard","Ruddy_Turnstone","Rufous_Necked_Stint","Ibis","Saker_Falcon","Sanderling",
"Sandpiper","Munia","Scaup","Scoter","Semipalmated_Sandpiper","Stint","Sharp_Tailed_Sandpiper","Shearwater","Shorebird","Shoveler","Shrike",
"Slaty_Backed_Gull","Slender_Billed_Gull","Snipe","Snowy_Owl","Softbill","Sooty_Tern","Sparrow","Spur_Winged_Goose","Starling","Scooter",
"Swiftlet","Sandgrouse","Common_Tern","Thrush","Tree_Sparrow","Tufted_Duck","Tufted_Duck_","Tundra_Swan","Turkey","Turtledove","Velvet_Scoter",
"Wedge_Tailed_Shearwater","Whiskered_Tern","White_Bellied_Bustard","White_Peafowl","White_Rumped_Munia","White_Fronted_Goose","White_Rumped_Sandpiper",
"White_Winged_Scoter","Widgeon","Wild_Chicken","Wild_Duck","Wood_Duck","Yellow_Billed_Duck","Yellow_Billed_Pintail"]

duck = ["American_Black_Duck","Green_Winged_Teal","American_Green_Winged_Teal", "Eurasian_Teal","Mallard","American_Wigeon","American_Widgeon",
"Northern_Pintail","Green_Winged_Teal_","Cinnamon_Teal","Blue_Winged_Teal_","Blue_Winged_Teal","Waterfowl","Australian_Shelduck",
"Pochard","Baikal_Teal","Bantam","Black_Duck","Black_Scoter","Breeder_Duck","Broiler_Duck","Bufflehead","Canvasback","Teal","Yellow_Billed_Teal",
"Common_Eider","Common_Pochard","Common_Scoter","Shelduck","Muscovy_Duck","Eurasian_Wigeon","Gadwall","Garganey","Common_Merganser","Gray_Teal",
"Greater_Scaup","Spot_Billed_Duck","Hooded_Merganser","Lesser_Scaup","Long_Tailed_Duck","Mallard_Duck",
"Mallard_Black_Duck_Hybrid","Smew","Northern_Shoveler","Northern_Shov","Pintail","Pintail_Duck","Red_Crested_Pochard","Red_Billed_Teal",
"Redhead_Duck","Redhead","Ring_Necked_Duck","Rosy_Billed_Pochard","Scaup","Scoter","Shoveler","Scooter","Tufted_Duck","Tufted_Duck_","Velvet_Scoter",
"White_Winged_Scoter","Widgeon","Wild_Duck","Wood_Duck","Yellow_Billed_Duck","Yellow_Billed_Pintail","Common_Goldeneye"]

other = ["Unknown","Insect","Environment","Laboratory_derived","environmment","LAB"]

unique = []
for label in y:
    if label["host"] not in unique:
        unique.append(label["host"])

hosts = []
for item in y:
    hosts.append(item["host"])

threshold = 200 #10/25 20/18 30/14 40/12 50/12 60/11 70/10 80/9 90/9 100/9 150/8 200/6
useable = []
for host in duck:
    if hosts.count(host) >= threshold:
        useable.append(host)
        print("More than or equal to " + str(threshold) + " occurences: " + str(host))
'''
    else:
        if hosts.count(host) > 0:
            print("Less than " + str(threshold) + " occurences: " + str(host))
        else:
            print("No occurence: " + str(host))
'''
print(len(useable))
    

'''
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special = []
anyc = 0
for p in x:
    for c in p:
        if c == "X":
            anyc += 1
        if c not in alphabet:
            print(c)
            special.append(c)

print(dataobj.dataToPhoc(x[0:1],5))
'''
'''
your_string = x[0]
l = 2
n = round((len(your_string)+0.1)/2.0)
parts = [your_string[i:i+n] for i in range(0, len(your_string), n)]
print(parts)
'''