#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║  🟠  ORANGE CRYSTAL TIKTOK 2026 - GLASS EDITION  🟠  ║
║     Ultimate Version - 9 Files - 1000+ Lines           ║
║                                                        ║
║  🟠  Firebase: comk-4302e                             ║
║  ☁️   Cloudinary: dt0tkbtzw / xk20_k                  ║
║  👑  Admin: jasim28v@gmail.com                        ║
║  👾  Avatars: DiceBear Big Smile (Random)              ║
║  💎  Design: Orange Crystal Glass                     ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 🟠 CONFIGURATION - الإعدادات
# ═══════════════════════════════════════════════════════════

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyBB4aIL-7cXL_FbsHT2Jj-T70EmF9Chc0A",
    "authDomain": "comk-4302e.firebaseapp.com",
    "databaseURL": "https://comk-4302e-default-rtdb.firebaseio.com",
    "projectId": "comk-4302e",
    "storageBucket": "comk-4302e.firebasestorage.app",
    "messagingSenderId": "817565218754",
    "appId": "1:817565218754:web:874fad2b98ee5789b5c85b",
    "measurementId": "G-DR25TWGM6M"
}

CLOUD_NAME = "dt0tkbtzw"
UPLOAD_PRESET = "xk20_k"
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"

# 🟠 Orange Color Palette
ORANGE_COLORS_JS = """[
    "linear-gradient(135deg, #ea580c, #f97316, #fb923c)",
    "linear-gradient(135deg, #c2410c, #ea580c, #f97316)",
    "linear-gradient(135deg, #9a3412, #c2410c, #ea580c)",
    "linear-gradient(135deg, #f97316, #fb923c, #fdba74)",
    "linear-gradient(135deg, #431407, #9a3412, #ea580c)"
]"""

