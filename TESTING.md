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
- [New Review Page](#New-Review-Page)
 

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
- On screen sizes less than 998px navigation links must collapse into burger icon and when selected 
must display as a side nav.
![Image](static/assets/images/readme-images/burger-screenshot.png)

<details>
<summary>Side Nav Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/sidenav-screenshot.png)
</p>
</details>

- For non logged in users nav links must display HOME | LOGIN | REGISTER
- For logged in users nav links must display  HOME | PROFILE | NEW REVIEW | LOGOUT
- For logged in admin users nav links must display  HOME | PROFILE | NEW REVIEW | MANAGE MAKES | LOGOUT
- Navbar must display the same across all pages.  

Functionality for both top nav and side nav links:  

- HOME is selected all users must be directed to home page.
- LOGIN is selected all users must be directed to login page.
- RESISTER is selected all users must be directed to register page.
- PROFILE is selected all logged in users must be directed to profile page.
- LOGOUT is selected all logged in users must be directed to login page and a flash message 
must appear with the message "YOU HAVE BEEN LOGGED OUT".  
![Image](static/assets/images/readme-images/logged-out-flash-screenshot.png)
- NEW REVIEW is selected all logged in users must be directed to new review page.
- MANAGE MAKES is selected logged admin in users must be directed to manage makes page.
- Functionality must remain the same across all pages.

## Footer

Display:

- Must display "Contact: Admin@carowners-rhys.com" on the top left side.
- Must display "Copyright 2021 Rhys Seddon" on the bottom left side.
- Facebook, Instagram and Twitter logos must display on the right side.
- Footer must display the same across all screen sizes and pages.

![Image](static/assets/images/readme-images/footer-screenshot.png)

Functionality:

- Facebook logo selected must redirect to facebook.com in a new browser window.
- Instagram logo selected must redirect to Instagram.com in a new browser window.
- Twitter logo selected must redirect to Twitter.com in a new browser window.

## Home Page

Display:

- The full width hero image must display below the navbar.

<details>
<summary>Background Image (Click for image)</summary>
<p align="center">

![Image](static/assets/images/cars-hero.jpg)
</p>
</details>

- Below hero image Welcome section must display on left and search bar on right.  
![Image](static/assets/images/readme-images/welcome-search-desktop-screenshot.png)

- Welcome section must display above search bar on mobile screen sizes.  

<details>
<summary>Welcome Section Mobile Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/welcome-search-mobile-screenshot.png)
</p>
</details>


- Welcome section must display the heading "WELCOME" with a paragraph of information 
and a register and login button below.

<details>
<summary>Welcome Section Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/welcome-screenshot.png)
</p>
</details>

- Search bar must display a magnifiying glass icon, a text input area with the
 placeholder "Search make or model" and a "search" and "reset" button.  
 ![Image](static/assets/images/readme-images/search-screenshot.png)

 - All reviews section must display a central title "ALL REVIEWS".
 - A dropdown accordion containing the reviews must display below.
 - Each accordion section header must contain a down arrow icon, the make, model, year and creator of the 
 review (owner)
 - When each header is selected a dropdown must appear below containing: Make, Model, Year, Review, Rating
 and Owner fields. 
 - For admin users "EDIT" button and "DELETE" buttons must also display on the accordion. 

 <details>
<summary>All reviews Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/all-reviews-screenshot.png)
</p>
</details>

- When there are no reviews in the database, in the place of the accordion a message will appear
 "NO REVIEWS FOUND".

Functionality:

- The welcome section "REGISTER" button when selected must redirect all users to the register page"
- The welcome section "LOGIN" button when selected must redirect all users to the login page"
- The search bar must search for any make or model key word in any of the reviews and those reviews
must then appear in the accordion below.
- If the search obtained no results in the place of the accordion a message "NO REVIEWS FOUND" must 
appear.
- If the user inputs less than 3 letters they must be given a warning displaying "Please lengthen this 
text to 3 characters or more (you are currently using *no. of characters* characters").
- If the "RESET" button is selected the page must revert back to all reviews (if any) displaying.
- When "EDIT" is selected on the review accordion admin users must be redirected to prefilled 
edit page.
- When "DELETE" is selected, the delete popup modal must appear.
- If "DELETE" is again selected on the modal, the corresponding review must be permanently deleted from the accordion 
and the database.
- If "CANCEL" is selected, it must revert back to the all reviews page.

 <details>
<summary>Delete Modal Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/delete-modal-screenshot.png)
</p>
</details>

## Register Page

Display:

- Must retain the basic layout and remain responsive on all screen sizes.
- Must have the central title "REGISTER"
- Central card panel form should display.
- Username input with icon and placeholder "Please enter a username - between 5 and 12 characters"  
- Password input with icon and placeholder "Please enter a password - between 5 and 12 characters"
- Central "REGISTER" button.
- Below card panel centrally must read "Already Registered? Login Here" and the "Login Here" text 
must display as a link.  

 <details>
<summary>Register Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/register-screenshot.png)
</p>
</details>

Functionality:

- The username and password input fields must only allow 12 characters to be entered.
- If less than 5 characters are entered the below line must turn red and when the 
register button is selected a warning will appear that reads: "Please match the format requested".
- If both fields are correctly completed the below lines will turn green, the user will be
redirected to the profile page and a flash message must appear: "WELCOME TO THE CLUB!"  
![Image](static/assets/images/readme-images/club-screenshot.png)
- Testing must be now carried out by selecting "LOGOUT" in the navbar, then the previous username 
and password re entered to check if the registration has been successful.
- The "Login Here" link below must redirect to login page.

## Login Page

Display:

