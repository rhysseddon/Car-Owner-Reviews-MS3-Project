# Testing

## Contents
- [Favicon](#Favicon)
- [Font](#Font)
 

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

## Home Page Test Case

- The full width hero image must display below the navbar.

<details>
<summary>Background Image (Click for image)</summary>
<p align="center">

![Image](static/assets/images/cars-hero.jpg)
</p>
</details>