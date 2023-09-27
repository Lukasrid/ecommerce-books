# Book Store

Book Store is an online store where people can browse and purchase new and used books. 

The Site can be accessed via https://book-store-lukarid-9168f1b715ae.herokuapp.com/

ADD IMAGE RESPONSIVE

# User Experience Design


## The Strategy Plane
---

### Site Goals
The goal of the site is so that the owner can sell new and used books to customers from around the globe. The site should provide easy and quick ways to organise the meterial presented for the consumer so they may find what they are looking for with ease. For regular customers who wish to purchase books on a regular basis a profile page is provided where personal information is stored quick and convenient checkouts. A personal purchase history is also provided so registered customers may view their previous orders at any time. 

### Agile Planning
The development of an ecommerce website requires an organized and efficient approach. Agile methodology provides a flexible and iterative framework that promotes collaboration, adaptability, and continuous improvement. Here is an overview of the Agile plan for creating this recipe sharing website.

The first sprint, "Project Setup," focuses on establishing the project foundation. This includes setting up the repository and version control system, defining project goals and user stories, and creating a basic Django project structure. An html layout will be created to display the books using bootstrap.

In the second sprint, "Book Navigation," a system to easily search for books will be implemented. This could be done by searching for specific keywords that match book titles, summaries or authors. The books will be put into specific genres that the customers could easily only display books from a specified genre if desired. The books on display will also have the option to be displayed in order of price, title, genre or new/used. Any book can be clicked so that you are taken to a new page where furthur more detailed information is provided about the selected book.

The third sprint, "Checkout and Payment," will allow users to add/remove books to a checkout bag where a total price will be calculated and the books ready for purchase will be on display. The user is can proceede to an intergrated payment system when when ready and fill in shipping detail.

In the fourth sprint, "User Profile and CRUD," users will be able to create accounts where they can store their personal shipping information and view previous purchases. Site admins will have access to add, delete and update books in the system

In the fifth sprint, "User Experience Enhancements," the focus shifts towards improving the overall user interface and experience. The website's design is refined to be visually appealing and user-friendly. success and error messages will be displayed for actions performed on the site and a small pop up window will be displayed when changes to the bag is made.

The final sprint, "Deployment and Final Touches," involves the deployment of the website on Heroku. The code is modified to work on all screen sizes through media quiries. Extensive testing and bug fixing are conducted to ensure a stable and error-free experience.

#### Epics & User Stories
This project consited of 6 main Epics

1. Project Setup
    - As a developer I need to develop a basic structure and layout so that i can easily navigate and edit the website
    - As a developer I need to create templates for each of the different pages of the website so that I can implement different functionality
    - As a developer i need to create a navigation bar so that other users can navigate the website
    - As a developer I need to create models so that I know what information is going to be displayed and can be edited
    - As a developer I need to connect the website to a database so that all the information thats input into the website can be stored somewhere

2. Book Navigation
    - As a user I can browse different genres so that it is easier to navigate
    - As a user I can select a book to gain a furthur understanding of the contents of the book
    - As a user I can search for books so that its easy to find books related to the search term
    - As a user I can organize the books by price, title, author or used/new
    - As a user I can see a picture of the book cover to grab my attention
    - As a user I can get result for searches with partial/incomplete words so that it makes searching easier


3. Checkout and Payment
    - As a user I can add/delete books to my checkout basket
    - As a user I can view my basket with the total sum and contents I have placed into it
    - As a user I can provide my shipping details
    - As a user I can pay for my books
    - As a developer I can safely store the users shipping information
    - As a developer I can recive the users payment for their books

4. User Profile and CRUD
    - As a user I can register and log in to a personal profile
    - As a user I can add my shipping details for faster checkout
    - As a user I can view my previous purchases
    - As a developer i can add, delete and update books on the website

5. User Experience Enhancements
    - As a developer I want the site to be visually pleasing so that people will want to return
    - As a user I am provided with a stable and bug free environment so that I can browse through the website with ease
    - As a user I am provided with regular updates on the the things I am doing

6. Deployment and Final Touches
    - As a user I can use the website on all my electronic devices so that I can access it anywhere I am
    - As a developer I need the website to be available to the public so that people can use it

## The Structure Plane
---
### Features
#### **All Pages**
- *Navigation Bar*

    The navigation bar is located at the top of every page on the websit. It is used to help navigate the website from any page. 

    ADD IMAGE

    - Logo/Header -> Visual representations of the website and also works as a links back to homepage.
    - Login/Logout -> A button located in the top right hand corner that allows user to navigate to the login page or log out of their current account. Clicking on the icon will allow users to see if they are logged in. Users can also navigate to their peronal profile from this button. If the user is a developeer they can also use this button to navigate to the page to add books.
    - Checkout bag -> A button next to the user profile button at the top right where users have access to their checkout bag.  
    - Search Bar -> The search bar located in the middle at the top of the screen where users can type in search phrases to search for books.
    - Book Access -> Access to books or specific book genres available under the search bar in drop down menus.

#### **Homepage**
- *Redirect to Books*

    On the homepage a button is presented to the user inviting them in to browse the book selection and redirects all the available books. A header is provided informing the user of a free delivery threshold.

    ADD IMAGE HOMEPAGE

