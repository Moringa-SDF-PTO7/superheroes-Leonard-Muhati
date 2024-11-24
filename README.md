# Introduction
# # Superheroes API
Welcome to the **Superheroes API**! This RESTful API allows you to manage superheroes and their superpowers. You can retrieve information about heroes, powers, and hero-power associations, as well as update and create new data.

## Prerequisites
To run this project, you need:

- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- 
You can install dependencies using a `Pipfile` or `requirements.txt`.

---
## Setup 
1. **Clone the repository**:
    ```bash
    git clone git@github.com:Moringa-SDF-PTO7/superheroes-Leonard-Muhati.git
    cd superheroes-Leonard-Muhati
    ```
2. **Install dependencies**:
    Use `pipenv`:
    ```bash
    pipenv install
    pipenv shell
    ```    
3. **Set up the database**:
    Initialize and migrate the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

4. **Run the application**:
    ```bash
    flask run
    ```

    By default, the app will run on `http://localhost:5555`.

---    
# overview

| Method | Endpoint             | Description                       |
|--------|-----------------------|-----------------------------------|
| GET    | `/`                  | Welcome message                   |
| GET    | `/heroes`            | Retrieve all superheroes          |
| GET    | `/heroes/<id>`       | Retrieve a superhero by ID         |
| GET    | `/powers`            | Retrieve all powers               |
| GET    | `/powers/<id>`       | Retrieve a power by ID             |
| PATCH  | `/powers/<id>`       | Update a power's description       |
| POST   | `/hero_powers`       | Assign a power to a hero           |

---

### Example Requests

#### Get All Heroes
**Request**:
```http
GET /heroes HTTP/1.1
```
Response:

```json

[
    {
        "id": 1,
        "name": "Clark Kent",
        "super_name": "Superman"
    },
    {
        "id": 2,
        "name": "Bruce Wayne",
        "super_name": "Batman"
    }
]
```
Update a Power
Request:

```http

PATCH /powers/1 HTTP/1.1
Content-Type: application/json

{
    "description": "This power allows heroes to fly at incredible speeds."
}
```
Response:

```json

{
    "id": 1,
    "name": "Flight",
    "description": "This power allows heroes to fly at incredible speeds."
}
```
Create Hero-Power Association
Request:

```http

POST /hero_powers HTTP/1.1
Content-Type: application/json

{
    "strength": "Strong",
    "hero_id": 1,
    "power_id": 2
}
```
Response:

```json

{
    "id": 1,
    "strength": "Strong",
    "hero_id": 1,
    "power_id": 2
}
```
----
# Models
### Hero

Represents a superhero with a real name and a super identity.

| Field       | Type    | 
|-------------|---------|
| `id`        | Integer | 
| `name`      | String  | 
| `super_name`| String  | 

---

### Power

Represents a superpower with a name and description.

| Field         | Type    |
|---------------|---------|
| `id`          | Integer | 
| `name`        | String  | 
| `description` | Text    | 

---

### HeroPower

Represents the relationship between a `Hero` and a `Power`. Includes additional information about the strength of the power for a specific hero.

| Field        | Type    | 
|--------------|---------|
| `id`         | Integer | 
| `strength`   | String  |
| `hero_id`    | Integer | 
| `power_id`   | Integer | 

---
## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

## Conclusion

The **Superheroes API** makes it easy to manage heroes, their powers, and their relationships. It's flexible, scalable, and ready to be extended for various projects. Feel free to explore, customize, and build something amazing!

