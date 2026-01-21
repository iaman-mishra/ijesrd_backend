import mongoose, { Schema } from "mongoose";
import { IUser, UserRole } from "./user.dto";
import { hashPassword } from "@/common/services/passport-jwt.service";

const UserSchema = new Schema<IUser>(
  {
    name: {
      type: String,
      required: true,
      trim: true,
    },

    email: {
      type: String,
      required: true,
      lowercase: true,
      trim: true,
      index: { unique: true },
    },

    password: {
      type: String,
      required: true,
      select: false,
    },

    role: {
      type: String,
      enum: Object.values(UserRole),
      default: UserRole.USER,
      required: true,
    },

    active: {
      type: Boolean,
      default: true,
    },

    blocked: {
      type: Boolean,
      default: false,
    },

    blockReason: {
      type: String,
      required: function (this: IUser) {
        return this.blocked === true;
      },
    },

    refreshToken: {
      type: String,
      select: false,
    },

    image: {
      type: String,
    },
  },
  { timestamps: true },
);

UserSchema.pre("save", async function () {
  if (!this.isModified("password")) return;
  this.password = await hashPassword(this.password);
});

export default mongoose.model<IUser>("User", UserSchema);
