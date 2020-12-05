import re

with open('04/input.txt', 'r') as fp:
    data = fp.read()

pattern1 = r'(?:\w{3}:\S+(?: |\n|$))*\n?' # To capture one "passport"
pattern2 = r'(\w{3}):(\S+)' # To capture keys within a passport
valid_keys = 0
valid_values = 0

def validate_keys(passport: dict):
    validkeys = [
        'byr', # (Birth Year)
        'iyr', # (Issue Year)
        'eyr', # (Expiration Year)
        'hgt', # (Height)
        'hcl', # (Hair Color)
        'ecl', # (Eye Color)
        'pid', # (Passport ID)
        #'cid' # (Country ID)
    ]

    passportkeys = list(passport.keys())

    for validkey in validkeys: # Looping throug passport keys and match towards valid keys.
        if validkey not in passportkeys:
            return False # if key is missing, 
    
    return True # If all is valid, the passport is valid - OK

def validate_values(passport: dict):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not 1920 <= int(passport.get('byr')) <= 2002: 
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not 2010 <= int(passport.get('iyr')) <= 2020: 
        return False
    
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not 2020 <= int(passport.get('eyr')) <= 2030:
        return False

    # hgt (Height) - a number followed by either cm or in:
    m = re.match(r'(\d+)(in|cm)', passport.get('hgt'))
    if m is not None:
        # If cm, the number must be at least 150 and at most 193.
        if m.group(2) == 'cm':
            if not 150 <= int(m.group(1)) <= 193:
                return False
        
        # If in, the number must be at least 59 and at most 76.
        if m.group(2) == 'in':
            if not 59 <= int(m.group(1)) <= 76:
                return False
    else:
        return False

    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not re.match(r'\#[0-9,a-f,A-F]{6}', passport.get('hcl')):
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not passport.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not re.match(r'^[0-9]{9}$', passport.get('pid')):
        return False

    return True


if __name__ == '__main__':
    for entry in re.findall(pattern1, data): # We find all passports
        passport = {} # Start with a clean list of keys
        for key, value in re.findall(pattern2, entry): # Append keys in passport to list
            passport[key] = value
        
        if validate_keys(passport) is True:
            valid_keys = valid_keys+1 # Increment if valid passport
            
            if validate_values(passport) is True:
                valid_values = valid_values+1 # Increment if valid passport
                
        
    print('Found %d valid passports in round 1' % valid_keys)
    print('Found %d valid passports in round 2' % valid_values)