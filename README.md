Coursify Web
## Project Description
Coursify Web is the browser-based frontend of the Coursify platform — a Senior High School course recommendation system. It provides students with a full psychometric assessment experience and personalized ML-powered course recommendations, while also offering dedicated dashboards for admins and superadmins to manage users and monitor platform analytics.
The web version supports all three user roles: student, admin, and superadmin. It communicates with the shared Coursify FastAPI backend via REST API.


## Features
Student
•	User Authentication — Registration with email OTP verification, login, forgot password with reset code flow, and JWT-based session management
•	RIASEC Assessment — Holland Interest Inventory with 36 questions across 6 personality types (Realistic, Investigative, Artistic, Social, Enterprising, Conventional)
•	Big Five Personality Assessment — OCEAN model profiling with 25 questions across 5 traits including reverse-scored items
•	Aptitude Assessment — 12-question subject tests across Math, Science, English, and Abstract Reasoning with easy / medium / hard difficulty tiers
•	ML-Powered Course Recommendations — Top 5 ranked college course suggestions with confidence scores
•	AI Profile Summary — Google Gemini generates a personalized counselor-style summary based on assessment results
•	Dashboard — Full assessment profile with RIASEC bar chart, Big Five trait cards, aptitude scores, top recommended courses, and quick stats panel
•	Assessment History — All past attempts with expandable score breakdowns per attempt (courses, RIASEC, Big Five, aptitude tabs)
•	Course Explorer — Browse and filter college courses by strand and category
•	Profile Management — Edit username, email, grade level, and academic strand
Admin
•	Analytics Dashboard — Platform statistics including total users, new registrations, active/inactive accounts, registration trend chart, strand breakdown, grade level breakdown, and role distribution; filterable by 7-day, 30-day, or all-time range
Superadmin
•	User Management — Paginated, searchable, and filterable user table with role assignment and account activation/deactivation
•	Audit Log — Timestamped record of all admin-initiated role and status changes
•	CSV Export — Download all user data as a CSV file
•	Role-Based Access Control — Three-tier access enforced via protected routes on the frontend


## Technology Stack
Layer	Technology
Framework	React.js (Create React App)
Routing	React Router v6
Charts	Recharts
Icons	React Icons
Local Storage	localStorage
Styling	Plain CSS (Nunito + Sora fonts via Google Fonts)
Environment	.env via REACT_APP_* variables


## System Architecture
Coursify Web (React.js)
        │
        │  localStorage
        │  ┌─────────────────────────────────┐
        │  │  token, coursify_user,           │
        │  │  coursify_role, coursify_        │
        │  │  assessment_progress             │
        │  └─────────────────────────────────┘
        │
        │  Protected Routes
        │  ┌──────────────────────────────────────────┐
        │  │  / (Login)                               │
        │  │  /register                               │
        │  │  /dashboard              → role: user    │
        │  │  /assessment             → role: user    │
        │  │  /courses                → role: user    │
        │  │  /profile                → role: user    │
        │  │  /admin/dashboard        → role: admin+  │
        │  │  /superadmin/dashboard   → role: superadmin│
        │  └──────────────────────────────────────────┘
        │
        │  REST API calls (JWT Bearer token)
        ▼
Coursify FastAPI Backend
All API requests include a Bearer token in the Authorization header. The ProtectedRoute component checks coursify_role from localStorage before rendering any route, redirecting unauthorized users to the appropriate fallback.

## Installation & Setup
Prerequisites
•	Node.js v18 or higher
•	npm or yarn
•	Coursify backend running locally or deployed (see backend README)
1. Clone the repository
git clone https://github.com/yourusername/coursify-web.git
cd coursify-web
2. Install dependencies
npm install
3. Configure the API
Create a .env file in the project root:
REACT_APP_API_URL=http://localhost:8000
Replace the value with your deployed backend URL if not running locally.
4. Start the development server
npm start
The app will be available at http://localhost:3000/coursify-web
5. Build for production
npm run build
The optimized build output will be in the build/ folder, ready for static hosting.
Note: The basename is set to /coursify-web in the router. If you deploy to a different path or domain root, update the basename prop in App.js accordingly.

