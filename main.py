import rpa as r
import pandas as pd
import os


r.init(turbo_mode=True)
r.url('https://rpachallenge.com')
#r.download('./assets/downloadFiles/challenge.xlsx')

r.click("/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a")

if os.path.exists("challenge.xlsx"):
    pass
else:
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')

df = pd.read_excel("challenge.xlsx")
df['Phone Number'] = df['Phone Number'].astype(str)

#print(df.dtypes)
#print(df.columns.tolist())

for i, row in df.iterrows():
    r.type('//*[@ng-reflect-name="labelFirstName"]', row["First Name"])
    r.type('//*[@ng-reflect-name="labelLastName"]', row["Last Name "])
    r.type('//*[@ng-reflect-name="labelAddress"]', row["Address"])
    r.type('//*[@ng-reflect-name="labelPhone"]', row["Phone Number"])
    r.type('//*[@ng-reflect-name="labelEmail"]', row["Email"])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', row["Company Name"])
    r.type('//*[@ng-reflect-name="labelRole"]', row["Role in Company"])
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')

r.snap('page', 'score.png')
r.wait(10)
r.close()
