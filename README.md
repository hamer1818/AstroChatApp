# AstroChatApp
<img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/hamer1818/AstroChatApp/CI">
<img alt="License" src="https://img.shields.io/github/license/hamer1818/AstroChatApp">
<img alt="Stars" src="https://img.shields.io/github/stars/hamer1818/AstroChatApp?style=social">

AstroChatApp is a real-time, secure chat application built with Astro for the frontend and Python's Flask-SocketIO for the backend. It offers seamless communication with features like user avatars, online user tracking, emoji support, and more.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
    - Frontend
    - Backend
- [Installation](#installation)
    - Prerequisites
    - Backend Setup
    - Frontend Setup
- [Usage](#usage)
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
- [Socket.IO](https://socket.io/)
- [Emoji Picker Element](https://www.npmjs.com/package/emoji-picker-element)

### Backend
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)

## Installation

### Prerequisites
- [Node.js](https://nodejs.org/) (v14.x or higher)
- [npm](https://www.npmjs.com/) (v6.x or higher)
- [Python](https://www.python.org/) (v3.6 or higher)
- [pip](https://pypi.org/project/pip/) (v21.x or higher)

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
