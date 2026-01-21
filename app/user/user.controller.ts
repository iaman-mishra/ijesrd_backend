import asyncHandler from "express-async-handler";
import { Request, Response } from "express";
import { createResponse } from "@/common/helper/response.helper";
import * as userService from "./user.services";

export const getAllUser = asyncHandler(async (req: Request, res: Response) => {
  const skip = req.query.skip ? parseInt(req.query.skip as string) : undefined;
  const limit = req.query.limit
    ? parseInt(req.query.limit as string)
    : undefined;
  const result = await userService.getAllUser({}, { skip, limit });
  if (skip || limit) {
    const count = await userService.countItems();
    res.send(
      createResponse({
        count,
        users: result,
      }),
    );
    return;
  }
  res.send(createResponse(result));
});
