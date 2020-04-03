from flask import Flask, render_template, request, redirect, flash, url_for 
import requests, folium
import pandas as pd
app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def homepage():   
    country = 'India'
    if request.method == 'POST':
        country = request.form['country']
        print(country)
        country = country.capitalize()
        ans = requests.get(url = "https://api.covid19api.com/summary").json()
        li = ans['Countries']
        CountryList=[]
        for i in li:
            CountryList.append(i['Country'])
        df = pd.DataFrame(columns=None)
        df['Country'] = CountryList
        df.to_csv("Country.csv")
        for i in li:
            if i['Country'] == country:
                newConfirmed = i['NewConfirmed']
                totalConfirmed = i['TotalConfirmed']
                newDeaths = i['NewDeaths']
                totalDeaths = i['TotalDeaths']
                newRecovered = i['NewRecovered']
                totalRecovered = i['TotalRecovered']

        return render_template('index.html',newCountry=country,newConfirmed=newConfirmed,totalConfirmed=totalConfirmed,newDeaths=newDeaths,totalDeaths=totalDeaths,newRecovered=newRecovered,totalRecovered=totalRecovered)
    return render_template('main1.html',x=country)

# @app.route('/pandemic/<country>')
# def pandemic(country):
    
    
#     print(country)
#     for i in li:
#         if i['Country'] == country:
#             newConfirmed = i['NewConfirmed']
#             totalConfirmed = i['TotalConfirmed']
#             newDeaths = i['NewDeaths']
#             totalDeaths = i['TotalDeaths']
#             newRecovered = i['NewRecovered']
#             totalRecovered = i['TotalRecovered']
#     return render_template('index.html',newCountry=country,newConfirmed=newConfirmed,totalConfirmed=totalConfirmed,newDeaths=newDeaths,totalDeaths=totalDeaths,newRecovered=newRecovered,totalRecovered=totalRecovered)

@app.route('/map',methods=['GET','POST'])
def Map():
    data=pd.read_csv("train.csv")
    data['active'] = data['ConfirmedCases']-data['Fatalities']
    m = folium.Map(location=[0, 0], width='100%', height='100%', left='0%', top='0%', position='relative', tiles='OpenStreetMap',    
            min_zoom=0, max_zoom=14, zoom_start=5)
    
    for i in range(0,len(data)):
        folium.Circle(
        color='red', 
        location = [data['Lat'].iloc[i],data['Long'].iloc[i]],
        tooltip='<li> Country :'+str(data['Country/Region'][i])+
                '<li> Confirmed :'+str(data['ConfirmedCases'][i])+
                '<li> Deaths :'+str(data['Fatalities'][i])+
                '<li> Active :'+str(data['active'][i]),
        radius=int(data.iloc[i]['ConfirmedCases'])**1.1
        ).add_to(m)
    m.save('./templates/osm.html')
    return render_template('osm.html')

# @app.route('/Live-update',methods=['Get','Post'])
# def liveUpdate():
#     if request.method == 'POST':
#         country = request.form['mapcountry']    
#         ans = requests.get(url=f"https://api.covid19api.com/dayone/country/{country}/status/confirmed").json()
        
#         lat=[]
#         lon=[]
#         date=[]
#         cases=[]
#         status=[]
#         for i in ans:
#             lat.append(i["Lat"])
#             lon.append(i["Lon"])
#             date.append(i["Date"][:10])
#             cases.append(i["Cases"])
#             status.append(i["Status"])

#         m = folium.Map(location=[lat[5], lon[5]], width='100%', height='100%', left='0%', top='0%', position='relative', tiles='OpenStreetMap',    
#             min_zoom=0, max_zoom=14, zoom_start=5)

#         # print(date)
#         for i in range(len(lat)):
#             folium.Circle(
#                 color='red',
#                 location=[lat[i], lon[i]], 
#                 tooltip='<li> Date :'+str(date[i]) +
#                         '<li> Number of Cases :'+str(cases[i]) +
#                         '<li> Status :' +str(status[i]), 
#                 radius=int(10000)
#             ).add_to(m)

#         m.save('./templates/live-update.html')


#         return render_template('live-update.html')
#     return None

if __name__=="__main__":
    app.run(debug=True)

    # News API Key 
    # 8d376cd332d047a9aa9468033438f7e9