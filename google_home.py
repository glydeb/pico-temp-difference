import os
import dialogflow_v2 as dialogflow
from google.oauth2 import service_account

# Load your Google Cloud credentials
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/credentials.json'
)

# Create a Dialogflow client
session_client = dialogflow.SessionsClient(credentials=credentials)

# Define the Dialogflow project ID
project_id = 'your-project-id'

def report_temperature(return_temp, supply_temp):
    # Create a session ID
    session_id = 'your-unique-session-id'
    session = session_client.session_path(project_id, session_id)

    # Define the intent you want to trigger
    intent_name = 'your-intent-name' 

    # Construct the Dialogflow request
    text_input = dialogflow.types.TextInput(
        text=f'Return air temperature is {return_temp} degrees Fahrenheit, and supply air temperature is {supply_temp} degrees Fahrenheit.',
        language_code='en-US',
    )
    query_input = dialogflow.types.QueryInput(text=text_input)

    # Send the request to Dialogflow
    response = session_client.detect_intent(
        session=session, query_input=query_input
    )

    # Handle the response from Dialogflow