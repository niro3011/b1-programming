import hashlib
from datetime import datetime

class User:
    def __init__(self, username, password, privilege_level="standard"):
        """
        Initialisiert einen neuen User
        
        Args:
            username: Benutzername
            password: Passwort (wird gehasht gespeichert)
            privilege_level: Berechtigungsstufe (admin/standard/guest)
        """
        self.username = username
        self.hashed_password = self._hash_password(password)
        self.privilege_level = privilege_level
        self.login_attempts = 0
        self.account_status = "active"
        self.activity_log = []
    
    def _hash_password(self, password):
        """Hasht das Passwort mit SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate(self, password):
        """
        Authentifiziert den User mit einem Passwort
        
        Returns:
            bool: True wenn erfolgreich, False sonst
        """
        if self.account_status == "locked":
            print(f"Account {self.username} ist gesperrt!")
            return False
        
        if self._hash_password(password) == self.hashed_password:
            self.reset_login_attempts()
            self.log_activity("Erfolgreicher Login")
            print(f"Login erfolgreich für {self.username}")
            return True
        else:
            self.login_attempts += 1
            self.log_activity(f"Fehlgeschlagener Login-Versuch ({self.login_attempts})")
            print(f"Falsches Passwort! Versuch {self.login_attempts}/3")
            
            if self.login_attempts >= 3:
                self.lock_account()
            return False
    
    def check_privileges(self):
        """Gibt die Berechtigungsstufe zurück"""
        return self.privilege_level
    
    def lock_account(self):
        """Sperrt den Account nach zu vielen fehlgeschlagenen Versuchen"""
        self.account_status = "locked"
        self.log_activity("Account wurde gesperrt")
        print(f"Account {self.username} wurde nach 3 fehlgeschlagenen Versuchen gesperrt!")
    
    def reset_login_attempts(self):
        """Setzt die Login-Versuche zurück"""
        self.login_attempts = 0
    
    def log_activity(self, activity):
        """Loggt Aktivitäten mit Zeitstempel"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {activity}"
        self.activity_log.append(log_entry)
    
    def display_info(self):
        """Zeigt User-Informationen an (ohne Passwort!)"""
        print(f"\n--- User Info ---")
        print(f"Username: {self.username}")
        print(f"Privilege Level: {self.privilege_level}")
        print(f"Login Attempts: {self.login_attempts}")
        print(f"Account Status: {self.account_status}")
    
    def show_activity_log(self):
        """Zeigt das Aktivitätslog an"""
        print(f"\n--- Activity Log für {self.username} ---")
        for entry in self.activity_log:
            print(entry)

if __name__ == "__main__":

    user1 = User("max_mueller", "sicheres_passwort123", "admin")

    user1.display_info()

    print(f"\nBerechtigungen: {user1.check_privileges()}")

    print("\n--- Login-Versuche ---")
    user1.authenticate("falsches_passwort")
    user1.authenticate("falsches_passwort")
    user1.authenticate("falsches_passwort")  
    user1.authenticate("sicheres_passwort123") 

    user1.show_activity_log()
    

    print("\n\n=== Neuer User ===")
    user2 = User("anna_schmidt", "geheim456", "standard")
    user2.authenticate("geheim456")  # Erfolg
    user2.display_info()