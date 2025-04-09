# Django Blog Authentication System

## Features
- User Registration
- Login & Logout
- Profile Viewing & Editing

## Setup
1. Add `'blog'` to `INSTALLED_APPS`.
2. Include `blog.urls` in your main `urls.py`.

## Usage
- `/register`: Create an account
- `/login`: Login
- `/logout`: Logout
- `/profile`: View or edit your email

## Forms
- `CustomUserCreationForm`: Adds email to registration
- CSRF protection enabled
