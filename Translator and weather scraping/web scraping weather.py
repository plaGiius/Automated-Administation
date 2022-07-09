import requests
from bs4 import BeautifulSoup as bs
#Weather report of Chennai, Mavic 2 Pro
#7th to 19th June Scraping
url="https://www.bbc.com/weather/1264527"
#url5="https://www.letusdrone.com/what-is-a-safe-wind-speed-for-dji-drones/"
r=requests.get(url)

forecast=bs(r.content,"lxml")
max_speed = 24 

#1.Chennai
wthr_che=forecast.findAll("span",{"class":"wr-wind-speed__value "})
wthr_che1=forecast.findAll("span",{"class":"wr-value--windspeed wr-value--windspeed--mph"})
for i in range(2):
    wind_spd_che=wthr_che1[i].text
    wind_spd_che2=list(wind_spd_che.split())
    current_speed_1=int(wind_spd_che2[0])
    if(current_speed_1 <= 24):
        print(1)
    else:
        print(0)
        
#2.Trivuvananthapuram
url2="https://www.bbc.com/weather/1254163"

r2=requests.get(url2)
forecast=bs(r2.content,"lxml")

wthr_tvm=forecast.findAll("span",{"class":"wr-wind-speed__value "})
wthr_tvm2=forecast.findAll("span",{"class":"wr-value--windspeed wr-value--windspeed--mph"})
for i in range(2):
    wind_spd_tvm=wthr_tvm2[i].text
    wind_spd_tvm2=list(wind_spd_tvm.split())
    current_speed_2=int(wind_spd_tvm2[0])
    if(current_speed_2 <= 24):
        print(1)
    else:
        print(0)


    

    
    

