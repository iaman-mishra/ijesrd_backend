import express from "express";
import * as userController from "./user.controller";

const userRoutes = express.Router();

userRoutes.get("/", userController.getAllUser);

export default userRoutes;