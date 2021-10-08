import re
import pandas as pd
import csv

df_raw = pd.read_csv('data/U.S._State_and_Territorial_Public_Mask_Mandates_From_April_10__2020_through_August_15__2021_by_County_by_Day.csv', dtype={"FIPS_State": str,"FIPS_County": str})
df_raw['FIPS_State'] = df_raw['FIPS_State'].str.zfill(2)
df_raw['FIPS_County'] = df_raw['FIPS_County'].str.zfill(3)
df_raw['FIPS'] = df_raw['FIPS_State'] + df_raw['FIPS_County']
df_nfdc = pd.read_csv('data/NfdcFacilities.csv')
df_airports = pd.read_csv('airports.csv')
df_raw['county_uppercase'] = df_raw['County_Name'].str.upper()
df_IATA = df_airports.merge(df_nfdc, how = 'inner', left_on = ['iata'], right_on = ['LocationID'])
df_raw = df_raw.merge(df_IATA, how = 'inner', left_on = ['State_Tribe_Territory','county_uppercase'], right_on = ['State','County'])
df_raw = df_raw[['iata','FIPS','State_Tribe_Territory','County_Name','city','latitude','longitude','date','order_code','Face_Masks_Required_in_Public','Source_of_Action','URL','Citation']]
df_raw = df_raw.rename(columns = {'city':'name'})

garbage_lst = [df_nfdc,df_airports,df_IATA]
del garbage_lst

df = df_raw[df_raw.groupby('Citation').date.transform('max') == df_raw['date']]
df_mask = df_raw[(df_raw['order_code'] == 1)]
df_mask = df_mask[df_mask.groupby('Citation').date.transform('max') == df_mask['date']]
df_nomask = df_raw[(df_raw['order_code'] == 2)]
df_nomask = df_nomask[df_nomask.groupby('Citation').date.transform('max') == df_nomask['date']]
#problem is here
df_order_count_tmp = df_raw[(df_raw['order_code'] == 1)]
df_order_count_tmp = df_order_count_tmp[['FIPS','Citation']].drop_duplicates()
df_order_count_tmp = df_order_count_tmp.groupby(['FIPS']).count().reset_index()
df_order_count_tmp = df_order_count_tmp.rename(columns = {'Citation':'order_count'})
df_mask = df_mask.merge(df_order_count_tmp, how = 'inner', left_on = 'FIPS', right_on = 'FIPS').drop_duplicates()
df_order_length_tmp = df_raw[(df_raw['order_code'] == 1)]
df_order_length_tmp = df_order_length_tmp[['FIPS','date']].drop_duplicates()
df_order_length_tmp = df_order_length_tmp.groupby(['FIPS']).count().reset_index()
df_order_length_tmp = df_order_length_tmp.rename(columns = {'date':'order_length_days'})
df_mask = df_mask.merge(df_order_length_tmp, how = 'inner', left_on = 'FIPS', right_on = 'FIPS').drop_duplicates()
df_mask_count = df_mask[['iata','order_count','order_length_days']].drop_duplicates()
garbage_lst = [df_raw,df_order_count_tmp,df_order_length_tmp]
del garbage_lst

df_edges = pd.read_csv('edges.csv')
df_edges = df_edges.merge(df_mask_count, how = 'inner', left_on = 'origin', right_on = 'iata').drop_duplicates()

df_filename = 'mask_mandates_all.csv'
df_mask_filename = 'mask_mandates.csv'
df_nomask_filename = 'no_mask_mandates.csv'
df_edges_filename = 'mask_edges.csv'
print("exporting " + df_filename)
df.to_csv(df_filename, index = False, quotechar='"',quoting=csv.QUOTE_ALL)
print("exporting " + df_nomask_filename)
df_nomask.to_csv(df_nomask_filename, index = False, quotechar='"',quoting=csv.QUOTE_ALL)
print("exporting " + df_mask_filename)
df_mask.to_csv(df_mask_filename, index = False, quotechar='"',quoting=csv.QUOTE_ALL)
print("exporting " + df_edges_filename)
df_edges.to_csv(df_edges_filename, index = False, quotechar='"',quoting=csv.QUOTE_ALL)

