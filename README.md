#  Backend Template

A robust and scalable backend template built with **Node.js**, **Express**, and **TypeScript**. This project is designed to serve as a solid foundation for building RESTful APIs, specifically tailored for flexible enough for general purpose use.

It includes essential features like MongoDB integration, Swagger documentation, centralized error handling, and security best practices.

## 🚀 Features

- **TypeScript Compatible**: Built with TypeScript for static type checking and better developer experience.
- **Modular Architecture**: Organized structure with strictly separated concerns (Controllers, Services, DTOs, Routes).
- **Database Integration**: MongoDB connection via **Mongoose**.
- **API Documentation**: Integrated **Swagger UI** for automatic API documentation (`/api-docs`).
- **Security**:
  - **Rate Limiting** to prevent abuse.
  - **CORS** enabled.
  - **Bcrypt** for password hashing.
  - Secure HTTP headers.
- **Input Validation & DTOs**: Structured data transfer objects.
- **Error Handling**: Global error handling middleware.
- **Logging**: HTTP request logging using **Morgan**.
- **Environment Management**: Configuration via `dotenv`.

## 🛠️ Tech Stack

- **Runtime**: Node.js
- **Framework**: Express.js
- **Language**: TypeScript
- **Database**: MongoDB (Mongoose ODM)
- **Documentation**: Swagger UI Express
- **Tools**: Nodemon (dev), ESLint/Prettier (recommended)

## 📂 Project Structure

```
├── app/
│   ├── common/             # Shared resources
│   │   ├── dto/            # Data Transfer Objects
│   │   ├── helper/         # Helper functions
│   │   ├── middleware/     # Custom middleware (Error handler, Rate limit)
│   │   ├── services/       # Common services (Database, Email, etc.)
│   │   └── swagger/        # Swagger configuration
│   ├── user/               # User module (Controller, Service, Route)
│   └── routes.ts           # Main application router
├── dist/                   # Compiled JavaScript files
├── .env.development        # Development environment variables
├── index.ts                # Application entry point
├── package.json            # Dependencies and scripts
└── tsconfig.json           # TypeScript configuration
```

## ⚡ Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v16+ recommended)
- [MongoDB](https://www.mongodb.com/) (Local or Atlas connection)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd ijesrd_backend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

### Configuration

Create a `.env` file (or use `.env.development` for dev) in the root directory and configure the following variables:

```env
# Server Configuration
NODE_ENV=development
PORT=5000

# Database Configuration
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/IJESRD
```

### Running the Application

- **Development Mode** (with hot-reload):

  ```bash
  npm run dev
  ```

- **Build Project**:

  ```bash
  npm run build
  ```

- **Production Mode**:
  ```bash
  npm run prod
  ```

## 📚 API Documentation

Once the server is running (in development mode), you can access the interactive API documentation at:

```
http://localhost:5000/api-docs
```

## 🤝 Contributing

1.  Fork the project
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the [ISC License](LICENSE).
