from lxml import etree
import random
import configparser
import setdata

#0: helmet
#1: shoulders
#2: boots
#3: belt
#4: shirt
#5: legs
#6: chest
#7: bracers
#8: gloves
#9: right hand
#10: left hand
#11: cape
#12: tabard
#13: quiver

HELMET_INDEX = 0
SHOULDERS_INDEX = 1
BOOTS_INDEX = 2
BELT_INDEX = 3
SHIRT_INDEX = 4
LEGS_INDEX = 5
CHEST_INDEX = 6
BRACERS_INDEX = 7
GLOVES_INDEX = 8
RIGHT_HAND_INDEX = 9
LEFT_HAND_INDEX = 10
CAPE_INDEX = 11
TABARD_INDEX = 12
QUIVER_INDEX = 13

set = "plate"

test_equip_dict = {}
test_equip_dict[HELMET_INDEX] = random.choice(setdata.sets[set]['helmets'])
test_equip_dict[SHOULDERS_INDEX] = random.choice(setdata.sets[set]['shoulders'])
test_equip_dict[TABARD_INDEX] = random.choice(setdata.sets[set]['tabards'])
test_equip_dict[CHEST_INDEX] = random.choice(setdata.sets[set]['chests'])
test_equip_dict[SHIRT_INDEX] = random.choice(setdata.sets[set]['shirts'])
test_equip_dict[CAPE_INDEX] = random.choice(setdata.sets[set]['capes'])
test_equip_dict[BRACERS_INDEX] = random.choice(setdata.sets[set]['bracers'])
test_equip_dict[GLOVES_INDEX] = random.choice(setdata.sets[set]['gloves'])
test_equip_dict[RIGHT_HAND_INDEX] = random.choice(setdata.sets[set]['right_handers'])
test_equip_dict[LEFT_HAND_INDEX] = random.choice(setdata.sets[set]['left_handers'])
test_equip_dict[BELT_INDEX] = random.choice(setdata.sets[set]['belts'])
test_equip_dict[LEGS_INDEX] = random.choice(setdata.sets[set]['legs'])
test_equip_dict[BOOTS_INDEX] = random.choice(setdata.sets[set]['boots'])
test_equip_dict[QUIVER_INDEX] = 0

race_list = ["dwarf","elf","gnome","halfling","human","orc"]
sex_list = ["male","female"]

race = random.choice(race_list)
sex = random.choice(sex_list)
section = race + "_" + sex

config = configparser.RawConfigParser()
config.read('gen_config.cfg')

FILE_NAME = config.get(section, 'file')

SKINCOLOR_MIN = int(config.get(section, 'skincolor_min'))
SKINCOLOR_MAX = int(config.get(section, 'skincolor_max'))

FACETYPE_MIN = int(config.get(section, 'facetype_min'))
FACETYPE_MAX = int(config.get(section, 'facetype_max'))

HAIRCOLOR_MIN = int(config.get(section, 'haircolor_min'))
HAIRCOLOR_MAX = int(config.get(section, 'haircolor_max'))

HAIRSTYLE_MIN = int(config.get(section, 'hairstyle_min'))
HAIRSTYLE_MAX = int(config.get(section, 'hairstyle_max'))

FACIALHAIR_MIN = int(config.get(section, 'facialhair_min'))
FACIALHAIR_MAX = int(config.get(section, 'facialhair_max'))

scale = float(config.get(section, 'scale'))

test_char_dict = {}
test_char_dict['skinColor'] = random.randint(SKINCOLOR_MIN, SKINCOLOR_MAX)
test_char_dict['faceType'] = random.randint(FACETYPE_MIN, FACETYPE_MAX)
test_char_dict['hairColor'] = random.randint(HAIRCOLOR_MIN, HAIRCOLOR_MAX)
test_char_dict['hairStyle'] = random.randint(HAIRSTYLE_MIN, HAIRSTYLE_MAX)
test_char_dict['facialHair'] = random.randint(FACIALHAIR_MIN, FACIALHAIR_MAX)
test_char_dict['eyeGlowType'] = 1
test_char_dict['showUnderwear'] = 1
test_char_dict['showEars'] = 1
test_char_dict['showHair'] = 1
test_char_dict['showFacialHair'] = 1
test_char_dict['showFeet'] = 0

def getStringFromTree(tree):
	string = str(etree.tostring(tree.getroot(), pretty_print=True, method="html"))
	string = string.replace("\\n", "\n")[2:-2]
	return string

def setEquipment(tree, equipData):
	for item in tree.iter('item'):
		slotID = int(list(item)[0].attrib['value'])
		list(item)[1].attrib['value'] = str(equipData[slotID])
		list(item)[2].attrib['value'] = str(-1)

def setCharacterDetails(tree, detailData):
	for datum in detailData.items():
		elem = list(tree.iter(datum[0]))[0]
		elem.attrib['value'] = str(datum[1])

characterData = etree.parse("character template.chr")

for f in characterData.iter('file'):
	f.attrib['name'] = FILE_NAME

setEquipment(characterData, test_equip_dict)
setCharacterDetails(characterData, test_char_dict)

with open('output.chr', 'w') as f:
	print(getStringFromTree(characterData), file=f)

with open('metadata.txt','w') as f:
	print(scale,file=f)
