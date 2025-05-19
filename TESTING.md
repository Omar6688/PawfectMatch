# ✅ TESTING.md — PawfectMatch

This document outlines all testing activities carried out on the **PawfectMatch** Django project, submitted for the Code Institute Full Stack Frameworks with Django Milestone (Project 4).

Testing covers:

- Manual UX and functional testing  
- HTML and CSS validation  
- Python and JS linting  
- Responsiveness checks across devices  
- Accessibility testing  
- Lighthouse performance audits  
- Bug fixes and known issues

---

## 📑 Table of Contents

- [Manual Testing](#manual-testing)
- [User Stories & Features Tested](#user-stories--features-tested)
- [Form & Model Validation](#form--model-validation)
- [Responsive Design Testing](#responsive-design-testing)
- [Browser Compatibility](#browser-compatibility)
- [Validator Testing](#validator-testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Python Linting (flake8)](#python-linting-flake8)
- [Accessibility Testing](#accessibility-testing)
- [Performance Testing](#performance-testing)
- [Bugs Fixed](#bugs-fixed)
- [Known Issues](#known-issues)


## 🧪 Manual Testing

All key pages and user interactions were manually tested across multiple devices and browsers.

Each test was conducted using the live Heroku deployment and local development server. Logged-in and anonymous states were checked, and feature flows were verified from start to finish.

---

### 🔍 Key Pages Manually Tested

| Page                         | Tests Performed                                                                 |
|------------------------------|----------------------------------------------------------------------------------|
| **Homepage**                 | Loads properly, shows welcome message and adoptable pets                        |
| **Sign Up / Login / Logout**| Allauth pages functional, redirects work, flash messages show correctly         |
| **Services List**            | Services display correctly with price, description, and layout                  |
| **Booking Form**             | Form submits successfully, Stripe redirect works, confirmation displayed        |
| **Booking Success**          | Confirmation messages shown (session-based), booking saved                      |
| **Support Page**             | Form submission stores message and redirects                                    |
| **Adoptable Pets List**      | All pets displayed with name, breed, age, image (or fallback image)             |
| **Adoptable Detail Page**    | Pet info visible, buttons show based on user type (Edit/Delete/Adopt)          |
| **Adoption Interest Form**   | Submits contact info (if logged in), redirects with success message             |
| **User Profile**             | Displays username and user-specific bookings if applicable                      |
| **Admin Panel**              | Superuser access works, all models are editable                                |
| **Custom Error Pages**       | 403, 404, and 500 pages display styled error messages with proper status codes  |

Each flow was tested both as a superuser and a normal user to ensure proper access control.

---

Additional screenshots will be included below after full testing is documented.



## ✅ User Stories & Features Tested

Each user story from the README was manually tested and verified. Below is a summary of the core features and whether each passed:

| User Story Description                                         | Tested As       | Status |
|----------------------------------------------------------------|------------------|--------|
| View available adoptable pets                                  | Anonymous User   | ✅     |
| View pet details                                                | Anonymous User   | ✅     |
| Adopt a pet (redirects to login if not logged in)              | Anonymous User   | ✅     |
| Express interest in a pet                                      | Logged-In User   | ✅     |
| Add, edit, or delete pets                                      | Admin / Staff    | ✅     |
| View list of available services                                | Any User         | ✅     |
| Book a pet service with Stripe                                 | Logged-In User   | ✅     |
| View booking confirmation                                      | Logged-In User   | ✅     |
| View my profile and bookings                                   | Logged-In User   | ✅     |
| Register new account                                           | New User         | ✅     |
| Login and logout flow                                          | Any User         | ✅     |
| Email confirmation                                             | New User         | ✅     |
| View support options (volunteer, donate, share)                | Any User         | ✅     |
| Submit support inquiry                                         | Any User         | ✅     |
| View flash messages (booking success, login/logout alerts)     | Any User         | ✅     |
| Mobile responsiveness for all pages                            | Any User         | ✅     |
| 403 / 404 / 500 custom error pages                             | Any User         | ✅     |

All acceptance criteria were fulfilled for each story. Screenshots will be added later for key flows.



## ✅ Form & Model Validation

All forms in the project use Django’s `ModelForm` and built-in validation system. Each form was tested with valid and invalid inputs to ensure that validation errors are shown appropriately and that valid submissions are saved correctly.

---

### 🧾 Booking Form

- ✅ Required fields: name, email, service, date
- ❌ Invalid data (e.g., blank name or invalid email) triggers error messages
- ✅ CSRF token present
- ✅ Stripe payment integration redirects to payment page after form submission

---

### 📩 Adoption Interest Form

- ✅ Required fields: name, email, message
- ✅ Optional field: phone
- ❌ Invalid inputs are blocked with field-specific error messages
- ✅ Form is only accessible to logged-in users (redirects to login if not)

---

### 📬 Support Form

- ✅ Required: name, email, message
- ✅ Validated automatically by Django
- ✅ Flash message shown after successful submission

---

### 🔐 Allauth Registration/Login

- ✅ Signup form validates email format and password match
- ✅ Flash messages shown after login, logout, and signup
- ✅ Redirects to homepage or profile upon login

---

All forms are protected by CSRF tokens, and all submissions are stored securely via Django models. Invalid submissions are never saved.



## 📱 Responsive Design Testing

The entire site layout was tested across desktop, tablet, and mobile screens to ensure content remains readable and accessible on all devices.

Responsiveness was implemented using Bootstrap 5’s grid system and utility classes.

---

### ✅ Devices Tested

| Device Type      | Model/OS                          | Result  |
|------------------|------------------------------------|---------|
| Desktop          | macOS (Chrome, Safari)             | ✅ Pass |
| Laptop           | macOS (Firefox, Chrome)            | ✅ Pass |
| Tablet           | iPad 10.2" (Safari, Chrome)        | ✅ Pass |
| Mobile Phone     | iPhone 13, iPhone SE (Safari)      | ✅ Pass |
| Mobile Emulator  | Chrome DevTools (iOS + Android)    | ✅ Pass |

---

### ✅ Layout Checks

- ✅ Navbar collapses into a hamburger menu on mobile
- ✅ Cards and forms resize correctly without overflow
- ✅ Buttons and text remain clickable/readable on all sizes
- ✅ Pet listings, service list, and forms adjust to viewport width
- ✅ Footer sticks to the bottom when content is short

Screenshots of mobile and tablet views will be added below.



## ♿ Accessibility & Performance Testing

### ✅ Accessibility (Lighthouse)

Using Google Chrome DevTools > Lighthouse, accessibility audits were performed on the home page, adoptable pets page, and booking page.

| Page                | Accessibility Score | Notes                                     |
|---------------------|---------------------|-------------------------------------------|
| Home                | ✅ 100%             | Good heading structure, contrast OK       |
| Adoptable Pets      | ✅ 100%             | Alt text on all pet images                |
| Booking Form        | ✅ 100%             | Labels match inputs, keyboard-navigable  |

All pages include:

- ✅ Semantic HTML (e.g., `<header>`, `<main>`, `<footer>`)
- ✅ Proper color contrast
- ✅ Keyboard navigation support
- ✅ Alt text on all images
- ✅ Form fields with labels

---

### ⚡ Performance (Lighthouse)

Performance audits using Lighthouse also showed solid results:

| Page                | Performance Score | Notes                             |
|---------------------|------------------|-----------------------------------|
| Home                | ✅ 96–100%       | Fast load with minimal blocking   |
| Adoptable Pets      | ✅ 95–98%        | Lazy loading optimized images     |
| Booking Form        | ✅ 95–99%        | Lightweight form with fast render |

Static files (CSS/JS) are served efficiently via **WhiteNoise** on Heroku.

---

### 🧪 Tools Used

- ✅ Chrome Lighthouse
- ✅ axe DevTools (accessibility extension)
- ✅ Manual keyboard-only navigation
- ✅ Screen reader test (VoiceOver on macOS)

Screenshots will be added below.



## ✅ Validation Testing

Validation tools were used to check for errors, warnings, and best practice compliance across the project.

---

### ✅ HTML Validation (W3C)

The homepage (`base.html`) was tested using the [W3C Markup Validator](https://validator.w3.org/).

✅ **Result**: No errors found after correcting misplaced `<body>` and `<script>` tags.

![HTML Validation Result for Homepage](documentation/testing/html-validator.png)

---

### CSS Validation

The deployed CSS file was tested using the W3C CSS Validation Service:  
[https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

![CSS Validation Screenshot](documentation/testing/css-validation.png)

- ✅ No errors or warnings were found in the CSS file.
- The code passes validation and meets modern web standards for styling.


### Python Code Validation - flake8 ✅

The project’s Python code was validated using the `flake8` linter to check for syntax and style issues.

**Results:**
- ✅ No critical errors were found.
- ⚠️ A few minor warnings were reported, including:
  - `E501`: Line too long (exceeding 79 characters).
  - `F401`: Unused imports (mostly in test or placeholder code).
  - `E302`, `E305`: Expected 2 blank lines before/after function or class definitions.

These are all considered minor stylistic issues and **do not impact functionality or runtime behavior**.

**Conclusion:**
The Python code is clean and functional. Minor flake8 warnings were reviewed and documented, and may be addressed in future refactoring for enhanced code readability.


---

### ⚙️ Deployment Checks

✅ Heroku deployment was tested with:

- `DEBUG = False` in production
- `ALLOWED_HOSTS` set correctly
- Environment variables handled securely via `env.py` and `os.getenv()`
- `collectstatic` completed with no errors
- AWS S3 correctly serves media files
- Stripe and email confirmation work on production

Screenshots of validator results will be added below.



## 🐞 Bug Fixes & Known Issues

---

### ✅ Fixed Bugs During Development

| Issue | Fix |
|-------|-----|
| AWS S3 images not displaying | Reconfigured `USE_AWS`, ensured `DEFAULT_FILE_STORAGE` and credentials were set properly |
| Stripe session not redirecting | Adjusted `success_url` and `cancel_url` to use `request.build_absolute_uri()` |
| Booking edit errors | Added missing `redirect` import in `bookings/views.py` |
| Media files broken in Heroku | Ran `collectstatic` and confirmed correct S3 bucket setup |
| Profile page crash for normal users | Conditional logic added to only show staff edit/delete buttons |
| Delete button not confirming | Added JavaScript confirmation to `script.js` |
| Pet image field migration error | Provided default during migration or manually set values |

---

### 🚧 Known Issues (Documented for Transparency)

| Issue | Notes |
|-------|-------|
| Email confirmation takes a few seconds | Expected delay with Gmail SMTP |
| No pagination for pet listings | All pets shown in a single scrollable view |
| No image compression | Large pet images may slightly slow load time (planned TinyPNG integration) |
| Email confirmation warning | Django 5.2 emits: `ACCOUNT_LOGIN_METHODS conflicts with ACCOUNT_SIGNUP_FIELDS` (non-critical) |
| Django development warning | "Do not use this server in production" shown during local testing (expected) |

These issues are not critical and do not affect functionality.

---

