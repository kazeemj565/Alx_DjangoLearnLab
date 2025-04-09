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

# Blog Post Management Features

## Functionality
- List all posts at `/`
- View individual post details at `/posts/<id>/`
- Create a new post at `/posts/new/` (authenticated users only)
- Edit and delete posts (author only)

## Permissions
- Guests can only read posts.
- Logged-in users can create posts.
- Only post authors can edit/delete their own posts.

## How to Test
1. Visit `/register` to sign up.
2. Create a new post.
3. Edit and delete your post.
4. Try accessing edit/delete on another user’s post — you should be denied.
