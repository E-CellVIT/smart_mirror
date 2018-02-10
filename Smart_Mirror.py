import requests
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import base64
from urllib.request import urlopen

from tkinter import Tk, Message,Label
root = Tk()
root.configure(background='black')
root.geometry("1366x768+0+0")

#image
path ="logo.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = TOP)
#centre
panel.config(background='black')
label = Label(root, text='Hello, world!')
label.pack(side=TOP)
label.config(foreground='white', background='black', text='WE BREED BUSINESS',font=('times',25))
panel.pack(side = TOP)
panel.config(background='black')

label = Label(root, text='Hello, world!')
label.pack(side=TOP)
label.config(foreground='black', background='black', text='Hey! Explore E-Cell,VIT',font=('times',30))
label = Label(root, text='Hello, world!')
label.pack(side=TOP)
label.config(foreground='black', background='black', text='Hey! Explore E-Cell,VIT',font=('times',30))
label = Label(root, text='Hello, world!')
label.pack(side=TOP)
label.config(foreground='black', background='black', text='Hey! Explore E-Cell,VIT',font=('times',30))
label = Label(root, text='Hello, world!')
label.pack(side=TOP)
label.pack(side=TOP)
label.config(foreground='black', background='black', text='Hey! Explore E-Cell,VIT',font=('times',30))
label.config(foreground='white', background='black', text='Hey! Explore E-Cell,VIT',font=('times',25))



#news
#Add your News API here
url = ('')
response = requests.get(url).json()

for i in range (0,4):
    formatted_data = response['articles'][i]['title']
    label = Label(root, text='Hello, world!')
    label.pack(side=BOTTOM)
    label.config(foreground='white', background='black', text=formatted_data)
    i=i+1
label = Label(root, text='Hello, world!')
label.pack(side=BOTTOM)
label.config(foreground='white', background='black', text='#StayUpdated',font=('times',22 , 'bold'))


#weather
frame = tk.Frame(root)
frame.config(background='black')
frame.pack(side=LEFT)

#Add your Weather API Here
wu_api = ""
wu_state = "India"
wu_city = "Vellore"
api_delay = "600000"
wu_uri = "http://api.wunderground.com/api/"+wu_api+"/conditions/q/"+wu_state+"/"+wu_city+".json"
wuLocation = tk.Label(frame,text='Location')
wuLocation.pack()
wuLocation.config(foreground='white', background='black', text='Location',font=('times',12))
wuTime = tk.Label(frame,text='Time')
wuTime.pack()
wuTime.config(foreground='white', background='black', text='Time',font=('times',12))
wuIcon = tk.Label(frame,image='')
wuIcon.pack()
wuIcon.config(background='black')
wuConditions = tk.Label(frame,text='Conditions')
wuConditions.pack()
wuConditions.config(foreground='white', background='black', text='Conditions',font=('times',12))
wuTempf = tk.Label(frame,text='Tempf')
wuTempf.pack()
wuTempf.config(foreground='white', background='black', text='Tempf',font=('times',12))
wuHumidity = tk.Label(frame,text='Humidity')
wuHumidity.pack()
wuHumidity.config(foreground='white', background='black', text='Humidity',font=('times',12))

def wuGet():

    # Request the weather info from Weather Underground
    wu_req = requests.get(wu_uri)
    data = wu_req.json()

    # Pull out the useful info
    current_weather =  data['current_observation']['weather']
    obs_conditions = "Current Conditions: "+current_weather
    obs_location = "Weather for "+str(data['current_observation']['display_location']['full'])
    obs_time = str(data['current_observation']['observation_time'])
    current_tempf = str(data['current_observation']['temp_f'])
    obs_tempf = "Current Temperature: "+current_tempf+" F"
    obs_humidity = "Relative Humidity: "+str(data['current_observation']['relative_humidity'])
    icon_url = data['current_observation']['icon_url']

    # Get the weather icon from the icon_url
    image_byt = urlopen(icon_url).read()
    image_b64 = base64.encodestring(image_byt)
    photo = tk.PhotoImage(data=image_b64)

    # Update the Labels with the Weather
    wuLocation.config(text=obs_location)
    wuTime.config(text=obs_time)
    wuIcon.image = photo
    wuIcon.config(image=photo)
    wuConditions.config(text=obs_conditions)
    wuTempf.config(text=obs_tempf)
    wuHumidity.config(text=obs_humidity)

    # Wait for the delay, next verse same as the first
    frame.after(api_delay, wuGet)


# Call wuGet to get the first update
wuGet()
root.mainloop()
root.mainloop()
