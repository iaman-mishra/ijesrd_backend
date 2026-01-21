import { BaseSchema } from "@/common/dto/base.dto";

export enum UserRole {
  USER = "USER",
  ADMIN = "ADMIN",
}

export interface IUser extends BaseSchema{
  name: string;
  email: string;
  password: string;
  role: UserRole;
  active?: boolean;
  blocked?: boolean;
  blockReason?: string;
  image?: string;
  refreshToken?: string;
}
