from django.shortcuts import render
import folium
from folium import plugins
import geocoder 
import pandas as pd

g = geocoder.ip('me')
# Create your views here.
def main(request):
    map = folium.Map(
        location=[37.3380807441504, 126.820584568561],
        zoom_start=20,
        width='100%',
        height='90%',
        position='relative',
    )
    plugins.LocateControl().add_to(map)
    folium.Marker(
        [37.3380807441504, 126.820584568561],
        popup='<b>my home</b>',
        tooltip='Click me!'
    ).add_to(map)

   

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 
    df = pd.read_csv('C:/budongsan/실시간매물.csv')
    print(df.columns)
    print(df[:3])

    return render(request,'../templates/index.html',{'map' : maps})
    