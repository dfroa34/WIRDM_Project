import Tkinter as tk
import tkFileDialog
from Tkinter import *
import tkMessageBox


def isTweetARumor(param):
    return True

def retrieveSimilarTweets(tweet):
    return ["Similar Tweet1", "Similar Tweet 2", "Similar Tweet 3", "Similar Tweet 4"]

class Interface_v2(tk.Tk):

    def notARumor1(self):
         tkMessageBox.showinfo("Thanks!", "Thanks for letting us know")
         self.btnTweet1.configure(state = DISABLED)

    def notARumor2(self):
        tkMessageBox.showinfo("Thanks!", "Thanks for letting us know")
        self.btnTweet2.configure(state=DISABLED)

    def notARumor3(self):
        tkMessageBox.showinfo("Thanks!", "Thanks for letting us know")
        self.btnTweet3.configure(state=DISABLED)

    def notARumor4(self):
        tkMessageBox.showinfo("Thanks!", "Thanks for letting us know")
        self.btnTweet4.configure(state=DISABLED)

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Rumor detector V1.0")

        #Interface elements

            #INPUT DATA SECTION. Initialize all the interface components
        labelInput = LabelFrame(self, text="Input data")
        self.lbl_description = Label(labelInput, text="Find out whether this tweet is a rumor or not:")
        self.lbl_user = Label(labelInput, text="User: ")
        self.userEntry = Entry(labelInput, validate="key", width = 50)
        self.tweetEntry = Text(labelInput, height=2, width=50)
        self.btnFindOut = tk.Button(text="Find out", command=self.search)
        self.result = Label(self, text="Result: ")

        photo = PhotoImage(file="C:\\Users\\diego\\PycharmProjects\\WIRDM_Project_GITHUB\\tweet.gif")
        self.logo = Label(labelInput, image=photo, height=30)
        self.logo.photo = photo

         #  SIMILAR RESULTS SECTION.  Initialize all the interface components
        labelResults = LabelFrame(self, text="Similar Tweets that are rumors as well:")

        self.tweet1 = Label(labelResults, text = "Tweet 1  Zika virus #Microcephaly #Funding #Vaccines.")
        self.tweet2 = Label(labelResults, text="Tweet 2")
        self.tweet3 = Label(labelResults, text="Tweet 3")
        self.tweet4 = Label(labelResults, text="Tweet 4")

        self.btnTweet1 = Button(labelResults, text="This is not a rumor", command = self.notARumor1)
        self.btnTweet2 = Button(labelResults, text="This is not a rumor", command = self.notARumor2)
        self.btnTweet3 = Button(labelResults, text="This is not a rumor", command = self.notARumor3)
        self.btnTweet4 = Button(labelResults, text="This is not a rumor", command = self.notARumor4)

        photo = PhotoImage(file="C:\\Users\\diego\\PycharmProjects\\WIRDM_Project_GITHUB\\tweet.gif")
        self.logo1 = Label(labelResults, image=photo, height=30)
        self.logo1.photo = photo

        photo = PhotoImage(file="C:\\Users\\diego\\PycharmProjects\\WIRDM_Project_GITHUB\\tweet.gif")
        self.logo2 = Label(labelResults, image=photo, height=30)
        self.logo2.photo = photo

        photo = PhotoImage(file="C:\\Users\\diego\\PycharmProjects\\WIRDM_Project_GITHUB\\tweet.gif")
        self.logo3 = Label(labelResults, image=photo, height=30)
        self.logo3.photo = photo

        photo = PhotoImage(file="C:\\Users\\diego\\PycharmProjects\\WIRDM_Project_GITHUB\\tweet.gif")
        self.logo4 = Label(labelResults, image=photo, height=30)
        self.logo4.photo = photo

        # Layout -------------------------------------------------------
            # Input Data - Add all the components to the layout
        labelInput.grid(row = 0, column = 0, columnspan = 4, sticky = W)

        self.lbl_description.grid(row=0, column=0, columnspan = 2, sticky=W)
        self.lbl_user.grid(row=1, column=0, sticky=W)
        self.userEntry.grid(row=1, column=1)
        self.logo.grid(row=2, column = 0)
        self.tweetEntry.grid(row=2, column=1, columnspan=2, sticky=W)
        self.btnFindOut.grid(row=3, column = 0, sticky = W)
        self.result.grid(row=3, column = 1, sticky = W)

            # Similar Tweets - Add all the components to the layout
        labelResults.grid(row=4, column=0, columnspan=4, stick=W)
        self.logo1.grid(row = 0, column =0)
        self.tweet1.grid(row = 0, column =1)
        self.btnTweet1.grid(row=0, column =2)
        self.logo2.grid(row=1, column=0)
        self.tweet2.grid(row=1, column=1)
        self.btnTweet2.grid(row=1, column=2)
        self.logo3.grid(row=2, column=0)
        self.tweet3.grid(row=2, column=1)
        self.btnTweet3.grid(row=2, column=2)
        self.logo4.grid(row=3, column=0)
        self.tweet4.grid(row=3, column=1)
        self.btnTweet4.grid(row=3, column=2)

        #self.lbl_tweet.grid(row=2, column=0, sticky=W)

        self.entry_frame = tk.Frame(self)
        self.entry_frame.grid(row = 1, column = 1)
        self.entry_frame.grid_columnconfigure(0, weight=1)

    def search(self):

        #Call the method from the other class who runs the classification process
        rumor = isTweetARumor("test")
        similarTweets = retrieveSimilarTweets("test")

        #Modify the interface given the result
        if rumor is True:
         self.result.configure(text = "Result: The rumor is true")
         self.tweet1.configure(text = similarTweets[0])
         self.tweet2.configure(text=similarTweets[1])
         self.tweet3.configure(text=similarTweets[2])
         self.tweet4.configure(text=similarTweets[3])


        else:
         self.result.configure(text="Result: The rumor is false")

        return 0




app = Interface_v2()
app.mainloop()
