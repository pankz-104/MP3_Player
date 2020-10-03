# importing required functionalities
from pygame import mixer
from tkinter import filedialog
from tkinter import * 


class MusicPlayer:
    def __init__(self, root):
        root.geometry('400x300')    # window size 
        root.title('Music Player')      # window titel 
        Load = Button(root, text='Load', width=10, font=('Times',10), command = self.load) # Buttons 
        Play = Button(root, text='Play', width=10, font=('Times',10), command = self.play)
        Pause = Button(root, text='Pause', width=10, font=('Times',10), command = self.pause)
        Stop = Button(root, text='Stop', width=10, font=('Times',10), command = self.stop)
        exit = Button(root, text='Exit', width=10, font=('Times',10), command = self.exit())
        Load.place(x = 0,y = 20)     # positioning buttons 
        Play.place(x = 100, y = 20)
        Pause.place(x = 200, y = 20)
        Stop.place(x = 300, y = 20)
        Exit.place(x = 100, y = -20)
        self.music_file = False
        self.playing_state = False

    def load(self):     # opening from file exxplorer and loading music file 
        self.music_file = filedialog.askopenfilename()

    def play(self):     # playing music file 
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):    # pause and unpause the music file 
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):     # stoping music file 
            mixer.music.stop()


root = Tk()
mp3_player = MusicPlayer(root)
root.mainloop()
