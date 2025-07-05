# Resume & Cover Letter Writer

A professional AI-powered resume and cover letter builder with a beautiful, human-like design.

## Features

- **AI-Powered Content Generation**: Uses GPT-3.5/4 to create professional, tailored content
- **Beautiful UI**: Modern, responsive design that doesn't look AI-generated
- **PDF Export**: High-quality PDF generation for both resumes and cover letters
- **Real-time Preview**: See your documents as you build them
- **Professional Templates**: Clean, ATS-friendly formatting
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile

## Technology Stack

### Frontend
- **HTML5**: Semantic markup for accessibility
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Interactive functionality and form handling
- **Font Awesome**: Professional icons
- **jsPDF**: Client-side PDF generation

### Backend
- **Python Flask**: Lightweight web framework
- **OpenAI API**: GPT-3.5/4 for content generation
- **Gunicorn**: Production WSGI server

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (optional - demo mode available)

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key** (optional):
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
   
   Or create a `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

### VS Code Setup

1. **Open the project folder in VS Code**

2. **Install Python extension** if not already installed

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure VS Code Python interpreter**:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your virtual environment

6. **Run the application**:
   - Open terminal in VS Code (`Ctrl+`` `)
   - Run: `python app.py`

## File Structure

```
resume-cover-letter-writer/
├── app.py                 # Flask backend application
├── index.html            # Main HTML file
├── requirements.txt      # Python dependencies
├── package.json         # Project metadata
├── README.md           # This file
└── static/
    ├── css/
    │   └── style.css    # Main stylesheet
    └── js/
        └── script.js    # Frontend JavaScript
```

## Usage

### Building a Resume

1. **Navigate to Resume Builder**: Click "Build Resume" or use the navigation menu
2. **Fill Personal Information**: Enter your name, email, phone, location, and LinkedIn
3. **Add Target Role**: Specify the position you're applying for
4. **Add Education**: Include your degrees, schools, and graduation years
5. **Add Experience**: Detail your work history with descriptions
6. **Add Skills**: List your relevant technical and soft skills
7. **Generate Resume**: Click "Generate Resume" to create your document
8. **Download PDF**: Click "Download PDF" to save your resume

### Creating a Cover Letter

1. **Navigate to Cover Letter Builder**: Click "Write Cover Letter" or use the navigation menu
2. **Personal Information**: Enter your contact details
3. **Job Information**: Specify the company, position, and hiring manager
4. **Content Fields**: Describe your experience, skills, and motivation
5. **Generate Cover Letter**: Click "Generate Cover Letter"
6. **Download PDF**: Save your cover letter as a PDF

## Customization

### Styling
- Edit `static/css/style.css` to modify colors, fonts, and layout
- The design uses CSS custom properties for easy theme changes
- Responsive breakpoints are included for mobile optimization

### AI Prompts
- Modify the prompt functions in `app.py` to change AI behavior
- Adjust `temperature` parameter for more/less creative output
- Customize system messages for different writing styles

### Features
- Add new form fields by updating both HTML and JavaScript
- Extend the API with additional endpoints
- Implement user authentication and data persistence

## Production Deployment

### Using Gunicorn
```bash
gunicorn app:app --bind 0.0.0.0:5000
```

### Environment Variables
Set these in production:
- `OPENAI_API_KEY`: Your OpenAI API key
- `FLASK_ENV`: Set to "production"

### Security Considerations
- Use HTTPS in production
- Implement rate limiting for API endpoints
- Validate and sanitize all user inputs
- Store API keys securely

## Demo Mode

The application includes a demo mode that works without an OpenAI API key:
- Generates professional-looking documents using templates
- Includes all form functionality and PDF export
- Perfect for testing and development

## Browser Compatibility

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the console for error messages
2. Ensure all dependencies are installed
3. Verify your OpenAI API key (if using AI features)
4. Check that the Flask server is running on port 5000

## Future Enhancements

- Multiple resume templates
- Cover letter templates
- User accounts and document storage
- Integration with job boards
- Advanced formatting options
- Multi-language support
