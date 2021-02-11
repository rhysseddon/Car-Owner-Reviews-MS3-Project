# Testing

## Contents
- [Favicon](#Favicon)
- [Font](#Font)
- [Navbar](#Navbar)
- [Footer](#Footer)
- [Footer](#Footer)
- [Home Page](#Home-Page)
- [Register Page](#Register-Page)
- [Login Page](#Login-Page)
- [Profile Page](#Profile-Page)
 

#### Return to [README.md](README.md)

## Favicon
- A red car must display as the favicon once the page has loaded.

![Image](static/assets/images/readme-images/favicon-screenshot.png)

## Font
- The font 'Faster One' must be the font used on all titles and headings throughout the site. 
- The font 'Contrail One' must be the font used in all other areas of the site.

## Navbar

Display:
- "CAR OWNER REVIEWS" title on left hand side.
- Links on right hand side.
![Image](static/assets/images/readme-images/navbar-screenshot.png)
- On screen sizes less than 998px navigation links should collapse into burger icon and when selected 
should display as a side nav.
![Image](static/assets/images/readme-images/burger-screenshot.png)

<details>
<summary>Side Nav Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/sidenav-screenshot.png)
</p>
</details>

- For non logged in users nav links should display HOME | LOGIN | REGISTER
- For logged in users nav links should display  HOME | PROFILE | NEW REVIEW | LOGOUT
- For logged in admin users nav links should display  HOME | PROFILE | NEW REVIEW | MANAGE MAKES | LOGOUT
- Navbar should display the same across all pages.  

Functionality for both top nav and side nav links:  

- HOME is selected all users should be directed to home page.
- LOGIN is selected all users should be directed to login page.
- RESISTER is selected all users should be directed to register page.
- PROFILE is selected all logged in users should be directed to profile page.
- LOGOUT is selected all logged in users should be directed to login page and a flash message should appear 
with the message "YOU HAVE BEEN LOGGED OUT".  
![Image](static/assets/images/readme-images/logged-out-flash-screenshot.png)
- NEW REVIEW is selected all logged in users should be directed to new review page.
- MANAGE MAKES is selected logged admin in users should be directed to manage makes page.
- Functionality should remain the same across all pages.

## Footer

Display:

- Should display "Contact: Admin@carowners-rhys.com" on the top left side.
- Should display "Copyright 2021 Rhys Seddon" on the bottom left side.
- Facebook, Instagram and Twitter logos should display on the right side.
- Footer should display the same across all screen sizes and pages.

![Image](static/assets/images/readme-images/footer-screenshot.png)

Functionality:

- Facebook logo selected should redirect to facebook.com in a new browser window.
- Instagram logo selected should redirect to Instagram.com in a new browser window.
- Twitter logo selected should redirect to Twitter.com in a new browser window.

## Home Page

Display:

- The full width hero image must display below the navbar.

<details>
<summary>Background Image (Click for image)</summary>
<p align="center">

![Image](static/assets/images/cars-hero.jpg)
</p>
</details>

- Below hero image Welcome section should display on left and search bar on right.  
![Image](static/assets/images/readme-images/welcome-search-desktop-screenshot.png)

- Welcome section should display above search bar on mobile screen sizes.  

<details>
<summary>Welcome Section Mobile Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/welcome-search-mobile-screenshot.png)
</p>
</details>


- Welcome section should display the heading "WELCOME" with a paragraph of information 
and a register and login button below.

<details>
<summary>Welcome Section Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/welcome-screenshot.png)
</p>
</details>

- Search bar should display a magnifiying glass icon, a text input area with the
 placeholder "Search make or model" and a "search" and "reset" button.  
 ![Image](static/assets/images/readme-images/search-screenshot.png)

 - All reviews section should display a central title "ALL REVIEWS".
 - A dropdown accordion containing the reviews should display below.
 - Each accordion section header should contain a down arrow icon, the make, model, year and creator of the 
 review (owner)
 - When each header is selected a dropdown should appear below containing: Make, Model, Year, Review, Rating
 and Owner fields. 
 - For admin users "EDIT" button and "DELETE" buttons should also display on the accordion. 

 <details>
<summary>All reviews Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/all-reviews-screenshot.png)
</p>
</details>

- When there are no reviews in the database, in the place of the accordion a message will appear
 "NO REVIEWS FOUND".

Functionality:

- The welcome section "REGISTER" button when selected should redirect all users to the register page"
- The welcome section "LOGIN" button when selected should redirect all users to the login page"
- The search bar should search for any make or model key word in any of the reviews and those reviews
should then appear in the accordion below.
- If the search obtained no results in the place of the accordion a message "NO REVIEWS FOUND" should 
appear.
- If the user inputs less than 3 letters they should be given a warning displaying "Please lengthen this 
text to 3 characters or more (you are currently using *no. of characters* characters").
- If the "RESET" button is selected the page should revert back to all reviews (if any) displaying.
- When "EDIT" is selected on the review accordion admin users should be redirected to prefilled 
edit page.
- When "DELETE" is selected, the delete popup modal should appear.
- If "DELETE" is again selected on the modal, the corresponding review will be permanently deleted from the accordion 
and the database.
- If "CANCEL" is selected, it should revert back to the all reviews page.

 <details>
<summary>Delete Modal Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/delete-modal-screenshot.png)
</p>
</details>

## Register Page

Display:

- Should retain the basic layout and remain responsive on all screen sizes.
- Should have the central title "REGISTER"
- Central card panel form should display.
- Username input with icon and placeholder "Please enter a username - between 5 and 12 characters"  
- Password input with icon and placeholder "Please enter a password - between 5 and 12 characters"
- Central "REGISTER" button.
- Below card panel centrally should read "Already Registered? Login Here" and the "Login Here" text 
should display as a link.  

 <details>
<summary>Register Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/register-screenshot.png)
</p>
</details>

Functionality:

- The username and password input fields should only allow 12 characters to be entered.
- If less than 5 characters are entered the below line should turn red and when the 
register button is selected a warning will appear that reads: "Please match the format requested".
- If both fields are correctly completed the below lines will turn green, the user will be
redirected to the profile page and a flash message will appear: "WELCOME TO THE CLUB!"  
![Image](static/assets/images/readme-images/club-screenshot.png)
- Testing should be now carried out by selecting "LOGOUT" in the navbar, then the previous username 
and password re entered to check if the registration has been successful.
- The "Login Here" link below should redirect to login page.

## Login Page

Display:

- Should retain the basic layout and remain responsive on all screen sizes.
- Should have the central title "LOGIN"
- Central card panel form should display.
- Username input with icon and placeholder "Please enter a username - between 5 and 12 characters"  
- Password input with icon and placeholder "Please enter a password - between 5 and 12 characters"
- Central "LOGIN" button.
- Below card panel centrally should read "Not Registered? Register Here" and the "Register Here" text 
should display as a link.  

 <details>
<summary>Login Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/login-screenshot.png)
</p>
</details>

Functionality:

- The username and password input fields should only allow 12 characters to be entered.
- If less than 5 characters are entered the below line should turn red and when the 
login button is selected a warning will appear that reads: "Please match the format requested".
- If both fields are correctly completed the below lines will turn green, the user will be
redirected to the profile page and a flash message will appear: "WELCOME *username*"  
![Image](static/assets/images/readme-images/welcome-profile-screenshot.png)
- The "Register Here" link below should redirect to login page.

## Profile Page

Display:

- Should retain the basic layout and remain responsive on all screen sizes.
- The page heading should display "*username*'s Profile".
- The sub heading should display "Your Reviews"
- A dropdown accordion containing the users reviews should display below.
- Each accordion section header should contain a down arrow icon, the make, model and year.
- When each header is selected a dropdown should appear below containing: Make, Model, Year, Review
and rating.
- "EDIT" and "DELETE" buttons should also display on the accordion header.
- When there are no reviews in the database, in the place of the accordion a message will appear
 "NO REVIEWS FOUND".
- Below the accordion a central button "ADD NEW REVIEW" with a plus icon.

<details>
<summary>Profile Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/profile-screenshot.png)
</p>
</details>

Functionality:

- When "EDIT" is selected on the review accordion users should be redirected to prefilled 
edit page.
- When "DELETE" is selected, the delete popup modal should appear.
- If "DELETE" is again selected on the modal, the corresponding review will be permanently deleted from the accordion 
and the database. 
- If "CANCEL" is selected, it should revert back to the all reviews page.
- If "ADD NEW REVIEW" is selected users should be directed to the new review page.






