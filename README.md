# Web scraping data from the Jumia website and saving it to a MySQL database and CSV file.
- Here, I provide code and illustrate how to scrape data from a website using the BeautifulSoup and **lxml** Python libraries. **lxml** is chosen as the parser for BeautifulSoup to parse the HTML content of the webpage, this is because **lxml** is faster than the default Python parser (html.parser).
- The scraped data is then saved to a **MySQL** database and **CSV File**.

## 💡 First we import the required libraries/dependencies

- **BeautifulSoup**: A library for parsing HTML and XML documents.
- **requests**: A library for making HTTP requests.
- **lxml**: A library for parsing XML and HTML, used by BeautifulSoup.
- **mysql.connector**: A library for connecting to a MySQL database.
- **datetime**: A module for manipulating dates and times.
- **csv**: A module for reading and writing CSV files.
  
![image](https://github.com/user-attachments/assets/7be4ba8c-b771-42be-a562-efd2f18b20ed)

## 💡 Now we fetch the HTML content
- Here we send a HTTP GET request to the specified URL and retrieve the HTML content of the webpage. The `.text` attribute converts the response content to a string.
  
  ![image](https://github.com/user-attachments/assets/0f3b1593-fa17-4367-92ab-35a1cfdbedf9)
  
## 💡 Saving the HTML Content to a File
- Here we open a file in write mode (`'w'`) at the specified path and write the HTML content to the file. The `encoding='utf-8'` ensures the file is written with UTF-8 encoding.

  ![image](https://github.com/user-attachments/assets/ce6db3f6-8f41-495e-9f81-5ec0a9e6cf3a)

## 💡 Parsing the HTML Content
- We create a BeautifulSoup object named `soup` by parsing the HTML content using the `lxml` parser.
- The `find_all` method searches for all `article` elements with the class `'prd _fb col c-prd'` and stores them in the `laptops` list.
  
![image](https://github.com/user-attachments/assets/b705b340-069b-40e3-b31b-081870cd8805)

## 💡 Connecting to the MySQL Database
- We then establish a connection to the MySQL database using the provided credentials and connection details.
- A cursor object is created to execute SQL queries.
  
![image](https://github.com/user-attachments/assets/ea8f3689-aebc-4a98-87e0-b8dffa454354)

## 💡 Creating the Table
- We use SQL query to create a table named `Laptops` if it does not already exist. The table has columns for storing laptop details and a primary key `Laptop_Id` that auto-increments.

![image](https://github.com/user-attachments/assets/c02824d5-8c51-4c10-85c2-eca9c992fdcb)

## 💡 Writing to a CSV File and Inserting Data into the Database
- This code opens a CSV file for writing and writes the header row.
- It then iterates over each laptop in the `laptops` list, extracting the relevant details.
- For each laptop, it prints the details, inserts them into the `Laptops` table in the database, and writes them to the CSV file.

![image](https://github.com/user-attachments/assets/32f3043b-6307-47b5-b0af-049795bd2738)

## 💡 Closing the Database Connection
- This code closes the cursor and the database connection and prints a confirmation message.
  
![image](https://github.com/user-attachments/assets/36c118df-8a4f-47f6-909d-3b1baf58f691)

## 💡 Summary 
- The script fetches HTML content from a Jumia webpage, parses it to extract laptop details, saves the details to a MySQL database and a CSV file, and prints the details to the console.

📌 **Follow the links to get the Python code, HTML code for the page being scraped, and CSV File.**
- [CSV Data](https://github.com/SHIVOGOJOHN/Web-scrapping-data-from-Jumia-website-and-save-to-a-sql-database-and-csv-file/blob/main/refurbLaptops.csv)
- [Python Code](https://github.com/SHIVOGOJOHN/Web-scrapping-data-from-Jumia-website-and-save-to-a-sql-database-and-csv-file/blob/main/jumia.py)
- [HTML Code](https://github.com/SHIVOGOJOHN/Web-scrapping-data-from-Jumia-website-and-save-to-a-sql-database-and-csv-file/blob/main/refurbLaptops.html)