#### **Book Selection Page**
- *Books and Order*
    
    The number of available books for the selected genre is displayed at the top left under the navigation bar and the a drop down menu to the right shows what kind of order the books are in and can also be used to reorganize the books.

    ADD IMAGE DROPDOWN MENU


- *Individual book boxes*

    All the available books for purchase are displayed in 4 columns.

    ADD IMAGE BOOK SELECTION

    - The number of available books for selected genre is displayed at the top.
    - The genre of the book each book displayed is stated atthe top of each book.
    - A picture of the book cover is then displayed
    - Followed by a the book title.
    - And then the Author.
    - A tag is then displayed if the book is used.
    - And then the price is displayed at the bottom.
    - If the user is a developer an Edit/Delete option is displayed under the price.
#### **Profile Page**

    Same as Homepage but the 'main feed' and 'recent activity feed' only show activity related to the user. Their name is also printed out at the top of the 'main feed'

![Profile Page](/static/images/Profile.JPG)



#### **Create Recipe Page**

![Create Recipe](/static/images/Create%20Recipe.JPG)

- *Dish*

    The user can enter a name for the recipe.

- *Cuisine*

    The user can select a cuisine the dish belongs to from a dropdown menu. The user is unable to create their own unique cuisines.

- *Description*

    The user can write a breif description of the recipe.

- *Ingredients*

    The user can write down a list of ingredients for the recipe.

- *Method*

    The user can write down instructions on how to prepare the recipe.

- *Image*

    The user can choose to include an image of the completed dish. (Optional)

- *Submit*

    The user then can click submit to send off the information to be stored in a PostgreSQL database to then be presented on the website. 

#### **Delete Page**
    When a a user tries to delete a recipe that they have created, they are redirected to the delete page where they are asked if they are sure about their choice. They then have the option to cancel by pressing 'Go Back' or to delete it by pressing 'Confirm'.

![Delete Page](/static/images/Delete%20page.JPG)

#### **Login Page**

    The user can enter their email and password in the fields provided and then click sign in. If they however do not have an account they can press the 'Sign up!' button to be redirected to the Register Page.

![Login](/static/images/Login%20Box.JPG)
 

#### **Register Page**

    The user can fill in the required fields and click the 'Register' button to register themselves as a member. They are also prompted with a 'Login' button at the bottom incase they already have an account.

![Register Box](/static/images/Register%20Box.JPG)

### Future Features
- The registration form and the create recipe form will be stylized better (ran out of time to figure out how to do this).
- A footer is to be added.
- Users will be able to make a contact list of people they like.
- Users will be able to save and favourite recipes.
- Direct private messaging to other user will be implented.
- Emails will be added so that admin can contact users.
- Users will be able to request new cuisines at admin approval.
- Users will be able to search for other usersand not only recipes.
- Screen responsiveness will be improved.
- Activity feed will include more than just comments.
- Sweet and savoury catagories will be added for easier navigation.
- Users will be able to add a profile picture and customize their profile page more.
- A heading will be added at the top for when browing a specific cuisine.
- The number of recipies available from a user will be displayed at the top of a profile page like it does for the homepage and cuisine catagories.
- Users will be able to delete their account
- Users will be able to report or flag inappropriate content.


## The Surface Plane
### Design
#### Color Scheme
The main color schmemes used on the wbsite was a grey (#e0e0e0) for the background a kind of red (#800000) for highlighting important words and features. Rest of the text is black.
#### Typography
A font called "Cougette" was used as the main title and other key titles. The rest of the text id "Open Sans". The back up fonts are "Tahoma" and "Sans-Serif".
#### Imagery
The logo image was made using [freelogodesign.org](https://www.freelogodesign.org/).

All other images were taken from [Pexels](https://www.pexels.com/).

# Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to insert icons.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- PostgreSQL
    - The database where all data is stored that is put into the website.
- Cloudinary
    - Where all the images that get uploaded are stored
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/

### External Python Modules
- asgiref==3.7.2
- cloudinary==1.33.0
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.3
- gunicorn==20.1.0
- Pillow==9.5.0
- psycopg2==2.9.6
- pytz==2023.3
- sqlparse==0.4.4
- urllib3==1.26.16
- whitenoise==6.5.0


# Testing
## Functionality Testing
The website has been thoroughly tested to see if it work, these include:

- All processed information gets stored in the linked up PostgreSQL database.
- All uploaded images get stored and viewd via Cloudinary.
- All links are working and take you to the right destination.
- All no information can be submitted without the right content and the required fields filled in.
- Non-registered users do not have access to features.
- Registered users do have access to features.
- Activity shows up in the correct order of when created/edited on all pages.
- Only relavant information shows up when viewing specific cuisines or profile pages.

## Validator Testing
### HTML Validator
The website was run through [W# HTML Validator](https://validator.w3.org/)

![HTML Validator](/static/images/HTML%20checker.JPG)

### Lighthouse
The lighthouse report showed decent results with areas of improvement in SEO and Best Practices.

![Lighthouse results](/static/images/lighthouse%20results.JPG)


# Development
### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘recipe-tracker’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](https://flavoured-adventures-f1491c2fd119.herokuapp.com/)

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.


# Credits

 ## Content

 ## Acknoledgements
 