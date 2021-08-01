import pandas as pd
def processing(data):

    data.rename(columns=data.iloc[0], inplace = True)

    data.drop(data.index[0], inplace = True)

    data.drop(data.columns[1],axis = 1 ,inplace = True)

    data.reset_index(drop=True, inplace=True)

    #data.rename(columns = {​​​​​'LOX Net Production (ton)': 'LOX_Net', 'GAN Net Production (ton)': 'GAN_Net', 'LIN Net Production(ton)':'LIN_Net', 'Total Net liquid production (ton)':'Total_Net_liquid'}​​​​​, inplace = True)

    data['Date'] = pd.to_datetime(data['Date']).dt.normalize()

    return data

def cleaning(df):
    data = df.iloc[:, 2:]
    dataframe=pd.DataFrame(columns=["Date" ,"production_1","production_2","production_3","Total production (ton)"])

    start=0

    for i in range(12):
        df = data.iloc[start:start+6, :].T
        df = processing(df)
        dataframe= dataframe.append(df, ignore_index=True)
        start += 11
    return dataframe