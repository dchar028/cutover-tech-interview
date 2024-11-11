import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from .store_data import get_all_data
from .fetch_data import fetch_nasa_apod, fetch_spotify_top_track
from datetime import datetime
from io import BytesIO
import requests

class TopTrackInSpaceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Top Track in Space")
        self.setGeometry(100, 100, 800, 600)
        self.current_date = datetime.now().date()  # Initialize current_date here
        self.initUI()

    def initUI(self):
        print("Initializing UI...")

        # Basic layout
        self.layout = QVBoxLayout()

        # NASA data labels
        self.nasa_title = QLabel("NASA Image of the Day: [Title Here]")
        self.nasa_title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.nasa_title)

        self.nasa_description = QLabel("NASA Description: [Description Here]")
        self.nasa_description.setWordWrap(True)
        self.layout.addWidget(self.nasa_description)

        # NASA Image display
        self.nasa_image_label = QLabel()
        self.layout.addWidget(self.nasa_image_label)

        # Spotify data labels
        self.spotify_title = QLabel("Top Track: [Song Title Here]")
        self.spotify_title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.spotify_title)

        self.spotify_artist = QLabel("Artist: [Artist Name Here]")
        self.layout.addWidget(self.spotify_artist)

        # Spotify Album Cover display
        self.spotify_album_cover = QLabel()
        self.layout.addWidget(self.spotify_album_cover)

        # Button to view Redis entries
        self.view_entries_button = QPushButton("View All Entries")
        self.view_entries_button.clicked.connect(self.show_all_entries)
        self.layout.addWidget(self.view_entries_button)

        # Table widget for displaying all entries
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        # Set layout
        self.setLayout(self.layout)

        # Load data for today
        self.load_data_for_today()

    def load_data_for_today(self):
        # Example date key for Redis data
        date_key = self.current_date.strftime("%Y-%m-%d")
        
        # Fetch data (for simplicity, assuming functions to fetch and store data are defined)
        nasa_data = fetch_nasa_apod()  # Replace with your method to get today's NASA data
        spotify_data = fetch_spotify_top_track()  # Replace with your method to get today's Spotify data

        self.display_data(nasa_data, spotify_data)

    def display_data(self, nasa_data, spotify_data):
        # NASA data display
        if nasa_data:
            self.nasa_title.setText(f"NASA Image of the Day: {nasa_data.get('title', 'No Title Available')}")
            self.nasa_description.setText(nasa_data.get('explanation', 'No Description Available'))
            try:
                image_url = nasa_data.get('url')
                if image_url:
                    image_response = requests.get(image_url)
                    image = QImage.fromData(BytesIO(image_response.content).read())
                    self.nasa_image_label.setPixmap(QPixmap.fromImage(image).scaled(400, 300, Qt.KeepAspectRatio))
            except Exception as e:
                print("Error displaying NASA image:", e)

        # Spotify data display
        if spotify_data:
            self.spotify_title.setText(f"Top Track: {spotify_data.get('name', 'Unknown Track')}")
            self.spotify_artist.setText(f"Artist: {spotify_data.get('artist', 'Unknown Artist')}")
            try:
                album_image_url = spotify_data.get("album_image_url")
                if album_image_url:
                    album_image_response = requests.get(album_image_url)
                    album_image = QImage.fromData(BytesIO(album_image_response.content).read())
                    self.spotify_album_cover.setPixmap(QPixmap.fromImage(album_image).scaled(150, 150, Qt.KeepAspectRatio))
            except Exception as e:
                print("Error displaying Spotify album cover:", e)

    def show_all_entries(self):
        print("View All Entries button clicked!")
        data = get_all_data()

        # Configure table with row and column count
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Date", "Image URL", "Track and Artist"])

        # Populate the table
        for row, entry in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(entry["date"]))
            self.table_widget.setItem(row, 1, QTableWidgetItem(entry["image_url"]))
            self.table_widget.setItem(row, 2, QTableWidgetItem(f"{entry['track_name']} by {entry['artist']}"))

        self.table_widget.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TopTrackInSpaceApp()
    window.show()
    sys.exit(app.exec_())
