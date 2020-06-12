Sentiment Analysis using Twitter’s Sampled Stream v1.

Exploring through recent tweets for the newly launched PlayStation5, I came across a lot of mixed reviews. This made me wonder if we can segregate good reviews from the bad. Twitter users now send over 500 million tweets every day. These numbers keep growing rapidly.  The tweets posted by a user are immediately available to his direct followers and can be quickly disseminated through the network via retweeting. Each tweet, with at most 280 characters can server as a good medium to gather product reviews for a company that is actively interested in getting customer feedback. 

After a bit of research, I found out that Twitter provides API functions to facilitate third-party users to access this data through developer accounts. The stream API provides almost real-time access to Twitter’s global stream of public tweets. For this project I wanted to make use of the Filtered Stream that would allow me to set rules, but that didn’t work as planned as the API is not currently available to new users. I ended up using Sampled Stream. 

The sampled stream endpoint allows developers to stream about 1% of all new public Tweets as they happen. You can connect no more than one client per session and can disconnect and reconnect no more than 50 times per 15-minute window.

This did not help accomplish my original plan to filter tweets based on a rule. So, for this project I will instead just try performing Sentiment Analysis using AWS Comprehend on some of the tweets that I am able to capture using a small python program. 

AWS Comprehend Service

AWS comprehend uses NLP to extract the insight about the content without needing any preprocessing requirements. It is capable of recognizing Entities, Languages, Sentiments, Key Phrases and other common elements of the given text or the document. One of the common use case of AWS Comprehend is to analyze the social media feed about your product and take necessary actions upon analyzing users valid sentiments.

Before going ahead, you will need to create a new app under twitter developer account. This will provide you with Consumer API keys i.e. API key and API secret key. You would also need your AWS access key and secret key to access AWS Comprehend service from your account.

I am using AWS Free Tier, that provides free sentiment analysis API for 50K units of text (5M characters) along with six other APIs Key Phrase Extraction, Entity Recognition, Language Detection, Syntax Analysis, Custom Entities, and Custom Classification) for the first 12 months. 

If you are outside free tier, this will cost money! Based on AWS’s pricing structure, 1 ,000 tweets will cost around 30 cents.

The output of the program will look something like this:

tweet-id
sentiment


I have chosen to hide the tweet text for privacy concerns. The screenshot below shows the tweet id followed by its sentiment.
 

In my next project I will try using the Filtered stream as soon as I get access to the API and plot a sentiment graph on a topic like PlayStation5.
