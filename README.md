#Facebook Message Data Analyzer#

This tool allows you to do some basic analytics on your Facebook Messaging History. Curious who is the top contributor in a particular group chat? This tool can answer that question.

Features Include:
* Finding the top contributors in a group chat (how many messages have been sent by a particular person in a particular chat).
* Getting the complete chat history of a single user.

Features that will be Implemented Soon:
* Sentiment Score analysis: see who is the most positive/negative in a group chat.

##Setup##
The setup for this tool is admittedly pretty annoying to setup.

1. Navigate to facebook.com and then to your account settings. Click on the general tab and then at the bottom of the page you should see an icon to request your facebook data. Once you click this button, facebook will send you an email saying that they are processing your request. After 2-3 hours, you should get another email with a link to all of your facebook data ever (nuts, I know).
![alt text](screenshots/request.jpg)
2. Clone this directory in the directory of your downloaded facebook files.
3. `pip install -r requirements.txt`
4. The way facebook stores your messages is in an extremely annoying html file. So the first part of this tool converts the annoying html to usable JSON (pickle) we can actually do stuff with. Run the following command:
```
python convert.py html/messages.htm output.txt
```
Assuming you've done this correctly, this part can take a while. For my 200 mb messages.htm file, it took nearly an hour.
5. Alright, now we're ready to have some fun, run the following command:
`python generate.py output.txt`
