import customtkinter as ctk
from tkinter import messagebox
from capture_images import capture_images
from train_model import train_model
from recognize_and_log import recognize_and_log

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Main UI
def main():
    def on_capture():
        user_id = entry_user_id.get()
        user_name = entry_user_name.get()
        if user_id.isdigit() and user_name.strip():
            capture_images(int(user_id), user_name.strip())
            messagebox.showinfo("Success", "Images captured successfully!")
        else:
            messagebox.showerror("Error", "User ID must be a number and Name cannot be empty.")

    def on_train():
        train_model()
        messagebox.showinfo("Success", "Model trained successfully!")

    def on_recognize():
        recognize_and_log()
        messagebox.showinfo("Success", "Attendance logged successfully!")

    # Create the main window
    root = ctk.CTk()
    root.title("Smart Attendance System")
    root.geometry("400x350")

    # User ID input
    label_user_id = ctk.CTkLabel(root, text="User ID:")
    label_user_id.pack(pady=10)
    entry_user_id = ctk.CTkEntry(root)
    entry_user_id.pack(pady=10)

    # User Name input
    label_user_name = ctk.CTkLabel(root, text="User Name:")
    label_user_name.pack(pady=10)
    entry_user_name = ctk.CTkEntry(root)
    entry_user_name.pack(pady=10)

    # Buttons
    btn_capture = ctk.CTkButton(root, text="Capture Images", command=on_capture)
    btn_capture.pack(pady=10)
    btn_train = ctk.CTkButton(root, text="Train Model", command=on_train)
    btn_train.pack(pady=10)
    btn_recognize = ctk.CTkButton(root, text="Recognize and Log", command=on_recognize)
    btn_recognize.pack(pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()