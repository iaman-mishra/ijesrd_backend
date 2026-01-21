export enum UserRole {
  USER = "USER",
  ADMIN = "ADMIN",
}

export interface IUser {
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
