import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
from PIL import Image, ImageTk

class SteganoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Steganography App")

        # Set warna latar belakang
        self.master.configure(bg='#f0f0f0')

        # Judul aplikasi
        self.title_label = tk.Label(master, text="Steganography App", font=('Helvetica', 16), bg='#f0f0f0')
        self.title_label.pack(pady=10)

        # Tombol untuk mengimpor gambar
        self.browse_button = tk.Button(master, text="Import Image", command=self.browse_image, bg='#ff9800', fg='white')
        self.browse_button.pack(pady=10)

        # Masukkan pesan
        self.message_label = tk.Label(master, text="Enter Message:", bg='#f0f0f0')
        self.message_label.pack()

        self.message_entry = tk.Entry(master, width=30)
        self.message_entry.pack()

        # Tombol untuk menyembunyikan pesan
        self.hide_button = tk.Button(master, text="Hide Message", command=self.hide_message, bg='#4caf50', fg='white')
        self.hide_button.pack(pady=10)

        # Tombol untuk membuka pesan tersembunyi
        self.reveal_button = tk.Button(master, text="Reveal Message", command=self.reveal_message, bg='#2196f3', fg='white')
        self.reveal_button.pack(pady=10)

        # Label untuk menampilkan gambar
        self.image_label = tk.Label(master, bg='#f0f0f0')
        self.image_label.pack()

    def browse_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def hide_message(self):
        if hasattr(self, 'image_path'):
            message = self.message_entry.get()
            secret = lsb.hide(self.image_path, message)
            secret_path = "img-sec.png"
            secret.save(secret_path)
            tk.messagebox.showinfo("Success", f"Message hidden successfully in {secret_path}")
            self.display_image(secret_path)
        else:
            tk.messagebox.showwarning("Warning", "Please select an image first.")

    def reveal_message(self):
        if hasattr(self, 'image_path'):
            revealed_message = lsb.reveal("img-sec.png")
            tk.messagebox.showinfo("Revealed Message", f"The revealed message is:\n{revealed_message}")
        else:
            tk.messagebox.showwarning("Warning", "Please select an image first.")

    def display_image(self, path):
        img = Image.open(path)
        img.thumbnail((300, 300))  # Resize image for display
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

def main():
    root = tk.Tk()
    app = SteganoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
