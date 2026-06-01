def validate_webhook_id(webhook_id):
    if not isinstance(webhook_id, str) or not webhook_id:
        raise ValueError("Invalid webhook ID. It must be a non-empty string.")
    # Additional validation logic can be added here
