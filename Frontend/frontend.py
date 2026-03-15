import sys
import os
import cv2
import traceback
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QFrame, QFileDialog, QStackedWidget, QDialog,
                             QGraphicsDropShadowEffect, QSizePolicy, QMessageBox)
from PyQt5.QtGui import QPixmap, QImage, QFont, QIcon, QColor
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QTimer, QThread, pyqtSignal
from PIL import Image, ImageDraw, ImageFont

# Import the matcher logic
from matcher_utils import find_best_match

class VideoThread(QThread):
    update_frame = pyqtSignal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cap = cv2.VideoCapture(0)
        self.running = False
        if not self.cap.isOpened():
            print("Error: Could not open webcam. Please check if the camera is connected and accessible.")

    def run(self):
        self.running = True
        while self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame_rgb.shape
                bytes_per_line = ch * w
                image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.update_frame.emit(image)
        self.cap.release()

    def stop(self):
        self.running = False
        self.wait()

class ClaraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FAMOUS FACE-OFF: CELEBS & THEIR SURPRISING LOOKALIKES")
        self.setStyleSheet("""QMainWindow {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1A237E, stop:1 #263238);}""")

        self.screen_sequence = ["splash", "clara"]
        self.current_index = 0
        self.navigation_history = []
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.splash_screen = self.create_splash_screen()
        self.clara_screen = self.create_clara_screen()
        self.central_widget.addWidget(self.splash_screen)
        self.central_widget.addWidget(self.clara_screen)

        self.show_splash()
        self.showMaximized()

    def resize_image(self, photo_path, target_width=None, target_height=None):
        try:
            full_path = os.path.normpath(photo_path)
            if not os.path.exists(full_path):
                print(f"Error: Image file not found at {full_path}")
                return None
            img = Image.open(full_path).convert('RGBA')
            screen_geometry = self.screen().availableGeometry()
            target_width = target_width or screen_geometry.width()
            target_height = target_height or screen_geometry.height()
            img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
            data = img.tobytes('raw', 'RGBA')
            qimg = QImage(data, img.width, img.height, QImage.Format_RGBA8888)
            return QPixmap.fromImage(qimg)
        except Exception as e:
            print(f"Image loading error for {photo_path}: {e}")
            return None

    def update_history(self, page):
        if not self.navigation_history or self.navigation_history[-1] != page:
            self.navigation_history.append(page)
        self.current_index = self.screen_sequence.index(page)

    def go_back(self):
        if self.current_index > 0:
            self.current_index -= 1
            prev_page = self.screen_sequence[self.current_index]
            if prev_page == "splash":
                self.show_splash()
            elif prev_page == "clara":
                self.show_clara()

    def create_splash_screen(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        # Background image
        label = QLabel()
        image_path = r"C:\Users\amrut\OneDrive\Desktop\Famousfaceoff1\Frontend\TitleCover Page (1).jpg"
        pixmap = self.resize_image(image_path)
        if not pixmap or pixmap.isNull():
            label.setText("Background image not found. Please check the path.")
            label.setStyleSheet("color: red; font: bold 20px 'Arial'; background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1A237E, stop:1 #263238);")
        else:
            screen_geometry = self.screen().availableGeometry()
            label.setPixmap(pixmap.scaled(screen_geometry.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
            label.setScaledContents(True)
            label.setFixedSize(screen_geometry.size())
            label.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(26, 35, 126, 128), stop:1 rgba(38, 50, 56, 128));""")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Button positions
        proceed_rely = 0.57  # 57% from top
        proceed_relx = 0.4   # 40% from left
        close_rely = 0.57    # 57% from top
        close_relx = 0.5     # 50% from left

        # Calculate pixel positions
        screen_geometry = self.screen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        proceed_x = int(screen_width * proceed_relx)
        proceed_y = int(screen_height * proceed_rely)
        close_x = int(screen_width * close_relx)
        close_y = int(screen_height * close_rely)

        # Proceed button
        proceed_btn = QPushButton("Proceed")
        proceed_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 16px 'Arial';
            padding: 12px 24px; border-radius: 6px; border: none;}
            QPushButton:hover {background-color: #03A9F4;}""")
        proceed_btn.setFixedSize(180, 60)
        proceed_btn.clicked.connect(self.show_clara)
        proceed_btn.setParent(widget)
        proceed_btn.move(proceed_x, proceed_y)
        proceed_btn.raise_()
        proceed_btn.show()

        # Close button
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""QPushButton {
            background-color: #D32F2F; color: white; font: bold 16px 'Arial';
            padding: 12px 24px; border-radius: 6px; border: none;}
            QPushButton:hover {background-color: #EF5350;}""")
        close_btn.setFixedSize(180, 60)
        close_btn.clicked.connect(self.close)
        close_btn.setParent(widget)
        close_btn.move(close_x, close_y)
        close_btn.raise_()
        close_btn.show()

        return widget

    def create_clara_screen(self):
        widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 0, 30, 50)
        main_layout.setSpacing(20)
        widget.setLayout(main_layout)

        # Set the background gradient
        widget.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4A148C, stop:1 #AB47BC);""")

        # Header
        header = QFrame()
        header.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4A148C, stop:1 #AB47BC); padding: 30px;""")
        header_layout = QVBoxLayout()
        header.setLayout(header_layout)
        # Update the title to match the Splash screen
        title_label = QLabel("🌟 FAMOUS FACE-OFF: CELEBS & THEIR SURPRISING LOOKALIKES")
        title_label.setStyleSheet("color: #FFFFFF; font: bold 40px 'Arial Black'; padding: 20px;")
        title_label.setAlignment(Qt.AlignCenter)
        self.animate_emoji(title_label)
        header_layout.addWidget(title_label)
        main_layout.addWidget(header)

        # Calculate half screen width
        available_width = self.screen().availableGeometry().width()
        half_width = available_width // 2

        # Content frame
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setSpacing(10)
        content_widget.setLayout(content_layout)
        content_widget.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4A148C, stop:1 #AB47BC); border-radius: 10px; padding: 20px;""")
        content_widget.setFixedWidth(half_width)
        content_widget.setMinimumHeight(600)

        # Add stretch before content for vertical centering
        content_layout.addStretch(1)

        heading_label = QLabel("👋 Welcome to CLARA 👋")
        heading_label.setStyleSheet("color: #FFFF00; font: bold 40px 'Arial'; background-color: transparent; text-shadow: 2px 2px 4px #000000;")
        heading_label.setAlignment(Qt.AlignCenter)
        heading_label.setWordWrap(True)
        self.animate_emoji(heading_label)
        content_layout.addWidget(heading_label)

        full_form_label = QLabel("Celebrity Look-A-Like Recognition Application")
        full_form_label.setStyleSheet("color: #FFFFFF; font: 28px 'Georgia'; background-color: transparent; text-shadow: 1px 1px 3px #000000;")
        full_form_label.setWordWrap(True)
        full_form_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(full_form_label)

        upload_btn = QPushButton("📸 Upload Photo")
        upload_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 18px 'Arial';
            padding: 12px 24px; border-radius: 5px;}
            QPushButton:hover {background-color: #03A9F4;}""")
        upload_btn.setFixedSize(300, 60)
        upload_btn.clicked.connect(self.show_upload_options)
        content_layout.addWidget(upload_btn, alignment=Qt.AlignHCenter)

        manual_btn = QPushButton("📖 Manual")
        manual_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 18px 'Arial';
            padding: 12px 24px; border-radius: 5px;}
            QPushButton:hover {background-color: #03A9F4;}""")
        manual_btn.setFixedSize(200, 60)
        manual_btn.clicked.connect(self.show_help_dialog)
        content_layout.addWidget(manual_btn, alignment=Qt.AlignHCenter)

        # Add Previous and Next buttons in the middle of the content layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        prev_btn = QPushButton("Previous")
        prev_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 18px 'Arial';
            padding: 10px 20px; border-radius: 5px;}
            QPushButton:hover { {</background-color: #03A9F4;}""")
        prev_btn.setFixedSize(140, 48)
        prev_btn.clicked.connect(self.go_back)
        button_layout.addWidget(prev_btn)

        next_btn = QPushButton("Next")
        next_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 18px 'Arial';
            padding: 10px 20px; border-radius: 5px;}
            QPushButton:hover {background-color: #03A9F4;}
            QPushButton:disabled {background-color: #616161;}""")
        next_btn.setFixedSize(140, 48)
        next_btn.setEnabled(False)
        button_layout.addWidget(next_btn)

        content_layout.addLayout(button_layout)

        # Add stretch after content for vertical centering
        content_layout.addStretch(1)

        # Horizontal layout for content and image
        content_layout_hbox = QHBoxLayout()
        content_layout_hbox.addWidget(content_widget, 1)

        # Add image on the right
        image_label = QLabel()
        image_path = r"C:\Users\amrut\OneDrive\Desktop\Famousfaceoff1\Frontend\Clara-removebg-preview.png"
        pixmap = self.resize_image(image_path, target_width=half_width, target_height=600)
        if pixmap and not pixmap.isNull():
            image_label.setPixmap(pixmap)
        else:
            image_label.setText("Image not found")
            image_label.setStyleSheet("color: red; font: 16px 'Arial';")
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setFixedWidth(half_width)
        content_layout_hbox.addWidget(image_label, 1)

        main_layout.addLayout(content_layout_hbox)

        return widget

    def animate_emoji(self, label):
        emojis = [i for i, c in enumerate(label.text()) if c in '👋🌌📸🎬✨🤖🎉📷🌟🏏😂🏆🕵🎞🌠🎁🗣🚀👀⚡☁🚀⏩🇮🇳📤👍🔄🎭📖']
        if emojis:
            anim = QPropertyAnimation(label, b"windowOpacity")
            anim.setDuration(1000)
            anim.setStartValue(0.8)
            anim.setEndValue(1.0)
            anim.setEasingCurve(QEasingCurve.InOutQuad)
            anim.start()
            anim.setLoopCount(-1)

    def add_glow_effect(self):
        glow = QGraphicsDropShadowEffect()
        glow.setColor(QColor(2, 136, 209, 180))
        glow.setBlurRadius(15)
        glow.setOffset(0)
        return glow

    def show_splash(self):
        self.central_widget.setCurrentWidget(self.splash_screen)
        self.update_history("splash")

    def show_clara(self):
        self.central_widget.setCurrentWidget(self.clara_screen)
        self.update_history("clara")

    def show_upload_options(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Upload Options")
        dialog.setFixedSize(700, 400)
        dialog.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1A237E, stop:1 #263238);""")
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        dialog.setLayout(layout)

        title_label = QLabel("Choose Your Starry Path! 🌟")
        title_label.setStyleSheet("color: #E0E0E0; font: bold 20px 'Arial Black'; padding: 20px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        content_frame = QFrame()
        content_frame.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #37474F, stop:1 #263238); padding: 20px; border-radius: 10px;""")
        content_layout = QVBoxLayout()
        content_layout.setSpacing(20)
        content_frame.setLayout(content_layout)

        upload_btn = QPushButton("📂 Upload from System")
        upload_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 16px 'Arial';
            padding: 15px 20px; border-radius: 5px; border: none;}
            QPushButton:hover {background-color: #03A9F4;}""")
        upload_btn.clicked.connect(self.upload_file)
        content_layout.addWidget(upload_btn, alignment=Qt.AlignHCenter)

        webcam_btn = QPushButton("🎥 Upload from Webcam")
        webcam_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 16px 'Arial';
            padding: 15px 20px; border-radius: 5px; border: none;}
            QPushButton:hover {background-color: #03A9F4;}""")
        webcam_btn.clicked.connect(lambda: self.use_webcam(dialog))
        content_layout.addWidget(webcam_btn, alignment=Qt.AlignHCenter)

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""QPushButton {
            background-color: #D32F2F; color: white; font: bold 16px 'Arial';
            padding: 15px 20px; border-radius: 5px; border: none;}
            QPushButton:hover {background-color: #EF5350;}""")
        close_btn.clicked.connect(dialog.accept)
        content_layout.addWidget(close_btn, alignment=Qt.AlignHCenter)

        layout.addWidget(content_frame)
        layout.addStretch()
        dialog.exec_()

    def show_help_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Manual")
        dialog.setFixedSize(700, 550)
        dialog.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        dialog.setModal(True)
        dialog.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1A237E, stop:1 #263238);""")

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        dialog.setLayout(layout)

        content_widget = QWidget()
        content_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        content_layout = QVBoxLayout()
        content_layout.setSpacing(10)
        content_widget.setLayout(content_layout)
        content_widget.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #37474F, stop:1 #263238); padding: 20px; border-radius: 10px;""")

        title_label = QLabel("Manual 📖")
        title_label.setStyleSheet("color: #E0E0E0; font: bold 20px 'Arial Black'; padding: 20px;")
        title_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(title_label)

        manual_description = """
        <ol style='margin: 0; padding-left: 20px;'>
            <li><b>Upload Your Photo</b> 📸: Choose 'Upload from System' for a clear, front-facing selfie or 'Upload from Webcam' for a live snapshot.</li>
            <li><b>Ensure Photo Quality</b> 🌞: Use a high-resolution photo with bright, even lighting. Avoid hats, sunglasses, or group shots for best results.</li>
            <li><b>AI Magic</b> 🤖: Our advanced deep learning AI instantly analyzes your face and matches you to an Indian celebrity from Bollywood, cricket, and more! 🌟</li>
            <li><b>View & Share</b> 📲: See a side-by-side comparison with your celebrity twin. Save or share it with friends!</li>
            <li><b>Stay Secure</b> 🔐: Your data is safe with us—privacy is our priority.</li>
            <li><b>Try More</b> 🎉: Upload different photos to discover new star matches and shine like a celebrity!</li>
        </ol>
        """
        description_label = QLabel(manual_description)
        description_label.setTextFormat(Qt.RichText)
        description_label.setStyleSheet("""color: #FFFFFF; font: 22px 'Georgia', 'Segoe UI Emoji'; background-color: transparent; text-shadow: 1px 1px 3px #000000; padding: 20px;""")
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignLeft)
        description_label.setFixedHeight(550)  # Increased from 500 to 550 to ensure all bullet points are visible
        description_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        content_layout.addWidget(description_label)

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""QPushButton {
            background-color: #D32F2F; color: white; font: bold 16px 'Arial';
            padding: 10px 20px; border-radius: 5px; border: none;}
            QPushButton:hover {background-color: #EF5350;}""")
        close_btn.setFixedSize(120, 40)
        close_btn.clicked.connect(dialog.accept)
        content_layout.addWidget(close_btn, alignment=Qt.AlignHCenter)

        content_layout.addStretch()
        layout.addWidget(content_widget)
        layout.addStretch()
        dialog.exec_()

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            print(f"Uploaded: {file_path}")
            try:
                match_name, similarity, celeb_img_path = find_best_match(file_path)
                if not match_name:
                    self.show_result("No face found in the uploaded image.", None, None, None)
                else:
                    self.show_result(match_name, similarity, file_path, celeb_img_path)
            except Exception as e:
                print(f"Error in upload_file: {str(e)}")
                traceback.print_exc()
                QMessageBox.warning(self, "Error", f"Failed to process the image: {str(e)}\nPlease try again with a clearer image in better lighting.")

    def show_result(self, match_name, similarity, user_img_path, celeb_img_path):
        print(f"Entering show_result: match_name={match_name}, similarity={similarity}, user_img_path={user_img_path}, celeb_img_path={celeb_img_path}")
        result_dialog = QDialog(self)
        result_dialog.setWindowTitle("🎯 Match Result")
        result_dialog.setFixedSize(1000, 600)
        # Apply the clara screen gradient to the result dialog
        result_dialog.setStyleSheet("""background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4A148C, stop:1 #AB47BC);""")
        layout = QVBoxLayout(result_dialog)

        try:
            print("Setting up title and score labels")
            # Replace underscores with spaces in match_name for display
            display_name = match_name.replace("_", " ") if match_name else "❌ No Match Found"
            title = QLabel(f"Your Celebrity Match: {display_name}")
            title.setStyleSheet("font: bold 28px 'Arial'; color: #00FFFF; text-shadow: 2px 2px 4px #000000;")
            title.setAlignment(Qt.AlignCenter)
            layout.addWidget(title)

            score = QLabel(f"Match Score: {similarity*100:.2f}%" if similarity else "")
            score.setStyleSheet("font: 20px 'Arial'; color: #00FF00; text-shadow: 1px 1px 3px #000000;")
            score.setAlignment(Qt.AlignCenter)
            layout.addWidget(score)

            print("Setting up image layout")
            img_layout = QHBoxLayout()
            for path in [user_img_path, celeb_img_path]:
                if path and os.path.exists(path):
                    print(f"Attempting to load image: {path}")
                    pixmap = self.resize_image(path, 400, 400)
                    if pixmap and not pixmap.isNull():
                        img_label = QLabel()
                        img_label.setPixmap(pixmap)
                        img_label.setAlignment(Qt.AlignCenter)
                        img_layout.addWidget(img_label)
                        print(f"Successfully loaded image: {path}")
                    else:
                        print(f"Failed to load image from {path}")
                        placeholder = QLabel(f"Image not found or failed to load: {path}")
                        placeholder.setStyleSheet("color: red; font: 16px 'Arial';")
                        img_layout.addWidget(placeholder)
                elif path:
                    print(f"Image path does not exist: {path}")
                    placeholder = QLabel(f"Image file missing: {path}")
                    placeholder.setStyleSheet("color: red; font: 16px 'Arial';")
                    img_layout.addWidget(placeholder)
            layout.addLayout(img_layout)

            print("Adding action buttons")
            action_layout = QHBoxLayout()
            save_btn = QPushButton("Save")
            save_btn.setStyleSheet("""QPushButton {
                background-color: #0288D1; color: white; font: bold 18px 'Arial';
                padding: 10px 20px; border-radius: 5px; border: none;}
                QPushButton:hover {background-color: #03A9F4;}""")
            save_btn.setFixedSize(120, 40)
            save_btn.clicked.connect(lambda: self.save_result(result_dialog, user_img_path, celeb_img_path, display_name, similarity))
            action_layout.addWidget(save_btn)

            share_btn = QPushButton("Share")
            share_btn.setStyleSheet("""QPushButton {
                background-color: #0288D1; color: white; font: bold 18px 'Arial';
                padding: 10px 20px; border-radius: 5px; border: none;}
                QPushButton:hover {background-color: #03A9F4;}""")
            share_btn.setFixedSize(120, 40)
            share_btn.clicked.connect(lambda: self.share_result(result_dialog, user_img_path, celeb_img_path, display_name, similarity))
            action_layout.addWidget(share_btn)

            delete_btn = QPushButton("Delete")
            delete_btn.setStyleSheet("""QPushButton {
                background-color: #0288D1; color: white; font: bold 18px 'Arial';
                padding: 10px 20px; border-radius: 5px; border: none;}
                QPushButton:hover {background-color: #03A9F4;}""")
            delete_btn.setFixedSize(120, 40)
            delete_btn.clicked.connect(result_dialog.accept)
            action_layout.addWidget(delete_btn)

            close_btn = QPushButton("Close")
            close_btn.setStyleSheet("background-color: #D32F2F; color: white; font: bold 18px 'Arial'; padding: 10px;")
            close_btn.setFixedSize(120, 40)
            close_btn.clicked.connect(result_dialog.accept)
            action_layout.addWidget(close_btn)

            action_layout.addStretch()
            layout.addLayout(action_layout)

        except Exception as e:
            print(f"Error in show_result: {str(e)}")
            traceback.print_exc()
            error_label = QLabel(f"An error occurred while displaying the result: {str(e)}")
            error_label.setStyleSheet("color: red; font: 16px 'Arial';")
            layout.addWidget(error_label)

            close_btn = QPushButton("Close")
            close_btn.setStyleSheet("background-color: #D32F2F; color: white; font: bold 18px 'Arial'; padding: 10px;")
            close_btn.clicked.connect(result_dialog.accept)
            layout.addWidget(close_btn)

        print("Showing result dialog")
        result_dialog.exec_()
        print("Result dialog closed")

    def create_composite_image(self, user_img_path, celeb_img_path, match_name, similarity):
        try:
            # Load and resize images to match Result screen
            user_img = Image.open(user_img_path).convert('RGB').resize((400, 400), Image.Resampling.LANCZOS)
            celeb_img = Image.open(celeb_img_path).convert('RGB').resize((400, 400), Image.Resampling.LANCZOS)

            # Create composite image (800x400)
            combined_img = Image.new('RGB', (800, 400))
            combined_img.paste(user_img, (0, 0))
            combined_img.paste(celeb_img, (400, 0))

            # Add text (match name and score)
            draw = ImageDraw.Draw(combined_img)
            try:
                font = ImageFont.truetype("arial.ttf", 24)  # Try to use Arial font
            except:
                font = ImageFont.load_default()  # Fallback to default font
            text = f"Match: {match_name}\nScore: {similarity*100:.2f}%"
            draw.text((10, 10), text, fill="white", font=font)

            return combined_img
        except Exception as e:
            print(f"Error creating composite image: {str(e)}")
            raise

    def save_result(self, dialog, user_img_path, celeb_img_path, match_name, similarity):
        if user_img_path and os.path.exists(user_img_path) and celeb_img_path and os.path.exists(celeb_img_path):
            try:
                combined_img = self.create_composite_image(user_img_path, celeb_img_path, match_name, similarity)

                # Save the composite image
                save_path, _ = QFileDialog.getSaveFileName(dialog, "Save Result", f"{match_name}_{similarity*100:.2f}.png", "PNG Files (*.png);;JPEG Files (*.jpg)")
                if save_path:
                    combined_img.save(save_path, quality=95)  # High quality to avoid compression
                    QMessageBox.information(dialog, "Success", f"Result saved to {save_path}")
            except Exception as e:
                print(f"Error in save_result: {str(e)}")
                traceback.print_exc()
                QMessageBox.warning(dialog, "Error", f"Failed to save the result: {str(e)}")
        else:
            QMessageBox.warning(dialog, "Error", "Cannot save: One or both images are missing.")

    def share_result(self, dialog, user_img_path, celeb_img_path, match_name, similarity):
        if user_img_path and os.path.exists(user_img_path) and celeb_img_path and os.path.exists(celeb_img_path):
            try:
                combined_img = self.create_composite_image(user_img_path, celeb_img_path, match_name, similarity)

                # Convert PIL image to QImage for clipboard
                combined_img_rgb = combined_img.convert("RGB")
                data = combined_img_rgb.tobytes("raw", "RGB")
                qimage = QImage(data, combined_img_rgb.width, combined_img_rgb.height, QImage.Format_RGB888)

                # Copy to clipboard
                from PyQt5.QtGui import QGuiApplication
                clipboard = QGuiApplication.clipboard()
                clipboard.setImage(qimage)
                QMessageBox.information(dialog, "Share", "Composite image copied to clipboard! You can paste it into an image-compatible app.")
            except Exception as e:
                print(f"Error in share_result: {str(e)}")
                traceback.print_exc()
                QMessageBox.warning(dialog, "Error", f"Failed to share the result: {str(e)}")
        else:
            QMessageBox.warning(dialog, "Error", "Cannot share: One or both images are missing.")

    def use_webcam(self, parent_dialog):
        webcam_dialog = QDialog(self)
        webcam_dialog.setWindowTitle("Webcam Capture")
        webcam_dialog.setFixedSize(640, 480)
        layout = QVBoxLayout()
        webcam_dialog.setLayout(layout)

        video_label = QLabel(webcam_dialog)
        video_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(video_label)

        capture_btn = QPushButton("Capture")
        capture_btn.setStyleSheet("""QPushButton {
            background-color: #0288D1; color: white; font: bold 16px 'Arial';
            padding: 10px 20px; border-radius: 5px; border: none;}
            QPushButton:hover {background-color: #03A9F4;}""")
        capture_btn.clicked.connect(lambda: self.capture_frame(video_thread, webcam_dialog, parent_dialog))
        layout.addWidget(capture_btn)

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""QPushButton {
            background-color: #D32F2F; color: white; font: bold 16px 'Arial';
            padding: 10px 20px; border-radius: 5px; border: none;}
            QPushButton:hover {background-color: #EF5350;}""")
        close_btn.clicked.connect(webcam_dialog.accept)
        layout.addWidget(close_btn)

        video_thread = VideoThread()
        if not video_thread.cap.isOpened():
            QMessageBox.warning(self, "Camera Error", "Could not access the webcam. Please ensure it is connected and not in use by another application.")
            webcam_dialog.accept()
            return

        video_thread.update_frame.connect(lambda frame: video_label.setPixmap(QPixmap.fromImage(frame).scaled(video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)))
        video_thread.start()

        webcam_dialog.exec_()
        video_thread.stop()

    def capture_frame(self, video_thread, webcam_dialog, parent_dialog):
        print("Attempting to capture frame...")
        temp_path = None
        try:
            if video_thread.isRunning() and video_thread.cap.isOpened():
                ret, frame = video_thread.cap.read()
                if ret:
                    print("Frame captured successfully.")
                    temp_path = os.path.join(self.base_dir, "temp_capture.jpg")
                    cv2.imwrite(temp_path, frame)
                    print(f"Temporary image saved at: {temp_path}")
                    try:
                        match_name, similarity, celeb_img_path = find_best_match(temp_path)
                        print(f"find_best_match result: match_name={match_name}, similarity={similarity}, celeb_img_path={celeb_img_path}")
                        # Validate celeb_img_path
                        if celeb_img_path and not os.path.exists(celeb_img_path):
                            print(f"Invalid celebrity image path: {celeb_img_path}")
                            celeb_img_path = None
                        if not match_name:
                            QMessageBox.warning(webcam_dialog, "Processing Error", "No face found in the captured image. Please ensure your face is centered and try again.")
                        else:
                            self.show_result(match_name, similarity, temp_path, celeb_img_path)
                    except Exception as e:
                        print(f"Error in find_best_match: {str(e)}")
                        traceback.print_exc()
                        QMessageBox.warning(webcam_dialog, "Error", f"Failed to process the image: {str(e)}\nPlease try again.")
                        # Keep webcam_dialog open for retry
                else:
                    print("Failed to capture frame.")
                    QMessageBox.warning(webcam_dialog, "Capture Error", "Failed to capture the frame. Please try again.")
            else:
                print("Camera not available.")
                QMessageBox.warning(webcam_dialog, "Camera Error", "Camera is not available. Please ensure it is connected and try again.")
        except Exception as e:
            print(f"Unexpected error in capture_frame: {str(e)}")
            traceback.print_exc()
            QMessageBox.warning(webcam_dialog, "Error", f"An unexpected error occurred: {str(e)}\nPlease try again.")
        finally:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                    print(f"Temporary image deleted: {temp_path}")
                except Exception as e:
                    print(f"Error deleting temporary image: {str(e)}")

def main():
    app = QApplication(sys.argv)
    # Set a global exception handler to catch unhandled exceptions
    sys.excepthook = lambda exc_type, exc_value, exc_traceback: print(f"Unhandled exception: {exc_type}, {exc_value}\n{''.join(traceback.format_tb(exc_traceback))}")
    window = ClaraApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()