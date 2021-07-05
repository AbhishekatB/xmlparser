from xml.dom import minidom
import pandas as pd

# parse an xml file by name

file = minidom.parse('DLTINS_20210117_01of01.xml')
f = file.getElementsByTagName("FinInstrmGnlAttrbts")
issr = file.getElementsByTagName("Issr")


arr = []
for i in range(0,2):
    temp_array = []
    temp_array.append(f[i].getElementsByTagName("Id")[0].firstChild.nodeValue)
    temp_array.append(f[i].getElementsByTagName("FullNm")[0].firstChild.nodeValue)
    temp_array.append(f[i].getElementsByTagName("ClssfctnTp")[0].firstChild.nodeValue)
    temp_array.append(f[i].getElementsByTagName("CmmdtyDerivInd")[0].firstChild.nodeValue)
    temp_array.append(f[i].getElementsByTagName("NtnlCcy")[0].firstChild.nodeValue)
    temp_array.append(issr[i].firstChild.nodeValue)
    arr.append(temp_array)

df = pd.DataFrame(arr,columns=["Id","FullNm","ClssfctnTp","CmmdtyDerivInd","NtnlCcy","Issr"])
df.to_csv('data.csv',index=False)

