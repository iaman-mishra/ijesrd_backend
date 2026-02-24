# app/core/email.py

from pathlib import Path
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import SecretStr, NameEmail, EmailStr
from typing import List
from app.core.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=SecretStr(settings.MAIL_PASSWORD),
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / "templates",
)


async def send_email(
    recipients: List[EmailStr],
    subject: str,
    template_name: str,
    template_body: dict,
):
    formatted_recipients: List[NameEmail] = []

    for recipient in recipients:
        formatted_recipients.append(
            NameEmail(
                name=str(recipient.split("@")[0]),
                email=str(recipient),
            )
        )

    message = MessageSchema(
        subject=subject,
        recipients=formatted_recipients,
        template_body=template_body,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name=template_name)
