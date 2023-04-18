# Create a function that takes a country's name and its area as arguments and returns the area of the country's
# proportion of the total world's landmass.
# Examples
# area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"
# area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"
# area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"

def area_country(country_name, country_area):
    total_land_area = 148940000
    proportion = (country_area / total_land_area) * 100
    return f"{country_name} is {proportion:.2f}% of the total world's landmass"


print(area_country("Iran", 1648195))
