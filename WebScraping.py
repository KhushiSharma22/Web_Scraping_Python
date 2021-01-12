import requests
import bs4
import pandas

url = "https://www.oyorooms.com/hotels-in-bangalore/"

hotels_info_list = []
hotels_info = {}

hotels_data = requests.get(url)
text = hotels_data.text
soup = bs4.BeautifulSoup(text,"lxml")

all_hotels = soup.find_all("div", {"class":"ListingHotelCardWrapper"})

for hotel in all_hotels:
    hotels_info["Name"] = hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
    hotels_info["Address"] = hotel.find("div",{"class":"listingHotelDescription_hotelAddress"}).text
    hotels_info["Price"] = hotel.find("span",{"class":"listingPrice_finalPrice"}).text

    try:
        hotels_info["Rating"] = hotel.find("div",{"class":"hotelRating"}).text
    except AttributeError:
        pass

    amenities_parent = hotel.find("div",{"class":"amenityWrapper"})

    amenities_list = []
    for amenity in amenities_parent.find_all("div",{"class":"amenityWrapper_amenity"}):
        amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())
        

    hotels_info["Amenity"] = ",".join(amenities_list[:-1])

    hotels_info_list.append(hottels_info)

dataFrame = pandas.DataFrame(hotels_info_list)
dataframe.to_csv("CSV_File")
