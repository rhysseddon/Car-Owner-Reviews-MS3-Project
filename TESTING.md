# Testing

## Contents
- [Favicon](#Favicon)
- [Font](#Font)
- [Navbar](#Navbar)
- [Footer](#Footer)
- [Footer](#Footer)
- [Home Page](#Home-Page)
 

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

Functionality on both top nav and side nav links:  

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
![Image](static/assets/images/readme-images/welcome-search-mobile-screenshot.png)

- Welcome section should display the heading "WELCOME" with a paragraph of information 
and a register and login button below.

<details>
<summary>Welcome Sectiom Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/welcome-search-mobile-screenshot.png)
</p>
</details>

- Search bar should display a magnifiying glass icon, a text input area with the
 placeholder "Search make or model" and a "search" and "reset" button.
 ![Image](static/assets/images/readme-images/search-screenshot.png)

 - All reviews section should display a central title "ALL REVIEWS".
 - A dropdown accordion containing the reviews should display below.
 - Each accordion section should contain a down arrow icon, the make, model, year and creator of the 
 review
 - For admin users "edit" button and "delete" buttons should also display on the accordion. 

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
- If the reset button is selected the page should revert back to all reviews (if any) displaying.
- When "Edit" is selected on the review accordion admin users should be redirected to prefilled 
edit page.
- When "Delete" is selected, the delete popup modal should appear.
- If delete is again selected on the modal, the coresponding review will be permanently deleted from the accordion 
and the database.
- If cancel is selected, it should revert back to the all reviews page.

 <details>
<summary>Delete Modal Screenshot (Click for image)</summary>
<p align="center">

![Image](static/assets/images/readme-images/delete-modal-screenshot.png)
</p>
</details>