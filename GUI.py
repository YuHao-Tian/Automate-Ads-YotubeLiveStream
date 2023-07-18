import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

window = tk.Tk()
window.title("YouTube API App")

# Example: Adding an entry field
# entry_2 = tk.Entry(window)
# interval = entry_2.pack()
# if (interval != None):
#     interval = float(interval)


# Example: Adding a button to trigger the API call


start_time = 180000


def youtube_api_function():
    global start_time
    # global interval
    broadcast_ID = a.get()
    Interval = int(b.get())
    # global textN
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json",
        scopes=["https://www.googleapis.com/auth/youtube.force-ssl"]
    )
    flow.run_local_server(
        port=8088, prompt="consent", authorization_prompt_message=""
    )
    credentials = flow.credentials

    youtube = build('youtube', 'v3', credentials=credentials, static_discovery=False)
    messagebox.showinfo("API Response", youtube)

    try:
        while True:
            cuepoint_insert_request = youtube.liveBroadcasts().insertCuepoint(
                id=broadcast_ID,
                body={
                    "cueType": "cueTypeAd",
                    "insertionOffsetTimeMs": start_time
                    # "durationSecs": 42,  # Duration of the cue point (in milliseconds), e.g., 60 seconds
                }
            )

            response = cuepoint_insert_request.execute()
            # messagebox.showinfo("API Response", response)
            # showMessage(response)
            print(response)
            textN = response.get('insertionOffsetTimeMs')
            f = open("response.txt", "a")
            f.write("Add Cue Point at: " + textN + "\n")
            f.close()
            time.sleep(Interval)
            print("go to me")
            start_time = start_time + Interval * 1000

    except HttpError as e:
        print('An HTTP error occurred:')
        messagebox.showinfo('An HTTP error occurred:', e.content)
        print(e.content)
    except Exception as e:
        print('An error occurred:')
        messagebox.showinfo("API Response", str(e))
        print(str(e))


def showMessage(message, timeout=5000):
    root = tk.Tk()
    root.withdraw()
    root.after(timeout, root.destroy)
    messagebox.showinfo('Info', message, master=root)


# Create an Entry widget
Label(window, text="Enter a broadcast ID:", font=('Calibri 10')).pack()
a = Entry(window, width=35)
a.pack()
Label(window, text="Enter a interval in seconds:", font=('Calibri 10')).pack()
b = Entry(window, width=35)
b.pack()

button = tk.Button(window, text="Call YouTube API", command=youtube_api_function)
button.pack()

window.mainloop()
