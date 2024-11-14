# AstroChatApp 🚀

[English](README.md) | [Türkçe](README.tr.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Stars](https://img.shields.io/github/stars/hamer1818/AstroChatApp?style=social)
![GitHub forks](https://img.shields.io/github/forks/hamer1818/AstroChatApp.svg?style=social&label=Fork)
![GitHub watchers](https://img.shields.io/github/watchers/hamer1818/AstroChatApp.svg?style=social&label=Watch)
![GitHub repo size](https://img.shields.io/github/repo-size/hamer1818/AstroChatApp.svg)
![Languages](https://img.shields.io/github/languages/count/hamer1818/AstroChatApp.svg)
![Top Language](https://img.shields.io/github/languages/top/hamer1818/AstroChatApp.svg)


AstroChatApp is a real-time chat application built with Astro for the frontend and Python's Flask-SocketIO for the backend. It offers seamless communication with features like user avatars, online user tracking, emoji support.


## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Demo

![AstroChatApp Demo](/public/ss.jpeg)

## Features
- **Real-Time Communication**: Instant messaging powered by Socket.IO.
- **User Avatars**: Upload and display user avatars.
- **Online Users List**: View currently online users.
- **Emoji Support**: Integrate emojis into your conversations.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **User-Friendly Interface**: Clean and intuitive UI built with Tailwind CSS.


## Technologies Used

### Frontend
- [Astro](https://astro.build/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Socket.IO Client](https://socket.io/)
- [Emoji Picker Element](https://www.npmjs.com/package/emoji-picker-element)


### Backend
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)


## Installation

### Prerequisites
- **Node.js** (v14 or later)
- **npm** (v6 or later)
- **Python** (v3.7 or later)
- **pip** (Python package installer)

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/hamer1818/AstroChatApp.git
    cd AstroChatApp
    ```
2. Open the `server` directory:
    ```bash
    cd server
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - Windows:
        ```bash
        venv\Scripts\activate
        ```
    - macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Start the Flask server:
    ```bash
    python main.py
    ```
7. The server should now be running on `http://localhost:5000`.

### Frontend Setup
1. Open a new terminal and navigate to the `root` directory of the project.
2. Install the required dependencies:
    ```bash
    npm install
    ```
3. Start the Astro development server:
    ```bash
    npm start
    ```
4. The frontend should now be running on `http://localhost:4321`.

## Usage
1. **Open the application in your browser**:
    - Navigate to http://localhost:4321.
2. Set Up Your Profile:
    - Upload an avatar image
    - Enter a unique username.
    - Click **Join Chat** to enter the chat room.
3. Start Chatting:
    - Type your message in the input field at the bottom.
    - Press **Enter** to send your message.
    - Use the emoji picker to add emojis to your messages.

## Contact
- **Hamza ORTATEPE** - [https://hamzaortatepe.com.tr](https://hamzaortatepe.com.tr/)
- **Email** - [hortatepe2002@gmail.com](mailto:hortatepe2002@gmail.com)
- **Github** - [https://github.com/hamer1818/AstroChatApp](https://github.com/hamer1818/AstroChatApp)

## Acknowledgements
- [Astro](https://astro.build/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [Socket.IO](https://socket.io/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Emoji Picker Element](https://www.npmjs.com/package/emoji-picker-element)

---

``Made with ❤️ by Hamza ORTATEPE``
