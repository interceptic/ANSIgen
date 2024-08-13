import requests

igns = []
uuid = []
shiyu_stats = []
message= []
price = []


def generate_ansi():
    
    ansi = """```ansi
[2;31mSelling:

"""
    for i in range(len(shiyu_stats)):
        for s in shiyu_stats[i]['profiles']:
            if shiyu_stats[i]['profiles'][s]['current'] == True:
                location = s

        try:
            cata = shiyu_stats[i]['profiles'][location]["data"]["dungeons"]["catacombs"]["level"]["level"] # cata level
        except KeyError as error:
            cata = 0
        try:   
            hotm = shiyu_stats[i]["profiles"][location]["data"]["mining"]["core"]["level"]["level"]
        except KeyError as error:
            hotm = 0
        try: 
            sa = round(shiyu_stats[i]['profiles'][location]["data"]["skills"]["averageSkillLevel"]) # average skill level
        except KeyError as error:
            sa = 0
        try:
           level = shiyu_stats[i]["profiles"][location]["data"]["skyblock_level"]["level"]
        except KeyError as error:
            level = 0
        try:
            unsnw = representTBMK(round(shiyu_stats[i]["profiles"][location]["data"]["networth"]["unsoulboundNetworth"]))
        except KeyError as error:
            unsnw = 0
        try:
            sbnw = representTBMK(round(shiyu_stats[i]["profiles"][location]["data"]["networth"]["networth"]) - round(shiyu_stats[i]["profiles"][location]["data"]["networth"]["unsoulboundNetworth"]))
        except KeyError as error:
            sbnw = 0
            print(error)
        try:
            zombie = shiyu_stats[i]["profiles"][location]["data"]["slayer"]["slayers"]["zombie"]["level"]["currentLevel"]
        except KeyError as error:
            zombie = 0
        try:
           spider = shiyu_stats[i]["profiles"][location]["data"]["slayer"]["slayers"]["spider"]["level"]["currentLevel"]
        except KeyError as error:
            spider = 0
        try:
            wolf = shiyu_stats[i]["profiles"][location]["data"]["slayer"]["slayers"]["wolf"]["level"]["currentLevel"]
        except KeyError as error:
            wolf = 0 
        try:
           enderman = shiyu_stats[i]["profiles"][location]["data"]["slayer"]["slayers"]["enderman"]["level"]["currentLevel"]
        except KeyError as error:
            enderman = 0
        try:
            vamp = shiyu_stats[i]["profiles"][location]["data"]["slayer"]["slayers"]["vampire"]["level"]["currentLevel"]
        except KeyError as error:
            vamp = 0
        try:
            blaze = shiyu_stats[i]["profiles"][location]["data"]["slayer"]["slayers"]["blaze"]["level"]["currentLevel"]
        except KeyError as error:
            blaze = 0

        message.append(f"""[2;31m[2;35m[2;30m[2;37mIGN:     [0m[2;30m[0m[2;35m[0m[2;31m[2;36m{igns[i]}: ${price[i]}[0m[2;31m[0m
[2;30m[2;37mLevel[0m[2;30m[0m:   [2;32m[2;33m{level}[0m[2;32m[0m
[2;30m[2;37mSA[0m[2;30m[0m:      [2;33m{sa}[0m
[2;37m[0m[2;37mUns NW[0m:  [2;33m{unsnw}[0m
[2;30m[2;37mSb NW[0m[2;30m[0m:   [2;33m{sbnw}[0m
[2;30m[2;37mCata[0m[2;30m[0m:    [2;33m{cata}[0m[2;33m
[0m[2;30m[2;37mHOTM[0m[2;30m[0m:    [2;33m{hotm}[0m
[2;37mSlayers[0m:[2;33m ({zombie}/{spider}/{wolf}/{enderman}/{vamp}/{blaze})""")

        
    final = ansi + """

[0m
""".join(message)
    final = final + """``` 
-# Generated using ANSIgen [- Here](<https://github.com/interceptic/ANSIgen>)"""
    with open('output.txt', 'w') as file:
        file.write(f"{final}")


def get_igns():
    on = True
    while on:
        response = str(input("Add a minecraft account, if you would like to stop adding leave message blank: "))
        if response == "":
            on = False
            break
        price.append(int(input('Desired Price for account: ')))
        igns.append(response)
    try:
        for username in igns:
            try:
                response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
                response = response.json()
                uuid.append(response['id'])
            except Exception as error:
                print(f'Error Fetching UUID info for {username}, with error {error}')
        for id in uuid:
            try:
                response = requests.get(f"https://sky.shiiyu.moe/api/v2/profile/{id}")
                print(f'Finished API call for uuid: {id}')
                info = response.json()
                shiyu_stats.append(info)
            except Exception as error:
                print(f'Exception getting stats for id: {id}, with error {error}')
    except Exception as error:
        pass
    generate_ansi()


def representTBMK(value):
	response = value
	if value >= 1000000000000:
		response = str(round(value / 1000000000000, 1)) + "T"
	elif value >= 1000000000:
		response = str(round(value / 1000000000, 1)) + "b"
	elif value >= 1000000:
		response = str(round(value / 1000000)) + "M"
	elif value >= 1000:
		response = str(round(value / 1000, 1)) + "K"

	return response
get_igns()
        