# PawfectMatch

🐾 **PawfectMatch**  
PawfectMatch is a pet adoption and service booking platform built with Django. It allows users to browse adoptable pets, book professional pet services, and support local animal shelters. The platform combines clean UX, secure user accounts, and a modular backend to serve multiple real-world needs in one responsive web app.

---

📖 **Project Story**  
This application was developed as part of the Code Institute Level 5 Diploma in Web Application Development, fulfilling the criteria for the **Full Stack Frameworks with Django** Milestone Project (Project 4).

PawfectMatch was inspired by the growing demand for unified platforms that help animal lovers adopt responsibly and access trusted services. The app includes multi-app Django architecture, Stripe-ready integration, and secure user authentication. It is fully responsive and works seamlessly across desktop, tablet, and mobile.

🔗 The live site will be available here: **[Live Site - PawfectMatch](#)**

🖼️ _Wireframes will be added below once finalized._

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
_As a potential adopter,_  
I want to browse available pets with their details  
So that I can find a pet that suits my lifestyle.

✅ **Acceptance Criteria**:

- I can view a list of pets with images, breed, and description.
- I can click to view more details about each pet.

---

**👤 Story 2: Site Visitor – Learn About Pet Services**  
_As a pet owner,_  
I want to view pet services offered  
So that I can decide which service I need.

✅ **Acceptance Criteria**:

- I can see a list of services with titles and descriptions.
- I can learn what each service offers before booking.

---

**👤 Story 3: New User – Register an Account**  
_As a new user,_  
I want to create an account  
So that I can book services or apply to adopt a pet.

✅ **Acceptance Criteria**:

- I can register with a username, email, and password.
- I am redirected and logged in after signing up.

---

**👤 Story 4: Registered User – Book a Pet Service**  
_As a logged-in user,_  
I want to book a grooming or veterinary service  
So that I can schedule care for my pet.

✅ **Acceptance Criteria**:

- I can select a service, choose a date, and leave a note.
- I receive confirmation of my booking.

---

**👤 Story 5: Supporter – Learn How to Help**  
_As a community member,_  
I want to see how I can support shelters  
So that I can volunteer or donate.

✅ **Acceptance Criteria**:

- I can access a Support page from the navigation.
- I see information on donations and volunteering.

---

**👤 Story 6: Admin – Manage Pets and Bookings**  
_As an admin or staff member,_  
I want to manage pets and bookings through the admin panel  
So that I can keep listings and appointments updated.

✅ **Acceptance Criteria**:

- I can log into the Django admin.
- I can add/edit/delete pets, services, and bookings.

---

**👤 Story 7: Logged-in User – View My Bookings**  
_As a logged-in user,_  
I want to see all my upcoming bookings  
So that I can manage or cancel them if needed.

✅ **Acceptance Criteria**:

- I can see a list of all bookings I’ve made.
- Each booking includes the service name and date.

---

**👤 Story 8: Logged-in User – Cancel a Booking**  
_As a user with a booking,_  
I want to cancel it before the scheduled time  
So that I avoid charges or rescheduling issues.

✅ **Acceptance Criteria**:

- I see a “Cancel” option next to my future bookings.
- Cancelled bookings are removed or marked clearly.

---

**👤 Story 9: Logged-in User – Edit Account Details**  
_As a registered user,_  
I want to update my profile details  
So that I can keep my information current.

✅ **Acceptance Criteria**:

- I can edit my email or password.
- Changes take effect after saving.

---

**👤 Story 10: Anonymous Visitor – Understand Site Purpose**  
_As a new visitor,_  
I want to understand what the site offers  
So that I know whether to sign up.

✅ **Acceptance Criteria**:

- I see clear messaging on the homepage.
- I’m invited to adopt, book services, or support shelters.

---

**👤 Story 11: Logged-in User – Adopt a Pet (Placeholder for future)**  
_As a registered user,_  
I want to apply to adopt a pet  
So that I can start the process of giving it a home.

✅ **Acceptance Criteria**:

- I can click an “Apply” button on the pet detail page.
- A form or message indicates that the request is received.

---

**👤 Story 12: Admin – Manage Support Inquiries**  
_As a site admin,_  
I want to manage support form submissions  
So that I can respond to donation or volunteer interest.

✅ **Acceptance Criteria**:

- I see support submissions in the admin.
- I can mark them as resolved or contacted.

---

**👤 Story 13: Visitor – Mobile-friendly Navigation**  
_As a user on mobile,_  
I want to use a responsive menu  
So that I can navigate the site easily.

✅ **Acceptance Criteria**:

- Navbar collapses into a hamburger menu.
- All links are accessible on mobile devices.

---

**👤 Story 14: Registered User – Get Feedback After Booking**  
_As a user who books a service,_  
I want to get a confirmation or error message  
So that I know whether my booking succeeded.

✅ **Acceptance Criteria**:

- I see a success or failure message after submitting a booking.
- Errors (like missing fields) are clearly highlighted.

---

**👤 Story 15: Developer – Write a Detailed README**  
_As a developer submitting this project,_  
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

## 🦴 The Skeleton Plane

### 🔹 Wireframes

Before development began, wireframes were created to plan the layout and user journey across the most important pages. These low-fidelity Balsamiq-style mockups helped map out responsive layouts, user interactions, and form placements across desktop, tablet, and mobile devices.

The wireframes ensured that the visual hierarchy and user flow aligned with the core goals of the application: promoting pet adoption, simplifying service bookings, and supporting shelter operations.

Each wireframe was used to guide the layout decisions during development and matches the final responsive design.

📸 **Final Wireframes**

| Page                                           | Preview                                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------ |
| **Homepage** (Desktop, Tablet, Mobile)         | ![Homepage Wireframe](documentation/wireframes/wireframe-home.png)             |
| **Adoptable Pets List** (Desktop)              | ![Adoptable Pets Wireframe](documentation/wireframes/wireframe-adopt-list.png) |
| **Pet Detail Page** (Desktop, Tablet, Mobile)  | ![Pet Detail Wireframe](documentation/wireframes/wireframe-pet-detail.png)     |
| **Booking Form** (Desktop)                     | ![Booking Form Wireframe](documentation/wireframes/wireframe-booking-form.png) |
| **User Profile Page** (Desktop)                | ![Profile Page Wireframe](documentation/wireframes/wireframe-profile.png)      |

> _Note: These wireframes reflect the actual layout and responsive behavior of the live project and were created using Balsamiq-style mockups for visual clarity and planning._

---

### 🗃️ Database Design (ERD)

### 🗃️ Database Design (ERD)

The following **Entity Relationship Diagram (ERD)** outlines the core data models and relationships used in the PawfectMatch Django application. Each model reflects a distinct part of the platform's functionality — such as pet adoption, service bookings, user messages, and authentication.

The diagram was created using [dbdiagram.io](https://dbdiagram.io) and is based on the actual Django models implemented in the project.

📸 **ERD Diagram Preview**

![PawfectMatch ERD](documentation/erd/erd-diagram.png)

---

#### 📊 Model Overview

| Model              | Field        | Type             | Notes                                      |
|-------------------|--------------|------------------|---------------------------------------------|
| **AdoptablePet**   | name         | CharField        | Name of the adoptable pet                   |
|                   | breed        | CharField        | Breed of the pet                            |
|                   | age          | IntegerField     | Age in years                                |
|                   | description  | TextField        | Short bio or personality description        |
|                   | image        | ImageField       | Photo uploaded via admin                    |
|                   | created_at   | DateTimeField    | Auto-added when pet is listed               |
| **AdoptionInterest** | pet        | FK → AdoptablePet| Links interest to a pet                     |
|                   | name         | CharField        | Name of interested adopter                  |
|                   | email        | EmailField       | Contact email                               |
|                   | phone        | CharField        | Optional phone number                       |
|                   | message      | TextField        | Message expressing adoption interest        |
|                   | created_at   | DateTimeField    | Timestamp of the request                    |
| **Service**        | name         | CharField        | Name of the pet service (e.g., grooming)    |
|                   | description  | TextField        | Description of service                      |
|                   | price        | DecimalField     | Price of the service in USD                 |
|                   | image        | ImageField       | Optional visual for service                 |
| **Booking**        | name         | CharField        | Name of user submitting booking             |
|                   | email        | EmailField       | Email of user                               |
|                   | service      | FK → Service     | Selected service                            |
|                   | date         | DateField        | Booking date                                |
|                   | message      | TextField        | Optional user message                       |
|                   | paid         | BooleanField     | Stripe payment status                       |
|                   | created_at   | DateTimeField    | Auto-added timestamp                        |
| **SupportMessage** | name         | CharField        | Sender's name                               |
|                   | email        | EmailField       | Sender's email                              |
|                   | message      | TextField        | The message content                         |
|                   | created_at   | DateTimeField    | Auto timestamp                              |

---

All models are linked logically via **ForeignKey relationships**, and validation is handled at both the model and form levels. Sensitive fields like emails and payment status are properly stored and protected.

---

### 🔐 Security

The following security best practices were implemented to protect user data and maintain integrity of the application:

- **Authentication & Authorization:** Implemented via `django-allauth` to manage user accounts.
- **Environment Variables:** All sensitive settings (e.g., `SECRET_KEY`, database credentials) are hidden using `.env` and `os.environ`.
- **Database Access:** Models such as Bookings are linked to individual users to ensure private access.
- **Custom Error Pages:** Friendly custom templates for 403, 404, and 500 errors to guide the user if issues occur.
- **CSRF Protection:** Enabled by default with Django middleware on all forms.
- **Input Validation:** Forms use Django’s built-in validation and widgets (e.g., date picker) to ensure correct inputs.

## 🎨 The Surface Plane

### 🖥️ Design Overview

PawfectMatch is designed to be warm, welcoming, and user-friendly — reflecting the heart of pet adoption and support. The site uses generous white space, soft contrast, clear buttons, and mobile-first responsiveness to ensure an enjoyable experience on all screen sizes.

Design priorities included:

- A clean **centered layout** with balanced spacing
- Clear, bold **calls to action** (like "View Available Pets")
- Intuitive navigation across **Home**, **Services**, and **Support**
- Consistent use of **Bootstrap 5.3.3** for layout and styling

---

### 🌈 Colour Scheme

The color palette of **PawfectMatch** is warm, accessible, and friendly — reflecting the welcoming tone of a pet adoption and care platform. Colors were selected to provide strong contrast, intuitive call-to-action highlights, and mobile readability.

| Element            | Color Code   | Purpose                                             |
|--------------------|--------------|-----------------------------------------------------|
| Background         | `#f8f9fa`    | Light gray used for overall background and sections |
| Navbar Background  | `#ffffff`    | Clean white for top navigation and base layout      |
| Primary Buttons    | `#198754`    | Bootstrap green (`btn-success`) used for CTAs       |
| Alert Highlights   | `#0d6efd`    | Bootstrap blue for flash messages and labels        |
| Danger Buttons     | `#dc3545`    | Bootstrap red used for delete actions               |
| Text               | `#212529`    | Very dark gray (almost black) for strong readability|
| Hover & Links      | `#0a58ca`    | Medium blue used for interactive states             |

> 🎨 All colors were chosen with accessibility in mind, ensuring proper contrast on both light and dark screens. Button colors were selected from the Bootstrap 5 utility palette for consistency and clarity.


---

### 📝 Typography

The site uses the default **Bootstrap typography system**, which ensures clean and responsive type sizing across all screen sizes:

- Font Family: **System font stack** for maximum compatibility
- Heading Sizes: Scalable based on viewport width (`h1` to `h5`)
- Body Text: Readable at `1rem` base size
- Alignment: Centered or left-aligned based on context

Readability was prioritized, especially for mobile users viewing pet details and service forms.

---

### 🖼️ Imagery

Images are central to the project’s emotional tone. Photos of pets are displayed in **cards** with soft shadows, rounded corners, and alt text for accessibility.

- 🐶 **Pet Images**: Shown on the homepage and pet detail page to highlight available animals for adoption.
- 📸 **Service Images**: Will be used to represent grooming, training, and veterinary services.
- 📂 All images are loaded via `image_url` fields and stored externally for performance.
- 🎯 Future optimization using tools like **TinyPNG** will improve performance.

> Note: All images are either owned or sourced from open-license repositories like [Unsplash](https://unsplash.com) or [Pexels](https://www.pexels.com). Each image will be properly credited in the README.

---

## 🛠️ Technologies Used

PawfectMatch leverages modern, reliable technologies across the front-end and back-end to ensure a responsive and dynamic user experience.

### 🌐 Languages

- **HTML5** – For page structure and semantic markup.
- **CSS3** – For visual styling and responsive layout.
- **JavaScript (optional)** – For future dynamic frontend behavior.
- **Python 3.12** – Backend language for Django framework.

---

### 🧰 Frameworks & Libraries

- **Django 5.2** – High-level Python web framework used for building models, views, and forms.
- **Django Allauth 65.7.0** – Integrated user authentication and registration.
- **Bootstrap 5.3.3** – CSS framework for responsive design and pre-styled components.
- **Gunicorn** – WSGI HTTP server used for production deployment.
- **WhiteNoise** – For efficient static file handling on Heroku.

---

### 🗃️ Databases

- **SQLite3** – Used during local development for simplicity.
- **PostgreSQL** – Production-grade relational database used on Heroku.

---

### 🧪 Tools & Platforms

- **Visual Studio Code** – Main IDE for writing and editing code.
- **Git** – Version control for managing changes.
- **GitHub** – Remote code hosting, issues, and project planning (Agile board).
- **Heroku** – Hosting platform for live deployment.
- **Balsamiq** – For wireframe design and UX planning.
- **DrawSQL / dbdiagram.io** – For creating the ERD (Entity Relationship Diagram).
- **Chrome DevTools** – For layout debugging, Lighthouse testing, and accessibility checks.

---

### ⚙️ Other Utilities

- **pip** – Python package manager for installing project dependencies.
- **dotenv / env.py** – Local environment variable management.
- **Favicon.io** – For generating a custom site favicon.
- **Font Awesome** – Icon library for interface icons.
- **TinyPNG** _(planned)_ – To optimize and compress uploaded images.

---

### 📦 Python Dependencies

All Python dependencies are listed in the `requirements.txt` file and installed via:

```bash
pip install -r requirements.txt
asgiref==3.8.1
Django==5.2
django-allauth==65.7.0
sqlparse==0.5.3

```


---

## 🛠️ Agile Planning

This project was developed using the Agile methodology and GitHub Projects (Kanban board) to manage tasks and user stories effectively.

A total of **17 user stories** were written, grouped under **4 Epics**:

### 📁 Epics & User Story Themes

| Epic                               | Description                                                              |
| ---------------------------------- | ------------------------------------------------------------------------ |
| **User Accounts & Authentication** | Registration, login/logout, profile access, email confirmation           |
| **Adoption Workflow**              | Browse pets, add/delete listings (admin), adopt flow                     |
| **Pet Services & Bookings**        | View services, book, pay via Stripe, see bookings                        |
| **Support & Community Sharing**    | Volunteer info, social sharing, confirmations, and custom error handling |

Each story was created using GitHub Issues with a markdown-based user story template and included clear, testable **acceptance criteria** (3–5 per story).

---

### 📌 Agile Board Structure

The GitHub Project board followed a classic **Kanban** format with three main columns:

- **To Do** – All planned user stories
- **In Progress** – Tasks currently being developed
- **Done** – Completed and verified user stories

Issues were regularly updated and moved between columns throughout development to reflect real progress.

---

### 📷 Agile Board Screenshot

![Agile board showing user stories organized in To Do, In Progress, and Done](documentation/agile-board.png)

> 📝 _Be sure to update the image path above to match your actual screenshot filename and folder (e.g., `assets/images/agile-board.png` if you're storing it there)._


---


---

## 🚀 Deployment

The **PawfectMatch** project was developed locally using `Visual Studio Code` and then deployed to **Heroku** using the Code Institute student template.

### 🔗 Live Site

The project is live at:  
[https://pawfectmatch-ok-c783577133e6.herokuapp.com](https://pawfectmatch-ok-c783577133e6.herokuapp.com)

---

### 🛠 Version Control & Hosting

- Git was used for local version control.
- The project was pushed to GitHub at regular intervals using descriptive commit messages.
- The repository is hosted at:  
  [https://github.com/Omar6688/PawfectMatch](https://github.com/Omar6688/PawfectMatch)

---

### 💻 How to Run Locally

To run the **PawfectMatch** project locally for development or testing, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Omar6688/PawfectMatch.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd PawfectMatch
    ```

3. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file in the root directory** and add your environment variables:
    ```env
    SECRET_KEY=your-secret-key
    DEVELOPMENT=True
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    STRIPE_PUBLIC_KEY=your-stripe-key
    STRIPE_SECRET_KEY=your-stripe-secret
    ```

6. **Apply database migrations**:
    ```bash
    python3 manage.py migrate
    ```

7. **Create a superuser account (optional but recommended)**:
    ```bash
    python3 manage.py createsuperuser
    ```

8. **Start the development server**:
    ```bash
    python3 manage.py runserver
    ```

9. **Open your browser and visit**:
    ```
    http://localhost:8000
    ```

You should now see the **PawfectMatch** homepage running locally! 🐾


### 🚀 Heroku Deployment

The **PawfectMatch** project was deployed to Heroku using the Code Institute student template and Heroku CLI. Below are the detailed steps followed:

---

### 🔧 Prerequisites

- GitHub repository set up with all project files.
- `requirements.txt`, `Procfile`, and `runtime.txt` present.
- Environment variables stored securely (locally in `.env`, and on Heroku dashboard).
- Heroku account with CLI installed.
- PostgreSQL add-on configured.

---

### 1️⃣ Prepare for Heroku

1. **Add required files**:
    - Create a `Procfile` (no file extension) with:
        ```text
        web: gunicorn pawfectmatch_project.wsgi
        ```
    - Ensure your `requirements.txt` is up to date:
        ```bash
        pip freeze > requirements.txt
        ```

2. **Install necessary packages** (already added):
    ```bash
    pip install gunicorn
    pip install dj-database-url psycopg2-binary
    pip install whitenoise
    ```

3. **Update `settings.py`**:
    - Set `ALLOWED_HOSTS` to include your Heroku domain.
    - Configure database with `dj-database-url`.
    - Use `os.getenv()` to load environment variables.
    - Add static/media file handling with WhiteNoise or AWS S3.

---

### 2️⃣ Create Heroku App

1. Log in to Heroku CLI:
    ```bash
    heroku login
    ```

2. Create the app:
    ```bash
    heroku create pawfectmatch-ok
    ```

3. Add Heroku remote to Git:
    ```bash
    heroku git:remote -a pawfectmatch-ok
    ```

---

### 3️⃣ Set Environment Variables on Heroku

In the **Heroku dashboard**, go to **Settings > Reveal Config Vars** and add the following:

| Key               | Value                    |
|------------------|--------------------------|
| SECRET_KEY        | your-django-secret-key   |
| DEBUG             | False                    |
| DEVELOPMENT       | False                    |
| USE_AWS           | True (if using AWS S3)   |
| STRIPE_PUBLIC_KEY | your-stripe-key          |
| STRIPE_SECRET_KEY | your-stripe-secret-key   |
| EMAIL_BACKEND     | django.core.mail.backends.smtp.EmailBackend |
| EMAIL_HOST        | smtp.gmail.com           |
| EMAIL_PORT        | 587                      |
| EMAIL_USE_TLS     | True                     |
| EMAIL_HOST_USER   | your-email@gmail.com     |
| EMAIL_HOST_PASSWORD | your-app-password      |

---

### 4️⃣ Deploy to Heroku

1. Push your code to Heroku:
    ```bash
    git push heroku main
    ```

2. Run migrations:
    ```bash
    heroku run python manage.py migrate
    ```

3. Create superuser on Heroku:
    ```bash
    heroku run python manage.py createsuperuser
    ```

---

### ✅ Live Site

The site is now live at:

🔗 [https://pawfectmatch-ok.herokuapp.com](https://pawfectmatch-ok.herokuapp.com)

You can log in using your test account or superuser credentials.

---

### 🧪 Notes

- Static files are served via AWS S3.
- Allauth and Stripe are fully working on production.
- Debug mode is disabled in production.

---


## 🙌 Credits & Acknowledgments

This project was developed as part of the **Code Institute Level 5 Diploma in Web Application Development**.

### 💬 Special Thanks

- **Gareth (My Mentor)** – A very special and sincere thank you to Gareth for his consistent guidance, encouragement, and expertise throughout this final project. His advice helped shape the project’s architecture, improve UX choices, and ensure a clear focus toward achieving a merit-level submission. As always, Gareth’s support went above and beyond, and I’m incredibly grateful for his mentorship.

- **Roman (Tutor Support)** – for helping resolve advanced AWS S3 and deployment issues with patience and clear solutions.

- **Code Institute** – for the structured curriculum, Django walkthroughs, and the excellent student support system, which made this full-stack project achievable.

- **Balsamiq** – used to create initial wireframe layouts in a user-focused and accessible format.

- **dbdiagram.io / DrawSQL** – used to generate the final Entity Relationship Diagram (ERD) for model planning and database logic.

---

### 🖼️ Image & Asset Sources

- **Pet images**: Placeholder animal images sourced from [Pexels](https://www.pexels.com) and [Unsplash](https://unsplash.com), licensed for free use with attribution.
- **Icons**: From [Font Awesome](https://fontawesome.com/) under their open-use license.
- **Favicon**: Generated using [Favicon.io](https://favicon.io/).

---

### 🧑‍💻 Code Inspiration

- Some logic and setup steps were referenced from:
  - Django documentation: https://docs.djangoproject.com
  - Stripe’s official documentation
  - Community answers on [Stack Overflow](https://stackoverflow.com)
  - Blog tutorials from [Real Python](https://realpython.com)

Where code was reused or adapted, it has been clearly credited in-line or in the comments.

---

_This project is built for educational purposes only and is not intended for commercial deployment._
