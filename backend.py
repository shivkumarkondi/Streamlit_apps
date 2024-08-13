import os,requests
from dotenv import load_dotenv
load_dotenv()


API_KEY= os.getenv('WEATHER_API_KEY')
def get_data(place,forcast_days=None,kind= None):    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = forcast_days * 8 
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    print(get_data(place="Tokyo",forcast_days=2,kind ='Temperature' ))