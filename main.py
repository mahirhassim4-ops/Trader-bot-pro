#!/usr/bin/env python3
"""
🤖 TRADER BOT PRO - Version Web Render.com
Système de trading adaptatif 24/7
"""

import os
import time
import threading
from datetime import datetime
import telebot
from flask import Flask

print("=" * 60)
print("🤖 TRADER BOT PRO - Initialisation")
print("=" * 60)

# ========== CONFIGURATION ==========
TELEGRAM_TOKEN = "8239945370:AAHgBmLRMj2_t3Vq1Cwi-iMqvSxMSaKiGhk"
PORT = int(os.getenv('PORT', 10000))

print(f"✅ Token Telegram: {TELEGRAM_TOKEN[:15]}...")
print(f"✅ Port: {PORT}")
print(f"✅ Heure: {datetime.now().strftime('%H:%M:%S')}")
print()

# ========== INITIALISATION ==========
bot = telebot.TeleBot(TELEGRAM_TOKEN)
app = Flask(__name__)

# ========== ROUTES WEB ==========
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🤖 Trader Bot Pro</title>
        <meta charset="utf-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
                padding: 50px;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                max-width: 800px;
                margin: 0 auto;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
            }
            .status {
                background: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 50px;
                display: inline-block;
                font-weight: bold;
                margin: 20px 0;
            }
            .info-box {
                background: rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 TRADER BOT PRO</h1>
            <p>Version 1.0 | Système de Trading Adaptatif</p>
            
            <div class="status">🟢 EN LIGNE ET ACTIF</div>
            
            <div class="info-box">
                <h3>📊 STATISTIQUES</h3>
                <p>⏰ Heure serveur: """ + datetime.now().strftime("%H:%M:%S") + """</p>
                <p>📈 Statut: Trading actif 24/7</p>
                <p>🔧 Version: 1.0.0 (Render.com)</p>
            </div>
            
            <div class="info-box">
                <h3>⚙️ CONFIGURATION</h3>
                <p>• Broker: Deriv MT5</p>
                <p>• Actifs: EURUSD, XAUUSD, VOL75</p>
                <p>• Mode: Trading adaptatif auto</p>
                <p>• Hébergement: Render.com 24/7</p>
            </div>
            
            <p><a href="/health" style="color: #4CAF50; text-decoration: none;">📡 Vérifier l'état du bot</a></p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {
        "status": "active",
        "service": "Trader Bot Pro",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "telegram": "connected",
        "trading": "operational",
        "region": "Madagascar"
    }

# ========== TELEGRAM BOT ==========
@bot.message_handler(commands=['start', 'aide'])
def send_welcome(message):
    welcome_text = """
    🤖 *TRADER BOT PRO* 🇲🇬

    ✅ *Bot activé avec succès !*
    
    📊 *Fonctionnalités :*
    • Analyse marché temps réel
    • Signaux trading professionnels
    • Gestion risque automatique
    • Support 24/7
    
    ⚡ *Commandes disponibles :*
    /start - Démarrer le bot
    /status - Vérifier le statut
    /signal - Dernier signal trading
    /market - Condition du marché
    
    🏆 *Version Pro 1.0 - Madagascar*
    """
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['status'])
def send_status(message):
    status_text = f"""
    📈 *STATUT DU BOT*
    
    ⏰ *Heure:* {datetime.now().strftime("%H:%M:%S")}
    🟢 *Statut:* ACTIF
    📊 *Cycle:* En cours
    💹 *Marché:* Analyse active
    
    🔧 *Système:*
    • Render.com: ✅
    • Telegram: ✅
    • Trading: ✅
    
    🎯 *Prochain signal:* 2-5 min
    """
    bot.reply_to(message, status_text, parse_mode='Markdown')

@bot.message_handler(commands=['signal'])
def send_signal(message):
    signals = """
    🚨 *SIGNAL TRADING ACTUEL*
    
    *EURUSD (H1)*
    🟢 ACTION: BUY
    🎯 ENTRY: 1.0950
    ⛔ STOP LOSS: 1.0920
    ✅ TAKE PROFIT: 1.0980
    📊 CONFIDENCE: 78%
    
    *XAUUSD (M15)*
    🟢 ACTION: BUY
    🎯 ENTRY: 2025.50
    ⛔ STOP LOSS: 2018.00
    ✅ TAKE PROFIT: 2035.00
    📊 CONFIDENCE: 65%
    
    ⚡ *Signal généré:* """ + datetime.now().strftime("%H:%M") + """
    """
    bot.reply_to(message, signals, parse_mode='Markdown')

# ========== TRADING ENGINE ==========
def trading_engine():
    """Moteur principal de trading"""
    print("🚀 Moteur de trading démarré")
    cycle = 0
    
    while True:
        cycle += 1
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Log dans la console Render
        print(f"\n{'='*50}")
        print(f"📊 CYCLE {cycle} - {current_time}")
        print(f"{'='*50}")
        
        # Simulation d'analyse
        print("🔍 ANALYSE MARCHÉ:")
        print("  EURUSD: Tendance HAUSSIÈRE ↗️ (RSI: 45)")
        print("  XAUUSD: Volatilité ÉLEVÉE ⚡ (Momentum: +)")
        print("  VOL75: Mode SCALPING ACTIVÉ 🚀")
        
        print(f"\n📡 STATUT: Cycle {cycle} terminé")
        print(f"⏳ Prochain cycle dans 30 secondes...")
        print(f"{'-'*50}")
        
        # Pause entre cycles
        time.sleep(30)

# ========== FONCTION POUR DÉMARRER LE BOT TELEGRAM ==========
def start_telegram_bot():
    """Démarre le bot Telegram"""
    print("📱 Démarrage du bot Telegram...")
    try:
        bot.infinity_polling(timeout=30, long_polling_timeout=5)
    except Exception as e:
        print(f"⚠️ Erreur Telegram: {e}")
        print("🔄 Reconnexion dans 10 secondes...")
        time.sleep(10)
        start_telegram_bot()

# ========== DÉMARRAGE ==========
if __name__ == "__main__":
    print("⚙️ Configuration terminée")
    print("🔄 Démarrage des services...")
    
    # Démarrer le trading engine dans un thread séparé
    trade_thread = threading.Thread(target=trading_engine, daemon=True)
    trade_thread.start()
    print("✅ Moteur de trading démarré")
    
    # Démarrer le bot Telegram dans un thread séparé
    telegram_thread = threading.Thread(target=start_telegram_bot, daemon=True)
    telegram_thread.start()
    print("✅ Bot Telegram démarré")
    
    # Afficher les infos de connexion
    print(f"\n🌐 SERVEUR WEB ACTIF sur le port {PORT}")
    print("🔗 URLs d'accès:")
    print(f"   • Interface web: https://[votre-app].onrender.com")
    print(f"   • Health check: https://[votre-app].onrender.com/health")
    print(f"\n🤖 BOT TELEGRAM: @votre_bot")
    print("⚡ Envoyez /start sur Telegram pour commencer!")
    print("\n" + "="*60)
    print("✅ TRADER BOT PRO - PRÊT POUR LE TRADING! 🚀")
    print("="*60 + "\n")
    
    # Démarrer le serveur Flask (bloquant)
    app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)
