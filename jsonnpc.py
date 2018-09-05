import random
from random import randrange as rr

'''
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
          line = aline
          return line
'''
def npc():
    firstname = "Test"
    lastname = "Name"

    # GENDER
    gender = random.choice(open('gender.txt').readlines())
    gender = gender.rstrip()

    # RACE
    race = random.choice(open('races.txt').readlines())
    race = race.split(' ', 1)[0]
    race = race.rstrip()

    if race == "Elf" and gender == "Female":
        firstname = random.choice(open('names/elf_female_altmer_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/elf_family_altmer_names.txt').readlines())
        lastname = lastname.rstrip()
    elif race == "Elf" and gender == "Male":
        firstname = random.choice(open('names/elf_male_altmer_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/elf_family_altmer_names.txt').readlines())
        lastname = lastname.rstrip()
        if rr(1, 101) == 1:
            gender = "Eunuch"
    elif race == "Dwarf" and gender == "Female":
        firstname = random.choice(open('names/dwarf_female_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/dwarf_family_names.txt').readlines())
        lastname = lastname.rstrip()
    elif race == "Dwarf" and gender == "Male":
        firstname = random.choice(open('names/dwarf_male_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/dwarf_family_names.txt').readlines())
        lastname = lastname.rstrip()
        if rr(1, 101) == 1:
            gender = "Eunuch"
    elif race == "Human" and gender == "Female":
        firstname = random.choice(open('names/human_female_breton_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/human_family_breton_names.txt').readlines())
        lastname = lastname.rstrip()
    elif race == "Human" and gender == "Male":
        firstname = random.choice(open('names/human_male_breton_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/human_family_breton_names.txt').readlines())
        lastname = lastname.rstrip()
        if rr(1, 21) == 1:
            gender == "Eunuch"
    elif race == "Ork" and gender == "Female":
       firstname = random.choice(open('names/ork_female_orsimer_names.txt').readlines())
       firstname = firstname.rstrip()
       lastname = random.choice(open('names/ork_family_orsimer_names.txt').readlines())
       lastname = lastname.rstrip()
    elif race == "Ork" and gender == "Male":
       firstname = random.choice(open('names/ork_male_orsimer_names.txt').readlines())
       firstname = firstname.rstrip()
       lastname = random.choice(open('names/ork_family_orsimer_names.txt').readlines())
       lastname = lastname.rstrip()
       if rr(1, 11) == 1:
           gender = "Eunuch"
    elif race == "Rakshasa" and gender == "Female":
       firstname = random.choice(open('names/cat_female_khajiit_names.txt').readlines())
       firstname = firstname.rstrip()
       lastname = random.choice(open('names/cat_family_khajiit_names.txt').readlines())
       lastname = lastname.rstrip()
    elif race == "Rakshasa" and gender == "Male":
        firstname = random.choice(open('names/cat_male_khajiit_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/cat_family_khajiit_names.txt').readlines())
        lastname = lastname.rstrip()
    elif race == "Drachen" and gender == "Female":
        firstname = random.choice(open('names/drachen_female_argonian_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/drachen_family_argonian_names.txt').readlines())
        lastname = lastname.rstrip()
    elif race == "Drachen" and gender == "Male":
        firstname = random.choice(open('names/drachen_male_argonian_names.txt').readlines())
        firstname = firstname.rstrip()
        lastname = random.choice(open('names/drachen_family_argonian_names.txt').readlines())
        lastname = lastname.rstrip()
        if rr(1, 11) > 1:
            gender = "Eunuch"


    profession = random.choice(open('class.txt').readlines())
    weight = rr(1, 5)
    if weight == 1:
        level = rr(1,5)
    elif weight == 2:
        level = rr(1,9)
    elif weight == 3:
        level = rr(1,13)
    else:
        level = rr(1,17)
    profession = profession.rstrip()

    # EQUIPMENT
    condition = random.choice(open('armor/armor_condition.txt').readlines())
    condition = condition.rstrip()
    armor = random.choice(open('armor/armor_types.txt').readlines())

    # PRINT
    #print '%s %s \n\t %s %s %s level %d' % (firstname, lastname, gender, race, profession, level)

    #if gender == "Female":
    #    print 'She wears {0} {1}'.format(condition, armor)
    #else:
    #    print 'He wears %s %s.' % (condition, armor)
    #    print 'He wears {0} {1}'.format(condition, armor)

    #print '"firstname" : "%s", "lastname" : "%s"' % (firstname, lastname)
    print '{"firstname" : "%s", "lastname" : "%s", "gender" : "%s", "race" : "%s", "profession" : "%s", "level" : "%d"}' % (firstname, lastname, gender, race, profession, level)


npc()

