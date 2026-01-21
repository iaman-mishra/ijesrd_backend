import express, { type Request, type Response } from "express";
import cors from "cors";
import http from "http";
import morgan from "morgan";

import swaggerUi from "swagger-ui-express";
import { initDB } from "@/common/services/database.service";
import { swaggerSpec } from "@/common/swagger/swagger.config";
import errorHandler from "@/common/middleware/error-handler.middleware";
import { globalLimiter } from "@/common/middleware/rate-limit.middleware";
import router from "@/routes";
import { loadConfig } from "@/common/helper/config.helper";

loadConfig();

const port = Number(process.env.PORT) ?? 5000;

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(morgan("dev"));
app.use(globalLimiter);

const initApp = async (): Promise<void> => {
  await initDB();
  app.use("/api", router);

  if (process.env.NODE_ENV !== "production") {
    app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));
  }

  app.get("/", (req: Request, res: Response) => {
    res.send("API Status: OK");
  });

  app.use(errorHandler);
  http.createServer(app).listen(port, () => {
    console.log("Server is running on port", port);
  });
};

initApp();