# ═══════════════════════════════════════════════════════════
# 🟠 UTILITY - دوال مساعدة
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    """حفظ ملف وحساب عدد الأسطر"""
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    """طباعة عنوان القسم"""
    print(f"\n{'='*60}")
    print(f"  🟠 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🟠 1. firebase-config.js - إعدادات Firebase + Cloudinary
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 🟠 ORANGE CRYSTAL 2026 - Configuration
// Firebase: comk-4302e | Cloudinary: dt0tkbtzw

const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";

// 🟠 Orange Crystal Settings
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {ORANGE_COLORS_JS};

// 🟠 App Info
const APP_NAME = "ORANGE CRYSTAL";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#f97316";
const SECONDARY_COLOR = "#fb923c";

console.log('🟠 %c'+APP_NAME+' v'+APP_VERSION+' Ready', 'color: #f97316; font-size: 16px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 🟠 2. auth.html - تسجيل الدخول والاشتراك
# ═══════════════════════════════════════════════════════════

def build_auth():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            min-height:100vh;
            background:radial-gradient(ellipse at top, #431407, #1a0a02, #000);
            display:flex;align-items:center;justify-content:center;
            font-family:'Segoe UI',sans-serif;overflow:hidden;
        }
        .bg-orb{
            position:fixed;border-radius:50%;filter:blur(130px);opacity:0.4;
            animation:orbFloat 20s infinite alternate;
        }
        .bg-orb:nth-child(1){width:400px;height:400px;background:#f97316;top:-100px;left:-100px}
        .bg-orb:nth-child(2){width:350px;height:350px;background:#fb923c;bottom:-100px;right:-100px;animation-delay:5s}
        .bg-orb:nth-child(3){width:300px;height:300px;background:#ea580c;top:50%;left:50%;animation-delay:10s}
        @keyframes orbFloat{0%{transform:translate(0,0) scale(1)}100%{transform:translate(50px,-50px) scale(1.3)}}

        .card{
            position:relative;z-index:1;width:90%;max-width:420px;
            background:rgba(249,115,22,0.03);
            backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
            border-radius:32px;padding:36px 24px;
            border:1px solid rgba(249,115,22,0.2);
            box-shadow:0 30px 70px rgba(249,115,22,0.15),inset 0 0 30px rgba(249,115,22,0.02);
            animation:fadeUp 0.8s ease;
        }
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}

        .logo{
            width:70px;height:70px;margin:0 auto 20px;
            background:linear-gradient(135deg, rgba(249,115,22,0.3), rgba(251,146,60,0.3));
            border-radius:20px;display:flex;align-items:center;justify-content:center;
            font-size:36px;border:1px solid rgba(249,115,22,0.2);
            box-shadow:0 15px 40px rgba(249,115,22,0.3);
        }
        h1{text-align:center;font-size:36px;font-weight:900;background:linear-gradient(to bottom, #fff, #fdba74);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}
        .sub{text-align:center;color:rgba(255,255,255,0.5);font-size:13px;margin-bottom:20px}

        .tabs{display:flex;gap:4px;background:rgba(249,115,22,0.06);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:500}
        .tab.active{background:linear-gradient(135deg, #f97316, #ea580c);color:#fff;box-shadow:0 8px 20px rgba(249,115,22,0.4)}

        .form{display:none;animation:fadeIn 0.4s ease}
        .form.active{display:block}
        @keyframes fadeIn{from{opacity:0}to{opacity:1}}

        input{
            width:100%;padding:15px 18px;margin:8px 0;
            border-radius:50px;background:rgba(249,115,22,0.04);
            border:1px solid rgba(249,115,22,0.15);color:#fff;
            font-size:14px;outline:none;transition:all 0.4s;
        }
        input:focus{border-color:rgba(249,115,22,0.6);box-shadow:0 0 20px rgba(249,115,22,0.1);background:rgba(249,115,22,0.08)}
        input::placeholder{color:rgba(255,255,255,0.3)}

        button{
            width:100%;padding:15px;margin-top:18px;
            background:linear-gradient(135deg, #f97316, #ea580c);
            border:none;border-radius:50px;color:#fff;
            font-weight:bold;font-size:15px;cursor:pointer;
            transition:all 0.3s;box-shadow:0 10px 30px rgba(249,115,22,0.4);
        }
        button:hover{transform:translateY(-2px);box-shadow:0 20px 40px rgba(249,115,22,0.6)}
        button:active{transform:scale(0.97)}
        button:disabled{opacity:0.5;pointer-events:none}

        .msg{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}
        .msg.success{color:#4ade80}

        .link{text-align:center;margin-top:20px;color:rgba(255,255,255,0.5);font-size:13px}
        .link a{color:#fb923c;text-decoration:none;font-weight:600}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>

    <div class="card">
        <div class="logo">🟠</div>
        <h1>ORANGE CRYSTAL</h1>
        <p class="sub">TikTok 2026 Ultra Pro</p>

        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchTab('login')">دخول</button>
            <button class="tab" id="tabRegister" onclick="switchTab('register')">اشتراك</button>
        </div>

        <!-- Login Form -->
        <div id="formLogin" class="form active">
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
            <button id="btnLogin" onclick="doLogin()">🚀 تسجيل الدخول</button>
            <div class="msg" id="loginMsg"></div>
        </div>

        <!-- Register Form -->
        <div id="formRegister" class="form">
            <input type="text" id="regName" placeholder="👤 اسم المستخدم" autocomplete="username">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
            <button id="btnRegister" onclick="doRegister()">🟠 إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>

    <script src="firebase-config.js"></script>
    <script>
        // ═══════════════════════════════════════
        // 🟠 TAB SWITCHING - تبديل التبويبات
        // ═══════════════════════════════════════
        function switchTab(type){
            // Reset all tabs
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');

            // Clear messages
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';

            // Show selected tab
            if(type === 'login'){
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            } else {
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }
        }

        // ═══════════════════════════════════════
        // 🟠 LOGIN - تسجيل الدخول
        // ═══════════════════════════════════════
        async function doLogin(){
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');

            if(!email || !password){
                msg.innerText = '❌ الرجاء ملء جميع الحقول';
                return;
            }

            btn.disabled = true;
            btn.innerHTML = '⏳ جاري الدخول...';
            msg.innerText = '';
            msg.className = 'msg';

            try {
                await auth.signInWithEmailAndPassword(email, password);
                console.log('🟢 Login successful');
                window.location.replace('index.html');
            } catch(error) {
                console.error('Login error:', error.code);
                btn.disabled = false;
                btn.innerHTML = '🚀 تسجيل الدخول';

                switch(error.code) {
                    case 'auth/user-not-found':
                        msg.innerText = '❌ لا يوجد حساب بهذا البريد';
                        break;
                    case 'auth/wrong-password':
                    case 'auth/invalid-credential':
                        msg.innerText = '❌ كلمة المرور غير صحيحة';
                        break;
                    case 'auth/invalid-email':
                        msg.innerText = '❌ بريد إلكتروني غير صالح';
                        break;
                    case 'auth/too-many-requests':
                        msg.innerText = '❌ محاولات كثيرة، حاول لاحقاً';
                        break;
                    default:
                        msg.innerText = '❌ خطأ: ' + error.message;
                }
            }
        }

        // ═══════════════════════════════════════
        // 🟠 REGISTER - إنشاء حساب
        // ═══════════════════════════════════════
        async function doRegister(){
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');

            // Validation
            if(!username || !email || !password){
                msg.innerText = '❌ الرجاء ملء جميع الحقول';
                return;
            }
            if(username.length < 3){
                msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل';
                return;
            }
            if(password.length < 6){
                msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل';
                return;
            }
            if(!email.includes('@') || !email.includes('.')){
                msg.innerText = '❌ بريد إلكتروني غير صالح';
                return;
            }

            btn.disabled = true;
            btn.innerHTML = '⏳ جاري إنشاء الحساب...';
            msg.innerText = '';
            msg.className = 'msg';

            try {
                // Step 1: Create auth account
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                console.log('🟢 Auth created:', uid);

                // Step 2: Generate random avatar
                const avatarUrl = DICEBEAR_URL + '?seed=' + uid;
                const coverColor = COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)];

                // Step 3: Prepare user data
                const userData = {
                    username: username,
                    email: email,
                    bio: '',
                    avatarUrl: avatarUrl,
                    hasCustomAvatar: false,
                    coverColor: coverColor,
                    followers: {},
                    following: {},
                    totalLikes: 0,
                    isVerified: false,
                    verifiedAt: null,
                    verifiedBy: null,
                    banned: false,
                    createdAt: Date.now(),
                    lastSeen: Date.now()
                };

                // Step 4: Save to database
                await db.ref('users/' + uid).set(userData);
                console.log('🟢 User data saved');

                // Step 5: Success
                msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
                msg.className = 'msg success';

                setTimeout(() => {
                    window.location.replace('index.html');
                }, 800);

            } catch(error) {
                console.error('Register error:', error.code);
                btn.disabled = false;
                btn.innerHTML = '🟠 إنشاء حساب';
                msg.className = 'msg';

                switch(error.code) {
                    case 'auth/email-already-in-use':
                        msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل';
                        break;
                    case 'auth/weak-password':
                        msg.innerText = '❌ كلمة المرور ضعيفة جداً';
                        break;
                    case 'auth/invalid-email':
                        msg.innerText = '❌ بريد إلكتروني غير صالح';
                        break;
                    case 'auth/operation-not-allowed':
                        msg.innerText = '❌ التسجيل غير مفعل، راجع إعدادات Firebase';
                        break;
                    default:
                        msg.innerText = '❌ خطأ: ' + (error.message || 'غير معروف');
                }
            }
        }

        // ═══════════════════════════════════════
        // 🟠 ENTER KEY SUPPORT
        // ═══════════════════════════════════════
        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keydown', function(e) {
                if(e.key === 'Enter') {
                    e.preventDefault();
                    if(document.getElementById('formLogin').classList.contains('active')) {
                        doLogin();
                    } else {
                        doRegister();
                    }
                }
            });
        });

        // ═══════════════════════════════════════
        // 🟠 AUTO REDIRECT IF LOGGED IN
        // ═══════════════════════════════════════
        auth.onAuthStateChanged(user => {
            if(user) {
                console.log('🟢 Already logged in, redirecting...');
                window.location.replace('index.html');
            }
        });

        console.log('🟠 Orange Crystal Auth Ready');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 3. index.html - الرئيسية (كل الكود داخلها)
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{
            --glass:rgba(249,115,22,0.03);
            --border:rgba(249,115,22,0.12);
            --accent:#f97316;
            --accent2:#fb923c;
            --bg:#0a0400;
        }
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            font-family:'Segoe UI',sans-serif;
            background:var(--bg);
            color:#fff;
            height:100vh;overflow:hidden;
            -webkit-tap-highlight-color:transparent;
            user-select:none;
        }

        /* LOADER */
        #loaderScreen{
            position:fixed;inset:0;z-index:9999;
            background:radial-gradient(ellipse at top, #431407, #1a0a02, #000);
            display:flex;align-items:center;justify-content:center;
            flex-direction:column;gap:16px;
        }
        .spinner-big{
            width:50px;height:50px;
            border:4px solid rgba(249,115,22,0.2);
            border-top-color:var(--accent);
            border-radius:50%;
            animation:spin 0.8s linear infinite;
        }
        @keyframes spin{to{transform:rotate(360deg)}}

        #mainApp{display:none;height:100vh;position:relative}

        /* TOP BAR */
        .topbar{
            position:fixed;top:0;left:0;right:0;z-index:100;
            display:flex;justify-content:space-between;align-items:center;
            padding:12px 20px;
            background:rgba(10,4,0,0.7);
            backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
            border-bottom:1px solid var(--border);
        }
        .logo-icon{
            width:36px;height:36px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:10px;display:flex;align-items:center;justify-content:center;
            font-weight:900;font-size:14px;
            box-shadow:0 8px 20px rgba(249,115,22,0.5);
        }
        .logo-text{
            font-weight:800;font-size:17px;
            background:linear-gradient(to bottom,#fff,#fdba74);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            margin-left:8px;
        }
        .tabs{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}
        .tab{
            background:none;border:none;color:rgba(255,255,255,0.5);
            padding:7px 16px;cursor:pointer;border-radius:25px;
            font-size:13px;font-weight:500;transition:all 0.3s;
        }
        .tab.active{background:rgba(249,115,22,0.25);color:#fff}
        .top-icons{display:flex;gap:16px}
        .top-icon{
            background:none;border:none;color:rgba(255,255,255,0.7);
            font-size:18px;cursor:pointer;transition:color 0.3s;
        }
        .top-icon:hover{color:var(--accent2)}

        /* VIDEOS */
        .videos-wrap{
            height:100vh;overflow-y:scroll;
            scroll-snap-type:y mandatory;
            scrollbar-width:none;-ms-overflow-style:none;
        }
        .videos-wrap::-webkit-scrollbar{display:none}
        .vid-card{height:100vh;scroll-snap-align:start;position:relative;background:#000}
        .vid-card video{width:100%;height:100%;object-fit:cover}

        /* VIDEO INFO */
        .vid-info{
            position:absolute;bottom:90px;left:14px;right:80px;z-index:20;
            text-shadow:0 2px 10px rgba(0,0,0,0.8);
        }
        .author-row{display:flex;align-items:center;gap:10px;margin-bottom:6px}
        .author-avatar{
            width:46px;height:46px;border-radius:50%;overflow:hidden;
            cursor:pointer;border:2px solid rgba(249,115,22,0.4);
            box-shadow:0 8px 20px rgba(0,0,0,0.4);
        }
        .author-avatar img{width:100%;height:100%;object-fit:cover}
        .author-name{
            font-weight:700;font-size:15px;cursor:pointer;
            display:flex;align-items:center;gap:6px;flex-wrap:wrap;
        }
        .verified-badge{color:#fb923c;font-size:14px}
        .btn-follow{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            padding:5px 14px;border-radius:20px;font-size:11px;
            font-weight:700;border:none;color:#fff;cursor:pointer;
            box-shadow:0 4px 15px rgba(249,115,22,0.4);
        }
        .caption{font-size:14px;margin-bottom:5px;line-height:1.4}
        .tag{color:var(--accent2);cursor:pointer;font-weight:500}
        .music{font-size:12px;opacity:0.8;display:flex;align-items:center;gap:6px;cursor:pointer}

        /* SIDE ACTIONS */
        .side-btns{
            position:absolute;right:14px;bottom:130px;
            display:flex;flex-direction:column;gap:22px;z-index:20;
        }
        .sbtn{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:#fff;cursor:pointer;
            font-size:10px;transition:transform 0.15s;
        }
        .sbtn:active{transform:scale(0.85)}
        .sbtn i{font-size:28px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}
        .sbtn.liked i{color:var(--accent)}
        .sbtn .cnt{font-weight:700;font-size:11px}

        /* BOTTOM NAV */
        .nav-bottom{
            position:fixed;bottom:0;left:0;right:0;
            display:flex;justify-content:space-around;align-items:center;
            padding:8px 0 20px;
            background:rgba(10,4,0,0.8);
            backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
            z-index:100;border-top:1px solid var(--border);
        }
        .nav-item{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:rgba(255,255,255,0.5);
            font-size:10px;cursor:pointer;transition:all 0.3s;
        }
        .nav-item i{font-size:22px}
        .nav-item.active{color:var(--accent2)}
        .btn-add{
            width:48px;height:48px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            margin-top:-24px;cursor:pointer;
            box-shadow:0 10px 30px rgba(249,115,22,0.6);
            border:none;color:#fff;font-size:20px;
        }

        /* TOAST */
        .toast{
            position:fixed;bottom:100px;left:50%;transform:translateX(-50%);
            background:rgba(10,4,0,0.9);padding:10px 22px;border-radius:50px;
            z-index:1000;opacity:0;transition:opacity 0.3s;pointer-events:none;
            border:1px solid var(--border);font-size:13px;
        }
        .toast.show{opacity:1}

        /* OVERLAY */
        .overlay{
            position:fixed;inset:0;background:rgba(10,4,0,0.97);
            backdrop-filter:blur(40px);z-index:400;overflow-y:auto;
        }
        .overlay-header{
            display:flex;justify-content:space-between;align-items:center;
            padding:16px;border-bottom:1px solid var(--border);
            position:sticky;top:0;background:rgba(10,4,0,0.8);
        }
        .btn-close{
            background:rgba(249,115,22,0.1);border:1px solid var(--border);
            color:#fff;width:36px;height:36px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            cursor:pointer;font-size:18px;transition:all 0.3s;
        }
        .btn-close:hover{background:rgba(249,115,22,0.2)}
    </style>
</head>
<body>

<!-- LOADER -->
<div id="loaderScreen">
    <div class="spinner-big"></div>
    <p style="color:rgba(255,255,255,0.6);font-size:15px">🟠 جاري التحميل...</p>
</div>

<!-- MAIN APP -->
<div id="mainApp">
    <!-- TOP BAR -->
    <div class="topbar">
        <div style="display:flex;align-items:center">
            <div class="logo-icon">🟠</div>
            <span class="logo-text">ORANGE CRYSTAL</span>
        </div>
        <div class="tabs">
            <button class="tab" onclick="switchFeed('following')">متابَعين</button>
            <button class="tab active" onclick="switchFeed('forYou')">لك</button>
        </div>
        <div class="top-icons">
            <i class="fas fa-search top-icon" onclick="openSearch()"></i>
            <i class="fas fa-bell top-icon" onclick="openNotifs()"></i>
        </div>
    </div>

    <!-- VIDEOS -->
    <div class="videos-wrap" id="videosWrap">
        <div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px">
            <i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#f97316"></i>
            <p>لا توجد فيديوهات بعد</p>
            <p style="font-size:12px;opacity:0.5">ارفع أول فيديو!</p>
        </div>
    </div>

    <!-- BOTTOM NAV -->
    <div class="nav-bottom">
        <button class="nav-item active"><i class="fas fa-home"></i><span>الرئيسية</span></button>
        <button class="nav-item" onclick="openSearch()"><i class="fas fa-search"></i><span>بحث</span></button>
        <a href="upload.html" class="btn-add"><i class="fas fa-plus"></i></a>
        <a href="chat.html" class="nav-item"><i class="fas fa-envelope"></i><span>رسائل</span></a>
        <a href="profile.html" class="nav-item"><i class="fas fa-user"></i><span>ملفي</span></a>
    </div>

    <!-- TOAST -->
    <div id="toast" class="toast">✅ تم النسخ</div>
</div>

<script src="firebase-config.js"></script>
<script>
    // ═══════════════════════════════════════
    // 🟠 GLOBAL VARIABLES
    // ═══════════════════════════════════════
    let currentUser = null;
    let currentUserData = null;
    let allUsers = {};
    let allVideos = [];
    let allSounds = {};
    let isMuted = true;
    let currentFeed = 'forYou';
    let currentShareUrl = null;

    // ═══════════════════════════════════════
    // 🟠 AUTH STATE CHECK
    // ═══════════════════════════════════════
    auth.onAuthStateChanged(async (user) => {
        if (!user) {
            window.location.replace('auth.html');
            return;
        }

        currentUser = user;
        console.log('🟢 User:', user.uid);

        // Load user data
        try {
            const snap = await db.ref('users/' + user.uid).get();
            if (snap.exists()) {
                currentUserData = { uid: user.uid, ...snap.val() };
            }
        } catch(e) {
            console.error('Error loading user:', e);
        }

        // Load all users
        db.ref('users').on('value', s => {
            allUsers = s.val() || {};
        });

        // Load videos
        db.ref('videos').on('value', s => {
            const data = s.val();
            if (!data) {
                allVideos = [];
                allSounds = {};
            } else {
                allVideos = [];
                allSounds = {};
                Object.entries(data).forEach(([key, value]) => {
                    const video = { id: key, ...value };
                    allVideos.push(video);
                    if (video.music) {
                        allSounds[video.music] = (allSounds[video.music] || 0) + 1;
                    }
                });
                allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
            }
            renderVideos();
        });

        // Presence
        db.ref('presence/' + user.uid).set(true);
        db.ref('presence/' + user.uid).onDisconnect().remove();

        // Show app
        document.getElementById('loaderScreen').style.display = 'none';
        document.getElementById('mainApp').style.display = 'block';
        console.log('🟠 App Ready');
    });

    // ═══════════════════════════════════════
    // 🟠 RENDER VIDEOS
    // ═══════════════════════════════════════
    function renderVideos() {
        const container = document.getElementById('videosWrap');
        if (!container) return;

        let filtered = currentFeed === 'forYou'
            ? allVideos
            : allVideos.filter(v => currentUserData?.following?.[v.sender]);

        if (!filtered.length) {
            container.innerHTML = `
                <div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px">
                    <i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#f97316"></i>
                    <p>${currentFeed === 'forYou' ? 'لا توجد فيديوهات بعد' : 'تابع مستخدمين لرؤية فيديوهاتهم'}</p>
                </div>`;
            return;
        }

        container.innerHTML = '';

        filtered.forEach(video => {
            const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
            const user = allUsers[video.sender] || { username: video.senderName || 'مستخدم' };
            const isFollowing = currentUserData?.following && currentUserData.following[video.sender];
            const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
            const caption = (video.description || '').replace(/#(\w+)/g, '<span class="tag">#$1</span>');
            const avatarUrl = user.avatarUrl || (DICEBEAR_URL + '?seed=' + video.sender);

            const div = document.createElement('div');
            div.className = 'vid-card';
            div.innerHTML = `
                <video loop playsinline muted data-src="${video.url}" poster="${video.thumbnail || ''}"></video>
                <div class="vid-info">
                    <div class="author-row">
                        <div class="author-avatar" onclick="window.location.href='profile.html'">
                            <img src="${avatarUrl}" alt="avatar">
                        </div>
                        <div class="author-name">
                            <span onclick="window.location.href='profile.html'">@${user.username}</span>
                            ${user.isVerified ? '<span class="verified-badge">✅</span>' : ''}
                            ${currentUser?.uid !== video.sender ?
                                `<button class="btn-follow" onclick="toggleFollow('${video.sender}', this)">${isFollowing ? 'متابع' : 'متابعة'}</button>`
                                : ''}
                        </div>
                    </div>
                    <div class="caption">${caption}</div>
                    <div class="music"><i class="fas fa-music"></i> ${video.music || 'Original Sound'}</div>
                </div>
                <div class="side-btns">
                    <button class="sbtn" onclick="toggleMute()">
                        <i class="fas ${isMuted ? 'fa-volume-mute' : 'fa-volume-up'}"></i>
                    </button>
                    <button class="sbtn like-btn ${isLiked ? 'liked' : ''}" onclick="toggleLike('${video.id}', this)">
                        <i class="fas fa-heart"></i><span class="cnt">${video.likes || 0}</span>
                    </button>
                    <button class="sbtn" onclick="openComments('${video.id}')">
                        <i class="fas fa-comment"></i><span class="cnt">${commentsCount}</span>
                    </button>
                    <button class="sbtn" onclick="openShare('${video.url}')">
                        <i class="fas fa-share"></i>
                    </button>
                </div>`;

            const videoEl = div.querySelector('video');
            videoEl.addEventListener('dblclick', e => {
                e.stopPropagation();
                const likeBtn = div.querySelector('.like-btn');
                if (likeBtn) toggleLike(video.id, likeBtn);
            });

            container.appendChild(div);
        });

        initVideoObserver();
    }

    // ═══════════════════════════════════════
    // 🟠 VIDEO OBSERVER
    // ═══════════════════════════════════════
    function initVideoObserver() {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                const video = entry.target.querySelector('video');
                if (entry.isIntersecting) {
                    if (!video.src) video.src = video.dataset.src;
                    video.muted = isMuted;
                    video.play().catch(() => {});
                } else {
                    video.pause();
                }
            });
        }, { threshold: 0.65 });

        document.querySelectorAll('.vid-card').forEach(seg => observer.observe(seg));
    }

    // ═══════════════════════════════════════
    // 🟠 UTILITY FUNCTIONS
    // ═══════════════════════════════════════
    function toggleMute() {
        isMuted = !isMuted;
        document.querySelectorAll('video').forEach(v => v.muted = isMuted);
    }

    function switchFeed(feed) {
        currentFeed = feed;
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        event.target.classList.add('active');
        renderVideos();
    }

    // ═══════════════════════════════════════
    // 🟠 LIKE
    // ═══════════════════════════════════════
    async function toggleLike(videoId, btn) {
        if (!currentUser) return;
        const ref = db.ref('videos/' + videoId);
        const snap = await ref.get();
        const video = snap.val();
        if (!video) return;

        let likes = video.likes || 0;
        let likedBy = video.likedBy || {};

        if (likedBy[currentUser.uid]) {
            likes--;
            delete likedBy[currentUser.uid];
        } else {
            likes++;
            likedBy[currentUser.uid] = true;
        }

        await ref.update({ likes, likedBy });
        btn.classList.toggle('liked');
        const countSpan = btn.querySelector('.cnt');
        if (countSpan) countSpan.innerText = likes;
    }

    // ═══════════════════════════════════════
    // 🟠 FOLLOW
    // ═══════════════════════════════════════
    async function toggleFollow(userId, btn) {
        if (!currentUser || currentUser.uid === userId) return;
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + userId);
        const targetRef = db.ref('users/' + userId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();

        if (snap.exists()) {
            await userRef.remove();
            await targetRef.remove();
            btn.innerText = 'متابعة';
        } else {
            await userRef.set(true);
            await targetRef.set(true);
            btn.innerText = 'متابع';
        }
    }

    // ═══════════════════════════════════════
    // 🟠 SHARE
    // ═══════════════════════════════════════
    function openShare(url) {
        currentShareUrl = url;
        showOverlay('📤 مشاركة', `
            <div onclick="copyLink()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer;border-bottom:1px solid var(--border)">
                <i class="fas fa-link" style="color:#f97316;font-size:20px"></i><span>نسخ الرابط</span>
            </div>
            <div onclick="shareWA()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer;border-bottom:1px solid var(--border)">
                <i class="fab fa-whatsapp" style="color:#25D366;font-size:20px"></i><span>WhatsApp</span>
            </div>
            <div onclick="shareTG()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer">
                <i class="fab fa-telegram" style="color:#0088cc;font-size:20px"></i><span>Telegram</span>
            </div>
        `);
    }
    window.copyLink = function() {
        navigator.clipboard.writeText(currentShareUrl);
        const toast = document.getElementById('toast');
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2000);
        closeOverlay();
    };
    window.shareWA = function() {
        window.open('https://wa.me/?text=' + encodeURIComponent(currentShareUrl), '_blank');
        closeOverlay();
    };
    window.shareTG = function() {
        window.open('https://t.me/share/url?url=' + encodeURIComponent(currentShareUrl), '_blank');
        closeOverlay();
    };

    // ═══════════════════════════════════════
    // 🟠 COMMENTS
    // ═══════════════════════════════════════
    async function openComments(videoId) {
        const snap = await db.ref('videos/' + videoId + '/comments').get();
        const comments = snap.val() || {};
        let commentsList = '';

        Object.values(comments).reverse().forEach(c => {
            const user = allUsers[c.userId] || { username: c.username || 'مستخدم' };
            commentsList += `
                <div style="display:flex;gap:10px;padding:10px 0;border-bottom:1px solid rgba(249,115,22,0.1)">
                    <img src="${user.avatarUrl || (DICEBEAR_URL + '?seed=' + c.userId)}" style="width:36px;height:36px;border-radius:50%">
                    <div>
                        <div style="font-weight:600">@${user.username}</div>
                        <div style="font-size:13px;opacity:0.8;margin-top:2px">${c.text}</div>
                    </div>
                </div>`;
        });

        showOverlay('💬 التعليقات', commentsList + `
            <div style="display:flex;gap:8px;padding-top:12px">
                <input type="text" id="cmtInput" placeholder="أضف تعليقاً..."
                    style="flex:1;padding:12px;border-radius:30px;background:rgba(249,115,22,0.04);border:1px solid rgba(249,115,22,0.15);color:#fff;outline:none">
                <button onclick="addComment('${videoId}')"
                    style="background:linear-gradient(135deg,#f97316,#ea580c);border:none;color:#fff;padding:12px 20px;border-radius:30px;font-weight:700;cursor:pointer;white-space:nowrap">نشر</button>
            </div>
        `);
    }
    window.addComment = async function(videoId) {
        const input = document.getElementById('cmtInput');
        if (!input || !input.value.trim()) return;

        await db.ref('videos/' + videoId + '/comments').push({
            userId: currentUser.uid,
            username: currentUserData?.username || 'مستخدم',
            text: input.value,
            timestamp: Date.now()
        });

        closeOverlay();
        openComments(videoId);
    };

    // ═══════════════════════════════════════
    // 🟠 SEARCH
    // ═══════════════════════════════════════
    function openSearch() {
        showOverlay('🔍 بحث', `
            <input type="text" id="searchQ" onkeyup="doSearch()" placeholder="ابحث عن مستخدمين، فيديوهات..."
                style="width:100%;padding:14px;border-radius:30px;background:rgba(249,115,22,0.04);border:1px solid rgba(249,115,22,0.15);color:#fff;font-size:14px;outline:none;margin-bottom:16px">
            <div id="searchR"></div>
        `);

        window.doSearch = function() {
            const query = document.getElementById('searchQ').value.toLowerCase();
            const resultsDiv = document.getElementById('searchR');
            if (!query) { resultsDiv.innerHTML = ''; return; }

            const users = Object.values(allUsers).filter(u => u.username?.toLowerCase().includes(query));
            const vids = allVideos.filter(v => (v.description || '').toLowerCase().includes(query));

            resultsDiv.innerHTML = `
                ${users.length ? `
                    <div style="margin-bottom:16px">
                        <h4 style="font-size:12px;opacity:0.5;margin-bottom:8px">👥 مستخدمين</h4>
                        ${users.map(u => `
                            <div onclick="window.location.href='profile.html'" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(249,115,22,0.1)">
                                <img src="${u.avatarUrl || (DICEBEAR_URL + '?seed=' + (u.uid || u.username))}" style="width:40px;height:40px;border-radius:50%">
                                <div>@${u.username} ${u.isVerified ? '<span class="verified-badge">✅</span>' : ''}</div>
                            </div>
                        `).join('')}
                    </div>
                ` : ''}
                ${vids.length ? `
                    <div>
                        <h4 style="font-size:12px;opacity:0.5;margin-bottom:8px">🎬 فيديوهات</h4>
                        ${vids.map(v => `
                            <div onclick="window.open('${v.url}', '_blank')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(249,115,22,0.1)">
                                <i class="fas fa-play-circle" style="color:#f97316;font-size:20px"></i>
                                <span style="font-size:13px">${(v.description || 'فيديو').substring(0, 40)}</span>
                            </div>
                        `).join('')}
                    </div>
                ` : ''}
                ${!users.length && !vids.length ? '<div style="text-align:center;opacity:0.5;padding:30px">لا توجد نتائج</div>' : ''}
            `;
        };

        setTimeout(() => {
            const input = document.getElementById('searchQ');
            if (input) input.focus();
        }, 300);
    }

    // ═══════════════════════════════════════
    // 🟠 NOTIFICATIONS
    // ═══════════════════════════════════════
    function openNotifs() {
        showOverlay('🔔 الإشعارات', `
            <div style="text-align:center;opacity:0.5;padding:40px">
                <i class="fas fa-bell" style="font-size:48px;color:#f97316;margin-bottom:12px;display:block"></i>
                <p>لا توجد إشعارات حالياً</p>
            </div>
        `);
    }

    // ═══════════════════════════════════════
    // 🟠 OVERLAY SYSTEM
    // ═══════════════════════════════════════
    function showOverlay(title, content) {
        const id = 'overlay_' + Date.now();
        const html = `
            <div id="${id}" class="overlay">
                <div class="overlay-header">
                    <h3 style="font-weight:700">${title}</h3>
                    <button class="btn-close" onclick="document.getElementById('${id}').remove()">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div style="padding:16px">${content}</div>
            </div>`;
        document.body.insertAdjacentHTML('beforeend', html);
    }

    function closeOverlay() {
        const overlay = document.querySelector('[style*="z-index:400"], .overlay');
        if (overlay && overlay.id.startsWith('overlay_')) overlay.remove();
    }

    console.log('🟠 Orange Crystal Index Ready');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 4. profile.html - الملف الشخصي + لوحة الأدمن
# ═══════════════════════════════════════════════════════════

def build_profile():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | ملفي</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-storage-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(249,115,22,0.03);--border:rgba(249,115,22,0.12);--accent:#f97316;--accent2:#fb923c;--bg:#0a0400}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .cover{height:220px;position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:40px;transition:background 0.5s}
        .btn-back{position:fixed;top:16px;right:16px;background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid rgba(249,115,22,0.2);color:#fff;font-size:18px}
        .btn-cover{position:absolute;top:16px;left:16px;background:rgba(0,0,0,0.4);backdrop-filter:blur(10px);border:1px solid rgba(249,115,22,0.2);color:#fff;padding:8px 16px;border-radius:20px;font-size:12px;cursor:pointer;z-index:50}
        .avatar-lg{width:110px;height:110px;border-radius:50%;overflow:hidden;border:4px solid rgba(249,115,22,0.4);box-shadow:0 12px 40px rgba(249,115,22,0.2);cursor:pointer;position:relative;z-index:2}
        .avatar-lg img{width:100%;height:100%;object-fit:cover}
        .stats{display:flex;justify-content:center;gap:35px;margin:20px 0}
        .stat-val{font-size:22px;font-weight:700;color:#fb923c}
        .stat-lbl{font-size:11px;opacity:0.5}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:0 12px}
        .thumb{aspect-ratio:9/16;background:rgba(249,115,22,0.03);border-radius:8px;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden}
        .thumb i{font-size:24px;color:rgba(255,255,255,0.6);z-index:1}
        .btn{background:rgba(249,115,22,0.08);border:1px solid var(--border);padding:10px 24px;border-radius:30px;color:#fff;cursor:pointer;font-size:14px;margin:4px;transition:all 0.3s}
        .btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none}
        .verified-badge{color:#fb923c;font-size:16px;margin-right:4px}
        .admin-section{margin-top:20px;padding:16px;background:rgba(249,115,22,0.05);border-radius:16px;border:1px solid rgba(249,115,22,0.2)}
        .admin-stats{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:16px}
        .stat-card{background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center}
        .stat-num{font-size:22px;font-weight:700;color:#fb923c}
        .admin-item{display:flex;justify-content:space-between;align-items:center;background:rgba(0,0,0,0.3);padding:10px;border-radius:10px;margin-bottom:6px}
        .admin-avatar{width:32px;height:32px;border-radius:50%;overflow:hidden}
        .admin-avatar img{width:100%;height:100%;object-fit:cover}
        .admin-btn{padding:5px 12px;border-radius:20px;font-size:11px;cursor:pointer;border:none;font-weight:600;color:#fff}
        .btn-verify{background:rgba(251,146,60,0.3);color:#fb923c}
        .btn-delete{background:rgba(239,68,68,0.3);color:#f87171}
        .spinner{width:32px;height:32px;border:3px solid rgba(249,115,22,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .load-center{display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)}
    </style>
</head>
<body>
<div class="load-center" id="loader"><div class="spinner"></div><span>🟠 تحميل الملف...</span></div>

<div id="content" style="display:none">
    <div class="cover" id="profileCover">
        <button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button>
        <button class="btn-cover" onclick="changeCover()"><i class="fas fa-palette"></i> تغيير الغلاف</button>
        <div class="avatar-lg" id="avatarDisplay" onclick="document.getElementById('avatarInput').click()"><img src="" alt="avatar"></div>
    </div>
    <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">

    <div style="text-align:center;padding:0 20px">
        <h2 id="nameDisplay" style="font-size:22px;font-weight:700;margin-top:8px"></h2>
        <p id="bioDisplay" style="font-size:13px;opacity:0.5;margin-top:4px"></p>
        <div class="stats">
            <div><div class="stat-val" id="statFollowing">0</div><div class="stat-lbl">يتابع</div></div>
            <div><div class="stat-val" id="statFollowers">0</div><div class="stat-lbl">متابع</div></div>
            <div><div class="stat-val" id="statLikes">0</div><div class="stat-lbl">إعجابات</div></div>
        </div>
        <div id="actionsBar" style="margin:12px 0"></div>
    </div>

    <div style="padding:16px">
        <h3 style="font-weight:700;margin-bottom:12px">🎬 فيديوهاتي</h3>
        <div class="grid" id="videosGrid"></div>
    </div>

    <div id="adminSection" style="padding:16px;display:none"></div>
</div>

<script src="firebase-config.js"></script>
<script>
    let profileUserId = null;
    let currentUser = null;
    let currentUserData = null;
    let allVideos = [];
    let allUsers = {};

    auth.onAuthStateChanged(async u => {
        if (!u) { window.location.href = 'auth.html'; return; }
        currentUser = u;
        const snap = await db.ref('users/' + u.uid).get();
        if (snap.exists()) currentUserData = { uid: u.uid, ...snap.val() };
        profileUserId = u.uid;
        await loadAll();
        await loadProfile();
        document.getElementById('loader').style.display = 'none';
        document.getElementById('content').style.display = 'block';
    });

    async function loadAll() {
        const us = await db.ref('users').once('value'); allUsers = us.val() || {};
        const vs = await db.ref('videos').once('value'); allVideos = Object.entries(vs.val() || {}).map(([k, v]) => ({ id: k, ...v }));
    }

    async function loadProfile() {
        const u = allUsers[profileUserId] || currentUserData;
        if (!u) return;
        document.getElementById('nameDisplay').innerHTML = '@' + (u.username || 'مستخدم') + (u.isVerified ? ' <span class="verified-badge">✅</span>' : '');
        document.getElementById('bioDisplay').innerText = u.bio || '';
        document.getElementById('statFollowing').innerText = Object.keys(u.following || {}).length;
        document.getElementById('statFollowers').innerText = Object.keys(u.followers || {}).length;
        const uvs = allVideos.filter(v => v.sender === profileUserId);
        document.getElementById('statLikes').innerText = uvs.reduce((s, v) => s + (v.likes || 0), 0);
        document.getElementById('profileCover').style.background = u.coverColor || COVER_COLORS[0];
        document.querySelector('#avatarDisplay img').src = u.avatarUrl || (DICEBEAR_URL + '?seed=' + profileUserId);

        const g = document.getElementById('videosGrid'); g.innerHTML = '';
        if (!uvs.length) g.innerHTML = '<div style="text-align:center;opacity:0.5;padding:40px;grid-column:1/-1">لا توجد فيديوهات</div>';
        else uvs.forEach(v => { const d = document.createElement('div'); d.className = 'thumb'; d.innerHTML = `<i class="fas fa-play"></i>${v.thumbnail ? `<img src="${v.thumbnail}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.5">` : ''}`; d.onclick = () => window.open(v.url, '_blank'); g.appendChild(d); });

        document.getElementById('actionsBar').innerHTML = `
            <button class="btn btn-primary" onclick="editProfile()"><i class="fas fa-edit"></i> تعديل الملف</button>
            <button class="btn" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> تسجيل خروج</button>
        `;

        if (ADMIN_EMAILS.includes(currentUser.email)) {
            document.getElementById('adminSection').style.display = 'block';
            loadAdminPanel();
        }
    }

    async function loadAdminPanel() {
        const us = allUsers, vs = {}; allVideos.forEach(v => vs[v.id] = v);
        const tl = Object.values(vs).reduce((s, v) => s + (v.likes || 0), 0);
        const vu = Object.values(us).filter(u => u.isVerified).length;

        document.getElementById('adminSection').innerHTML = `
            <div class="admin-section">
                <h3 style="color:#fb923c;font-weight:700;margin-bottom:12px"><i class="fas fa-shield-alt"></i> لوحة تحكم الأدمن</h3>
                <div class="admin-stats">
                    <div class="stat-card"><div class="stat-num">${Object.keys(us).length}</div><div style="font-size:10px;opacity:0.5">مستخدمين</div></div>
                    <div class="stat-card"><div class="stat-num">${Object.keys(vs).length}</div><div style="font-size:10px;opacity:0.5">فيديوهات</div></div>
                    <div class="stat-card"><div class="stat-num">${tl}</div><div style="font-size:10px;opacity:0.5">إعجابات</div></div>
                    <div class="stat-card"><div class="stat-num">${vu}</div><div style="font-size:10px;opacity:0.5">موثقين</div></div>
                </div>
                <h4 style="font-weight:700;margin-bottom:8px;color:#fb923c"><i class="fas fa-check-circle"></i> توثيق الحسابات</h4>
                <div style="max-height:250px;overflow-y:auto">
                    ${Object.entries(us).filter(([id, u]) => !u.banned).slice(0, 15).map(([id, u]) => `
                        <div class="admin-item">
                            <div style="display:flex;align-items:center;gap:8px">
                                <div class="admin-avatar"><img src="${u.avatarUrl || (DICEBEAR_URL + '?seed=' + id)}"></div>
                                <span>@${u.username || '?'} ${u.isVerified ? '<span class="verified-badge">✅</span>' : ''}</span>
                            </div>
                            <button class="admin-btn btn-verify" onclick="toggleVerify('${id}')">${u.isVerified ? 'إلغاء التوثيق' : 'توثيق ✅'}</button>
                        </div>`).join('')}
                </div>
            </div>`;

        window.toggleVerify = async (id) => {
            if (confirm('تأكيد؟')) {
                const r = await db.ref('users/' + id).once('value');
                const d = r.val();
                await db.ref('users/' + id).update({ isVerified: !d.isVerified });
                alert('✅ تم');
                await loadAll();
                await loadProfile();
            }
        };
    }

    function editProfile() {
        const u = allUsers[profileUserId] || currentUserData;
        const name = prompt('اسم المستخدم:', u?.username || '');
        const bio = prompt('السيرة الذاتية:', u?.bio || '');
        if (name !== null && bio !== null) {
            db.ref('users/' + profileUserId).update({ username: name, bio: bio });
            loadAll().then(() => loadProfile());
        }
    }

    async function changeCover() {
        const idx = prompt(`اختر غلاف (1-${COVER_COLORS.length}):`);
        if (idx && idx >= 1 && idx <= COVER_COLORS.length) {
            const nc = COVER_COLORS[idx - 1];
            await db.ref('users/' + profileUserId + '/coverColor').set(nc);
            document.getElementById('profileCover').style.background = nc;
        }
    }

    async function uploadAvatar(inp) {
        const file = inp.files[0]; if (!file) return;
        const fd = new FormData(); fd.append('file', file); fd.append('upload_preset', UPLOAD_PRESET);
        const res = await fetch('https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', { method: 'POST', body: fd });
        const data = await res.json();
        await db.ref('users/' + profileUserId).update({ avatarUrl: data.secure_url, hasCustomAvatar: true });
        document.querySelector('#avatarDisplay img').src = data.secure_url;
    }
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 5. upload.html - رفع الفيديو
# ═══════════════════════════════════════════════════════════

def build_upload():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | رفع فيديو</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(249,115,22,0.03);--border:rgba(249,115,22,0.12);--accent:#f97316;--accent2:#fb923c;--bg:#0a0400}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(10,4,0,0.8);position:sticky;top:0;z-index:10}
        .btn-back{background:rgba(249,115,22,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .container{max-width:500px;margin:0 auto;padding:20px}
        .dropzone{border:2px dashed rgba(249,115,22,0.3);border-radius:20px;padding:50px 20px;text-align:center;cursor:pointer;background:var(--glass);margin-bottom:20px}
        .dropzone i{font-size:48px;color:var(--accent)}
        .dropzone video{width:100%;max-height:250px;object-fit:contain;margin-top:12px;border-radius:12px;display:none}
        .form-card{background:var(--glass);border:1px solid var(--border);border-radius:20px;padding:20px}
        .form-card label{display:block;font-size:13px;opacity:0.7;margin-bottom:6px;margin-top:12px}
        .form-card textarea,.form-card input{width:100%;padding:14px 16px;border-radius:16px;background:rgba(249,115,22,0.04);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif}
        .form-card textarea{min-height:80px}
        .progress-wrap{display:none;margin:16px 0}
        .progress-bar{background:rgba(255,255,255,0.1);border-radius:30px;height:6px}
        .progress-fill{background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;border-radius:30px;width:0%}
        .progress-text{text-align:center;font-size:12px;margin-top:6px;color:#fb923c}
        .btn-upload{width:100%;padding:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:30px;color:#fff;font-weight:700;font-size:15px;cursor:pointer;margin-top:16px;box-shadow:0 10px 25px rgba(249,115,22,0.4)}
        .btn-upload:disabled{opacity:0.5}
        .status{text-align:center;margin-top:12px;font-size:13px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>📤 رفع فيديو جديد</h2></div>
<div class="container">
    <div class="dropzone" onclick="document.getElementById('videoFile').click()"><i class="fas fa-cloud-upload-alt"></i><p>اضغط لاختيار فيديو</p><span style="font-size:11px;opacity:0.5">MP4 - حتى 100MB</span><video id="preview" controls></video></div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">
    <div class="form-card">
        <label>🎬 وصف الفيديو</label><textarea id="vidDesc" placeholder="اكتب وصفاً... #هاشتاقات"></textarea>
        <label>🎵 الموسيقى</label><input type="text" id="vidMusic" placeholder="Original Sound">
        <div class="progress-wrap" id="progressWrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div><div class="progress-text" id="progressText">0%</div></div>
        <button class="btn-upload" id="uploadBtn" onclick="upload()">🟠 رفع الفيديو</button>
        <div class="status" id="status"></div>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,selectedFile=null;
    auth.onAuthStateChanged(async u=>{if(!u)window.location.href='auth.html';currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()}});
    function onFilePick(inp){const f=inp.files[0];if(!f||!f.type.startsWith('video/')){alert('اختر فيديو صحيح');return}if(f.size>100*1024*1024){alert('أقل من 100MB');return}selectedFile=f;const r=new FileReader();r.onload=e=>{const v=document.getElementById('preview');v.src=e.target.result;v.style.display='block'};r.readAsDataURL(f)}
    async function upload(){
        if(!selectedFile){alert('اختر فيديو');return}if(!currentUser){alert('سجل دخول');return}
        const desc=document.getElementById('vidDesc').value;const music=document.getElementById('vidMusic').value||'Original Sound';
        const pw=document.getElementById('progressWrap');pw.style.display='block';const pf=document.getElementById('progressFill');pf.style.width='0%';const pt=document.getElementById('progressText');pt.innerText='0%';
        const st=document.getElementById('status');st.innerHTML='';const btn=document.getElementById('uploadBtn');btn.disabled=true;
        const fd=new FormData();fd.append('file',selectedFile);fd.append('upload_preset',UPLOAD_PRESET);
        const xhr=new XMLHttpRequest();xhr.open('POST','https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
        xhr.upload.onprogress=e=>{if(e.lengthComputable){const p=Math.round(e.loaded/e.total*100);pf.style.width=p+'%';pt.innerText=p+'%'}};
        xhr.onload=async()=>{const r=JSON.parse(xhr.responseText);await db.ref('videos/').push({url:r.secure_url,thumbnail:r.secure_url.replace('.mp4','.jpg'),description:desc,music:music,sender:currentUser.uid,senderName:currentUserData?.username,likes:0,likedBy:{},comments:{},timestamp:Date.now()});st.innerHTML='✅ تم الرفع بنجاح!';st.style.color='#4ade80';setTimeout(()=>window.location.href='index.html',1500)};
        xhr.onerror=()=>{st.innerHTML='❌ فشل الرفع';btn.disabled=false;st.style.color='#f87171'};xhr.send(fd);
    }
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 6. chat.html - الدردشة
# ═══════════════════════════════════════════════════════════

def build_chat():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | دردشة</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(249,115,22,0.03);--border:rgba(249,115,22,0.12);--accent:#f97316;--accent2:#fb923c;--bg:#0a0400}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;display:flex;flex-direction:column}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border)}
        .btn-back{background:rgba(249,115,22,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}
        .bubble{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px}
        .bubble.sent{background:linear-gradient(135deg,var(--accent),var(--accent2));align-self:flex-end}
        .bubble.received{background:rgba(249,115,22,0.06);align-self:flex-start}
        .input-bar{display:flex;gap:10px;padding:12px;background:rgba(10,4,0,0.9);border-top:1px solid var(--border)}
        .input-bar input{flex:1;padding:12px 16px;border-radius:30px;background:var(--glass);border:1px solid var(--border);color:#fff;font-size:14px;outline:none}
        .btn-send{width:42px;height:42px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px}
        .conv-item{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer}
        .chat-avatar{width:40px;height:40px;border-radius:50%;overflow:hidden}
        .chat-avatar img{width:100%;height:100%;object-fit:cover}
        .spinner{width:32px;height:32px;border:3px solid rgba(249,115,22,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px"><div class="spinner"></div><span>🟠 تحميل...</span></div>
<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>💬 المحادثات</h2></div><div id="convList" style="flex:1;overflow-y:auto"></div></div>
<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button><div class="chat-avatar" id="chatAvatar"></div><h3 id="chatName">محادثة</h3></div><div class="msgs" id="msgsList"></div><div class="input-bar"><input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()"><button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,allUsers={},chatUserId=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const us=await db.ref('users').once('value');allUsers=us.val()||{};document.getElementById('loader').style.display='none';showConvs()});
    function showConvs(){document.getElementById('chatView').style.display='none';document.getElementById('convView').style.display='flex';chatUserId=null;loadConvs()}
    async function loadConvs(){const cl=document.getElementById('convList');cl.innerHTML='';const snap=await db.ref('private_messages').once('value');const all=snap.val()||{};const found=new Set();Object.keys(all).forEach(cid=>{const[u1,u2]=cid.split('_');const other=u1===currentUser.uid?u2:u2===currentUser.uid?u1:null;if(other&&!found.has(other)&&allUsers[other])found.add(other)});if(!found.size){cl.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px">لا محادثات</div>';return}found.forEach(uid=>{const u=allUsers[uid];const d=document.createElement('div');d.className='conv-item';d.innerHTML=`<div class="chat-avatar"><img src="${u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}"></div><div><div style="font-weight:600">@${u?.username||'?'} ${u?.isVerified?'<span style="color:#fb923c">✅</span>':''}</div></div>`;d.onclick=()=>openChat(uid);cl.appendChild(d)})}
    async function openChat(uid){chatUserId=uid;const u=allUsers[uid];document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');document.getElementById('chatAvatar').innerHTML=`<img src="${u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}">`;document.getElementById('convView').style.display='none';document.getElementById('chatView').style.display='flex';await loadMsgs()}
    function getChatId(){return[currentUser.uid,chatUserId].sort().join('_')}
    async function loadMsgs(){const ml=document.getElementById('msgsList');ml.innerHTML='';if(!chatUserId)return;const snap=await db.ref('private_messages/'+getChatId()).once('value');const ms=snap.val()||{};Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{const sent=m.senderId===currentUser.uid;const d=document.createElement('div');d.className='bubble '+(sent?'sent':'received');d.innerHTML=`${m.type==='image'?`<img src="${m.imageUrl}" style="max-width:200px;border-radius:12px;cursor:pointer" onclick="window.open('${m.imageUrl}')">`:m.text}<div style="font-size:9px;opacity:0.5;margin-top:4px">${new Date(m.timestamp).toLocaleTimeString()}</div>`;ml.appendChild(d)});ml.scrollTop=ml.scrollHeight}
    async function sendMsg(){const inp=document.getElementById('msgInput');const txt=inp.value.trim();if(!txt||!chatUserId)return;await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});inp.value='';await loadMsgs()}
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 7. explore.html - استكشاف
# ═══════════════════════════════════════════════════════════

def build_explore():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | استكشاف</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(249,115,22,0.03);--border:rgba(249,115,22,0.12);--accent:#f97316;--accent2:#fb923c;--bg:#0a0400}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,4,0,0.8);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(249,115,22,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        h2{font-size:18px;font-weight:700}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px}
        .thumb{aspect-ratio:9/16;background:rgba(249,115,22,0.05);display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden;transition:transform 0.2s}
        .thumb:hover{transform:scale(1.03);z-index:1}
        .thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
        .thumb i{position:absolute;font-size:24px;color:#fff;z-index:1;opacity:0;transition:opacity 0.3s}
        .thumb:hover i{opacity:1}
        .thumb .views{position:absolute;bottom:4px;left:4px;font-size:10px;background:rgba(0,0,0,0.6);padding:2px 6px;border-radius:10px}
        .spinner{width:32px;height:32px;border:3px solid rgba(249,115,22,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🌐 استكشاف</h2></div>
<div class="grid" id="exploreGrid"><div class="spinner" style="grid-column:1/-1"></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;loadExplore()});
    async function loadExplore(){
        const snap=await db.ref('videos').once('value');
        const videos=snap.val()||{};
        const allVids=Object.entries(videos).map(([k,v])=>({id:k,...v})).sort((a,b)=>(b.likes||0)-(a.likes||0));
        const g=document.getElementById('exploreGrid');
        if(!allVids.length){g.innerHTML='<div style="text-align:center;padding:40px;grid-column:1/-1;opacity:0.5">لا توجد فيديوهات</div>';return}
        g.innerHTML=allVids.map(v=>`<div class="thumb" onclick="window.open('${v.url}','_blank')">${v.thumbnail?`<img src="${v.thumbnail}">`:''}<i class="fas fa-play"></i><span class="views">❤️ ${v.likes||0}</span></div>`).join('');
    }
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 8. notifications.html - الإشعارات
# ═══════════════════════════════════════════════════════════

def build_notifications():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | إشعارات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(249,115,22,0.03);--border:rgba(249,115,22,0.12);--accent:#f97316;--bg:#0a0400}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,4,0,0.8);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(249,115,22,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .notif-item{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);align-items:center}
        .notif-icon{width:40px;height:40px;border-radius:50%;background:rgba(249,115,22,0.1);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--accent)}
        .spinner{width:32px;height:32px;border:3px solid rgba(249,115,22,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🔔 الإشعارات</h2></div>
<div id="notifsList"><div class="spinner"></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;loadNotifs()});
    async function loadNotifs(){
        const snap=await db.ref('notifications/'+currentUser.uid).once('value');
        const ns=snap.val()||{};
        const c=document.getElementById('notifsList');
        const items=Object.values(ns).reverse();
        if(!items.length){c.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#f97316;margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';return}
        c.innerHTML=items.map(n=>`<div class="notif-item"><div class="notif-icon"><i class="fas fa-bell"></i></div><div><div style="font-weight:600">${n.from||'مستخدم'}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${n.msg||''}</div></div></div>`).join('');
    }
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 9. settings.html - الإعدادات
# ═══════════════════════════════════════════════════════════

def build_settings():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟠 ORANGE CRYSTAL | إعدادات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(249,115,22,0.03);--border:rgba(249,115,22,0.12);--accent:#f97316;--bg:#0a0400}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,4,0,0.8);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(249,115,22,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .setting-item{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}
        .setting-item:hover{background:var(--glass)}
        .setting-item i{color:var(--accent);font-size:18px;width:30px}
        .btn-danger{background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.3);color:#f87171;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>⚙️ الإعدادات</h2></div>
<div style="padding:8px 0">
    <div class="setting-item" onclick="window.location.href='profile.html'"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-user"></i><span>تعديل الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-lock"></i><span>الخصوصية</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-globe"></i><span>اللغة</span></div><span style="opacity:0.5;font-size:13px">العربية</span></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-info-circle"></i><span>حول التطبيق</span></div><span style="opacity:0.5;font-size:13px">v2026.1</span></div>
    <button class="btn-danger" onclick="if(confirm('تسجيل الخروج؟')){auth.signOut();window.location.href='auth.html'}"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button>
</div>
<script src="firebase-config.js"></script>
<script>
    auth.onAuthStateChanged(u=>{if(!u)window.location.href='auth.html'});
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟠 MAIN - التشغيل الرئيسي
# ═══════════════════════════════════════════════════════════

def main():
    """الدالة الرئيسية - توليد جميع الملفات"""
    
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  🟠  ORANGE CRYSTAL TIKTOK 2026 - GLASS EDITION  🟠  ║
║     Ultimate Generator - 9 Files - 1000+ Lines           ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING FILES - إنشاء الملفات")
    
    write("firebase-config.js", build_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("profile.html", build_profile())
    write("upload.html", build_upload())
    write("chat.html", build_chat())
    write("explore.html", build_explore())
    write("notifications.html", build_notifications())
    write("settings.html", build_settings())
    
    print(f"""
{'='*60}
  🟠 BUILD COMPLETE - تم الإنشاء بنجاح!
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 9 ملفات تم إنشاؤها

  📁 الملفات:
     1. firebase-config.js   → إعدادات Firebase + Cloudinary
     2. auth.html            → تسجيل دخول + اشتراك
     3. index.html           → الرئيسية + فيديوهات
     4. profile.html         → ملف شخصي + لوحة أدمن
     5. upload.html          → رفع فيديو
     6. chat.html            → دردشة خاصة
     7. explore.html         → استكشاف
     8. notifications.html   → إشعارات
     9. settings.html        → إعدادات

  🔑 بيانات الاتصال:
     • Firebase: comk-4302e
     • Cloudinary: dt0tkbtzw / xk20_k
     • Admin: jasim28v@gmail.com

  🟠 للتشغيل: افتح auth.html في المتصفح
  🟠 ORANGE CRYSTAL 2026 READY!
{'='*60}
    """)

# ═══════════════════════════════════════════════════════════
# 🟠 ENTRY POINT
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
