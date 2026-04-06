#Importing the requests library for URL get requests
import requests

#Reading from CSV file
urlData = open("Task 2 - Intern.csv")

#Iterating through the list of URLs in the CSV file
for url in urlData:
    #Attempting to open the URL and requesting the URL status
    try:
        urlStatus = requests.get(url)
        print(urlStatus.status_code, url)

    #Exception handling for any errors when requesting the URL status
    except requests.exceptions.HTTPError as errh:
        print("Error - HTTP")
    except requests.exceptions.ReadTimeout as errrt:
        print("Error - Took Too Long (Timeout)")
    except requests.exceptions.ConnectionError as conerr:
        print("Error - No Connection")
    except requests.exceptions.RequestException as errex:
        print("Error - Other Reasons")
