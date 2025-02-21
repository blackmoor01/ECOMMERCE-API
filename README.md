# E-commerce API

## 🚀 Overview
This is a **RESTful API** built with **Django & Django REST Framework (DRF)** for an **e-commerce platform**. It manages **products, user authentication, orders, and inventory** while implementing security best practices like **JWT authentication** and **rate limiting**.

## 🛠 Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Deployment**: Render
- **API Documentation**: https://ecommerce-api-0r20.onrender.com

## 📌 Features
✅ **User Authentication & Authorization** (JWT-based login & registration)
✅ **Product Management** (Create, update, delete, and list products)
✅ **Order Processing** (Create orders, calculate total price, and track order history)
✅ **Role-Based Access Control (RBAC)** (Admin vs. Regular Users)
✅ **Optimized Database Queries** (Handles high traffic efficiently)
✅ **Rate Limiting** (Prevents API abuse)
✅ **Data Migration Script** (Migrate legacy CSV data to PostgreSQL)

## 🛠 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
 git clone https://github.com/blackmoor01/ECOMMERCE-API.git
 cd ecommerce-api
```

### **2️⃣ Create & Activate a Virtual Environment**
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate it (For Windows: venv\Scripts\activate)
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory and add the following:
```ini
SECRET_KEY='your-secret-key'
DEBUG=True
DB_NAME=ecommerce_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=6432
ACCESS_TOKEN_LIFETIME=30
REFRESH_TOKEN_LIFETIME=1
```

### **5️⃣ Apply Migrations & Start Server**
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 🔑 Authentication
This API uses **JWT Authentication**. To get a token:
```sh
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
```
It will return an `access` and `refresh` token. Use the `access` token for authenticated requests.

## 📌 API Endpoints
| Endpoint                 | Method | Description                    | Auth Required |
|--------------------------|--------|--------------------------------|--------------|
| `/api/products/`         | GET    | List all products              | ❌ No |
| `/api/products/`         | POST   | Add a new product (Admin)      | ✅ Yes |
| `/api/products/{id}/`    | GET    | Retrieve a product             | ❌ No |
| `/api/products/{id}/`    | PUT    | Update a product (Admin)       | ✅ Yes |
| `/api/orders/`           | GET    | Get user orders                | ✅ Yes |
| `/api/orders/`           | POST   | Create an order                | ✅ Yes |
| `/api/orders/{id}/`      | DELETE | Cancel an order                | ✅ Yes |
| `/api/users/`            | POST   | Register a new user            | ❌ No |
| `/api/token/`            | POST   | Get access token (Login)       | ❌ No |

## 🛠 Deployment
This project is deployed on **Render**, ensuring seamless scalability and availability.

### **Using Render**
- Automatically deploys the API with **PostgreSQL** as the managed database.
- Handles environment variables securely.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
### 📌 Contact
For any questions, feel free to reach out:
📧 Email: klvnafriyie123@gmail.com
💼 LinkedIn: (https://linkedin.com/in/kelvin-afriyie-833546231/)
🔗 GitHub: (https://github.com/blackmoor01)

