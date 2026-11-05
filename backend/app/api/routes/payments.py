import hashlib, hmac
from fastapi import APIRouter, HTTPException, Request
from app.core.config import settings
router = APIRouter()
@router.post("/razorpay/webhook")
async def razorpay_webhook(request: Request):
    raw_body = await request.body()
    signature = request.headers.get("X-Razorpay-Signature", "")
    secret = settings.RAZORPAY_WEBHOOK_SECRET
    if not secret:
        raise HTTPException(status_code=503, detail="Payment webhook is not configured")
    expected = hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise HTTPException(status_code=400, detail="Invalid webhook signature")
    # TODO: persist event ID with a unique constraint, then process idempotently.
    return {"received": True}
