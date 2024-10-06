"""The class to init the windows"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Application(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly", title="ArtifactsWarpper")

        self.geometry("800x600")

        # create frames
        self.index_frame = ttk.Frame(self)
        self.new_account_frame = ttk.Frame(self)
        self.connect_frame = ttk.Frame(self)
        self.game_frame = ttk.Frame(self)

        self.create_widgets()

        # display index frame on start
        self.show_frame(self.index_frame)
        # define quit button
        quit_button = ttk.Button(self, text="Quitter", command=self.quit, bootstyle=DANGER)
        quit_button.pack(pady=50, side="bottom")

    def create_widgets(self):
        """_summary_"""
        self.create_index_frame_widgets()
        self.create_new_account_windgets()

    def create_index_frame_widgets(self):
        """INDEX_FRAME"""
        index_label = ttk.Label(self.index_frame, text="Bienvenue sur le wrapper Artifactsmmo")
        create_account_button = ttk.Button(
            self.index_frame, text="Créer un compte",
            command=lambda: self.show_frame(self.new_account_frame),
            bootstyle=SUCCESS
            )
        connexion_button = ttk.Button(
            self.index_frame, text="Se connecter",
            command=lambda: self.show_frame(self.connect_frame)
            )
        index_label.pack(pady=20)
        create_account_button.pack(pady=10)
        connexion_button.pack(pady=10)

    def create_new_account_windgets(self):
        # CREATE ACCOUNT FRAME
        title = ttk.Label(self.new_account_frame, text="Ici vous pouvez créer un compte")
        connection_frame = ttk.Frame(self.new_account_frame, borderwidth=5, relief="ridge")
        username_label = ttk.Label(connection_frame, text="Pseudo de connexion")
        username_entry = ttk.Entry(connection_frame, name='username', bootstyle=PRIMARY)
        password_label = ttk.Label(connection_frame, text="Mot de passe")
        password_entry = ttk.Entry(connection_frame, name='password', bootstyle=PRIMARY)
        email_label = ttk.Label(connection_frame, text="Email")
        email_entry = ttk.Entry(connection_frame, name='email', bootstyle=PRIMARY)
        create_account_button = ttk.Button(connection_frame, text="Créer un compte")

        title.pack(pady=20)
        connection_frame.pack(pady=20)
        username_label.grid(row=1, column=0, pady=10, padx=5, sticky=E)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0, pady=10, padx=5, sticky=E)
        password_entry.grid(row=2, column=1)
        email_label.grid(row=3, column=0, pady=10, padx=5, sticky=E)
        email_entry.grid(row=3, column=1)
        create_account_button.grid(row=4, column=0, columnspan=2, pady=20, padx=40, sticky=EW)
        

    def show_frame(self, frame):
        # Cache toutes les frames
        self.index_frame.pack_forget()
        self.new_account_frame.pack_forget()
        self.connect_frame.pack_forget()
        self.game_frame.pack_forget()

        # Affiche la frame demandée
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