## Test accounts 
User: 
E: yunasilva01@gmail.com 
P: Genesis1:1

E: anyachan.maki@gmail.com 
P: Genesis1:1

Super admin: 
E: seanfinn830@gmail.com 
P: Genesis1:1

## Known Limitations
•	Admin and superadmin roles are web-only — The mobile version of Coursify only supports the student role. Logging in with admin or superadmin credentials on the mobile app will not grant access to any admin features
•	Email delivery in deployment — OTP verification and password reset emails use Gmail SMTP which requires outbound ports 465 or 587. Most cloud hosting providers block these ports, causing connection timeouts in production. Locally this works fine since the machine can connect directly. The proper solution for production is to replace Gmail SMTP with a dedicated email API service such as SendGrid or Mailgun
•	Assessment results not editable — Once an assessment is submitted it is permanently stored; there is no way to retake or delete a specific attempt from the UI
•	No real-time updates — The analytics dashboard and user management table require a manual page refresh to reflect the latest data

Coursify Web
Project Description
Coursify Web is the browser-based frontend of the Coursify platform — a Senior High School course recommendation system. It provides students with a full psychometric assessment experience and personalized ML-powered course recommendations, while also offering dedicated dashboards for admins and superadmins to manage users and monitor platform analytics.
The web version supports all three user roles: student, admin, and superadmin. It communicates with the shared Coursify FastAPI backend via REST API.
Features
Student
•	User Authentication — Registration with email OTP verification, login, forgot password with reset code flow, and JWT-based session management
•	RIASEC Assessment — Holland Interest Inventory with 36 questions across 6 personality types (Realistic, Investigative, Artistic, Social, Enterprising, Conventional)
•	Big Five Personality Assessment — OCEAN model profiling with 25 questions across 5 traits including reverse-scored items
•	Aptitude Assessment — 12-question subject tests across Math, Science, English, and Abstract Reasoning with easy / medium / hard difficulty tiers
•	ML-Powered Course Recommendations — Top 5 ranked college course suggestions with confidence scores
•	AI Profile Summary — Google Gemini generates a personalized counselor-style summary based on assessment results
•	Dashboard — Full assessment profile with RIASEC bar chart, Big Five trait cards, aptitude scores, top recommended courses, and quick stats panel
•	Assessment History — All past attempts with expandable score breakdowns per attempt (courses, RIASEC, Big Five, aptitude tabs)
•	Course Explorer — Browse and filter college courses by strand and category
•	Profile Management — Edit username, email, grade level, and academic strand
Admin
•	Analytics Dashboard — Platform statistics including total users, new registrations, active/inactive accounts, registration trend chart, strand breakdown, grade level breakdown, and role distribution; filterable by 7-day, 30-day, or all-time range
Superadmin
•	User Management — Paginated, searchable, and filterable user table with role assignment and account activation/deactivation
•	Audit Log — Timestamped record of all admin-initiated role and status changes
•	CSV Export — Download all user data as a CSV file
•	Role-Based Access Control — Three-tier access enforced via protected routes on the frontend
Technology Stack
Layer	Technology
Framework	React.js (Create React App)
Routing	React Router v6
Charts	Recharts
Icons	React Icons
Local Storage	localStorage
Styling	Plain CSS (Nunito + Sora fonts via Google Fonts)
Environment	.env via REACT_APP_* variables
System Architecture
Coursify Web (React.js)
        │
        │  localStorage
        │  ┌─────────────────────────────────┐
        │  │  token, coursify_user,           │
        │  │  coursify_role, coursify_        │
        │  │  assessment_progress             │
        │  └─────────────────────────────────┘
        │
        │  Protected Routes
        │  ┌──────────────────────────────────────────┐
        │  │  / (Login)                               │
        │  │  /register                               │
        │  │  /dashboard              → role: user    │
        │  │  /assessment             → role: user    │
        │  │  /courses                → role: user    │
        │  │  /profile                → role: user    │
        │  │  /admin/dashboard        → role: admin+  │
        │  │  /superadmin/dashboard   → role: superadmin│
        │  └──────────────────────────────────────────┘
        │
        │  REST API calls (JWT Bearer token)
        ▼

