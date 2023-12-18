# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:27:19 2023

@author: mm16jdc
"""

import pandas as pd
import osgb

with open('trigmap.html','r') as f:
    lines1 = f.readlines()
    


def ll(gr):
    lat, lon = osgb.grid_to_ll(osgb.parse_grid(gr))
    return [lat,lon]

def get_icon(con):
    if con in ['Good','Moved','Slightly damaged']:
        return 'greenIcon'
    elif con in ['Unreachable but visible', 'Damaged', 'Toppled']:
        return 'blueIcon'
    elif con in ['Remains', 'Possibly missing']:
        return 'goldIcon'
    elif con in ['Destroyed', 'Converted', 'Not Logged', 'Unknown']:
        return 'redIcon'
    else:
        print(con)
    
df = pd.read_csv('C:/Users/mm16jdc/Downloads/trigpoints-2883134.csv')
df= df.set_index('waypoint')
ddict = df.to_dict('index')

lines2=[]
i=0
while i<len(lines1):
    if i<162:
        lines2.append(lines1[i])    
        
    elif len(lines1[i])<5:
        lines2.append(lines1[i])
    
    elif lines1[i][:6]=='var TP':
        try:
            var = lines1[i].split(' =')[0]
            var = var.replace('var ','')
            con = ddict[var]['condition']
            cond = get_icon(con)
            k = lines1[i].split('icon:')
            lines2.append(k[0]+'icon: '+cond+'});'+'\n')
            k = lines1[i+1].split('Condition:')
            lines2.append(k[0]+'Condition: '+con+'", {maxWidth :500});'+'\n')
            lines2.append('                '+con.replace(' ','')+'.addLayer('+var+');'+'\n')
            lines2.append(lines1[i+3])
        except:
            print(var)
            lines2.append(lines1[i])
            lines2.append(lines1[i+1])
            lines2.append(lines1[i+2])
            lines2.append(lines1[i+3])
        i=i+1
        
    elif i>27610:
        lines2.append(lines1[i])
    i=i+1

with open('trigmap.html','w') as f:
    f.writelines(lines2)