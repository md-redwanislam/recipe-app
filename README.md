# Savorly – Recipe Sharing Platform

A recipe-sharing web application built with **Django**. Users can register, manage their profiles, create recipes, add ingredients and cooking instructions, and share published recipes with everyone.

## Features

### User Authentication
- Custom user model with UUID primary keys.
- Email and password-based registration and login.
- Django session-based authentication.
- User logout.
- Protected pages for authenticated users.

### User Profiles
- Custom profile with name, email, phone number, and bio.
- Profile picture uploads using Cloudinary.
- Users can update their own profile information and profile picture.

### Recipe Management
- Create recipes with a title, description, and cover image.
- Add multiple ingredients to a recipe.
- Add multiple cooking instructions with step numbers.
- Save recipes as Draft or Published.
- Edit and delete your own recipes.
- UUID primary keys for recipe-related models.

### Public Recipe Browsing
- Published recipes are visible to everyone.
- Draft recipes are excluded from the public recipe list.
- Recipe descriptions are truncated on the list page.
- Visitors can open a recipe to see its full description, ingredients, and instructions.
- Only recipe owners can see their Edit and Delete options.
- Users cannot edit or delete recipes belonging to other users.

### Image Storage
- Cloudinary integration for profile pictures and recipe cover images.
- Old recipe cover images are deleted when replaced or when a recipe is deleted.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web framework |
| TiDB | Relational database |
| PyMySQL | MySQL-compatible database driver |
| Cloudinary | Image storage |
| Pillow | Image processing |
| Bootstrap 5 | Frontend styling |
| HTML | Server-rendered templates |
| JavaScript | Optional frontend interactions |

## Project Structure

```text
project/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       └── profile.html
│   ├── admin.py
│   ├── forms.py
│   ├── managers.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── recipe/
│   ├── migrations/
│   ├── templates/
│   │   └── recipe/
│   │       ├── create_recipe.html
│   │       ├── edit_recipe.html
│   │       ├── delete_recipe.html
│   │       ├── recipe_list.html
│   │       └── recipe_detail.html
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base_generic.html
│   └── registration/
│       ├── login.html
│       └── registration.html
│
├── .env
├── .gitignore
├── manage.py
└── requirements.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-cloudinary-api-key
CLOUDINARY_API_SECRET=your-cloudinary-api-secret

DB_HOST=your-tidb-host
DB_PORT=4000
DB_NAME=your-database-name
DB_USER=your-database-username
DB_PASSWORD=your-database-password
```

Make sure your Django database configuration reads these variables and matches your TiDB connection settings.

**Important:** Never commit your `.env` file or expose your Cloudinary credentials.

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

## Application Routes

| Route | Description | Access |
|---|---|---|
| `/auth/register/` | User registration | Public |
| `/auth/login/` | User login | Public |
| `/auth/logout/` | User logout | Authenticated |
| `/auth/profile/` | View and update profile | Authenticated |
| `/recipes/` | Browse published recipes | Public |
| `/recipes/` | Create a recipe | Authenticated |
| `/recipes/<UUID>/` | View recipe details | Public for published recipes; owner for drafts |
| `/recipes/<UUID>/edit/` | Edit a recipe | Recipe owner |
| `/recipes/<UUID>/delete/` | Delete a recipe | Recipe owner |

## Recipe Status

Recipes have two possible statuses:

- **Draft:** A private recipe visible only to its owner.
- **Published:** A recipe visible to everyone.

Only published recipes appear on the public recipe listing page.

## Database Models

### CustomUser
Stores user account and profile information.

### Recipe
Stores recipe details, including:
- Author
- Title
- Description
- Cover image
- Publication status
- Creation and update timestamps

### Ingredient
Stores ingredients associated with a recipe:
- Quantity
- Unit
- Name

### Instruction
Stores cooking instructions associated with a recipe:
- Step number
- Description

All application models use UUID primary keys.

## Image Storage

Cloudinary is used to store uploaded profile pictures and recipe cover images.

The application uses Django's storage configuration to manage image uploads.

Recipe cover image cleanup is handled through Django model signals when an image is replaced or its recipe is deleted.

## Development Notes

- Django templates are used for server-side rendering.
- Django Forms are used for authentication and profile operations.
- Django ModelForms are used for recipe-related forms.
- Django inline formsets manage multiple ingredients and instructions.
- Django's built-in authentication and session management handle user login.
- Database transactions are used when saving recipes and their related records.
- Recipe ownership is verified on the server before editing or deleting.

## License

This project is currently developed for learning and educational purposes.
