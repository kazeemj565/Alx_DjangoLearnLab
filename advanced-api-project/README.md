## API Views - Book Endpoints

| Endpoint              | Method | Description              | Auth Required |
|-----------------------|--------|--------------------------|---------------|
| /api/books/           | GET    | List all books           | No            |
| /api/books/<id>/      | GET    | Get book details         | No            |
| /api/books/create/    | POST   | Create a new book        | Yes           |
| /api/books/<id>/update/ | PUT/PATCH | Update a book       | Yes           |
| /api/books/<id>/delete/ | DELETE | Delete a book          | Yes           |

Permissions:
- Create/Update/Delete views require the user to be authenticated.


## 🔍 Book API Query Features

### 📑 Filtering
You can filter by title, author ID, or publication year:


### 🔎 Searching
Search by partial matches in title or author name:


### ↕️ Ordering
Order results by title or publication year (ascending/descending):
