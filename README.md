# IT Consultancy Booking System

A Flask-based consultancy booking and payment system with PayU integration, designed for Vercel deployment.

## Features

- Service listing and booking
- Real-time slot availability
- PayU payment gateway integration
- User account management
- Legal pages (Terms & Conditions, Refund Policy)
- Responsive design with shadcn-like styling and Uber-inspired design system

## Tech Stack

- Flask (Python)
- TailwindCSS (via CDN)
- HTMX (optional)
- PayU Payment Gateway
- SQLite (development) / PostgreSQL (production)
- Vercel for deployment

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on `.env.example` and configure your environment variables
5. Run the application:
   ```bash
   flask run
   ```

## Deployment to Vercel

1. Push your code to a Git repository
2. Connect your repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy!

## Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel configuration
├── .env.example        # Environment variables template
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Home page
│   ├── services.html   # Services listing
│   ├── booking.html    # Service booking
│   ├── payment_success.html
│   ├── payment_failed.html
│   ├── terms.html
│   ├── refund_policy.html
│   ├── login.html
│   └── account.html
└── static/             # Static assets (if any)
```

## PayU Integration

The system integrates with PayU Payment Gateway for processing payments of ₹100,000+ securely. The integration includes:

- Secure hash generation for payment requests
- Callback verification for payment confirmation
- Automatic slot booking upon successful payment

## Legal Compliance

The system includes required legal pages for PayU compliance:
- Terms & Conditions
- Refund Policy
