import pandas as pd

# # Merging wards (map) with stations and zones

postcode = pd.read_csv("London_postcodes.csv")
ward = pd.read_csv("London_Wards.csv")
station = pd.read_csv("London_stations.csv")

pcd_target = ward['Ward'].unique()
postcode = postcode[postcode['Ward'].isin(pcd_target)]

station_postcode = station.merge(postcode, left_on = 'Postcode', right_on = 'Postcode', how = "left")

col_1 = ['Station', 'Zone', 'Ward']
station_postcode = station_postcode[col_1]

ward_station = ward.merge(station_postcode, left_on = 'Ward', right_on = 'Ward', how = "right")
ward_station = ward_station[ward_station['Ward ID'].notnull()]

ward_no_station = ward[~ward['Ward'].isin(station_postcode['Ward'].unique())]


cols = ["Latitude", "Longitude", "Borough", "Ward", "Point Order", "Station", "Zone"]
ward_station = ward_station[cols]

cols_2 = ["Latitude", "Longitude", "Borough", "Ward", "Point Order"]
ward_no_station = ward_no_station[cols_2]

ward_all = ward_station.append(ward_no_station)

ward_all.to_csv('ward_station.csv')
