#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import requests as re
import datetime as dt


url_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
url_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
url_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"


recovered_df = pd.read_csv(url_recovered)
deaths_df = pd.read_csv(url_deaths)
confirmed_df = pd.read_csv(url_confirmed)

recovered_df = recovered_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'])
recovered_df.rename(columns={
    'variable':'DATE',
    'value':'RECOVERED',
    'Lat':'LATITUDE',
    'Long':'LONGITUDE',
    'Country/Region':'COUNTRY_REGION',
    'Province/State':'PROVINCE_STATE'
},inplace=True)
recovered_df['DATE'] = pd.to_datetime(recovered_df['DATE'])

deaths_df = deaths_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'])
deaths_df.rename(columns={
    'variable':'DATE',
    'value':'DEATHS',
    'Lat':'LATITUDE',
    'Long':'LONGITUDE',
    'Country/Region':'COUNTRY_REGION',
    'Province/State':'PROVINCE_STATE'
},inplace=True)
deaths_df['DATE'] = pd.to_datetime(deaths_df['DATE'])

confirmed_df = confirmed_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'])
confirmed_df.rename(columns={
    'variable':'DATE',
    'value':'CONFIRMED',
    'Lat':'LATITUDE',
    'Long':'LONGITUDE',
    'Country/Region':'COUNTRY_REGION',
    'Province/State':'PROVINCE_STATE'
},inplace=True)
confirmed_df['DATE'] = pd.to_datetime(confirmed_df['DATE'])


confirmed_df.fillna(value='NA',inplace=True)
recovered_df.fillna(value='NA',inplace=True)
deaths_df.fillna(value='NA',inplace=True)

all_df = confirmed_df.merge(recovered_df,how='left',on=['PROVINCE_STATE','COUNTRY_REGION','DATE','LATITUDE','LONGITUDE'])
all_df = all_df.merge(deaths_df,how='left',on=['PROVINCE_STATE','COUNTRY_REGION','DATE','LATITUDE','LONGITUDE'])

all_df.to_csv('../data/all_data.csv',index=False)

