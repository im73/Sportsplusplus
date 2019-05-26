import datetime
import io
import re


def PUThandle(data):

    keyarr=[]
    valarr=[]
    stream = io.BytesIO(data)

    for item in stream:
        strpre=item.decode()
        if strpre[0]=='-':
            continue
        elif strpre[0]=='C':
            keyarr.append(re.findall("name=\"(.+?)\"",strpre))
        elif strpre=="\r\n":
            continue
        else:
            valarr.append(strpre.replace("\r\n",""))

    datadic={}

    for i in range(len(keyarr)):
        datadic[keyarr[i][0]]=valarr[i]

    return datadic

def get_date_set(begin_date, end_date):

    dates = []
    dt = datetime.datetime.strptime(begin_date, '%Y-%m-%d')
    date = begin_date
    while date <= end_date:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime('%Y-%m-%d')
    return dates
