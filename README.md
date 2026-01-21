# IJESRD Backend API

This is the backend API for the IJESRD (International Journal of Engineering Science Research and Development) platform. It provides the core services, database connectivity, and API endpoints for the application.

## 🚀 Technologies

- **Runtime**: Node.js
- **Framework**: Express.js
- **Language**: TypeScript
- **Database**: MongoDB (via Mongoose)
- **Documentation**: Swagger UI
- **Security & Utils**:
  - `bcrypt` for password hashing
  - `cors` for Cross-Origin Resource Sharing
  - `express-rate-limit` for API rate limiting
  - `morgan` for HTTP request logging

## 🛠 Prerequisites

Ensure you have the following installed on your machine:

- [Node.js](https://nodejs.org/) (v16 or higher recommended)
- [MongoDB](https://www.mongodb.com/) (Local or Atlas)

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd ijesrd_backend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add the following configuration:
   ```env
   PORT=5000
   MONGODB_URI=mongodb://localhost:27017/ijesrd_db
   NODE_ENV=development
   ```

## 🏃‍♂️ Running the Server

### Development Mode

Runs the server with `nodemon` for hot-reloading.

```bash
npm run dev
```

### Build

Compiles TypeScript code to JavaScript in the `dist` folder.

```bash
npm run build
```

### Production Mode

Runs the compiled JavaScript from the `dist` folder.

```bash
npm run prod
```

## 📖 API Documentation

The API documentation is auto-generated using Swagger.

- **URL**: `http://localhost:5000/api-docs`
- **Desc**: Access interactive API documentation and test endpoints directly.

## 📂 Project Structure

```
ijesrd_backend/
├── app/
│   ├── common/           # Shared resources (middleware, services, swagger config)
│   ├── user/             # User module (controllers, models, services)
│   └── routes.ts         # Main router aggregation
├── index.ts              # Entry point
├── package.json          # Dependencies and scripts
└── tsconfig.json         # TypeScript configuration
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
