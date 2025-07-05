from flask import Flask, request, jsonify, render_template, send_from_directory
import openai
import os
from datetime import datetime
import json
import logging

app = Flask(__name__, static_folder='static', template_folder='.')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/health')
def health_check():
    """Simple health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()})

@app.route('/api/info')
def app_info():
    """Returns basic application metadata"""
    return jsonify({
        'app': 'Resume & Cover Letter Generator',
        'version': '1.1.0',
        'language': 'Python (Flask)',
        'model': 'gpt-3.5-turbo',
        'status': 'running'
    })

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    try:
        data = request.json
        logging.info("Resume generation request received.")

        prompt = create_resume_prompt(data)

        if openai.api_key:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional resume writer. Create a well-formatted HTML resume that looks professional and modern. Use proper HTML structure with inline CSS for styling. Make it ATS-friendly and visually appealing."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            resume_html = response.choices[0].message.content
        else:
            resume_html = generate_demo_resume(data)

        return jsonify({'resume': resume_html})
    
    except Exception as e:
        logging.error(f"Error generating resume: {e}")
        return jsonify({'resume': generate_demo_resume(data)})

@app.route('/api/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    try:
        data = request.json
        logging.info("Cover letter generation request received.")

        prompt = create_cover_letter_prompt(data)

        if openai.api_key:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional career counselor. Write a compelling cover letter in HTML format with proper business letter structure. Make it personalized, professional, and engaging. Use inline CSS for styling."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            cover_letter_html = response.choices[0].message.content
        else:
            cover_letter_html = generate_demo_cover_letter(data)

        return jsonify({'coverLetter': cover_letter_html})

    except Exception as e:
        logging.error(f"Error generating cover letter: {e}")
        return jsonify({'coverLetter': generate_demo_cover_letter(data)})

def create_resume_prompt(data):
    prompt = f"""
    Create a professional resume in HTML format for the following person:

    Personal Information:
    - Name: {data['personalInfo']['fullName']}
    - Email: {data['personalInfo']['email']}
    - Phone: {data['personalInfo']['phone']}
    - Location: {data['personalInfo']['location']}
    - LinkedIn: {data['personalInfo']['linkedin']}

    Target Role: {data['targetRole']}

    Education:
    """
    for edu in data['education']:
        prompt += f"- {edu['degree']} from {edu['school']} ({edu['year']})"
        if edu['gpa']:
            prompt += f" - GPA: {edu['gpa']}"
        prompt += "\n"

    prompt += "\nWork Experience:\n"
    for exp in data['experience']:
        prompt += f"- {exp['title']} at {exp['company']} ({exp['duration']})\n"
        prompt += f"  {exp['description']}\n"

    prompt += f"\nSkills: {', '.join(data['skills'])}\n"

    prompt += """
    Please ensure the resume:
    - Has clean and professional typography
    - Uses a subtle blue and gray color palette
    - Is structured and ATS-compliant
    - Includes contact info at the top
    - Starts with a professional summary (if role provided)
    - Contains sections for Education, Experience, and Skills
    - Is visually appealing and modern
    """
    return prompt

def create_cover_letter_prompt(data):
    prompt = f"""
    Write a professional cover letter in HTML format for:

    Applicant:
    - Name: {data['personalInfo']['fullName']}
    - Email: {data['personalInfo']['email']}
    - Phone: {data['personalInfo']['phone']}
    - Address: {data['personalInfo']['address']}

    Job Information:
    - Company: {data['jobInfo']['company']}
    - Position: {data['jobInfo']['position']}
    - Hiring Manager: {data['jobInfo']['hiringManager']}

    Experience: {data['experience']}
    Skills: {data['skills']}
    Motivation: {data['motivation']}

    The letter should:
    - Use correct business letter formatting
    - Be personalized to the company and role
    - Emphasize relevant experience and skills
    - Include a strong intro and call to action
    - Be formatted in HTML with inline CSS
    """
    return prompt

# Demo resume and cover letter remain unchanged (from your original code)
# ---- generate_demo_resume() and generate_demo_cover_letter() functions stay as is ----

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
