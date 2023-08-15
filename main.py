import os
import openai
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.llms import OpenAI
from langchain.utilities.zapier import ZapierNLAWrapper

load_dotenv()
# Set environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
ZAPIER_NLA_API_KEY = os.environ.get("ZAPIER_NLA_API_KEY")

# Initialize resources and cache them
@st.cache_resource()
def initialize_resources(openai_api_key, zapier_nla_api_key):
    # Initialize required resources and return an agent.
    llm = OpenAI(temperature=0)
    zapier = ZapierNLAWrapper()
    toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
    agent = initialize_agent(
        toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent

st.title("Zapier NLA + Google Docs")

# Add a temperature slider
temperature = st.slider("Set temperature for OpenAI", min_value=0.0, max_value=1.0, value=0.9, step=0.1)
action = st.selectbox("Select a Zapier NLA action:", ['',"Create a Google Doc", "Email a Google Doc"])

if action == "Email a Google Doc":
    topic = st.text_input("What is the Doc about?")
    email = st.text_input("Which Email do you want to send to?")
elif action == "Create a Google Doc":
    topic = st.text_input("What is the Doc about?")

def generate_response(prompt):
    print('Attempting to generate response w/ given prompt: ', prompt)
    response = openai.ChatCompletion.create(
        temperature=temperature,
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant. Generate content for a Google Doc based on the topic."},
                {"role": "user", "content": prompt}]
    )
    output_response = response.choices[0]['message']['content']
    print("The response is: ", output_response)
    return output_response

# When the "Submit" button is clicked

if st.button("Submit"):
    response= generate_response(topic)
    # Add input fields for action
    if action == "Create a Google Doc":
        agent = initialize_resources(OPENAI_API_KEY, ZAPIER_NLA_API_KEY)
        response = generate_response(topic)
        st.write(response)
        action = agent.run(topic + "Create a new google doc and use this as the body content:" + response + ". Then give me a link to the Google Doc you created." )
        st.write(action)
    elif action == "Email a Google Doc":
        agent = initialize_resources(OPENAI_API_KEY, ZAPIER_NLA_API_KEY)
        response = generate_response(topic)
        st.write(response)
        action = agent.run(topic + " recipient: " +  email + " here is the content you need to add" )
        st.write(action)