# TwitterBot
## Why use a 3-legged protocol over a 2-legged one?
A 3-legged protocol is needed here because there is a third party application involved (the Bot) 
that needs to get a request token from me to generate an access token that allows it to imporsonate me on Twitter

## How to Change the Number of Training Epochs
Simply change the value of the variable 'nsteps' on line 41 of the bot.py file 

## How to Tweet
I recomment running the code here: https://colab.research.google.com/drive/1p0J_XpDgmW9XTUowpifA26oy0WTyNcir?usp=sharing .There are instructions commented. First, you will need to run the first segment of code in the notebook to install packages. After this, restart the runtime. Then, if you would like to retrain the model run all of the remaining code except the one that includes the comment "# run this segment only if you are not retraining the model). If you would not like to retrain the model, run all of the remaining code except the 3 that include the comment "#ONLY RUN THIS SEGMENT IF YOU WISH TO RETRAIN THE MODEL".
If you would like to run it in a terminal, you can do that witht he python file I have included, but that will have to run on a CPU and retrain the model (i have not fully tested this and would much prefer it if you ran it in Google Colab). 

## How to perform Botometer Analysis
run 'python bot_rating.py' wherever the file 'bot_rating.py' is located. The function prints out the returned json. (the value to the 'english' key is the bot rating)

## Return values 
My function returned the following object:
{'cap': {'english': *0.9158377984126878*, 'universal': 0.8859379719494699}, 'display_scores': {'english': {'astroturf': 0.4, 'fake_follower': 4.1, 'financial': 2.4, 'other': 4.8, 'overall': 4.8, 'self_declared': 4.2, 'spammer': 2.8}, 'universal': {'astroturf': 0.0, 'fake_follower': 4.2, 'financial': 2.2, 'other': 4.6, 'overall': 4.6, 'self_declared': 4.6, 'spammer': 2.8}}, 'raw_scores': {'english': {'astroturf': 0.07, 'fake_follower': 0.83, 'financial': 0.48, 'other': 0.96, 'overall': 0.96, 'self_declared': 0.84, 'spammer': 0.56}, 'universal': {'astroturf': 0.0, 'fake_follower': 0.85, 'financial': 0.4405833333333333, 'other': 0.9266666666666665, 'overall': 0.9266666666666665, 'self_declared': 0.92, 'spammer': 0.55}}, 'user': {'majority_lang': 'en', 'user_data': {'id_str': '1488596326455693314', 'screen_name': 'JackOCo64130255'}}}

The bolded number after 'english' is my bot rating of 0.916. It did not fool the botometer at all because it's responses were pretty much gibberish. I think I should have trained my model more. 

## Proposal
I'm not sure about the ethics of restricting the uses of bots on social media. I have seen some bots used that are entertaining (Twitter @NFL_Scorigami), and I don't see why this should be taken down. However, for political content, I can see how bots may be harmful to public viewers. People's opinions can be easily swayed by the words of their peers, so I think it may be necessary for bot use to be moderated. However, I think that people themselves are as good at identifying bots as the Botometer is based on their social media experience, so i don't think that the Botometer can be implemented as a moderation tool yet. 

