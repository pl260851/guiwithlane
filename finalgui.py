
import tkinter as tk
from tkinter import messagebox, Button, Label, Canvas
import cv2
import numpy as np
from PIL import Image, ImageTk
import threading



def draw_lines(img, lines):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)



def detect_lanes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, np.array([]), minLineLength=100, maxLineGap=50)
    line_img = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
    if lines is not None:
        draw_lines(line_img, lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_img, 1, 1)
    return combo_image



def video_loop():
    cap = cv2.VideoCapture('/Users/aidahuang/Downloads/pvid.mov')  # Adjust the path to your video
    if not cap.isOpened():
        messagebox.showerror("Error", "Error opening video file")
        return

    while True:
        ret, frame = cap.read()
        if ret:
            lane_frame = detect_lanes(frame)
            lane_frame = cv2.cvtColor(lane_frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(lane_frame)
            photo = ImageTk.PhotoImage(image)

           
            video.image = photo  # Keep a reference
            video.create_image(0, 0, anchor=tk.NW, image=photo)

            root.update_idletasks()
            root.update()
        else:
            break
    cap.release()


# Main GUI setup
root = tk.Tk()
root.geometry("510x510")
root.title("Control")



def createGUI(user_firstname):
    vidlabel = Label(root, text="Video")
    vidlabel.grid(row=0, column=0)

    global video  # Make 'video' global to access it in video_loop
    video = Canvas(root, width=200, height=200, background='black')
    video.grid(row=1, column=0)

    feedlabel = Label(root, text="No Feed")
    feedlabel.grid(row=2, column=0)

    forwardbutton = Button(root, text="Forward")
    forwardbutton.grid(row=1, column=6)

    backbutton = Button(root, text="Backward")
    backbutton.grid(row=1, column=7)

    rightbutton = Button(root, text="Right")
    rightbutton.grid(row=1, column=8)

    leftbutton = Button(root, text="Left")
    leftbutton.grid(row=1, column=9)

    stopbutton = Button(root, text="Stop")
    stopbutton.grid(row=2, column=6)

    logout = Button(root, text="Logout", command=root.destroy)
    logout.grid(row=2, column=7)

    messagebox.showinfo("Logged in!", "Welcome, " + user_firstname)

    
    threading.Thread(target=video_loop).start()



createGUI("User")

root.mainloop()