Coursify FastAPI Backend
All API requests include a Bearer token in the Authorization header. The ProtectedRoute component checks coursify_role from localStorage before rendering any route, redirecting unauthorized users to the appropriate fallback.

## Installation & Setup
Prerequisites
•	Node.js v18 or higher
•	npm or yarn
•	Coursify backend running locally or deployed (see backend README)
1. Clone the repository
git clone https://github.com/yourusername/coursify-web.git
cd coursify-web
2. Install dependencies
npm install
3. Configure the API
Create a .env file in the project root:
REACT_APP_API_URL=http://localhost:8000
Replace the value with your deployed backend URL if not running locally.
4. Start the development server
npm start
The app will be available at http://localhost:3000/coursify-web
5. Build for production
npm run build
The optimized build output will be in the build/ folder, ready for static hosting.
Note: The basename is set to /coursify-web in the router. If you deploy to a different path or domain root, update the basename prop in App.js accordingly.

## Known Limitations
•	Admin and superadmin roles are web-only — The mobile version of Coursify only supports the student role. Logging in with admin or superadmin credentials on the mobile app will not grant access to any admin features
•	Email delivery in deployment — OTP verification and password reset emails use Gmail SMTP which requires outbound ports 465 or 587. Most cloud hosting providers block these ports, causing connection timeouts in production. Locally this works fine since the machine can connect directly. The proper solution for production is to replace Gmail SMTP with a dedicated email API service such as SendGrid or Mailgun
•	Assessment results not editable — Once an assessment is submitted it is permanently stored; there is no way to retake or delete a specific attempt from the UI
•	No real-time updates — The analytics dashboard and user management table require a manual page refresh to reflect the latest data

Coursify Backend
Project Description
Coursify Backend is the shared FastAPI server that powers both the Coursify Web and Coursify Mobile applications. It handles user authentication, psychometric assessment scoring, machine learning course recommendations, AI-generated profile summaries, and role-based admin operations.
It is built with Python and FastAPI, uses MongoDB Atlas as the database, and exposes a REST API consumed by both frontend platforms via JWT-authenticated requests.
Features
•	User Authentication — Registration with email OTP verification, login, JWT token issuance, forgot password with reset code, and password reset
•	Role-Based Access Control — Three-tier role system (user, admin, superadmin) enforced via FastAPI middleware dependencies on all protected endpoints
•	Assessment Engine — Randomized question delivery across RIASEC, Big Five, and Aptitude collections; server-side scoring with reverse-scoring support for Big Five
•	ML Course Recommendations — scikit-learn model accepts RIASEC raw scores, Big Five trait means, aptitude percentages, and strand to return top 5 ranked courses with confidence scores
•	AI Profile Summaries — Google Gemini API generates personalized counselor-style summaries from scored assessment data
•	Assessment History — Stores all completed assessment results per user; returns full score breakdowns including RIASEC, Big Five, aptitude, and recommendations
•	Admin Analytics — Aggregated user statistics, registration trends, strand/grade breakdowns, and role distribution with date range filtering
•	User Management — Superadmin endpoints for listing, searching, filtering, role updating, and status toggling of user accounts
•	Audit Logging — Every role change and status change is recorded with actor, timestamp, and new value inside the user document
•	CSV Export — Streams all user data as a downloadable CSV file
•	Account Seeding — CLI scripts to seed superadmin and admin accounts interactively

## Technology Stack
Layer	Technology
API Framework	FastAPI (Python)
Database	MongoDB Atlas
Async DB Driver	Motor
Authentication	JWT via python-jose
Password Hashing	Passlib / bcrypt
Request Validation	Pydantic
Email (local)	Gmail SMTP via smtplib / aiosmtplib
ML Model	scikit-learn
AI Summaries	Google Gemini (google-generativeai)
Environment	python-dotenv
Hosting	Render

