#!/usr/bin/env python3
"""
🤖 MADA TRADING BOT - Version Opérationnelle
Bot adaptatif pour Deriv MT5 - Trading M1 à H1
"""

import os
import sys
import logging
from datetime import datetime

# Configuration logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('bot.log')
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Point d'entrée principal"""
    logger.info("=" * 60)
    logger.info("🚀 MADA TRADING BOT - DÉMARRAGE")
    logger.info("🇲🇬 Version Opérationnelle 1.0")
    logger.info("=" * 60)
    
    # Vérifier les variables d'environnement
    token = os.getenv('TELEGRAM_TOKEN')
    if not token or token == "VOTRE_TOKEN_ICI":
        logger.error("❌ TELEGRAM_TOKEN non configuré!")
        logger.info("ℹ️  Ajoutez TELEGRAM_TOKEN dans Render.com")
        return
    
    logger.info(f"✅ Token Telegram: {token[:15]}...")
    
    # Initialiser les composants
    try:
        # Essayer d'importer MT5
        try:
            import MetaTrader5 as mt5
            mt5_available = True
        except ImportError:
            logger.warning("⚠️  MetaTrader5 non installé - Mode TEST")
            mt5_available = False
        
        # Démarrer le bot adaptatif
        from bot_core import AdaptiveTradingBot
        
        bot = AdaptiveTradingBot(
            telegram_token=token,
            mt5_enabled=mt5_available,
            trading_mode=os.getenv('TRADING_MODE', 'DEMO')
        )
        
        logger.info("✅ Bot initialisé avec succès!")
        logger.info("📊 Mode: %s", "MT5 Actif" if mt5_available else "Test")
        logger.info("⏰ Démarrage: %s", datetime.now().strftime("%H:%M:%S"))
        
        # Démarrer le bot
        bot.run()
        
    except Exception as e:
        logger.error(f"❌ Erreur d'initialisation: {e}")
        logger.info("🔄 Redémarrage dans 30 secondes...")
        import time
        time.sleep(30)
        main()  # Redémarrage automatique

if __name__ == "__main__":
    main()
