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

        <p>The Information you Requested is: """+ data+"""</p>

        <p style="font-family:verdana">This is a paragraph.</p>

        <p style="font-family:'Courier New'">This is another paragraph.</p>

      </body>

    </html>""")


    ################# CSS
    myfile.close()

def main():


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

        myDataP2DB = datajson['player'][1]['dateBorn']
        myDataP2N = datajson['player'][1]['strNationality']
        myDataP2T = datajson['player'][1]['strTeam']

        myDataP3DB = datajson['player'][2]['dateBorn']
        myDataP3N = datajson['player'][2]['strNationality']
        myDataP3T = datajson['player'][2]['strTeam']
        
    ####MENU
        print ("1. player1 ")
        print ("2. player2  ")
        print ("3. player3  ")
        choise = int(input("choose a player \n"))

        # outer if stmt
        if choise == 1:
            print("1. dateBorn  ")
            print("2. player Nationality  ")
            print("3. players Team  ")
            option = int(input("choose an option \n"))

        # Choosing a specific menu option
            # inner if stmt
            if option == 1:
                print (myDataP1DB)
                writeHTML(myDataP1DB)  # call function to write string data to HTML file
  
            elif option == 2:
                print (myDataP1N)
                writeHTML(myDataP1N)  # call function to write string data to HTML file

            elif option == 3:
                print (myDataP1T)
                writeHTML(myDataP1T)  # call function to write string data to HTML file

        elif choise == 2:
            print("1. dateBorn  ")
            print("2. player nationality  ")
            print("3. players team  ")
            option = int(input("choose an option \n"))

            if option == 1:
                print (myDataP2DB)
                writeHTML(myDataP2DB)  # call function to write string data to HTML file

            elif option == 2:
                print (myDataP2N)
                writeHTML(myDataP2N)  # call function to write string data to HTML file

            elif option == 3:
                print (myDataP2T)
                writeHTML(myDataP2T)  # call function to write string data to HTML file

        elif choise == 3:
            print("1. dateBorn  ")
            print("2. player nationality  ")
            print("3. players team  ")
            option = int(input("choose an option \n"))
            
            if option == 1:
                print (myDataP3DB)
                writeHTML(myDataP3DB)  # call function to write string data to HTML file

            elif option == 2:
                print (myDataP3N)
                writeHTML(myDataP3N)  # call function to write string data to HTML file

            elif option == 3:
                print (myDataP3T)
                writeHTML(myDataP3T)  # call function to write string data to HTML file

        else:
            print ("This is not a valid choise")   
main()