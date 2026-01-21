import { ProjectionType, QueryOptions } from "mongoose";
import { IUser } from "./user.dto";
import userSchema from "./user.schema";

export const getAllUser = async (
  projection?: ProjectionType<IUser>,
  options?: QueryOptions<IUser>,
) => {
  const result = await userSchema.find({}, projection, options).lean();
  return result;
};

export const countItems = () => {
  return userSchema.countDocuments();
};
