"""
Cœur du bot trading adaptatif
"""

import time
import asyncio
from datetime import datetime, timedelta

class AdaptiveTradingBot:
    """Bot de trading qui s'adapte aux conditions marché"""
    
    def __init__(self, telegram_token, mt5_enabled=False, trading_mode="DEMO"):
        self.telegram_token = telegram_token
        self.mt5_enabled = mt5_enabled
        self.trading_mode = trading_mode
        self.adaptation_mode = "AUTO"
        self.market_conditions = {}
        
        print("=" * 60)
        print("🤖 BOT TRADING ADAPTATIF")
        print("=" * 60)
        print(f"📊 Mode: {trading_mode}")
        print(f"🔄 Adaptation: {self.adaptation_mode}")
        print(f"📈 MT5: {'✅ Connecté' if mt5_enabled else '⚠️  Test'}")
        print("=" * 60)
    
    def detect_market_conditions(self):
        """Détecte les conditions actuelles du marché"""
        conditions = {
            "volatility": "MODERATE",
            "trend": "NEUTRAL",
            "session": self.get_current_session(),
            "risk_level": "MEDIUM",
            "recommended_timeframes": ["M15", "H1"],
            "recommended_assets": ["EURUSD", "XAUUSD"]
        }
        
        # Simulation d'adaptation
        hour = datetime.now().hour
        if 8 <= hour <= 16:
            conditions["session"] = "LONDON"
            conditions["recommended_assets"] = ["EURUSD", "GBPUSD"]
        elif 13 <= hour <= 21:
            conditions["session"] = "US"
            conditions["recommended_assets"] = ["US30", "VOL75"]
        
        self.market_conditions = conditions
        return conditions
    
    def get_current_session(self):
        """Détermine la session de trading actuelle"""
        hour = datetime.now().hour
        if 0 <= hour < 8:
            return "ASIAN"
        elif 8 <= hour < 16:
            return "LONDON"
        elif 13 <= hour < 21:
            return "US"
        else:
            return "OVERLAP" if 13 <= hour < 16 else "AFTER_HOURS"
    
    def generate_signal(self, asset="EURUSD"):
        """Génère un signal de trading adaptatif"""
        # Simulation - sera remplacé par analyse réelle
        import random
        
        signal_types = ["BUY", "SELL", "HOLD"]
        confidence = random.randint(60, 90)
        
        signal = {
            "asset": asset,
            "action": random.choice(signal_types),
            "confidence": confidence,
            "timestamp": datetime.now(),
            "entry": round(1.0800 + random.uniform(-0.0020, 0.0020), 4),
            "stop_loss": round(1.0750 + random.uniform(-0.0010, 0.0010), 4),
            "take_profit": round(1.0850 + random.uniform(-0.0010, 0.0010), 4),
            "timeframe": random.choice(["M5", "M15", "H1"]),
            "risk_level": "MEDIUM",
            "adaptation_notes": self.market_conditions
        }
        
        return signal
    
    def run_analysis_cycle(self):
        """Cycle d'analyse adaptatif"""
        print("\n" + "=" * 40)
        print("🔍 ANALYSE ADAPTATIVE EN COURS")
        print("=" * 40)
        
        # Détection conditions
        conditions = self.detect_market_conditions()
        print(f"📊 Session: {conditions['session']}")
        print(f"📈 Volatilité: {conditions['volatility']}")
        print(f"🎯 Actifs recommandés: {', '.join(conditions['recommended_assets'])}")
        
        # Génération signaux
        for asset in conditions['recommended_assets'][:2]:  # 2 premiers actifs
            signal = self.generate_signal(asset)
            print(f"\n📡 Signal {asset}:")
            print(f"   Action: {signal['action']} ({signal['confidence']}% confiance)")
            print(f"   Timeframe: {signal['timeframe']}")
            print(f"   Entry: {signal['entry']}")
            print(f"   SL: {signal['stop_loss']} | TP: {signal['take_profit']}")
        
        print("=" * 40)
    
    def run(self):
        """Boucle principale du bot"""
        print("\n🔄 DÉMARRAGE DU CYCLE DE TRADING")
        print("📱 Le bot est maintenant opérationnel!")
        print("💡 Envoyez /start sur Telegram pour commencer")
        
        cycle_count = 0
        try:
            while True:
                cycle_count += 1
                current_time = datetime.now().strftime("%H:%M:%S")
                
                print(f"\n🕒 Cycle {cycle_count} - {current_time}")
                print("-" * 30)
                
                # Exécuter l'analyse
                self.run_analysis_cycle()
                
                # Attendre avant prochain cycle
                wait_time = 60  # 1 minute pour la démo
                print(f"\n⏳ Prochaine analyse dans {wait_time} secondes...")
                time.sleep(wait_time)
                
        except KeyboardInterrupt:
            print("\n🛑 Arrêt demandé")
        except Exception as e:
            print(f"\n❌ Erreur: {e}")
            print("🔄 Redémarrage dans 30 secondes...")
            time.sleep(30)
            self.run()
