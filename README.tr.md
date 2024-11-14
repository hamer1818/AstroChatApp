# AstroChatApp 🚀

[English](README.md) | [Türkçe](README.tr.md)

![Lisans](https://img.shields.io/github/license/hamer1818/AstroChatApp)
![Yıldızlar](https://img.shields.io/github/stars/hamer1818/AstroChatApp?style=social)
![GitHub çatalları](https://img.shields.io/github/forks/hamer1818/AstroChatApp.svg?style=social&label=Fork)
![GitHub takipçileri](https://img.shields.io/github/watchers/hamer1818/AstroChatApp.svg?style=social&label=Watch)
![GitHub repo boyutu](https://img.shields.io/github/repo-size/hamer1818/AstroChatApp.svg)
![Diller](https://img.shields.io/github/languages/count/hamer1818/AstroChatApp.svg)
![Ana Dil](https://img.shields.io/github/languages/top/hamer1818/AstroChatApp.svg)

AstroChatApp, ön yüzünde Astro ve arka yüzünde Python'un Flask-SocketIO'sunu kullanan gerçek zamanlı bir sohbet uygulamasıdır. Kullanıcı avatarları, çevrimiçi kullanıcı takibi, emoji desteği gibi özelliklerle kesintisiz iletişim sunar.

## İçindekiler

- [Demo](#demo)
- [Özellikler](#özellikler)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
  - [Ön Yüz](#ön-yüz)
  - [Arka Yüz](#arka-yüz)
- [Kurulum](#kurulum)
  - [Ön Koşullar](#ön-koşullar)
  - [Arka Yüz Kurulumu](#arka-yüz-kurulumu)
  - [Ön Yüz Kurulumu](#ön-yüz-kurulumu)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)
- [İletişim](#iletişim)
- [Teşekkürler](#teşekkürler)

## Demo

![AstroChatApp Demo](/public/ss.jpeg)

## Özellikler
- **Gerçek Zamanlı İletişim**: Socket.IO ile desteklenen anlık mesajlaşma
- **Kullanıcı Avatarları**: Kullanıcı avatarlarını yükleme ve görüntüleme
- **Çevrimiçi Kullanıcı Listesi**: Çevrimiçi kullanıcıları görüntüleme
- **Emoji Desteği**: Konuşmalarınıza emoji ekleme
- **Duyarlı Tasarım**: Hem masaüstü hem mobil cihazlar için optimize edilmiş
- **Kullanıcı Dostu Arayüz**: Tailwind CSS ile oluşturulmuş temiz ve sezgisel kullanıcı arayüzü

## Kullanılan Teknolojiler

### Ön Yüz
- [Astro](https://astro.build/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Socket.IO Client](https://socket.io/)
- [Emoji Picker Element](https://www.npmjs.com/package/emoji-picker-element)

### Arka Yüz
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)

## Kurulum

### Ön Koşullar
- **Node.js** (v14 veya üzeri)
- **npm** (v6 veya üzeri)
- **Python** (v3.7 veya üzeri)
- **pip** (Python paket yükleyicisi)

### Arka Yüz Kurulumu
1. Depoyu klonlayın:
    ```bash
    git clone https://github.com/hamer1818/AstroChatApp.git
    cd AstroChatApp
    ```
2. `server` dizinine gidin:
    ```bash
    cd server
    ```
3. Sanal ortam oluşturun:
    ```bash
    python -m venv venv
    ```
4. Sanal ortamı etkinleştirin:
    - Windows için:
        ```bash
        venv\Scripts\activate
        ```
    - macOS/Linux için:
        ```bash
        source venv/bin/activate
        ```
5. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
6. Flask sunucusunu başlatın:
    ```bash
    python main.py
    ```
7. Sunucu artık `http://localhost:5000` adresinde çalışıyor olmalı.

### Ön Yüz Kurulumu
1. Yeni bir terminal açın ve projenin `kök` dizinine gidin.
2. Gerekli bağımlılıkları yükleyin:
    ```bash
    npm install
    ```
3. Astro geliştirme sunucusunu başlatın:
    ```bash
    npm start
    ```
4. Ön yüz artık `http://localhost:4321` adresinde çalışıyor olmalı.

## Kullanım
1. **Uygulamayı tarayıcınızda açın**:
    - http://localhost:4321 adresine gidin.
2. Profilinizi Ayarlayın:
    - Bir avatar resmi yükleyin
    - Benzersiz bir kullanıcı adı girin
    - Sohbet odasına girmek için **Sohbete Katıl**'a tıklayın
3. Sohbete Başlayın:
    - Alttaki giriş alanına mesajınızı yazın
    - Mesajı göndermek için **Enter**'a basın
    - Mesajlarınıza emoji eklemek için emoji seçiciyi kullanın

## İletişim
- **Hamza ORTATEPE** - [https://hamzaortatepe.com.tr](https://hamzaortatepe.com.tr/)
- **E-posta** - [hortatepe2002@gmail.com](mailto:hortatepe2002@gmail.com)
- **Github** - [https://github.com/hamer1818/AstroChatApp](https://github.com/hamer1818/AstroChatApp)

## Teşekkürler
- [Astro](https://astro.build/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [Socket.IO](https://socket.io/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Emoji Picker Element](https://www.npmjs.com/package/emoji-picker-element)

---

``Hamza ORTATEPE tarafından ❤️ ile yapıldı``