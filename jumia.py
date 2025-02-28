from bs4 import BeautifulSoup
import requests
import lxml
import mysql.connector
from datetime import datetime
import csv

#scrap jumia for 'refurbished laptops'
response = requests.get("https://www.jumia.co.ke/computing/?tag=REFU").text # .text converts the responcse content to a string

#save the response to a file
with open(r"C:\Users\A\Downloads\refurbLaptops.html", 'w', encoding='utf-8') as file:
    file.write(response)

#find all the laptops
soup=BeautifulSoup(response, "lxml")
laptops=soup.find_all("article", class_='prd _fb col c-prd')


#connect to the database
connection=mysql.connector.connect(
    charset="utf8mb4",
    connection_timeout=10,
    database="xxxxxx",
    host="mysql-f3601b9-jonesjorney-bd4e.f.aivencloud.com",
    password="xxxxxx",
    port=21038,
    user="xxxxx"
)

cursor=connection.cursor()

#Create a table in the database if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS Laptops(
    Laptop_Id INT AUTO_INCREMENT PRIMARY KEY,
    Laptop_Brand VARCHAR(255),
    Laptop_Price VARCHAR(255),
    Laptop_Old_Price VARCHAR(255),
    Laptop_Discount VARCHAR(255),
    Laptop_Ratings VARCHAR(255),
    Scraped_At DATETIME
)          
    """)


#Open a csv file for writing
with open(r"C:\Users\A\Downloads\refurbLaptops.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(["Laptop_Brand", "Laptop_Price", "Laptop_Old_Price", "Laptop_Discount", "Laptop_Ratings", "Scraped_At"])
    

    #insert the laptops into the database
    for lap in laptops:
        laptop_brand = lap.find("h3", class_="name").text
        laptop_price = lap.find("div", class_="prc").text
        laptop_old_price = lap.find("div", class_="old").text if lap.find ("div", class_="old") else None
        laptop_discount = lap.find("div", class_="bdg _dsct _sm").text if lap.find("div", class_="bdg _dsct _sm") else None
        laptop_ratings = lap.find("div", class_="rev").text if lap.find("div", class_="rev") else None
        scraped_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        print(f'''
    Laptop Info: {laptop_brand}
    Laptop Price: {laptop_price}
    Laptop Old Price: {laptop_old_price}
    Laptop Discount: {laptop_discount}
    Laptop Ratings: {laptop_ratings}
            ''')
        
        cursor.execute("INSERT INTO Laptops(Laptop_Brand, Laptop_Price, Laptop_Old_Price, Laptop_Discount, Laptop_Ratings, Scraped_At) VALUES(%s, %s, %s, %s, %s, %s)", (laptop_brand, laptop_price, laptop_old_price, laptop_discount, laptop_ratings, scraped_at))
        connection.commit()

        # Write the data row to the CSV file
        csvwriter.writerow([laptop_brand, laptop_price, laptop_old_price, laptop_discount, laptop_ratings, scraped_at])

#close the database connection
cursor.close()
connection.close()

print("Data has been saved to the database")
