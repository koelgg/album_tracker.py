mport tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import ttkbootstrap as tb

class AlbumTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Album Tracker")
        self.albums = []

        self.style = tb.Style(theme="lumen")
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("Album", "Artist", "Favorite"), show="headings", height=12)
        self.tree.heading("Album", text="Album")
        self.tree.heading("Artist", text="Artist")
        self.tree.heading("Favorite", text="★")
        self.tree.column("Album", width=180)
        self.tree.column("Artist", width=140)
        self.tree.column("Favorite", width=40, anchor="center")
        self.tree.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        btn_frame = ttk.Frame(self.root, padding=(10, 0))
        btn_frame.pack(fill="x")
        self.add_btn = ttk.Button(btn_frame, text="Add Album", command=self.add_album)
        self.add_btn.pack(side="left", padx=5)
        self.mark_btn = ttk.Button(btn_frame, text="Toggle Favorite", command=self.toggle_favorite)
        self.mark_btn.pack(side="left", padx=5)
        self.del_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_album)
        self.del_btn.pack(side="left", padx=5)

    def add_album(self):
        album = simpledialog.askstring("Add Album", "Enter album name:", parent=self.root)
        if not album:
            return
        artist = simpledialog.askstring("Add Album", "Enter artist name:", parent=self.root)
        if not artist:
            return
        self.tree.insert("", "end", values=(album, artist, ""))
        self.albums.append({"album": album, "artist": artist, "favorite": False})

    def toggle_favorite(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showinfo("No selection", "Please select an album.")
            return
        idx = self.tree.index(selected)
        fav = self.tree.set(selected, "Favorite")
        if fav == "★":
            self.tree.set(selected, "Favorite", "")
            self.albums[idx]["favorite"] = False
        else:
            self.tree.set(selected, "Favorite", "★")
            self.albums[idx]["favorite"] = True

    def delete_album(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showinfo("No selection", "Please select an album.")
            return
        idx = self.tree.index(selected)
        self.tree.delete(selected)
        self.albums.pop(idx)

if __name__ == "__main__":
    root = tb.Window(themename="lumen")
    app = AlbumTrackerApp(root)
    root.mainloop()
