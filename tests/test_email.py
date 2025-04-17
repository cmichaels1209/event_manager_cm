import pytest
from unittest.mock import AsyncMock, patch
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

@pytest.mark.asyncio
async def test_send_markdown_email():
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }

    template_manager = TemplateManager()
    email_service = EmailService(template_manager=template_manager)

    with patch.object(email_service.smtp_client, "send_email", new=AsyncMock()) as mock_send:
        await email_service.send_user_email(user_data, 'email_verification')
        mock_send.assert_called_once()
