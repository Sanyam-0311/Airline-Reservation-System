#TICKET FUNCTION WORKING INCORRECTLY WHILE CALLING THROUGH EXISITING FUNCTION

from tkinter import *
from tkinter.ttk import *
import mysql.connector
import sys
from twilio.rest import Client

#Basic syntax to connect to databse
mydb = mysql.connector.connect(  host="localhost",  user="root",  password="Sanyam123",  database="alr")
mycursor=mydb.cursor()


#User function to welcome user to my project on AIrline Reservation System
def user():
  print('WELCOME TO AIRLINE RESERVATION SYSTEM !!!')
  inp=input("Are you an existing user or do you want to create a new account :"
            "Enter yes if you are an existing user ")
  if inp.lower()!='yes':
    new()
  else :
    existing()


#Defined a new function to store values of new user
def new():
  mydb = mysql.connector.connect(host="localhost", user="root", password="Sanyam123", database="alr")             #Globally defined for the function new as it is getting called by another function
  mycursor = mydb.cursor()

  while True:
    login_id = int(input('Enter your login id:'))
    if login_id / 1000 >= 9:
      print('Invalid, Enter a 4 digit login id ')
      continue
    else:
      mycursor.execute("SELECT * FROM login")
      for i in mycursor:
        if i[0] == login_id:
          print('This login ID already exists, Please enter a new login ID')
          new()
    login_username = input('Enter your username:')
    if len(login_username)>8:
       print('Invalid, Enter a proper 8 digit username ,'
           'Enter your login ID again')
       continue
    user_password = input('Enter the password:')
    if len(user_password)>8:
      print('Invalid, Enter a proper 8 digit password '
            'Enter your login ID again')
      continue
    break
  print('Credentials stored succesfully !!')
  mycursor.execute(" insert into Login values(%s,%s,%s)",(login_id,login_username,user_password))
  mydb.commit()
  book=input('Do you want to book tickets... ? '
      'Enter Y to book and N to exit ')
  if book=='Y' or book=='y':
    booking()
  else:
    sys.exit('This is a project made by Sanyam Shah and Shreya Joshi \n '
             'Thank you !')


#Defined a function booking to store values of user to book tickets
def booking():
  ab_source = input('Enter place of origin :')
  ab_destination = input('Enter your destination:')
  mycursor.execute("select ae_title from airlines_enquiry")
  for i in mycursor:
    print(i[0])
  ab_Flight=input('Enter your choice of airlines from following airlines:')
  ab_date = input('Enter your date of travel: (Format:YYYY-MM-DD) ')
  ab_type = input('Enter your type of seat i.e. class (Economy,Prime,Business,Luxury):')
  ab_id=input('Enter your login ID ')
  mycursor.execute("insert into airlines_booking values(%s,%s,%s,%s,%s,%s)", (ab_source,ab_destination,ab_Flight,ab_date,ab_type,ab_id))
  mydb.commit()

  passenger()


#Defined a function passenger to store values of traveller
def passenger():
  while True:
    print('Now please enter the traveller details ')
    p_id = int(input('Passenger id: i.e. Enter your login ID '))
    p_name = input('Enter your name:')
    p_adress = input('Enter your adress:')
    p_email = input('Enter your Email ID:')
    p_mobile= int(input('Enter your mobile number:'))
    if p_mobile/10000000000 >= 9:
      print('Invalid, Enter 10 digit mobile number')
      continue
    break
  mycursor.execute(" insert into passenger values(%s,%s,%s,%s,%s)", (p_id,p_name,p_adress,p_email,p_mobile))
  mydb.commit()
  print('Passenger values stored successfully !!!')
  print('Your ticket has been booked !')
  see_ticket=input('Do you want to see your ticket ? Enter Y to check your ticket !')
  if see_ticket=='Y' or see_ticket=='y':
    ticket()
  else:
    sys.exit('This is a project made by Sanyam Shah and Shreya Joshi \n '
             'Thank you !!!')


