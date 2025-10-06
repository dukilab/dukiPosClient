import tkinter as tk
from tkinter import messagebox
import requests,re

API_ENDPOINT = 'https://dukipos.sakaduki.com/api/v1/'
FONT  = ("MS Gothic", 50)
HEIGHT = 1
status = 0



statusText = "Ready"

shopItems = [
    {"name": "ハンバーガー", "price": 100},
    {"name": "タピ(ミルク)", "price": 200},
    {"name": "タピ(イチゴ)", "price": 200},
    {"name": "タピ(マンゴー)", "price": 200},
    {"name": "肉串", "price": 300},
]

r = requests.get(API_ENDPOINT + 'ping')
if(r.status_code == 200):
    messagebox.showerror('エラー', 'APIは甘え')

def numIncrease(event:tk.Event):
    i = GetInt(event.widget.winfo_name())
    if(itemAmount[i] >= 2):
        return
    itemAmount[i] += 1
    itemAmountText[i].config(text=str(itemAmount[i]))
    

def numDecrease(event:tk.Event):
    i = GetInt(event.widget.winfo_name())

    itemAmount[i] -= 1
    itemAmountText[i].config(text=str(itemAmount[i]))

def GetInt(s:str):
    return int(re.sub(r'[^0-9]', '', s))

root = tk.Tk()
root.title("dukiPos Client - v1.0 - ©2025 Sakaduki")

statusBar = tk.Label(root, text="Ready", font=FONT, bd=1, relief=tk.SUNKEN, anchor=tk.W, textvariable=statusText)
statusBar.pack(side=tk.TOP, fill=tk.X)

itemList = tk.Frame(root)


i = 0
itemFrame = []
itemLabel = []
itemIncrease = []
itemDecrease = []
itemAmountText = []
itemAmountStr = []
itemAmount = []
for item in shopItems:
    itemFrame.append(tk.Frame(itemList, height=HEIGHT))
    itemFrame[i].grid(row = i, column = 0)
    itemLabel.append(tk.Label(itemFrame[i], text=item["name"], font=FONT, width=12, anchor=tk.W, height=HEIGHT))
    itemLabel[i].grid(row=0, column=0)
    itemIncrease.append(tk.Button(itemFrame[i], text="+", font=FONT, height=HEIGHT, name=f"{i}_inc"))
    itemIncrease[i].grid(row=0, column=1)

    itemDecrease.append(tk.Button(itemFrame[i], text="-", font=FONT, height=HEIGHT, name=f"{i}_dec"))
    itemDecrease[i].grid(row=0, column=2)

    itemAmountStr.append("")
    itemAmount.append(0)
    itemAmountText.append(tk.Label(itemFrame[i], text="0", font=FONT, bd=1, relief=tk.SUNKEN, anchor=tk.E, height=HEIGHT))
    itemAmountText[i].grid(row=0, column=3)

    itemIncrease[i].bind("<Button-1>", numIncrease)
    itemDecrease[i].bind("<Button-1>", numDecrease)

    i+=1

itemList.pack(side=tk.TOP, anchor=tk.W, expand=True)



root.mainloop()