import numpy as np
import pandas as pd

holidays=pd.read_csv('holidays_events.csv',parse_dates=['date'])
#remove transferred holidays
holidays.drop(holidays[holidays['transferred']==True].index,inplace=True)

stores=pd.read_csv('stores.csv')
items=pd.read_csv('items.csv')
train=pd.read_csv('train.csv',parse_dates=['date'])
def make_holidays(store_nbr,stores,holidays):
    city,state=stores[stores['store_nbr']==4][['city','state']].values[0]
    indx_national=holidays[holidays['locale']=='National'].index
    indx_regional=holidays[(holidays['locale']=='Regional') & (holidays['locale_name']==state)].index
    indx_local=holidays[(holidays['locale']=='Local') & (holidays['locale_name']==city)].index
    indx=np.append(np.append(indx_national,indx_regional),indx_local)
    indx.sort()

    return holidays.loc[indx][['date','type']].rename(columns={'date':'ds','type':'holiday'})


def make_item_store_ds(item_nbr,store_nbr,train,stores,items,holidays):
    return train[(train.store_nbr==store_nbr) & (train.item_nbr==item_nbr)][['date','unit_sales']].rename(columns={'date':'ds','unit_sales':'y'})



def make_type_store (item_family,store_nbr,train,stores,items,holidays):
    tmp=train[(train['store_nbr']==store_nbr) & (train['family']==item_family)]    
    return tmp.groupby(['store_nbr','family']).agg({'unit_sales':np.mean})


def make_type_store_ds (item_class,store_nbr,train,stores,items,holidays):
    tmp=train[(train['store_nbr']==store_nbr) & (train['class']==item_class)]    
    return tmp.groupby(['store_nbr','class']).agg({'unit_sales':np.mean})




def make_type_store_ds (item_nbr,store_nbr,train,stores,items,holidays):
    train.groupby(['store_nbr','item_nbr']).agg({'unit_sales':np.mean})


