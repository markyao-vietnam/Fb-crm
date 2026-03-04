# FastAPI CRM Documentation

## Installation
To install the FastAPI CRM, you need to have Python 3.7 or higher installed. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/markyao-vietnam/Fb-crm.git
   cd Fb-crm
   ```
2. Create a `.env` file based on the `.env.example` file and configure your environment variables.

## Configuration
- Make sure to configure the database url in the `.env` file following this format:
  
  ```bash
  DATABASE_URL=sqlite:///./test.db
  ```  
  or any other database driver you are using.

## API Endpoints
### User Management
- `POST /users/` - Create a user  
- `GET /users/` - Get all users  
- `GET /users/{user_id}` - Get user by ID  
- `PUT /users/{user_id}` - Update user by ID  
- `DELETE /users/{user_id}` - Delete user by ID  

### CRM Features
- Create, Read, Update and Delete (CRUD) operations for users and other resources.  
- Authentication and authorization features using JWT.

## Project Structure
```
Fb-crm/
│
├── app/
│   ├── main.py          # Entry point
│   ├── api/             # Folder for API routes
│   ├── models/          # Database models
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Business logic
│   └── tests/           # Test cases
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Security Notes
- Ensure that only authorized users can access certain endpoints.
- Keep your dependencies updated to avoid vulnerabilities.

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and create a pull request.


For more information, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).