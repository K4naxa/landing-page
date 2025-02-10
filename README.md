# Personal Landing Page
[Pohjosenpaja.fi](https://pohjosenpaja.fi/)

A personal landing page built with Vue 3, designed to showcase my skills, projects, and experience as a full-stack web developer. This site serves as a central hub for potential clients and employers to learn about my capabilities and get in touch. Security is a priority, with reCAPTCHA v3 integrated into the contact form and CV download process to prevent spam and abuse as well as keep my personal information safe.

## Features

*   **Responsive Design:**  Optimal viewing experience across all devices.
*   **Interactive Sections:** Engaging sections to showcase projects, skills, and experience with smooth scrolling navigation.
*   **Secure Contact Form:** Contact form integrated with reCAPTCHA v3 to prevent spam submissions.
*   **Protected CV Download:**  CV download feature secured with reCAPTCHA v3 to prevent automated downloads and protect personal information.
*   **Mobile-Friendly Navigation:** Intuitive mobile navigation with swipe gestures.
*   **Toast Notifications:**  User-friendly feedback using Vue3-Toastify for form submissions and other actions.

## Technical Highlights

*   **Frontend:**
    *   Built with Vue 3 for a reactive and component-based architecture.
    *   Styled using Tailwind CSS for rapid UI development and a modern aesthetic.
    *   Mobile swipe navigation using `@vueuse/core`.
*   **Backend:**
    *   FastAPI (Python) backend for handling API requests, including contact form submissions and CV downloads.
    *   reCAPTCHA v3 integration on both the contact form and CV download endpoints for enhanced security.
*   **reCAPTCHA v3:** Implemented on the contact form and CV download to ensure security and prevent spam.
*   **Vue3-Toastify:**  Provides user feedback with toast notifications for successful or failed actions.
*   **Axios:** Used for making HTTP requests to the backend API.
*   **Mobile Swipe Navigation:**  Enables easy browsing on touch devices.
*   **Modal Closing:** Mobile swipe backwards closes the current open modal, improving user experience.


## Technologies Used

*   [Vue 3](https://vuejs.org/):  A progressive JavaScript framework for building user interfaces.
*   [Tailwind CSS](https://tailwindcss.com/):  A utility-first CSS framework for rapid UI development.
*   [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
*   [VueUse](https://vueuse.org/): Collection of essential Vue Composition Utilities
*   [Vue3-Toastify](https://github.com/Maronato/vue3-toastify): Library for toast notifications.
*   [Axios](https://axios-http.com/):  Promise based HTTP client for the browser and node.js
*   [Python](https://www.python.org/)
*   [ReCaptcha V3](https://developers.google.com/recaptcha/): Free service that protects your site from spam and abuse.

## Setup

### Prerequisites

*   [Node.js](https://nodejs.org/) (v16 or higher)
*   [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)
*   [Python 3.7+](https://www.python.org/downloads/)
*   [pip](https://pypi.org/project/pip/)


## Security

This project implements reCAPTCHA v3 to protect against spam and abuse.

*   **reCAPTCHA v3:**  Validates user interactions to differentiate between legitimate users and bots.  The backend verifies the reCAPTCHA token received from the frontend before processing contact form submissions or allowing CV downloads.
*   **Environment Variables:** Sensitive information (API keys, email credentials) are stored in environment variables to prevent them from being hardcoded in the application.