- Must retain the basic layout and remain responsive on all screen sizes.
- Must have the central title "LOGIN"
- Central card panel form must display.
- Username input with icon and placeholder "Please enter a username - between 5 and 12 characters"  
- Password input with icon and placeholder "Please enter a password - between 5 and 12 characters"
- Central "LOGIN" button.
- Below card panel centrally must read "Not Registered? Register Here" and the "Register Here" text 
must display as a link.  

 <details>
<summary>Login Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/login-screenshot.png)
</p>
</details>

Functionality:

- The username and password input fields must only allow 12 characters to be entered.
- If less than 5 characters are entered the below line must turn red and when the 
login button is selected a warning will appear that reads: "Please match the format requested".
- If both fields are correctly completed the below lines will turn green, the user will be
redirected to the profile page and a flash message must appear: "WELCOME *username*"  
![Image](static/assets/images/readme-images/welcome-profile-screenshot.png)
- The "Register Here" link below must redirect to login page.

## Profile Page

Display:

- Must retain the basic layout and remain responsive on all screen sizes.
- The page heading must display "*username*'s Profile".
- The sub heading must display "Your Reviews"
- A dropdown accordion containing the users reviews must display below.
- Each accordion section header must contain a down arrow icon, the make, model and year.
- When each header is selected a dropdown must appear below containing: Make, Model, Year, Review
and rating.
- "EDIT" and "DELETE" buttons must also display on the accordion header.
- When there are no reviews in the database, in the place of the accordion a message must appear
 "NO REVIEWS FOUND".
- Below the accordion a central button "ADD NEW REVIEW" with a plus icon.

<details>
<summary>Profile Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/profile-screenshot.png)
</p>
</details>

Functionality:

- When "EDIT" is selected on the review accordion users must be redirected to prefilled 
edit page.
- When "DELETE" is selected, the delete popup modal must appear.
- If "DELETE" is again selected on the modal, the corresponding review must be permanently deleted from the accordion 
and the database. 
- If "CANCEL" is selected, it must revert back to the all reviews page.
- If "ADD NEW REVIEW" is selected users must be directed to the new review page.

## New Review

Display:

- Must retain the basic layout and remain responsive on all screen sizes.
- Must display the heading "NEW REVIEW"
- A card panel from must display with a Make dropdown field. Followed by text input fields for:
Model, Year with "YYYY" placeholder, Review and rating 0-5.
- A central "SAVE" button with save icon.

<details>
<summary>New Review Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/new-review-screenshot.png)
</p>
</details>

Functionality:

- The Make dropdown field must have the placeholder "Choose a make" and must contain all the makes
held in the database.
- When a make is selected it must appear in the dropdown and a green line must appear below.
- The model text input field must only allow 20 characters to be entered.
- The model text input field must underline in green if less than 20 characters are entered.
- The year input field must underline in red if anything other than 4 numbers is entered.
- The year input field must underline in green if 4 numbers are entered.
- The review input field must only allow 200 characters to be entered.
- The review input field must underline in red if less than 5 characters are entered.
- The rating input field must underline in red if anything other than 1 number 0 - 5 is entered.
- When the "SAVE" button is selected - if any of the input fields are underlined in red, a warning must 
flash with "Please match the format requested".
- If any field is selected and left unfilled, when selecting elsewhere that field must underline in red. 
- When the save button is selected - if any of the fields are empty, a warning must flash with 
" Please fill in this field". Or if the drop down is empty "Please select an item in the list"
- If all of the fields are underlined in green, and the "SAVE" button is selected, the data from each field 
must be saved to the database and the user must be re-directed to the home page with 
a message: "REVIEW SUCCESSFULLY ADDED".
- The review data must now appear in the users profile accordion and on the homepage accordion.
![Image](static/assets/images/readme-images/success-review-screenshot.png)


## Edit Review

Display:

- Must retain the basic layout and remain responsive on all screen sizes.
- Must display the heading "EDIT REVIEW"
- A pre-filled card panel from must display containing the data from the review the user wished to edit.
- The card panel must contain Make (dropdown field). Followed by text input fields for:
Model, Year with "YYYY" placeholder, Review and rating 0-5.
- A central "SAVE" button with save icon and "CANCEL" button with cancel icon.

<details>
<summary>New Review Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/edit-review-screenshot.png)
</p>
</details>

Functionality:

- The form must be pre filled with the data from the review the user wished to edit.
- The Make dropdown field must have the placeholder "Choose a make" and must contain all the makes
held in the database.
- When a make is selected it must appear in the dropdown and a green line must appear below.
- The model text input field must only allow 20 characters to be entered.
- The model text input field must underline in green if less than 20 characters are entered.
- The year input field must underline in red if anything other than 4 numbers is entered.
- The year input field must underline in green if 4 numbers are entered.
- The review input field must only allow 200 characters to be entered.
- The review input field must underline in red if less than 5 characters are entered.
- The rating input field must underline in red if anything other than 1 number 0 - 5 is entered.
- When the "SAVE" button is selected - if any of the input fields are underlined in red, a warning must 
flash with "Please match the format requested".
- If any field is selected and left empty, when selecting elsewhere that field must underline in red. 
- When the save button is selected - if any of the fields are empty, a warning must flash with 
" Please fill in this field". Or if the drop down is empty "Please select an item in the list"
- If all of the fields are underlined in green, and the "SAVE" button is selected, the data from each 
field must be saved to the database and the user must re-direct to the users profile page with a 
message: "REVIEW SUCCESSFULLY EDITED".
- The review data must now appear in the users profile accordion and on the homepage accordion.
![Image](static/assets/images/readme-images/review-success-edit-screenshot.png)
- If the "CANCEL" button is selected the user should be re-directed to the profile page. 


