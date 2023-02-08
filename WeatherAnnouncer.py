def weatherAnnouncer(temp, clearSkies, windy):
    #try to combine these two statements into one if statement!
    tempClass = temperatureClassification(temp)
    if(tempClass == 'HOT' and clearSkies and not windy):
        return 'Wear summer clothes today.'
    if(tempClass == 'HOT' and clearSkies and windy):
        return 'Wear summer clothes today.'


def temperatureClassification(temp):
    pass


#if hot and clear and not windy: 'Wear summer clothes today. 
print('TESTING', weatherAnnouncer(77, True, False))
# if hot and not clear and windy: 'Wear summer clothes today, but bring a rain jacket just in case.'
print('TESTING', weatherAnnouncer(95, False, True))
# if hot and not clear and not windy: 'Wear summer clothes today, but bring an umbrella just in case.'
print('TESTING', weatherAnnouncer(95, False, False))

# if fair AND clear AND not windy: 'Wear whatever you would like today.'
print('TESTING', weatherAnnouncer(56, True, False))
# if fair AND otherwise: 'Wear a jacket today.'
print('TESTING', weatherAnnouncer(56, False, False))

# if cold AND windy AND PC: 'Just stay inside today.'
print('TESTING', weatherAnnouncer(22, False, True))
# if cold AND otherwise: 'Wear winter gear today.'
print('TESTING', weatherAnnouncer(2, True, True)) 
