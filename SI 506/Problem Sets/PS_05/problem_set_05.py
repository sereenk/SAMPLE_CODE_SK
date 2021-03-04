# START PROBLEM SET 05
print('Problem Set 05')
mens_champions = [
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'australian open','Seed': 1,'Year': 2015},
    {'Champion': 'Stan Wawrinka','Country': 'SUI','Major': 'french open','Seed': 8,'Year': 2015},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'wimbledon','Seed': 1,'Year': 2015},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'us open','Seed': 1,'Year': 2015},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'australian open','Seed': 1,'Year': 2016},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'french open','Seed': 1,'Year': 2016},
    {'Champion': 'Andy Murray','Country': 'GBR','Major': 'wimbledon','Seed': 2,'Year': 2016},
    {'Champion': 'Stan Wawrinka','Country': 'SUI','Major': 'us open','Seed': 3,'Year': 2016},
    {'Champion': 'Roger Federer','Country': 'SUI','Major': 'australian open','Seed': 17,'Year': 2017},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'french open','Seed': 4,'Year': 2017},
    {'Champion': 'Roger Federer','Country': 'SUI','Major': 'wimbledon','Seed': 3,'Year': 2017},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'us open','Seed': 1,'Year': 2017},
    {'Champion': 'Roger Federer','Country': 'SUI','Major': 'australian open','Seed': 2,'Year': 2018},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'french open','Seed': 1,'Year': 2018},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'wimbledon','Seed': 12,'Year': 2018},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'us open','Seed': 6,'Year': 2018},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'australian open','Seed': 1,'Year': 2019},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'french open','Seed': 2,'Year': 2019},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'wimbledon','Seed': 1,'Year': 2019},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'us open','Seed': 2,'Year': 2019}
 ]

womens_champions = [
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'australian open','Seed': 1,'Year': 2015},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'french open','Seed': 1,'Year': 2015},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'wimbledon','Seed': 1,'Year': 2015},
    {'Champion': 'Flavia Pennetta','Country': 'ITA','Major': 'us open','Seed': 26,'Year': 2015},
    {'Champion': 'Angelique Kerber','Country': 'GER','Major': 'australian open','Seed': 7,'Year': 2016},
    {'Champion': 'Garbiñe Muguruza','Country': 'ESP','Major': 'french open','Seed': 4,'Year': 2016},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'wimbledon','Seed': 1,'Year': 2016},
    {'Champion': 'Angelique Kerber','Country': 'GER','Major': 'us open','Seed': 2,'Year': 2016},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'australian open','Seed': 2,'Year': 2017},
    {'Champion': 'Jeļena Ostapenko','Country': 'LAT','Major': 'french open','Seed': 0,'Year': 2017},
    {'Champion': 'Garbiñe Muguruza','Country': 'ESP','Major': 'wimbledon','Seed': 14,'Year': 2017},
    {'Champion': 'Sloane Stephens','Country': 'USA','Major': 'us open','Seed': 0,'Year': 2017},
    {'Champion': 'Carolina Wozniacki','Country': 'DEN','Major': 'australian open','Seed': 2,'Year': 2018},
    {'Champion': 'Simona Halep','Country': 'ROU','Major': 'french open','Seed': 1,'Year': 2018},
    {'Champion': 'Angelique Kerber','Country': 'GER','Major': 'wimbledon','Seed': 11,'Year': 2018},
    {'Champion': 'Naomi Osaka','Country': 'JPN','Major': 'us open','Seed': 20,'Year': 2018},
    {'Champion': 'Naomi Osaka','Country': 'JPN','Major': 'australian open','Seed': 4,'Year': 2019},
    {'Champion': 'Ashleigh Barty','Country': 'AUS','Major': 'french open','Seed': 8,'Year': 2019},
    {'Champion': 'Simona Halep','Country': 'ROU','Major': 'wimbledon','Seed': 7,'Year': 2019},
    {'Champion': 'Bianca Andreescu','Country': 'CAN','Major': 'us open','Seed': 15,'Year': 2019}
 ]
# PROBLEM 1 (20 points)
print('\nProblem 1')
dark_horse_seed = 0
dark_horse = None

for a in womens_champions[1:4]:
    current_seed = 0
    if a["Seed"] > current_seed :
        current_seed = a["Seed"]
    else: continue
    dark_horse_seed = current_seed
    dark_horse = a["Champion"]

print(dark_horse)
print(dark_horse_seed)

# PROBLEM 2 (20 points)
print('\nProblem 2')
USOpen_native_winners = []

USOpen_native_winners = []

for b in womens_champions:
    if b["Country"] == "USA":
        if b["Major"] == "us open":
            USOpen_native_winners.append(b["Champion"])

print(USOpen_native_winners)


# PROBLEM 3 (20 points)
print('\nProblem 3')
mens_champions_times = {}

for info in mens_champions:
    count = 0
    name = info.get('Champion')
   # print(name)
    if name not in mens_champions_times:
        mens_champions_times[name] = 1
    else:
        mens_champions_times[name] +=1

print(mens_champions_times)


# PROBLEM 4 (20 points)
print('\nProblem 4')
most_GS_times = 0
most_GS_champion = None

for key,value in mens_champions_times.items():
    if value >= 8:
        most_GS_champion = key
        most_GS_times = value


print(most_GS_champion)
print(most_GS_times)

# PROBLEM  5 (20 points)
print('\nProblem 5')
womens_AO_times = {}
most_AO_champion = None
most_AO_times = 0

for info_2 in womens_champions:
    if info_2['Major'] == 'australian open':
        count = 0
        name = info_2.get('Champion')
        if name not in womens_AO_times:
            womens_AO_times[name] = 1
        else:
            womens_AO_times[name] +=1

print(womens_AO_times)


for key,value in womens_AO_times.items():
    if value > 1:
        most_AO_champion = key
        most_AO_times = value


print(most_AO_champion)
print(most_AO_times)