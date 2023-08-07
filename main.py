import openai
import streamlit as st
import subprocess

# Initialize OpenAI API and server base
openai.api_key = "EMPTY"
openai.api_base = "http://zanino.millennium.berkeley.edu:8000/v1"


# Function to get response from Gorilla Server
def get_gorilla_response(prompt, model):
    try:
        # Create a chat completion using OpenAI API
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        print("Response: ", completion)
        return completion.choices[0].message.content
    except Exception as e:
        print("An error occurred:", e)


# Function to extract code from output
def extract_code_from_output(output):
    code = output.split("code>>>:")[1]
    return code


# Function to execute generated code
def run_generated_code(file_path):
    command = ["python", file_path]
    try:
        # Run the generated code as a subprocess
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            st.success("Generated code executed successfully.")
            st.code(result.stdout, language="python")
        else:
            st.error("Generated code execution failed:")
            st.code(result.stderr, language="bash")
    except Exception as e:
        st.error("Error running generated code:", e)


# Set Streamlit layout
st.set_page_config(layout="wide")


# Main function
def main():
    st.markdown(
        """
        <style>
            .center-image {
                display: flex;
                justify-content: center;
            }
        </style>
        <a href="https://pythonpythonme.netlify.app/index.html">
        <div class="center-image">
        <img src="https://pythonpythonme.netlify.app/PythonPythonME.png" alt="Header image">
        </div>
        </a>
        <p></p>
        <p></p>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit app title and input prompt
    st.title("Gorilla LLM App 🦍‍🐒")
    input_prompt = st.text_area("Enter User prompt:")

    # Model selection dropdown
    model_options = ('gorilla-7b-hf-v1', 'gorilla-mpt-7b-hf-v0')
    option = st.selectbox('Select any model:', model_options)

    # Button to trigger Gorilla Magic
    if st.button("Generate"):
        if len(input_prompt) > 0:
            # Split app layout into two columns
            col1, col2 = st.columns([1, 1])

            # First column: Get Gorilla Server response
            with col1:
                result = get_gorilla_response(prompt=input_prompt, model=option)
                st.write(result)

            # Second column: Display generated code
            with col2:
                code_result = extract_code_from_output(result)
                if option == "gorilla-7b-hf-v1":
                    st.subheader("Output Generated")
                    st.code(code_result, language='python')
                elif option == "gorilla-mpt-7b-hf-v0":
                    lines = code_result.split('\\n')
                    for line in lines[:-1]:
                        st.code(line, language='python')

                file_path = f"generated_code_{option.replace('-', '_')}.py"
                with open(file_path, 'w') as file:
                    file.write(code_result)
                run_generated_code(file_path)

    st.markdown(
        '''
        <style>
            .center-image {
                display: flex;
                justify-content: center;
            }
            .follow-me {
                text-align: center;
            }
            .social-icons {
                display: flex;
                justify-content: center;
                list-style: none;
                padding: 0;
            }
            .social-icons li {
                margin: 0 10px;
            }
        </style>
        <body>
            <div class="center-image">
                <h4>Anoop Johny 🤖</h4>
            </div>
            <div class="center-image">
                <h4>Follow Me</h4>
            </div>
            <div class="center-image">
                <ul class="social-icons">
                    <li><a href="https://www.linkedin.com/in/anoop-johny-30a746181/"><img src="https://pythonpythonme.netlify.app/static/res/linkedin.png" width="55" height="55" alt="LinkedIn"></a></li>
                    <li><a href="https://github.com/flyfir248"><img src="https://pythonpythonme.netlify.app/static/res/github.png" width="55" height="55" alt="GitHub"></a></li>
                    <li><a href="https://pythonpythonme.netlify.app/index.html"><img src="https://pythonpythonme.netlify.app/static/res/web.png" width="55" height="55" alt="Website"></a></li>
                    <li><a href="https://medium.com/@anoopjohny2000"><img src="https://pythonpythonme.netlify.app/static/res/medium.png" width="55" height="55" alt="Medium"></a></li>
                    <li><a href="https://www.kooapp.com/profile/anoop2DEVLJ"><img src="https://www.kooapp.com/_next/static/media/logoKuSolidOutline.1f4fa971.svg" width="55" height="55" alt="The Koo App" width="55" height="55"></a></li>
                </ul>
            </div>
            <footer class="footer">
                <div class="container">
                    <div class="row">
                        <div class="center-image">
                            <p class="text-muted">© 2023-2024 PythonPythonME.</p>
                            <p>All rights reserved.</p>
                        </div>
                    </div>
                </div>
            </footer>
        </body>
        ''',
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
