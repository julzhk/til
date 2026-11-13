Either use this service : https://app.burnerapp.com
or...apparently Twilio does this neatly: 

You can forward incoming calls from your Twilio number to another phone ==using [Twilio Studio](https://www.google.com/search?q=Twilio+Studio) or a [Twilio Function](https://www.google.com/search?q=Twilio+Function)==. [[1](https://www.twilio.com/code-exchange/simple-call-forwarding), [2](https://www.twilio.com/docs/studio/tutorials/how-to-forward-calls)]

Option 1: Forward Calls Using [Twilio Studio](https://www.google.com/search?q=Twilio+Studio) (No-Code Method)

- Log in to the [Twilio Console](https://www.google.com/search?q=Twilio+Console).

- Go to **Studio** > **Flows** and click the **+** (plus) icon to create a new flow.

- Select **Call Forwarding** from the template list (or start from scratch and use the **Connect Call To**widget).

- Click on the forward widget and enter your **destination phone number** in [E.164 format](https://help.twilio.com/articles/115016033048-Forward-Incoming-Calls-with-Twilio-Studio) (e.g., `+1`followed by your 10-digit number).

- Click **Save**, then click **Publish** at the top of the flow.

- Navigate to **Phone Numbers** > **Manage Numbers** and select your Twilio phone number.

- Scroll down to the **Voice & Fax** section.

- Under **A Call Comes In**, select **Studio Flow**, choose your newly created call forwarding flow, and click **Save**. [[1](https://www.twilio.com/docs/studio/tutorials/how-to-forward-calls), [2](https://www.youtube.com/watch?v=4-PV4O5PCtc&t=40), [3](https://help.twilio.com/articles/115016033048-Forward-Incoming-Calls-with-Twilio-Studio), [4](https://www.youtube.com/watch?v=atshc8I-AjA&t=22)]