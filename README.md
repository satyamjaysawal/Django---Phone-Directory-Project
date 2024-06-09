'''
Coding Task
Create a REST api to be consumed by a mobile app, which is somewhat similar to various popular apps
which tell you if a number is spam, or allow you to find a person’s name by searching for their phone
number.
You can use whichever language/framework you're most comfortable in. However, we give strong
preference to candidates in the pipeline who’ve done it using Django, and to a lesser extent Flask or
Rails. For persistence you need to use a relational database along with an ORM for your framework. We
will not evaluate NoSQL or raw SQL queries.
Terminology and assumptions:
● Each registered user of the app can have zero or more personal “contacts”.
● The “global database” is basically the combination of all the registered users and their personal
contacts (who may or may not be registered users).
● The UI will be built by someone else - you are simply making the REST API endpoints to be
consumed by the front end.
● You will be writing the code as if it’s for production use and should thus have the required
performance and security. However, only you should use only a web server (the development
server is fine) and a database, and just incorporate all concepts using these two servers. Do not
use other servers.
Data to be stored for each user:
● Name, Phone Number, Email Address.
Registration and Profile:
● A user has to register with at least name and phone number, along with a password, before
using. He can optionally add an email address.
● Only one user can register on the app with a particular phone number.
● A user needs to be logged in to do anything; there is no public access to anything.
● You can assume that the user’s phone contacts will be automatically imported into the app’s
database - you don’t need to implement importing the contacts.
Spam:
● A user should be able to mark a number as spam so that other users can identify spammers via
the global database. Note that the number may or may not belong to any registered user or
contact - it could be a random number.
Search:
● A user can search for a person by name in the global database. Search results display the name,
phone number and spam likelihood for each result matching that name completely or partially.
Results should first show people whose names start with the search query, and then people
whose names contain but don’t start with the search query.
● A user can search for a person by phone number in the global database. If there is a registered
user with that phone number, show only that result. Otherwise, show all results matching that
phone number completely - note that there can be multiple names for a particular phone number
in the global database, since contact books of multiple registered users may have different names
for the same phone number.
● Clicking a search result displays all the details for that person along with the spam likelihood. But
the person’s email is only displayed if the person is a registered user and the user who is
searching is in the person’s contact list.
Data Population:
● For your testing you should write a script or other facility that will populate your database with a
decent amount of random, sample data.
'''




## Django - Phone Directory Project

![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/5aba0ca5-0f58-4f37-9aae-3d08cc0e64ca)


![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/8986e4be-f73b-4694-b3d7-b212c3df2d69)


![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/26ef2f78-175e-4c52-b9d7-5eafd6e3b9e6)


![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/6980a2a0-02a3-4093-92c4-06555bb85849)


![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/83343bf3-8d9b-4d60-b8d9-f988a07c4a17)


![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/2c4a7b84-ad0b-49b8-a75e-ddc41ed91138)

## http://127.0.0.1:8000/
## http://127.0.0.1:8000/admin/
## http://127.0.0.1:8000/api/users/register/
## http://127.0.0.1:8000/api/users/login

![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/d6168899-e67a-49c0-adfe-8a0bb0227939)


![image](https://github.com/satyamjaysawal/Django_Project/assets/108862706/7f304728-5bae-4935-b79e-29e1bd472c56)




