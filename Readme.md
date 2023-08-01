# Password Hash

## Inspiration
Wanted to learn about password hashing so I implemented the SHA-1 algorithm and made a Django app with authentication features. Note: The app does not use the implementation and it is only for learning purposes.
## What it does
Login, logout. Will further modify to display information about SHA1.
## How we built it
Django and digital ocean with app. 

https://docs.digitalocean.com/tutorials/app-deploy-django-app/

https://www.youtube.com/watch?v=kVUYzbNM2wU&ab_channel=GKTCSINNOVATIONS
## Challenges we ran into
Yesterday I tried using docker and although I setup a DO droplet and managed to deploy a Django app, I could not figure out how to develop in the environment and did not want to make a Django app in the terminal... So I used the App Platform feature instead. Took a little while to find the create additional service -> database feature when creating the app in digital ocean.
## Accomplishments that we're proud of
Authentication feature and correctly implemented SHA1 algorithm.
## What we learned
Reminded myself of some Django, learned about Digital Ocean web services, and learned about hashing and specifically the SHA1 algorithm.
## What's next for Password Hasher
More styling and actually showcase the algorithm. Right now the algorithm is sitting in a python file called sha1.py and there is nothing about it displayed in the web app.
