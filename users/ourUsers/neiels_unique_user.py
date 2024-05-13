import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")


# Track presence time 
start_time = time.time()
presence_time = start_time
end_time = 10
check = False
imageBool = False
while int(presence_time) != end_time: # seconds
    #track time
    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    print(f"End time: {end_time} seconds")
    time.sleep(2) 
 
    try:
        divs = driver.find_elements(By.TAG_NAME, 'div')

        if imageBool == False:
            print(f"Div count: {len(divs)}")
            if len(divs) == 1:
                end_time = end_time + end_time
            end_time = end_time * len(divs)
            imageBool = True
    except NoSuchElementException:
        print("Divs not found")

    try:
        
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')
        count = 0
        if (check == False):
            for e in paragraphs:
                par = e.text
                for i in par:
                    if (i == "I"):
                        count = count + 1
                        end_time = end_time + 10
                        check = True
            print(f"There is {count} I's")              
    
            
        # if imageBool == False:
        #     print(f"Div count: {len(number7)}")
        #     if len(number7) == 1:
        #         end_time = end_time + end_time
        #     end_time = end_time * len(number7)
        #     imageBool = True
    except NoSuchElementException:
        print("no number 7s not found")

    


# Close the browser
driver.quit()
