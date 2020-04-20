import sqlite3
import webscrape


#Getting the base price through web scraping
bij = {}
ud = {}
bang = {}
bij = webscrape.bij_price
ud = webscrape.u_price
bang = webscrape.bang_price

def price_reduction(investment, profit):
    ratio = (investment/profit)*100
    if(ratio>=90):
        return 7
    elif(ratio<90 and ratio>=70):
        return 5
    elif(ratio<70 and ratio>=50):
        return 4
    elif(ratio<50 and ratio>=20):
        return 2
    else:
        return 1

def calculate_price(ratio, location, crop):
    if(location=='Bijapur'):
        base = bij[crop]
        print('base: ',base)
        final = base - ((base*ratio)/100)
        return final
    elif(location=='Udupi'):
        base = ud[crop]
        print('base: ', base)
        final = base - ((base*ratio)/100)
        return final
    else:
        base = bang[crop]
        print('base: ', base)
        final = base - ((base * ratio) / 100)
        return final


def bijapur():
    conn = sqlite3.connect('crop.db')
    c = conn.cursor()
    c.execute("SELECT id, crop, investment, profit FROM bijapur")
    for i in c.fetchall():
        index = i[0]
        ratio = price_reduction(i[2],i[3])
        final_price = calculate_price(ratio, 'Bijapur', i[1])
        print(index,final_price)
        c.execute("UPDATE bijapur SET price= ? WHERE id= ?",(final_price,index))
    conn.commit()
    conn.close()

def udupi():
    conn = sqlite3.connect('crop.db')
    c = conn.cursor()
    c.execute("SELECT id, crop, investment, profit FROM udupi")
    for i in c.fetchall():
        index = i[0]
        ratio = price_reduction(i[2],i[3])
        final_price = calculate_price(ratio, 'Udupi', i[1])
        print(final_price)
        c.execute("UPDATE udupi SET price= ? WHERE id= ?", (final_price, index))
    conn.commit()
    conn.close()

def bangalore():
    conn = sqlite3.connect('crop.db')
    c = conn.cursor()
    c.execute("SELECT id, crop, investment, profit FROM bangalore")
    for i in c.fetchall():
        index = i[0]
        ratio = price_reduction(i[2],i[3])
        final_price = calculate_price(ratio, 'Bangalore rural', i[1])
        print(final_price)
        c.execute("UPDATE bangalore SET price= ? WHERE id= ?", (final_price, index))
    conn.commit()
    conn.close()


bijapur()
udupi()
bangalore()