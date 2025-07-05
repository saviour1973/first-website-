from flask import Flask, request, jsonify, render_template, send_from_directory
import openai
import os
from datetime import datetime
import json

app = Flask(__name__, static_folder='static', template_folder='.')

# Configure OpenAI API key
# You need to set your OpenAI API key as an environment variable
# export OPENAI_API_KEY="your-api-key-here"
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    try:
        data = request.json
        
        # Create a prompt for the AI
        prompt = create_resume_prompt(data)
        
        # Generate resume using OpenAI
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
            # Fallback to demo content if no API key
            resume_html = generate_demo_resume(data)
        
        return jsonify({'resume': resume_html})
        
    except Exception as e:
        print(f"Error generating resume: {e}")
        # Return demo content on error
        return jsonify({'resume': generate_demo_resume(data)})

@app.route('/api/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    try:
        data = request.json
        
        # Create a prompt for the AI
        prompt = create_cover_letter_prompt(data)
        
        # Generate cover letter using OpenAI
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
            # Fallback to demo content if no API key
            cover_letter_html = generate_demo_cover_letter(data)
        
        return jsonify({'coverLetter': cover_letter_html})
        
    except Exception as e:
        print(f"Error generating cover letter: {e}")
        # Return demo content on error
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
    
    Please create a modern, professional resume in HTML format with:
    1. Clean, readable typography
    2. Professional color scheme (blues and grays)
    3. Proper sections and hierarchy
    4. ATS-friendly structure
    5. Inline CSS styling
    6. Contact information at the top
    7. Professional summary if target role is provided
    8. Well-organized sections for education, experience, and skills
    
    Make it look like it was created by a professional resume writer, not AI.
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
    
    Create a compelling cover letter that:
    1. Follows proper business letter format
    2. Is personalized to the company and role
    3. Highlights relevant experience and skills
    4. Shows genuine interest and motivation
    5. Has a professional tone
    6. Is formatted in HTML with inline CSS
    7. Includes proper date and addressing
    8. Has a strong opening and closing
    
    Make it sound natural and human-written, not AI-generated.
    """
    
    return prompt

def generate_demo_resume(data):
    """Generate a demo resume when AI is not available"""
    personal_info = data['personalInfo']
    education = data['education']
    experience = data['experience']
    skills = data['skills']
    target_role = data['targetRole']
    
    contact_info = []
    if personal_info['email']:
        contact_info.append(personal_info['email'])
    if personal_info['phone']:
        contact_info.append(personal_info['phone'])
    if personal_info['location']:
        contact_info.append(personal_info['location'])
    
    resume_html = f"""
    <div class="generated-content">
        <h1>{personal_info['fullName']}</h1>
        <div class="contact-info">
            {' • '.join(contact_info)}
            {f'<br><a href="{personal_info["linkedin"]}" style="color: #1e40af;">{personal_info["linkedin"]}</a>' if personal_info['linkedin'] else ''}
        </div>
        
        {f'<h2>Objective</h2><p>Seeking a {target_role} position where I can leverage my skills and experience to drive meaningful impact and contribute to organizational success.</p>' if target_role else ''}
        
        {f'<h2>Education</h2>' if education else ''}
        {''.join([f'<div style="margin-bottom: 1rem;"><h3>{edu["degree"]}</h3><p style="margin: 0; color: #6b7280;">{edu["school"]} • {edu["year"]}{f" • GPA: {edu["gpa"]}" if edu["gpa"] else ""}</p></div>' for edu in education])}
        
        {f'<h2>Professional Experience</h2>' if experience else ''}
        {''.join([f'<div style="margin-bottom: 1.5rem;"><h3>{exp["title"]}</h3><p style="margin: 0; color: #6b7280; font-weight: 500;">{exp["company"]} • {exp["duration"]}</p><p style="margin-top: 0.5rem;">{exp["description"]}</p></div>' for exp in experience])}
        
        {f'<h2>Skills</h2><p>{", ".join(skills)}</p>' if skills else ''}
    </div>
    """
    
    return resume_html

def generate_demo_cover_letter(data):
    """Generate a demo cover letter when AI is not available"""
    personal_info = data['personalInfo']
    job_info = data['jobInfo']
    experience = data['experience']
    skills = data['skills']
    motivation = data['motivation']
    
    current_date = datetime.now().strftime('%B %d, %Y')
    
    cover_letter_html = f"""
    <div class="generated-content">
        <div style="margin-bottom: 2rem;">
            <h1 style="font-size: 1.5rem; margin-bottom: 0.5rem;">{personal_info['fullName']}</h1>
            <div class="contact-info">
                {personal_info['address']}<br>
                {personal_info['email']}<br>
                {personal_info['phone']}
            </div>
        </div>
        
        <div style="margin-bottom: 2rem;">
            <p>{current_date}</p>
        </div>
        
        <div style="margin-bottom: 2rem;">
            <p>{'Dear ' + job_info['hiringManager'] + ',' if job_info['hiringManager'] else 'Dear Hiring Manager,'}</p>
        </div>
        
        <p>I am writing to express my strong interest in the {job_info['position']} position at {job_info['company']}. {motivation if motivation else f'I am excited about the opportunity to contribute to your team and help drive the company\'s continued success.'}</p>
        
        {f'<p>In my professional experience, {experience} These experiences have prepared me well for the challenges and opportunities that come with the {job_info["position"]} role.</p>' if experience else ''}
        
        {f'<p>My technical skills include {skills}, which align well with the requirements for this position. I am confident that these abilities, combined with my passion for excellence, make me a strong candidate for your team.</p>' if skills else ''}
        
        <p>I am particularly drawn to {job_info['company']} because of its reputation for innovation and commitment to excellence. I would welcome the opportunity to discuss how my background and enthusiasm can contribute to your team's success.</p>
        
        <p>Thank you for considering my application. I look forward to hearing from you soon.</p>
        
        <div style="margin-top: 2rem;">
            <p>Sincerely,</p>
            <p style="font-weight: 600; margin-top: 0.5rem;">{personal_info['fullName']}</p>
        </div>
    </div>
    """
    
    return cover_letter_html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
