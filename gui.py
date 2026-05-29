import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLineEdit,
    QSlider,
    QScrollArea,
    QSizePolicy
)


COLORS = {
    "bg": "#0B0F14",
    "surface": "#121821",
    "surface_2": "#171E29",
    "border": "#242D3A",
    "accent": "#6D8DFF",
    "text": "#F3F5F7",
    "muted": "#98A2B3",
    "success": "#22C55E"
}


class PillButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setObjectName("pill")

        self.setFixedHeight(42)


class SearchCard(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("searchCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(22)

        badge = QLabel("AI-Powered Job Discovery")
        badge.setObjectName("badge")

        title = QLabel("Find opportunities\nnear you")
        title.setObjectName("heroTitle")

        subtitle = QLabel(
            "Search jobs by geographic location, "
            "radius, and work preferences."
        )
        subtitle.setObjectName("subtitle")
        subtitle.setWordWrap(True)

        self.search = QLineEdit()
        self.search.setPlaceholderText(
            "Search city, region or country..."
        )
        self.search.setMinimumHeight(58)

        radius_row = QHBoxLayout()

        radius_label = QLabel("Search Radius")
        radius_label.setObjectName("sectionLabel")

        self.radius_value = QLabel("50 km")
        self.radius_value.setObjectName("muted")

        radius_row.addWidget(radius_label)
        radius_row.addStretch()
        radius_row.addWidget(self.radius_value)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(5)
        self.slider.setMaximum(100)
        self.slider.setValue(50)

        self.slider.valueChanged.connect(
            lambda v: self.radius_value.setText(f"{v} km")
        )

        work_label = QLabel("Work Style")
        work_label.setObjectName("sectionLabel")

        pill_row = QHBoxLayout()
        pill_row.setSpacing(10)

        self.remote = PillButton("Remote")
        self.hybrid = PillButton("Hybrid")
        self.office = PillButton("On-site")

        self.hybrid.setChecked(True)

        pill_row.addWidget(self.remote)
        pill_row.addWidget(self.hybrid)
        pill_row.addWidget(self.office)

        self.find_btn = QPushButton(
            "Find Opportunities"
        )
        self.find_btn.setObjectName("primaryButton")
        self.find_btn.setFixedHeight(60)

        layout.addWidget(badge)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(10)
        layout.addWidget(self.search)
        layout.addLayout(radius_row)
        layout.addWidget(self.slider)
        layout.addWidget(work_label)
        layout.addLayout(pill_row)
        layout.addStretch()
        layout.addWidget(self.find_btn)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JobRadar")
        self.resize(1550, 920)
        self.setMinimumSize(1280, 800)

        root = QWidget()
        self.setCentralWidget(root)

        main = QVBoxLayout(root)
        main.setContentsMargins(30, 30, 30, 30)
        main.setSpacing(24)

        # NAVBAR
        nav = QFrame()
        nav.setObjectName("navbar")

        nav_layout = QHBoxLayout(nav)
        nav_layout.setContentsMargins(26, 18, 26, 18)

        brand_col = QVBoxLayout()

        brand = QLabel("JobRadar")
        brand.setObjectName("brand")

        sub = QLabel("Premium Job Discovery")
        sub.setObjectName("navSub")

        brand_col.addWidget(brand)
        brand_col.addWidget(sub)

        status = QLabel("● Live Search")
        status.setObjectName("status")

        nav_layout.addLayout(brand_col)
        nav_layout.addStretch()
        nav_layout.addWidget(status)

        # CONTENT
        content = QHBoxLayout()
        content.setSpacing(26)

        # LEFT
        left = SearchCard()
        left.setFixedWidth(470)

        # RIGHT PLACEHOLDER
        right_panel = QFrame()
        right_panel.setObjectName("resultsPanel")

        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(36, 36, 36, 36)

        featured = QLabel("Featured Jobs")
        featured.setObjectName("resultsTitle")

        desc = QLabel(
            "Your personalized job matches will appear here."
        )
        desc.setObjectName("muted")

        hero_card = QFrame()
        hero_card.setObjectName("heroJob")

        hero_layout = QVBoxLayout(hero_card)
        hero_layout.setContentsMargins(28, 28, 28, 28)

        company = QLabel("Spotify")
        company.setObjectName("company")

        role = QLabel("Senior Python Engineer")
        role.setObjectName("jobRole")

        meta = QLabel(
            "Stockholm • 720k NOK • 92% Match"
        )
        meta.setObjectName("meta")

        hero_layout.addWidget(company)
        hero_layout.addWidget(role)
        hero_layout.addWidget(meta)

        right_layout.addWidget(featured)
        right_layout.addWidget(desc)
        right_layout.addSpacing(18)
        right_layout.addWidget(hero_card)
        right_layout.addStretch()

        content.addWidget(left)
        content.addWidget(right_panel)

        main.addWidget(nav)
        main.addLayout(content)

        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet(f"""
            QMainWindow {{
                background: {COLORS["bg"]};
            }}

            QWidget {{
                color: {COLORS["text"]};
                font-family: Segoe UI;
            }}

            #navbar {{
                background: rgba(18,24,33,0.95);
                border: 1px solid {COLORS["border"]};
                border-radius: 28px;
            }}

            #brand {{
                font-size: 28px;
                font-weight: 700;
            }}

            #navSub {{
                color: {COLORS["muted"]};
                font-size: 13px;
            }}

            #status {{
                color: {COLORS["success"]};
                font-size: 14px;
                font-weight: 600;
            }}

            #searchCard {{
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:1,
                    stop:0 #141C26,
                    stop:1 #10161F
                );

                border: 1px solid #283241;
                border-radius: 34px;
            }}

            #badge {{
                background: rgba(109,141,255,0.15);
                border: 1px solid rgba(109,141,255,0.25);
                border-radius: 14px;
                padding: 10px 18px;
                max-width: 220px;
                font-size: 13px;
                font-weight: 600;
            }}

            #heroTitle {{
                font-size: 42px;
                font-weight: 700;
                line-height: 1.1;
            }}

            #subtitle {{
                color: {COLORS["muted"]};
                font-size: 15px;
            }}

            QLineEdit {{
                background: rgba(255,255,255,0.03);
                border: 1px solid {COLORS["border"]};
                border-radius: 20px;
                padding-left: 22px;
                font-size: 15px;
            }}

            QLineEdit:focus {{
                border: 1px solid {COLORS["accent"]};
            }}

            #sectionLabel {{
                font-size: 14px;
                font-weight: 600;
            }}

            #muted, #meta {{
                color: {COLORS["muted"]};
            }}

            QSlider::groove:horizontal {{
                height: 6px;
                border-radius: 3px;
                background: #1E2633;
            }}

            QSlider::handle:horizontal {{
                background: {COLORS["accent"]};
                width: 22px;
                margin: -8px 0;
                border-radius: 11px;
            }}

            #pill {{
                background: rgba(255,255,255,0.03);
                border: 1px solid {COLORS["border"]};
                border-radius: 18px;
                padding: 10px 18px;
                font-size: 14px;
                font-weight: 600;
            }}

            #pill:checked {{
                background: rgba(109,141,255,0.18);
                border: 1px solid {COLORS["accent"]};
            }}

            #primaryButton {{
                background: {COLORS["accent"]};
                border: none;
                border-radius: 20px;
                font-size: 15px;
                font-weight: 700;
                color: white;
            }}

            #primaryButton:hover {{
                background: #7B98FF;
            }}

            #resultsPanel {{
                background: rgba(18,24,33,0.95);
                border-radius: 34px;
                border: 1px solid {COLORS["border"]};
            }}

            #resultsTitle {{
                font-size: 30px;
                font-weight: 700;
            }}

            #heroJob {{
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:1,
                    stop:0 #1A2230,
                    stop:1 #121A25
                );

                border-radius: 30px;
                border: 1px solid #2A3444;
            }}

            #company {{
                font-size: 14px;
                color: {COLORS["muted"]};
            }}

            #jobRole {{
                font-size: 28px;
                font-weight: 700;
            }}
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    font = QFont("Segoe UI")
    app.setFont(font)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())