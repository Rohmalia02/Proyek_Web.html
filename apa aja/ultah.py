<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selamat Ulang Tahun</title>
    <style>
        body {
            text-align: center;
            background-color: #bbdefb;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        h1 {
            color: #0d47a1;
            margin-top: 20px;
            font-size: 28px;
        }
        .hidden {
            display: none;
        }
        .cake {
            width: 200px;
            height: 200px;
            background: url('https://i.imgur.com/8B0BMpR.png') no-repeat center;
            background-size: cover;
            margin: 20px auto;
            border-radius: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
        }
        .button {
            padding: 12px 25px;
            font-size: 18px;
            color: white;
            background-color: #1e88e5;
            border: none;
            cursor: pointer;
            border-radius: 15px;
            margin-top: 10px;
            font-weight: bold;
            transition: 0.3s;
        }
        .button:hover {
            background-color: #0d47a1;
            transform: scale(1.1);
        }
        .candle {
            width: 10px;
            height: 40px;
            background: #ffeb3b;
            position: relative;
            margin: 0 auto;
            border-radius: 5px;
        }
        .flame {
            width: 12px;
            height: 22px;
            background: orange;
            border-radius: 50%;
            position: absolute;
            top: -22px;
            left: -1px;
            animation: flicker 1s infinite alternate;
        }
        @keyframes flicker {
            0% { opacity: 1; transform: scale(1); }
            100% { opacity: 0.6; transform: scale(1.1); }
        }
    </style>
</head>
<body>
    <div id="page1">
        <h1>Selamat Ulang Tahun</h1>
        <button class="button" onclick="startCelebration()">Mulai Perayaan</button>
    </div>

    <div id="page2" class="hidden">
        <h1>Masukkan Nama Anda</h1>
        <input type="text" id="nameInput" placeholder="Nama Anda">
        <button class="button" onclick="nextPage(3)">Lanjut</button>
    </div>

    <div id="page3" class="hidden">
        <h1>Selamat Ulang Tahun, <span id="userName"></span></h1>
        <button class="button" onclick="nextPage(4)">Lanjut</button>
    </div>

    <div id="page4" class="hidden">
        <h1>Semoga semua impianmu terkabul</h1>
        <p>Semoga sukses dan lolos SNBT tahun ini</p>
        <button class="button" onclick="nextPage(5)">Lanjut</button>
    </div>

    <div id="page5" class="hidden">
        <h1>Selamat Ulang Tahun</h1>
        <div class="cake">
            <div class="candle">
                <div class="flame"></div>
            </div>
        </div>
    </div>

    <audio id="birthdaySong" src="https://www.fesliyanstudios.com/play-mp3/387" preload="auto"></audio>

    <script>
        function startCelebration() {
            playSong();
            nextPage(2);
        }

        function nextPage(page) {
            document.querySelectorAll('div').forEach(div => div.classList.add('hidden'));
            document.getElementById(`page${page}`).classList.remove('hidden');
            if (page === 3) {
                const name = document.getElementById("nameInput").value;
                document.getElementById("userName").textContent = name;
            }
        }

        function playSong() {
            document.getElementById('birthdaySong').play();
        }
    </script>
</body>
</html>
