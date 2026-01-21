import swaggerJsdoc from "swagger-jsdoc";

const options: swaggerJsdoc.Options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "IJESRD Backend API",
      version: "1.0.0",
      description: "API documentation for IJESRD Backend",
    },
    servers: [
      {
        url: "http://localhost:5000",
        description: "Development server",
      },
    ],
  },
  apis: ["./app/**/*.ts"],
};

export const swaggerSpec = swaggerJsdoc(options);
