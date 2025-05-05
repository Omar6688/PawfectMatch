# PawfectMatch
🐾 **PawfectMatch**  
PawfectMatch is a pet adoption and service booking platform built with Django. It allows users to browse adoptable pets, book professional pet services, and support local animal shelters. The platform combines clean UX, secure user accounts, and a modular backend to serve multiple real-world needs in one responsive web app.

---

📖 **Project Story**  
This application was developed as part of the Code Institute Level 5 Diploma in Web Application Development, fulfilling the criteria for the **Full Stack Frameworks with Django** Milestone Project (Project 4).

PawfectMatch was inspired by the growing demand for unified platforms that help animal lovers adopt responsibly and access trusted services. The app includes multi-app Django architecture, Stripe-ready integration, and secure user authentication. It is fully responsive and works seamlessly across desktop, tablet, and mobile.

🔗 The live site will be available here: **[Live Site - PawfectMatch](#)**

🖼️ *Wireframes will be added below once finalized.*


---

## 📑 Table of Contents

- [User Experience Design](#user-experience-design)
  - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
  - [The Scope Plane](#the-scope-plane)
    - [Features](#features)
    - [Future Features](#future-features)
  - [The Structure Plane](#the-structure-plane)
    - [Database Models and Logic](#database-models-and-logic)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Security](#security)
  - [The Surface Plane](#the-surface-plane)
    - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [Technologies Used](#technologies-used)
- [Agile Planning](#agile-planning)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)



## 💡 User Experience Design

### 🧭 The Strategy Plane

#### 🎯 Site Goals

The primary goal of PawfectMatch is to provide a trusted, user-friendly platform where:

- 🐶 Pet seekers can browse adoptable animals with photos and descriptions.
- 🐾 Registered users can book pet-related services like grooming, training, and veterinary appointments.
- 💖 Supporters can contribute through donations or volunteer signups.
- 🧑‍💻 Admins and staff can manage pet listings, services, and bookings via a secure admin dashboard.

The app supports the goals of both users and the platform owner (the shelter/service provider), enabling:

- Efficient connection between users and pet care providers.
- Centralized management of bookings, pets, and services.
- A potential revenue stream via Stripe payment integration.

#### 🧑‍🤝‍🧑 Target Audience

- Individuals or families looking to adopt a pet.
- Pet owners searching for trusted services like grooming or training.
- Animal lovers who want to support local shelters via volunteering or donations.
- Admins managing shelter operations and service providers.

The platform is optimized for desktop, tablet, and mobile users, ensuring accessibility on all devices.



#### 📋 User Stories

Below are the primary user stories that guided the development of PawfectMatch. Each includes clear Acceptance Criteria to define completion.

---

**👤 Story 1: Site Visitor – View Available Pets**  
*As a potential adopter,*  
I want to browse available pets with their details  
So that I can find a pet that suits my lifestyle.

✅ **Acceptance Criteria**:  
- I can view a list of pets with images, breed, and description.  
- I can click to view more details about each pet.

---

**👤 Story 2: Site Visitor – Learn About Pet Services**  
*As a pet owner,*  
I want to view pet services offered  
So that I can decide which service I need.

✅ **Acceptance Criteria**:  
- I can see a list of services with titles and descriptions.  
- I can learn what each service offers before booking.

---

**👤 Story 3: New User – Register an Account**  
*As a new user,*  
I want to create an account  
So that I can book services or apply to adopt a pet.

✅ **Acceptance Criteria**:  
- I can register with a username, email, and password.  
- I am redirected and logged in after signing up.

---

**👤 Story 4: Registered User – Book a Pet Service**  
*As a logged-in user,*  
I want to book a grooming or veterinary service  
So that I can schedule care for my pet.

✅ **Acceptance Criteria**:  
- I can select a service, choose a date, and leave a note.  
- I receive confirmation of my booking.

---

**👤 Story 5: Supporter – Learn How to Help**  
*As a community member,*  
I want to see how I can support shelters  
So that I can volunteer or donate.

✅ **Acceptance Criteria**:  
- I can access a Support page from the navigation.  
- I see information on donations and volunteering.

---

**👤 Story 6: Admin – Manage Pets and Bookings**  
*As an admin or staff member,*  
I want to manage pets and bookings through the admin panel  
So that I can keep listings and appointments updated.

✅ **Acceptance Criteria**:  
- I can log into the Django admin.  
- I can add/edit/delete pets, services, and bookings.


---

**👤 Story 7: Logged-in User – View My Bookings**  
*As a logged-in user,*  
I want to see all my upcoming bookings  
So that I can manage or cancel them if needed.

✅ **Acceptance Criteria**:  
- I can see a list of all bookings I’ve made.  
- Each booking includes the service name and date.

---

**👤 Story 8: Logged-in User – Cancel a Booking**  
*As a user with a booking,*  
I want to cancel it before the scheduled time  
So that I avoid charges or rescheduling issues.

✅ **Acceptance Criteria**:  
- I see a “Cancel” option next to my future bookings.  
- Cancelled bookings are removed or marked clearly.

---

**👤 Story 9: Logged-in User – Edit Account Details**  
*As a registered user,*  
I want to update my profile details  
So that I can keep my information current.

✅ **Acceptance Criteria**:  
- I can edit my email or password.  
- Changes take effect after saving.

---

**👤 Story 10: Anonymous Visitor – Understand Site Purpose**  
*As a new visitor,*  
I want to understand what the site offers  
So that I know whether to sign up.

✅ **Acceptance Criteria**:  
- I see clear messaging on the homepage.  
- I’m invited to adopt, book services, or support shelters.

---

**👤 Story 11: Logged-in User – Adopt a Pet (Placeholder for future)**  
*As a registered user,*  
I want to apply to adopt a pet  
So that I can start the process of giving it a home.

✅ **Acceptance Criteria**:  
- I can click an “Apply” button on the pet detail page.  
- A form or message indicates that the request is received.

---

**👤 Story 12: Admin – Manage Support Inquiries**  
*As a site admin,*  
I want to manage support form submissions  
So that I can respond to donation or volunteer interest.

✅ **Acceptance Criteria**:  
- I see support submissions in the admin.  
- I can mark them as resolved or contacted.

---

**👤 Story 13: Visitor – Mobile-friendly Navigation**  
*As a user on mobile,*  
I want to use a responsive menu  
So that I can navigate the site easily.

✅ **Acceptance Criteria**:  
- Navbar collapses into a hamburger menu.  
- All links are accessible on mobile devices.

---

**👤 Story 14: Registered User – Get Feedback After Booking**  
*As a user who books a service,*  
I want to get a confirmation or error message  
So that I know whether my booking succeeded.

✅ **Acceptance Criteria**:  
- I see a success or failure message after submitting a booking.  
- Errors (like missing fields) are clearly highlighted.

---

**👤 Story 15: Developer – Write a Detailed README**  
*As a developer submitting this project,*  
I want to create a professional, informative README  
So that assessors and other developers understand the app.

✅ **Acceptance Criteria**:  
- The README explains the purpose, features, and technologies.  
- All key sections (UX, Features, ERD, Deployment, Testing) are included.



## 🧭 The Scope Plane

### ✅ Features Implemented

The following features are included in the initial version of the **PawfectMatch** app:

#### 🐾 1. Home Page
- Introduces the site's purpose: pet adoption and pet services.
- Highlights core areas: Adopt, Services, and Support.
- Displays available pets dynamically with images and details.

#### 👤 2. User Authentication
- Full user registration, login, and logout using **django-allauth**.
- Redirects users after login and logout.
- Sign-up form includes email and password confirmation.

#### 📄 3. Pet Listings
- Pets are shown with name, age, breed, description, and image.
- Clicking a pet takes users to a detail page.

#### 🔍 4. Pet Detail Page
- Shows full details of an individual pet.
- Includes a button to apply for adoption (to be implemented).

#### 🛠️ 5. Pet Services App
- Users can browse available pet services (e.g., grooming, training).
- Services are listed with name, description, and price.

#### 📅 6. Booking Functionality
- Logged-in users can book a service by selecting a date and writing a message.
- CSRF protection and validation are included.
- Bookings saved to the database and displayed in the admin panel.

#### 💬 7. Support Page
- Allows users to send inquiries or support requests.
- Message is stored and viewable by admins via Django admin.

#### 🌐 8. Navigation Bar
- Contains links to Login, Logout, Sign Up, Services, and Support.
- Navigation adjusts based on authentication state.
- Fully responsive with Bootstrap.

#### 🔐 9. Admin Panel
- Admin can manage pets, services, bookings, and support inquiries.
- Superuser created for administrative tasks.

#### 📱 10. Responsive Design
- Uses Bootstrap 5 for mobile, tablet, and desktop responsiveness.
- Layout adapts to different devices gracefully.

---

### 🚧 Features Left to Implement

These features are out of scope for this version but planned for future development:

- 📝 Adoption form submission and approval workflow.
- 📊 User dashboard showing bookings, adoption status, and profile details.
- 🔍 Search/filter for pets and services.
- 💳 Stripe payment integration for paid bookings or donations.
- 🗓️ Calendar view for appointments.
- 📈 Admin dashboard with charts for analytics.
- 💌 Email notifications for bookings and support submissions.
- 🌙 Dark mode UI toggle.
- 🖼️ Custom pet profiles with galleries and reviews.


## 🏗️ The Structure Plane

### 🔄 Application Structure

The **PawfectMatch** project is built with Django and follows a modular app structure:

- `core`: Handles homepage, navigation, and shared templates (like `base.html`).
- `services`: Displays pet-related services.
- `bookings`: Manages service bookings (via forms and models).
- `support`: Allows users to send support messages.
- `templates/`: Contains app-specific HTML templates, all extending `base.html`.
- `static/`: Will hold custom CSS, JavaScript, and images.
- `media/`: Will be used for user-uploaded pet images (in future updates).

All Django apps are logically separated for clarity and reuse.

---

### 🧩 URL Structure

The `urls.py` files are organized to include:

- `accounts/`: For authentication using django-allauth.
- `/`: The core homepage and dynamic pet listing.
- `/services/`: Lists available pet services.
- `/bookings/`: Booking form for logged-in users.
- `/support/`: Support/contact page.
- `admin/`: Django admin panel access for superusers.

---

### 🖥️ Views & Templates

- Each app contains its own views and templates.
- All templates extend `base.html`, which includes the navigation bar and Bootstrap.
- Views are function-based for clarity and simplicity.
- Templates use Django templating language to dynamically render content like pets and services.

---

### 🔐 Authentication & Access Control

- Authentication is handled by **django-allauth**.
- Navigation adjusts based on whether the user is logged in.
- Certain views (like bookings) are protected and require login.

---

### 📊 Data Flow

- Pet data is passed from the `core` views into the homepage and pet detail pages.
- Booking data is submitted via a secure form and saved to the database.
- Admins can access all data via the Django admin panel.

---

Let me know once this is added and committed — then we’ll move to the **Skeleton Plane**, including your wireframes, database (ERD), and security practices. Ready?

