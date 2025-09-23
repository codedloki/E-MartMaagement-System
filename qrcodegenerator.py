from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class QRGenerate:
    def __init__(self, root):
        self.root = root
        self.root.title("Setup 2FA")
        self.root.geometry("700x500+0+0")

        # ============================= Setting Background ============================= #
        bg_path = BASE_DIR/"images"/"pexels-simon-berger-1323550.jpg"

        try:
            bg_img = Image.open(bg_path)
            bg_img = bg_img.resize((700, 500), Image.Resampling.LANCZOS)
            self.bg = ImageTk.PhotoImage(bg_img)
        except Exception as e:
            print("Background image error:", e)
            self.bg = None

        if self.bg:
            lbl_bg = Label(self.root, image=self.bg)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Place inside frame
        frame = Frame(self.root, bg="white")
        frame.place(x=100, y=100, width=500, height=300)

        register_lbl = Label(frame, text="SETUP 2FA",
                             font=("times new roman", 20, "bold"),
                             fg="brown", bg="white")
        register_lbl.place(x=20, y=20)

        # ============================= QR Code Image ============================= #
        qr_path = BASE_DIR/"qrcodes"/"code.png"

        if qr_path.exists():
            try:
                img = Image.open(qr_path)
                # Resize if needed (optional)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                
                # ✅ Convert PIL Image → Tkinter PhotoImage and store as instance variable
                self.qr_photo = ImageTk.PhotoImage(img)
                
                # ✅ Create label for QR code
                qr_label = Label(frame, image=self.qr_photo, bg="white")
                qr_label.place(x=250, y=60)
                
                # ✅ Add instruction text
                instruction_lbl = Label(frame, text="Scan this QR code with your authenticator app",
                                      font=("times new roman", 12),
                                      bg="white", fg="black")
                instruction_lbl.place(x=150, y=270)

            except Exception as e:
                print("QR image error:", e)
                error_lbl = Label(frame, text="Failed to load QR code",
                                font=("times new roman", 12),
                                bg="white", fg="red")
                error_lbl.place(x=150, y=70)
        else:
            print(f"QR code image not found at: {qr_path}")
            error_lbl = Label(frame, text="QR code not generated yet.",
                            font=("times new roman", 12),
                            bg="white", fg="red")
            error_lbl.place(x=150, y=70)
            
        # Add close button
        close_btn = Button(frame, text="Close", command=self.root.destroy,
                          font=("times new roman", 12, "bold"), bg="brown", fg="white")
        close_btn.place(x=200, y=270, width=100)

    def update_qr_code(self):
        """Method to reload QR code if needed"""
        qr_path = BASE_DIR/"qrcodes"/"code.png"
        if qr_path.exists():
            try:
                img = Image.open(qr_path)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                self.qr_photo = ImageTk.PhotoImage(img)
                # You would need to update the label here if implementing refresh functionality
            except Exception as e:
                print("Error updating QR code:", e)