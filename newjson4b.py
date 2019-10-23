'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to write out received data to an HTML file 
'''

import requests
import json

# Find APIs at - https://apilist.fun/

# For any indentation errors, make sure there are no tabs (\t) by doing 
# a full replace of \t with 4 actual spaces

def writeHTML(data):
    myfile = open("playerAPI.html","w") # use "a" to "append"
    
    ############### CSS
    
    myfile.write("""
    <html>

      <head>
        <title> MY PAGE </title>
      </head>

      <body>
        <font size="3" color="red">This is some text!</font>
        <font size="2" color="blue">This is some text!</font>
        <font face="verdana" color="green">This is some text!</font>
        <h1>Welcome to My Soccer Home Page</h1>

        <p>Go to <a href='https://apilist.fun/api/the-sports-db'>The Sports DB</a> for API Info.</p>

        <h1 style="background-color:DodgerBlue;">Here is player you requested</h1>

        <p>Date Born: """+ data+"""</p>

        <p style="font-family:verdana">This is a paragraph.</p>

        <p style="font-family:'Courier New'">This is another paragraph.</p>

      </body>

    </html>""")


    ################# CSS
    myfile.close()

def main():

    # Pull the data from the website and store it so that we can use it later

    #######
    # use API to get info about all the players on the Arsenal Soccer Team
    response = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Arsenal")

    # if API call is correct
    if (response.status_code == 200):
        
        # load as a JSON to access specific data more easily
        datajson = response.json()
        myDataP1DB = datajson['player'][0]['dateBorn']
        myDataP1N = datajson['player'][0]['strNationality']
        myDataP1T= datajson['player'][0]['strTeam']
        #writeHTML(myData1)  # call function to write string data to HTML file

    
    ####MENU

        print ("1. player1 ")
        print ("2. player2  ")
        print ("3. player3  ")
        choise = int(input("choose a player \n"))

        # outer if stmt
        if choise == 1:
            print("1. dateBorn  ")
            print("2. player nationality  ")
            print("3. players team  ")
            option = int(input("choose an option \n"))

        # Choosing a specific menu option
            # inner if stmt
            if option == 1:
                print (myDataP1DB)
            elif option == 2:
                print (myDataP1N)
            elif option == 3:
                print (mydataP1T)

        elif choise == 2:
            print("1. dateBorn  ")
            print("2. player nationality  ")
            print("3. players team  ")
            
         


        elif choise == 3:
            print("1. dateBorn  ")
            print("2. player nationality  ")
            print("3. players team  ")
             
        

        else:
            print ("This is not a valid choise")

    

main()