#Defined a function ticket to store the ticket of the traveller
def ticket():
  mydb = mysql.connector.connect(host="localhost", user="root", password="Sanyam123", database="alr")               #Globally defined for the function ticket as it is getting called by another function
  mycursor = mydb.cursor()

  ab_ID = int(input('Enter your unique ticket id that is your login ID: '))
  val = (ab_ID,)          #Storing value in list format
  mydb.commit()
  print("           TICKET       \n ")
  passenger_values ='select p_name,p_email from passenger where passenger.p_id=%s'
  mycursor.execute(passenger_values,val)
  for i in mycursor:
    print('Name of the passenger is: ',i[0])
    print('Email id of the passenger is: ', i[1])
  #airplane_val='select airlines_booking.ab_date,airlines_booking.ab_source,airlines_booking.ab_destination,airlines_booking.ab_flight,airlines_booking.ab_type ,ticket.ab_id from airlines_booking inner join ticket on airlines_booking.ab_id=%s;'
  airplane_values = 'select ab_source,ab_destination,ab_flight,ab_date,ab_type from airlines_booking where ab_id=%s'
  mycursor.execute(airplane_values, val)
  for i in mycursor:
    print('Source Airport:',i[0])
    print('Destination Airport:', i[1])
    print('Flight Name: ', i[2])
    print('Date of Flight: ',i[3])
    print('Type of Seat: ',i[4])

  opt=input('Do you want to get the SMS for the following ticket booked ? \n'
        'Enter yes to get the sms :')
  if opt.lower()=='yes':
    sms()

  can=input('Do you want to cancel your ticket ?? \n'
            'Enter "cancel" to cancel the ticket or any other key to exit the program ')
  if can.lower()=='cancel':
    cancel()
  else:
    sys.exit('This is a project made by Sanyam Shah and Shreya Joshi \n'
           'Thank you !!!')

  #sms()
  #ID=input('ENter your airline booking id to get the ')


#Defined a function to cancel the ticket booked by the user
def cancel():
  mydb = mysql.connector.connect(host="localhost", user="root", password="Sanyam123", database="alr")         #Globally defined for the function cancel as it is getting called by another function
  mycursor = mydb.cursor()
  while True:
    c=input('Do you want to cancel your booking, Enter Y to cancel ! or any other key to Exit ')
    if c=='Y' or c=='y':
      ab_ID=int(input('Enter your unique ticket id that is your login ID:'))
      val = (ab_ID,)
      sql1 = "select p_name from passenger,airlines_booking where passenger.p_id=%s"
      mycursor.execute(sql1, val)
      print(f'Flight ticket for passenger named ',mycursor.fetchall()[0][0],' has been cancelled! ')       #TWO ARRAYS AS firstly it will return multiple values, in which we need to count only the first values ; and that value will be tuple so converted it into normal string
      sql2 = 'delete from airlines_booking where airlines_booking.ab_id=%s'
      sql3= 'delete from login where login.login_id=%s'
      sql4='delete from passenger where passenger.p_id=%s'
      mycursor.execute(sql2, val)
      mycursor.execute(sql3, val)
      mycursor.execute(sql4, val)
      mydb.commit()
      print('Thank you !')

    else:
      sys.exit('This is a project made by Sanyam Shah and Shreya Joshi \n'
               'Thank you !!!')


#Error in taking multiple values
def existing():

  option=input('Do you want to cancel your ticket or do you want to view your ticket ?'
        'If you want to cancel your ticket then please enter c or '
        'if you want to view your ticket then please enter v: ')
  if option=='c' or option=='C':
    cancel()
  elif option=='v' or option=='V':
    while True:
      login_id = int(input('Enter your login id:'))
      mycursor.execute("SELECT * FROM login")
                   # To check if value is already present in the table
      for i in mycursor:
        if i[0]==login_id:
          ticket()
      else:
          print('Enter a correct login ID, there is no such user for this particular ID')
      continue


#Defined a function to print the sms on user's mobile
def sms():

  mydb = mysql.connector.connect(host="localhost", user="root", password="Sanyam123", database="alr")
  mycursor = mydb.cursor()
  account_sid = 'ACaa09698f7e6c933dc919c74a063d23f6'
  auth_token = '96f074c685667aa10cc6430021316b0d'
  client = Client(account_sid, auth_token)
  number = +918356088944
  ab_ID = int(input('Enter your unique ticket id that is your login ID: '))
  val = (ab_ID,)
  passenger_name = 'select p_name from passenger where passenger.p_id=%s'
  mycursor.execute(passenger_name, val)
  for i in mycursor:
    name=i[0]
  airplane_values = 'select ab_source,ab_destination,ab_flight,ab_date,ab_type from airlines_booking where ab_id=%s'
  mycursor.execute(airplane_values, val)
  for i in mycursor:
    Source_Airport=i[0]
    Destination_Airport=i[1]
    Flight_Name=i[2]
    Date_of_Flight=i[3]
  message = client.messages.create(body=f'Thank you {name} for booking a flight with us!\n '
                                        f'Passenger Name:{name} \n'
                                        f'Flight :{Flight_Name} \n'
                                        f'Source Airport :{Source_Airport} \n'
                                        f'Destination Airport: {Destination_Airport}\n' \
  f' The flight is scheduled on {Date_of_Flight}',from_=+13609681982, to=number)

  print(message.body)



#Defined a function close to close the dialogue box
def Close():                #defined a function to close the window on clicking of the button
  root.destroy()


#Defined a main function
while True:
  root = Tk()
  Label(root)
  photo = PhotoImage(file=r'Flightpicture.png')
  Button(root,image=photo,command=Close).pack()
  mainloop()
  user()
  #sms()