# Description
*Powered by Youtube APIs.	
This app is used for automatically adding ads for Youtube Live Stream.
On the app's panel, you will see three sections: Select secret files, Enter broadcast ID and Set interval times in seconds.
![alt text](https://github.com/YuHao-Tian/Automate-Ads-YotubeLiveStream/blob/main/exe.jpg?raw=true)

What is secret files? Secret files, also known as OAuth 2.0 Client IDs, are a part of the authentication and authorization process used in the YouTube API. OAuth 2.0 is an open standard protocol that allows applications to access user data from various services, such as YouTube, without directly handling the user's credentials.

How could I get my own secret files?
Get access to this tutorial link: https://www.youtube.com/watch?v=irhhMLKDBZ8

Where can I find you broadcast ID?
There are multiples way you can find your broadcast ID. The simplest way is checking your Live Stream page Link(URL), which format is 
https://studio.youtube.com/video/YOUR_BROAD_CAST_ID/livestreaming. So you can just copy and past your YOUR_BROAD_CAST_ID into this app.

What is suitable interval times?
There's not a specific boundary of youtube add cue points API. However, I recommand setting interval times larger than 60 in real live stream.

How could I check if I operate it successfully?
After you finish three sections, click"click on me" button, you will redirect to web page and select your live broadcast account and channel. After that, if the app didn't show any pop-ups alerts, it indicates you operate this app succesfully!

**After you operate this app succesfully, you will get a reponse.txt file under the same folder of your app(or your secret file's folder). You can check added cue points in this file. After each live stream, deleting this reponse.txt is recommanded.

!!Notice: Because the limitation of tkinter, the app appears dead or lagging when is used. This is a normal state and do not need to worry about it's availability.

If you have any advice and question, feel free to contact me: yuhaotian2022@gmail.com
