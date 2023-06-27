# import od_lib.definitions.path_definitions as path_definitions
import pandas as pd
import os

# input directory
POLITICIANS_INPUT = "../01_preprocessing/06/"
FACTIONS_INPUT = "../final/"

# output directory
POLITICIANS_OUTPUT = "01/"

if not os.path.exists(POLITICIANS_OUTPUT):
    os.makedirs(POLITICIANS_OUTPUT)

factions = pd.read_pickle(os.path.join(FACTIONS_INPUT, "factions.pkl"))
mps = pd.read_pickle(os.path.join(POLITICIANS_INPUT, "mps.pkl"))

mps.insert(2, "faction_id", -1)

for faction_name, faction_id in zip(factions.faction_name, factions.id):
    mps.faction_id.loc[mps.institution_name == faction_name] = faction_id

mps.to_pickle(os.path.join(POLITICIANS_OUTPUT, "mps.pkl"))
