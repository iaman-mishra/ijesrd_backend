import mongoose, { Schema } from "mongoose";
import { IUser, UserRole } from "./user.dto";
import { hashPassword } from "@/common/services/passport-jwt.service";

const UserSchema = new Schema<IUser>(
  {
    name: { type: String },
    email: {
      type: String,
      required: true,
      unique: true,
      lowercase: true,
      trim: true,
    },
    active: { type: Boolean, required: false, default: true },
    role: {
      type: String,
      required: true,
      enum: Object.values(UserRole),
      default: UserRole.USER,
    },
    password: { type: String, required: true, select: false },
    refreshToken: { type: String, select: false },
    blocked: { type: Boolean, default: false },
    blockReason: { type: String },
    image: { type: String },
  },
  { timestamps: true },
);

UserSchema.pre("save", async function () {
  if (!this.isModified("password")) return;
  this.password = await hashPassword(this.password);
});

UserSchema.index({ email: 1 });

export default mongoose.model<IUser>("User", UserSchema);
