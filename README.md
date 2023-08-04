# events_webpage
Event Web Page Project is used to create event details and update and delete event details by Event organizer and also to intimate the audience about event. 

Main changes in the above Even Website are: 
1)In your mysql Database  create Database name as eventwebsite_db
2)The below commands are run in your terminal or commandprompt after download this event_webpage -->cd event_webpage (change the directory main project and makemigration command as follows) -->python manage.py makemigrations(Afther the makemigrations migrate using next command) -->python manage.py migrate (After migrate different tables are created in the Database) -->python manage.py createsuperuser (it is used log into admin page) -->Python manage.py runserver (after login data enter into two diffeterent tables are one is Locations table and another one is event table) 
3)Enter the url 127.0.0.1:8000/ then Homepage will appear in that login and SignUp pages are at top right corner 
4)After lo SignUp login with credential then it all events all visible 
5)If click at Event name it will update event details
6)In all event page top left corner we have ADDEVENT if we need to add desired events then click that ADDEVENT button add them
