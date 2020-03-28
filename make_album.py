
def city_country(city,country):
    """Return a City and Country name"""
    location = city + ' ,  ' + country
    return location.title()

while True:
   print("\n Please tell me your City name and Country")
   print("\n Finish the system with q")
   city_name = input("\n City name:")

   if city_name == 'q':
    break
   country_name = input("\n Country name:")

   if country_name == 'q':
    break
   location = city_country(city_name,country_name)
   print("\n {}".format(location))
