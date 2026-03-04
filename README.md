# Fb-crm Documentation

## Setup Instructions  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/markyao-vietnam/Fb-crm.git  
   cd Fb-crm  
   ```  
2. Install dependencies:  
   ```bash  
   npm install  
   ```  
3. Configure environment variables as described in the **Environment Variables** section.

## API Endpoints  
- **GET /api/v1/users**  
  - Description: Retrieve a list of users.  
  - Response: An array of user objects.
- **POST /api/v1/users**  
  - Description: Create a new user.  
  - Body: `{ "name": "John Doe", "email": "john@example.com" }`  
  - Response: The created user object.

## Environment Variables  
- `DB_URL`: URL for the database connection.  
- `PORT`: Port where the application runs (default: 3000).

## Usage Examples  
### Retrieve Users  
```bash  
curl -X GET http://localhost:3000/api/v1/users  
```
### Create User  
```bash  
curl -X POST http://localhost:3000/api/v1/users \  
-H "Content-Type: application/json" \  
-d '{"name":"John Doe", "email":"john@example.com"}'  
```
