# Noa - AI-Powered Social Media Automation Platform

Noa is a Flask-based web application for social media automation, featuring AI-powered content creation, scheduling, and engagement management.

## Features

- **AI Content Creation**: Generate engaging social media content with AI intelligence
- **AI Engagement**: Automatically reply to comments using smart AI agents
- **Multi-Platform Support**: LinkedIn, YouTube, Facebook, Instagram, Twitter
- **Email Subscription System**: Collect and manage user subscriptions
- **Contact Form**: Handle user inquiries and support requests
- **Responsive Design**: Modern, mobile-friendly interface
- **Database Integration**: SQLite database for data persistence

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Icons**: SVG icons and custom graphics

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Updated_Chnage
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
Updated_Chnage/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── noa_database.db       # SQLite database (created automatically)
├── static/               # Static files
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   └── images/          # Images and icons
└── templates/            # HTML templates
    ├── index.html       # Home page
    ├── features.html    # Features page
    ├── pricing.html     # Pricing page
    ├── about.html       # About page
    ├── contact.html     # Contact page
    ├── 404.html         # 404 error page
    └── 500.html         # 500 error page
```

## Routes

- `/` - Home page
- `/features` - Features overview
- `/pricing` - Pricing plans
- `/about` - About Noa
- `/contact` - Contact form
- `/api/subscribe` - Email subscription endpoint (POST)
- `/api/contact` - Contact form endpoint (POST)

## Database Schema

The application automatically creates the following tables:

### Subscriptions Table
- `id` (INTEGER PRIMARY KEY)
- `email` (TEXT UNIQUE)
- `created_at` (TIMESTAMP)

### Contact Messages Table
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT)
- `email` (TEXT)
- `message` (TEXT)
- `created_at` (TIMESTAMP)

## Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key (defaults to 'noa-secret-key-2024')
- `DATABASE`: Database file path (defaults to 'noa_database.db')

### Customization
1. **Branding**: Update logo images in `static/images/`
2. **Styling**: Modify CSS in `static/css/`
3. **Content**: Edit HTML templates in `templates/`
4. **Functionality**: Extend Flask routes in `app.py`

## Development

### Adding New Features
1. Create new routes in `app.py`
2. Add corresponding templates in `templates/`
3. Update navigation links
4. Test thoroughly

### Database Changes
1. Modify the `init_db()` function in `app.py`
2. Delete the existing database file
3. Restart the application to recreate tables

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set `SECRET_KEY` environment variable
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure reverse proxy (e.g., Nginx)
4. Set up SSL certificates

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## API Endpoints

### POST /api/subscribe
Subscribe to newsletter
```json
{
  "Newsletter-Email-2": "user@example.com"
}
```

### POST /api/contact
Submit contact form
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, I have a question..."
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

© 2024 Noa. All Rights Reserved.

## Support

For support and questions, please contact us through the contact form on the website or email support@noa.com.

---

**Built with ❤️ for social media automation** 