## System Architecture
                    ┌─────────────────────────────────┐
                    │       Coursify Web (React)       │
                    │       Coursify Mobile (Expo)     │
                    └────────────────┬────────────────┘
                                     │
                          REST API — Bearer JWT
                                     │
                    ┌────────────────▼────────────────┐
                    │         FastAPI Backend          │
                    │                                  │
                    │  ┌──────────────────────────┐   │
                    │  │        API Routers        │   │
                    │  │                           │   │
                    │  │  /api/auth/*              │   │
                    │  │    register, verify,      │   │
                    │  │    login, profile,        │   │
                    │  │    forgot-password,       │   │
                    │  │    reset-verify,          │   │
                    │  │    reset-password         │   │
                    │  │                           │   │
                    │  │  /api/assessment/*        │   │
                    │  │    questions, submit,     │   │
                    │  │    results/latest,        │   │
                    │  │    results/history        │   │
                    │  │                           │   │
                    │  │  /api/admin/*             │   │
                    │  │    analytics, users,      │   │
                    │  │    users/{id}/role,       │   │
                    │  │    users/{id}/status,     │   │
                    │  │    audit-log,             │   │
                    │  │    export/users           │   │
                    │  │                           │   │
                    │  │  /api/ai/*                │   │
                    │  │    profile-summary        │   │
                    │  └────────────┬─────────────┘   │
                    │               │                  │
                    │  ┌────────────▼─────────────┐   │
                    │  │     Role Middleware       │   │
                    │  │  require_admin()          │   │
                    │  │  require_superadmin()     │   │
                    │  │  get_current_user()       │   │
                    │  └──────────────────────────┘   │
                    └───┬──────────────┬───────────┬───┘
                        │              │           │
           ┌────────────▼──┐  ┌────────▼──────┐  ┌▼──────────────────┐
           │ MongoDB Atlas │  │  scikit-learn │  │  Google Gemini AI  │
           │               │  │   ML Model    │  │                    │
           │  collections: │  │               │  │  Input: scored     │
           │  users        │  │  Input:       │  │  RIASEC + BigFive  │
           │  questions_   │  │  riasec_raw   │  │  + aptitude +      │
           │    riasec     │  │  bigfive_raw  │  │  strand            │
           │  questions_   │  │  aptitude_pct │  │                    │
           │    bigfive    │  │  strand       │  │  Output: 3–4 line  │
           │  questions_   │  │               │  │  profile summary   │
           │    aptitude   │  │  Output:      │  └───────────────────┘
           │  assessment_  │  │  top 5 courses│
           │    results    │  │  + confidence │
           └───────────────┘  └───────────────┘
                                      │
                             ┌────────▼────────┐
                             │   Gmail SMTP     │
                             │  OTP + Password  │
                             │  Reset Emails    │
                             └─────────────────┘
Assessment scoring flow:
1.	Client submits strand, RIASEC answers, Big Five answers, and aptitude answers
2.	Backend fetches question documents from MongoDB to resolve subcategories and correct answers
3.	RIASEC raw scores are summed per code; Big Five means are computed per trait with reverse scoring applied; aptitude correct counts are converted to percentages
4.	Scored data is passed to the scikit-learn ML model which returns top 5 ranked courses
5.	Full result document is stored in assessment_results collection
6.	Recommendations are returned to the client immediately

## Installation & Setup
Prerequisites
•	Python 3.10 or higher
•	MongoDB Atlas account (or local MongoDB instance)
•	Google Gemini API key
•	Gmail account with App Password enabled (for local email testing)
1. Clone the repository
git clone https://github.com/yourusername/coursify-backend.git
cd coursify-backend
2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root:
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
GEMINI_API_KEY=your_google_gemini_api_key
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
FRONTEND_URL=http://localhost:3000
5. Seed the superadmin account
python seed_superadmin.py
You will be prompted to enter a username, email, and password. If the email already exists, the account will be upgraded to superadmin.
6. Seed an admin account (optional)
python seed_admin.py
7. Run the development server
uvicorn main:app --reload
The API will be available at http://localhost:8000
Interactive API docs are accessible at http://localhost:8000/docs
Known Limitations
•	Email delivery in deployment — Gmail SMTP requires outbound ports 465 or 587, which most cloud hosting providers (including Render's free tier) block. This causes connection timeouts when sending OTP and password reset emails in production. Locally, email delivery works because the machine connects directly. The correct solution for production is to replace Gmail SMTP with a dedicated email API service such as SendGrid or Mailgun, which deliver email over HTTPS (port 443) instead
•	In-memory OTP storage — Pending registrations and password reset codes are stored in Python dictionaries (pending_users, reset_codes) in memory. This means they are lost on server restart and will not work correctly if the backend is scaled to multiple instances. A production-ready solution would store these temporarily in MongoDB or Redis with a TTL index
•	ML model is static — The scikit-learn model is loaded once at startup from a local file. It does not retrain automatically as new assessment data accumulates
•	Admin and superadmin roles are web-only — The mobile application supports the student role only. Admin and superadmin credentials will authenticate successfully via the API but the mobile app does not implement any admin UI or navigation

## Screenshots
Mobile
<img width="720" height="1560" alt="c07c86a3-df1d-4146-a726-d1ea4808b13d" src="https://github.com/user-attachments/assets/d3f76639-f0ec-4a65-9172-20548b58c436" />
<img width="720" height="1560" alt="60966dfc-4477-4a2a-9bd3-f6fa6690be81" src="https://github.com/user-attachments/assets/fb4cd478-51e5-4df8-b32d-94106ad4f594" />
<img width="720" height="1560" alt="0a15ad24-a04e-46f0-9ac0-88c82ad158be" src="https://github.com/user-attachments/assets/5915ec9e-e24b-412b-81ae-ad6f06eb9dae" />
<img width="720" height="1560" alt="0aaae7cd-9c5e-4f19-9926-3bbb49e8f61e" src="https://github.com/user-attachments/assets/2ef8dec6-5893-46a4-b01c-946134a0440e" />
<img width="720" height="1560" alt="0a156cee-59da-44fe-bd62-fdbac7262808" src="https://github.com/user-attachments/assets/b04e320e-0dbb-473a-83e3-2da363a6c25c" />
<img width="720" height="1560" alt="a8360659-2049-41e6-bef4-6ae80b8fd124" src="https://github.com/user-attachments/assets/b425e5d1-4360-4412-b3c5-4e39e95eb390" />
<img width="720" height="1560" alt="10bb9424-4dda-4ce4-8d2f-e434967e8010" src="https://github.com/user-attachments/assets/96dbd741-2016-4dce-b340-438c92047609" />

Web
<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/b21e9f65-5a63-4a73-bfbb-339b59f64523" />
<img width="1920" height="1080" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/1da1ab12-2308-42f9-94b4-b8821600c9d3" />
<img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/4d3c3480-0587-4ae8-95a1-89856206c461" />
<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/0edc5e9a-8be6-42f4-a644-98e45e9d30ce" />
<img width="1920" height="1080" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/3beff505-58bd-4821-bcbc-85fa8f32edda" />
<img width="1920" height="1080" alt="Screenshot (10)" src="https://github.com/user-attachments/assets/aa1a410f-4b2c-4512-a0fb-f6b64a318009" />
<img width="1920" height="1080" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/6911caa8-3be4-42f6-a70b-097692d8d401" />
<img width="1920" height="1080" alt="Screenshot (8)" src="https://github.com/user-attachments/assets/66894455-8c8c-4ffb-8c96-21920c85707e" />

Admin & SuperAdmin
<img width="1920" height="1080" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/0ef782e3-292d-47d7-a508-41c82f1d6efa" />
<img width="1920" height="1080" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/c94969d8-b3c6-4c95-b301-f4b696deefd6" />
<img width="1920" height="1080" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/79861b3c-2342-4710-9849-9a6f0b08b51d" />
<img width="1920" height="1080" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/5c498384-ef2c-40a1-bd7e-7055efad6118" />

FastAPI 
<img width="1920" height="1080" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/7fdefe7b-cca4-449a-ad76-9b5093a1e63d" />






