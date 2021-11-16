# Example 1: Creates service object, sends initial message, and
# receives response.
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():

    return render_template("index.html")

@app.route('/result',methods = ['POST'])
def result():
   if request.method == 'POST':
        # Create Assistant service object.
        authenticator = IAMAuthenticator('A_xwvOFfKWbhLn7ZkEtmqd8bnPRXEunl74Crx1uM5jFS')  # replace with API key
        assistant_id = '3c315324-f29b-4b53-b663-8c3ea46122ce'
        assistant = AssistantV2(
           version='2021-11-14',
           authenticator=authenticator
        )
        assistant.set_service_url('https://api.kr-seo.assistant.watson.cloud.ibm.com')

        sessres = assistant.create_session(
           assistant_id=assistant_id
        ).get_result()

        response = assistant.message(
           assistant_id=assistant_id,
           session_id=sessres['session_id'],
           input={
               'message_type': 'text',
               'text': '초기세팅'
           }
        ).get_result()

        # Print the output from dialog, if any. Supports only a single
        # text response.
        if response['output']['generic']:
            if response['output']['generic'][0]['response_type'] == 'text':
                result = response['output']['generic'][0]['text']
        return result

if __name__ == '__main__':
    app.run(debug=True)