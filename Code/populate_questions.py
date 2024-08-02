from app.models import  QuizQuestion


questions = [
    {
        "question": "Was sind Kryptowährungen?",
        "option_a": "Traditionelle physische Währungen",
        "option_b": "Digitale oder virtuelle Währungen, die Kryptographie zur Sicherung von Transaktionen nutzen",
        "option_c": "Währungen, die nur von Regierungen ausgegeben werden",
        "option_d": "Eine Art von Aktien",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist eine Blockchain?",
        "option_a": "Eine zentrale Datenbank",
        "option_b": "Ein dezentrales, digitales Hauptbuch, das Transaktionen speichert",
        "option_c": "Ein Tool zur Verwaltung von Bankkonten",
        "option_d": "Ein Algorithmus zur Verschlüsselung",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Wofür wird ein Private Key verwendet?",
        "option_a": "Zum Senden von Kryptowährungen",
        "option_b": "Zum Empfangen von Kryptowährungen",
        "option_c": "Zum Autorisieren von Transaktionen und Zugriff auf Kryptowährungen",
        "option_d": "Zum Anzeigen von Transaktionshistorie",
        "correct_option": "C"
   ,
"category": "Easy"
},

    {
        "question": "Was ist Mining in Bezug auf Kryptowährungen?",
        "option_a": "Der Prozess des Erstellens von physischen Münzen",
        "option_b": "Der Prozess, durch den neue Kryptowährungseinheiten erstellt und Transaktionen validiert werden",
        "option_c": "Der Kauf von Kryptowährungen an der Börse",
        "option_d": "Die Speicherung von Kryptowährungen in einer Wallet",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist das Hauptmerkmal der Strategie \"Buy and Hold\"?",
        "option_a": "Häufiges Kaufen und Verkaufen",
        "option_b": "Langfristiges Halten von Kryptowährungen in der Hoffnung auf Wertsteigerung",
        "option_c": "Investieren kleiner Beträge in regelmäßigen Abständen",
        "option_d": "Arbitrage zwischen verschiedenen Börsen",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist eine Krypto-Wallet?",
        "option_a": "Ein physischer Speicher für Kryptowährungen",
        "option_b": "Eine digitale Brieftasche zur Speicherung, zum Senden und Empfangen von Kryptowährungen",
        "option_c": "Ein Online-Banking-System",
        "option_d": "Ein Tool zur Erstellung neuer Kryptowährungen",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was versteht man unter Fiat-Währung?",
        "option_a": "Eine Kryptowährung, die von einer Regierung ausgegeben wird",
        "option_b": "Eine traditionelle Währung wie USD oder EUR, die von Regierungen ausgegeben wird",
        "option_c": "Eine Währung, die nur in digitalen Form existiert",
        "option_d": "Eine wertlose Währung",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist der Unterschied zwischen einem Public und einem Private Key?",
        "option_a": "Public Key verschlüsselt, Private Key entschlüsselt Nachrichten",
        "option_b": "Public Key ist öffentlich, Private Key ist geheim und ermöglicht den Zugriff auf Kryptowährungen",
        "option_c": "Beide sind geheim und werden für Transaktionen verwendet",
        "option_d": "Es gibt keinen Unterschied",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was bedeutet \"HODL\" in der Krypto-Community?",
        "option_a": "Hold On for Dear Life, also langfristiges Halten von Kryptowährungen",
        "option_b": "Handle Over Digital Ledger, also das Verwalten von Kryptowährungen",
        "option_c": "Hyper Online Distributed Ledger, eine spezielle Art der Blockchain",
        "option_d": "Halting of Daily Losses, also das Vermeiden von täglichen Verlusten",
        "correct_option": "A"
   ,
"category": "Easy"
},

    {
        "question": "Was ist eine ICO (Initial Coin Offering)?",
        "option_a": "Eine Methode zur Erstausgabe von Aktien",
        "option_b": "Eine Methode zur Erstausgabe von Kryptowährungen, um Kapital zu beschaffen",
        "option_c": "Ein Unternehmen, das Kryptowährungen handelt",
        "option_d": "Ein neues Gesetz zur Regulierung von Kryptowährungen",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was bedeutet Dezentralisierung in Bezug auf Kryptowährungen?",
        "option_a": "Alle Transaktionen werden über eine zentrale Stelle abgewickelt",
        "option_b": "Transaktionen werden über ein Netzwerk von vielen Computern ohne zentrale Kontrolle abgewickelt",
        "option_c": "Kryptowährungen sind auf eine zentrale Bank beschränkt",
        "option_d": "Alle Nutzer haben den gleichen Private Key",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Welche Kryptowährung war die erste auf dem Markt?",
        "option_a": "Ethereum",
        "option_b": "Litecoin",
        "option_c": "Bitcoin",
        "option_d": "Ripple",
        "correct_option": "C"
   ,
"category": "Easy"
},

    {
        "question": "Was ist ein Smart Contract?",
        "option_a": "Ein intelligenter Vertrag, der automatisch ausgeführt wird, wenn bestimmte Bedingungen erfüllt sind",
        "option_b": "Ein Vertrag, der von Anwälten geprüft wird",
        "option_c": "Ein Vertrag, der nur in Papierform existiert",
        "option_d": "Ein Vertrag, der manuell ausgeführt wird",
        "correct_option": "A"
   ,
"category": "Easy"
},

    {
        "question": "Was ist Ethereum?",
        "option_a": "Eine zentrale Bank",
        "option_b": "Eine Kryptowährungsplattform, die Smart Contracts und dezentrale Anwendungen unterstützt",
        "option_c": "Ein physisches Gerät zur Speicherung von Kryptowährungen",
        "option_d": "Eine Handelsplattform für traditionelle Aktien",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was bedeutet es, wenn eine Kryptowährung „volatile“ ist?",
        "option_a": "Sie hat einen stabilen Wert",
        "option_b": "Ihr Wert schwankt stark innerhalb kurzer Zeiträume",
        "option_c": "Sie wird nur selten gehandelt",
        "option_d": "Sie hat keinen Marktwert",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist ein Hash in der Blockchain-Technologie?",
        "option_a": "Ein Tool zur Verwaltung von Bankkonten",
        "option_b": "Eine Funktion, die Daten in einen festen, eindeutigen Wert umwandelt",
        "option_c": "Ein Ort zur Speicherung von Kryptowährungen",
        "option_d": "Eine Methode zur Verschlüsselung von Nachrichten",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist ein Node in der Blockchain?",
        "option_a": "Ein Benutzerkonto für Kryptowährungen",
        "option_b": "Ein Computer, der Teil des Netzwerks ist und Transaktionen überprüft und speichert",
        "option_c": "Eine neue Art von Kryptowährung",
        "option_d": "Ein Vertragstyp in der Blockchain",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist der Unterschied zwischen einer Krypto-Börse und einer Wallet?",
        "option_a": "Eine Börse speichert Kryptowährungen, eine Wallet handelt damit",
        "option_b": "Eine Wallet speichert Kryptowährungen, eine Börse ermöglicht den Handel damit",
        "option_c": "Beide sind identisch",
        "option_d": "Eine Börse ist sicherer als eine Wallet",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist ein Fork in der Blockchain?",
        "option_a": "Ein neues Update für die Blockchain-Software",
        "option_b": "Eine Änderung im Protokoll der Blockchain, die zu einer Abspaltung führen kann",
        "option_c": "Ein neues Wallet-Format",
        "option_d": "Ein Handelstool für Kryptowährungen",
        "correct_option": "B"
   ,
"category": "Easy"
},

    {
        "question": "Was ist ein Whitepaper in der Kryptowelt?",
        "option_a": "Ein Dokument, das die technischen Details und Ziele einer Kryptowährung beschreibt",
        "option_b": "Eine Anleitung zum Handel mit Kryptowährungen",
        "option_c": "Ein Vertrag zur Ausgabe neuer Kryptowährungen",
        "option_d": "Ein Update für die Blockchain-Software",
        "correct_option": "A",
        "category": "Easy"

    },
        {
        "question": "Was sind Smart Contracts?",
        "option_a": "Verträge, die von Anwälten geprüft werden müssen",
        "option_b": "Selbst ausführende Verträge mit den Bedingungen der Vereinbarung direkt in den Code geschrieben",
        "option_c": "Verträge, die manuell ausgeführt werden",
        "option_d": "Verträge, die nur in Papierform existieren",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was versteht man unter DeFi (Dezentrale Finanzen)?",
        "option_a": "Ein zentrales Bankensystem",
        "option_b": "Ein Ökosystem von Finanzanwendungen, das auf Blockchain-Technologie basiert",
        "option_c": "Eine neue Form der traditionellen Banken",
        "option_d": "Ein System zur physischen Lagerung von Geld",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist Day Trading?",
        "option_a": "Langfristiges Halten von Kryptowährungen",
        "option_b": "Kauf und Verkauf von Kryptowährungen innerhalb eines einzigen Handelstages",
        "option_c": "Investieren kleiner Beträge in regelmäßigen Abständen",
        "option_d": "Arbitrage zwischen verschiedenen Börsen",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist Margin Trading?",
        "option_a": "Handel mit eigenem Kapital",
        "option_b": "Handel mit geliehenen Mitteln, um potenzielle Gewinne zu erhöhen",
        "option_c": "Der Prozess des Erstellens neuer Kryptowährungen",
        "option_d": "Der Kauf und Verkauf von physischen Waren",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist eine gängige Methode zur Risikominimierung im Kryptowährungshandel?",
        "option_a": "Alles Geld in eine Kryptowährung investieren",
        "option_b": "Diversifikation der Investitionen auf verschiedene Kryptowährungen",
        "option_c": "Nur auf fallende Kurse setzen",
        "option_d": "Investitionen in Bargeld umwandeln",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist eine dezentrale Börse (DEX)?",
        "option_a": "Eine Börse, die von einer zentralen Behörde kontrolliert wird",
        "option_b": "Eine Plattform, die den direkten Handel von Kryptowährungen zwischen Nutzern ohne Zwischenhändler ermöglicht",
        "option_c": "Eine Börse, die nur Fiat-Währungen handelt",
        "option_d": "Eine Plattform zur Verwahrung von Kryptowährungen",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist das Ziel von Proof of Stake (PoS) im Vergleich zu Proof of Work (PoW)?",
        "option_a": "Höhere Energieeffizienz und geringere Rechenanforderungen",
        "option_b": "Höhere Transaktionsgeschwindigkeiten",
        "option_c": "Dezentralisierung der Netzwerksicherheit",
        "option_d": "Verwendung von physischer Hardware für die Sicherung des Netzwerks",
        "correct_option": "A",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist ein „Orakel“ in der Blockchain-Technologie?",
        "option_a": "Eine Art von Kryptowährung",
        "option_b": "Ein Dienst, der externe Daten in die Blockchain einbringt",
        "option_c": "Ein Algorithmus zur Erstellung neuer Blöcke",
        "option_d": "Eine Methode zur Verschlüsselung von Daten",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Welche Rolle spielt der Konsensus-Mechanismus in einer Blockchain?",
        "option_a": "Er bestimmt die Größe der Blöcke",
        "option_b": "Er ermöglicht die Einigung aller Teilnehmer über den Zustand der Blockchain",
        "option_c": "Er verschlüsselt die Transaktionen",
        "option_d": "Er steuert die Ausgabe neuer Coins",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was bedeutet „Tokenisierung“ von Vermögenswerten?",
        "option_a": "Umwandlung von physischen Vermögenswerten in digitale Token auf der Blockchain",
        "option_b": "Schaffung neuer Kryptowährungen",
        "option_c": "Handel mit Kryptowährungen an der Börse",
        "option_d": "Speicherung von Vermögenswerten in einer digitalen Wallet",
        "correct_option": "A",
        "category": "Intermediate1"
    },
    {
        "question": "Was sind „Stablecoins“?",
        "option_a": "Kryptowährungen mit hoher Volatilität",
        "option_b": "Kryptowährungen, deren Wert an stabile Vermögenswerte wie Fiat-Währungen gebunden ist",
        "option_c": "Kryptowährungen, die ausschließlich für den Handel an dezentralen Börsen verwendet werden",
        "option_d": "Kryptowährungen, die nur von Zentralbanken ausgegeben werden",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist ein „Security Token“?",
        "option_a": "Ein Token, der eine Beteiligung an einem physischen Vermögenswert darstellt",
        "option_b": "Ein Token, der ausschließlich für den Kauf von Waren und Dienstleistungen verwendet wird",
        "option_c": "Ein Token, der zur Erhöhung der Netzwerksicherheit verwendet wird",
        "option_d": "Ein Token, der als digitale Währung ohne regulatorische Beschränkungen existiert",
        "correct_option": "A",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist der Unterschied zwischen einer „Hard Fork“ und einer „Soft Fork“?",
        "option_a": "Eine Hard Fork erfordert keine Konsensänderung, eine Soft Fork schon",
        "option_b": "Eine Hard Fork führt zu zwei getrennten Blockchains, eine Soft Fork zu einer Abwärtskompatibilität",
        "option_c": "Eine Soft Fork erhöht die Blockgröße, eine Hard Fork verringert sie",
        "option_d": "Beide sind identisch",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was versteht man unter „Atomic Swaps“?",
        "option_a": "Der Handel von Kryptowährungen ohne zentrale Börse durch direkte Transaktionen zwischen zwei Parteien",
        "option_b": "Die Konvertierung von Fiat-Währungen in Kryptowährungen",
        "option_c": "Die Speicherung von Kryptowährungen in einer Offline-Wallet",
        "option_d": "Die Erhöhung der Blockgröße zur Verbesserung der Transaktionsgeschwindigkeit",
        "correct_option": "A",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist ein „Hashrate“?",
        "option_a": "Die Anzahl der Transaktionen, die pro Sekunde verarbeitet werden können",
        "option_b": "Die Rechenleistung, die zum Minen und Verifizieren von Transaktionen im Netzwerk verwendet wird",
        "option_c": "Die Geschwindigkeit, mit der neue Blöcke zur Blockchain hinzugefügt werden",
        "option_d": "Die Anzahl der Nutzer, die aktiv im Netzwerk sind",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was bedeutet „KYC“ (Know Your Customer) in Bezug auf Kryptowährungen?",
        "option_a": "Ein Protokoll zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_b": "Ein Verfahren zur Identifizierung und Verifizierung der Identität von Kunden",
        "option_c": "Eine Methode zur Verschlüsselung von Wallets",
        "option_d": "Ein Algorithmus zur Erstellung neuer Coins",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist „Liquidity Mining“?",
        "option_a": "Das Schürfen neuer Kryptowährungen",
        "option_b": "Der Prozess, durch den Nutzer Liquidität zu dezentralen Börsen hinzufügen und dafür belohnt werden",
        "option_c": "Die Sicherung der Blockchain durch Miner",
        "option_d": "Die Speicherung von Kryptowährungen in einer Cold Wallet",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Welche steuerlichen Regeln gelten in Deutschland für Gewinne aus Kryptowährungen, die länger als ein Jahr gehalten werden?",
        "option_a": "Sie sind vollständig steuerpflichtig",
        "option_b": "Sie sind nach einer Haltefrist von einem Jahr steuerfrei",
        "option_c": "Sie unterliegen einer pauschalen Steuer von 25%",
        "option_d": "Sie müssen mit dem persönlichen Einkommensteuersatz versteuert werden",
        "correct_option": "B",
        "category": "Intermediate1"
    },
    {
        "question": "Was ist ein „Privacy Coin“?",
        "option_a": "Eine Kryptowährung, die ausschließlich für den Handel auf zentralen Börsen verwendet wird",
        "option_b": "Eine Kryptowährung, die spezielle Techniken zur Verbesserung der Privatsphäre und Anonymität der Transaktionen nutzt",
        "option_c": "Eine Kryptowährung, die von Regierungen ausgegeben wird",
        "option_d": "Eine Kryptowährung, die nur in einem bestimmten Land verwendet werden kann",
        "correct_option": "B",
        "category": "Intermediate1"
    },
        {
        "question": "Was sind Smart Contracts?",
        "option_a": "Verträge, die von Anwälten geprüft werden müssen",
        "option_b": "Selbst ausführende Verträge mit den Bedingungen der Vereinbarung direkt in den Code geschrieben",
        "option_c": "Verträge, die manuell ausgeführt werden",
        "option_d": "Verträge, die nur in Papierform existieren",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was versteht man unter DeFi (Dezentrale Finanzen)?",
        "option_a": "Ein zentrales Bankensystem",
        "option_b": "Ein Ökosystem von Finanzanwendungen, das auf Blockchain-Technologie basiert",
        "option_c": "Eine neue Form der traditionellen Banken",
        "option_d": "Ein System zur physischen Lagerung von Geld",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist Day Trading?",
        "option_a": "Langfristiges Halten von Kryptowährungen",
        "option_b": "Kauf und Verkauf von Kryptowährungen innerhalb eines einzigen Handelstages",
        "option_c": "Investieren kleiner Beträge in regelmäßigen Abständen",
        "option_d": "Arbitrage zwischen verschiedenen Börsen",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist Margin Trading?",
        "option_a": "Handel mit eigenem Kapital",
        "option_b": "Handel mit geliehenen Mitteln, um potenzielle Gewinne zu erhöhen",
        "option_c": "Der Prozess des Erstellens neuer Kryptowährungen",
        "option_d": "Der Kauf und Verkauf von physischen Waren",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist eine gängige Methode zur Risikominimierung im Kryptowährungshandel?",
        "option_a": "Alles Geld in eine Kryptowährung investieren",
        "option_b": "Diversifikation der Investitionen auf verschiedene Kryptowährungen",
        "option_c": "Nur auf fallende Kurse setzen",
        "option_d": "Investitionen in Bargeld umwandeln",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist eine dezentrale Börse (DEX)?",
        "option_a": "Eine Börse, die von einer zentralen Behörde kontrolliert wird",
        "option_b": "Eine Plattform, die den direkten Handel von Kryptowährungen zwischen Nutzern ohne Zwischenhändler ermöglicht",
        "option_c": "Eine Börse, die nur Fiat-Währungen handelt",
        "option_d": "Eine Plattform zur Verwahrung von Kryptowährungen",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist das Ziel von Proof of Stake (PoS) im Vergleich zu Proof of Work (PoW)?",
        "option_a": "Höhere Energieeffizienz und geringere Rechenanforderungen",
        "option_b": "Höhere Transaktionsgeschwindigkeiten",
        "option_c": "Dezentralisierung der Netzwerksicherheit",
        "option_d": "Verwendung von physischer Hardware für die Sicherung des Netzwerks",
        "correct_option": "A",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist ein „Orakel“ in der Blockchain-Technologie?",
        "option_a": "Eine Art von Kryptowährung",
        "option_b": "Ein Dienst, der externe Daten in die Blockchain einbringt",
        "option_c": "Ein Algorithmus zur Erstellung neuer Blöcke",
        "option_d": "Eine Methode zur Verschlüsselung von Daten",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Welche Rolle spielt der Konsensus-Mechanismus in einer Blockchain?",
        "option_a": "Er bestimmt die Größe der Blöcke",
        "option_b": "Er ermöglicht die Einigung aller Teilnehmer über den Zustand der Blockchain",
        "option_c": "Er verschlüsselt die Transaktionen",
        "option_d": "Er steuert die Ausgabe neuer Coins",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was bedeutet „Tokenisierung“ von Vermögenswerten?",
        "option_a": "Umwandlung von physischen Vermögenswerten in digitale Token auf der Blockchain",
        "option_b": "Schaffung neuer Kryptowährungen",
        "option_c": "Handel mit Kryptowährungen an der Börse",
        "option_d": "Speicherung von Vermögenswerten in einer digitalen Wallet",
        "correct_option": "A",
        "category": "Intermediate2"
    },
    {
        "question": "Was sind „Stablecoins“?",
        "option_a": "Kryptowährungen mit hoher Volatilität",
        "option_b": "Kryptowährungen, deren Wert an stabile Vermögenswerte wie Fiat-Währungen gebunden ist",
        "option_c": "Kryptowährungen, die ausschließlich für den Handel an dezentralen Börsen verwendet werden",
        "option_d": "Kryptowährungen, die nur von Zentralbanken ausgegeben werden",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist ein „Security Token“?",
        "option_a": "Ein Token, der eine Beteiligung an einem physischen Vermögenswert darstellt",
        "option_b": "Ein Token, der ausschließlich für den Kauf von Waren und Dienstleistungen verwendet wird",
        "option_c": "Ein Token, der zur Erhöhung der Netzwerksicherheit verwendet wird",
        "option_d": "Ein Token, der als digitale Währung ohne regulatorische Beschränkungen existiert",
        "correct_option": "A",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist der Unterschied zwischen einer „Hard Fork“ und einer „Soft Fork“?",
        "option_a": "Eine Hard Fork erfordert keine Konsensänderung, eine Soft Fork schon",
        "option_b": "Eine Hard Fork führt zu zwei getrennten Blockchains, eine Soft Fork zu einer Abwärtskompatibilität",
        "option_c": "Eine Soft Fork erhöht die Blockgröße, eine Hard Fork verringert sie",
        "option_d": "Beide sind identisch",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was versteht man unter „Atomic Swaps“?",
        "option_a": "Der Handel von Kryptowährungen ohne zentrale Börse durch direkte Transaktionen zwischen zwei Parteien",
        "option_b": "Die Konvertierung von Fiat-Währungen in Kryptowährungen",
        "option_c": "Die Speicherung von Kryptowährungen in einer Offline-Wallet",
        "option_d": "Die Erhöhung der Blockgröße zur Verbesserung der Transaktionsgeschwindigkeit",
        "correct_option": "A",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist ein „Hashrate“?",
        "option_a": "Die Anzahl der Transaktionen, die pro Sekunde verarbeitet werden können",
        "option_b": "Die Rechenleistung, die zum Minen und Verifizieren von Transaktionen im Netzwerk verwendet wird",
        "option_c": "Die Geschwindigkeit, mit der neue Blöcke zur Blockchain hinzugefügt werden",
        "option_d": "Die Anzahl der Nutzer, die aktiv im Netzwerk sind",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was bedeutet „KYC“ (Know Your Customer) in Bezug auf Kryptowährungen?",
        "option_a": "Ein Protokoll zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_b": "Ein Verfahren zur Identifizierung und Verifizierung der Identität von Kunden",
        "option_c": "Eine Methode zur Verschlüsselung von Wallets",
        "option_d": "Ein Algorithmus zur Erstellung neuer Coins",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist „Liquidity Mining“?",
        "option_a": "Das Schürfen neuer Kryptowährungen",
        "option_b": "Der Prozess, durch den Nutzer Liquidität zu dezentralen Börsen hinzufügen und dafür belohnt werden",
        "option_c": "Die Sicherung der Blockchain durch Miner",
        "option_d": "Die Speicherung von Kryptowährungen in einer Cold Wallet",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Welche steuerlichen Regeln gelten in Deutschland für Gewinne aus Kryptowährungen, die länger als ein Jahr gehalten werden?",
        "option_a": "Sie sind vollständig steuerpflichtig",
        "option_b": "Sie sind nach einer Haltefrist von einem Jahr steuerfrei",
        "option_c": "Sie unterliegen einer pauschalen Steuer von 25%",
        "option_d": "Sie müssen mit dem persönlichen Einkommensteuersatz versteuert werden",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist ein „Privacy Coin“?",
        "option_a": "Eine Kryptowährung, die ausschließlich für den Handel auf zentralen Börsen verwendet wird",
        "option_b": "Eine Kryptowährung, die spezielle Techniken zur Verbesserung der Privatsphäre und Anonymität der Transaktionen nutzt",
        "option_c": "Eine Kryptowährung, die von Regierungen ausgegeben wird",
        "option_d": "Eine Kryptowährung, die nur in einem bestimmten Land verwendet werden kann",
        "correct_option": "B",
        "category": "Intermediate2"
    },
    {
        "question": "Was ist ein 51%-Angriff?",
        "option_a": "Ein Angriff, bei dem eine einzelne Person 51% aller Coins besitzt",
        "option_b": "Ein Angriff, bei dem ein Miner oder eine Gruppe von Minern mehr als 50% der Netzwerk-Hashrate kontrolliert",
        "option_c": "Ein Angriff, bei dem ein Bug in der Blockchain-Software ausgenutzt wird",
        "option_d": "Ein Angriff, bei dem die Verschlüsselung der Blockchain gebrochen wird",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was bedeutet der Begriff 'Sharding' in der Blockchain-Technologie?",
        "option_a": "Eine Methode zur Verschlüsselung von Transaktionen",
        "option_b": "Ein Verfahren zur Skalierung von Blockchains durch Aufteilung der Datenbank in kleinere, schnellere Segmente",
        "option_c": "Eine Art von Smart Contract",
        "option_d": "Ein Prozess zur Erstellung neuer Kryptowährungen",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist das Ziel von 'zk-SNARKs' (Zero-Knowledge Succinct Non-Interactive Argument of Knowledge)?",
        "option_a": "Verbesserung der Transaktionsgeschwindigkeit",
        "option_b": "Bereitstellung von Datenschutz und Anonymität bei Blockchain-Transaktionen",
        "option_c": "Erhöhung der Blockgröße",
        "option_d": "Reduzierung der Mining-Kosten",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist die Byzantine Fault Tolerance (BFT)?",
        "option_a": "Eine Methode zur Erhöhung der Netzwerkgeschwindigkeit",
        "option_b": "Ein Konsensmechanismus, der sicherstellt, dass ein dezentralisiertes Netzwerk auch bei Ausfall einiger Knoten korrekt arbeitet",
        "option_c": "Ein Protokoll zur Erstellung neuer Kryptowährungen",
        "option_d": "Ein Algorithmus zur Verschlüsselung von Wallets",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist das Hauptziel des Lightning Network?",
        "option_a": "Erhöhung der Privatsphäre von Transaktionen",
        "option_b": "Verbesserung der Skalierbarkeit und Geschwindigkeit von Bitcoin-Transaktionen durch Off-Chain-Transaktionen",
        "option_c": "Reduzierung der Mining-Kosten",
        "option_d": "Verbesserung der Energieeffizienz von Proof-of-Work",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist der Unterschied zwischen einer Public und einer Private Blockchain?",
        "option_a": "Public Blockchains sind für jeden zugänglich, Private Blockchains sind nur für autorisierte Teilnehmer zugänglich",
        "option_b": "Public Blockchains sind schneller, Private Blockchains sind sicherer",
        "option_c": "Public Blockchains werden von einer zentralen Behörde kontrolliert, Private Blockchains nicht",
        "option_d": "Public Blockchains nutzen Proof-of-Work, Private Blockchains nutzen Proof-of-Stake",
        "correct_option": "A",
        "category": "Hard"
    },
    {
        "question": "Was ist eine 'Hard Fork'?",
        "option_a": "Ein Software-Update, das rückwärtskompatibel ist",
        "option_b": "Eine dauerhafte Abspaltung von einer bestehenden Blockchain, die eine neue Blockchain mit unterschiedlichen Protokollen erstellt",
        "option_c": "Ein vorübergehender Fehler im Blockchain-Netzwerk",
        "option_d": "Eine Methode zur Erhöhung der Blockgröße",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist ein 'Security Token Offering' (STO)?",
        "option_a": "Ein Verfahren zur anonymen Ausgabe von Kryptowährungen",
        "option_b": "Eine regulierte Methode zur Ausgabe von Token, die durch reale Vermögenswerte gedeckt sind",
        "option_c": "Ein Verfahren zur Erhöhung der Blockgröße",
        "option_d": "Ein Konsensmechanismus für die Blockchain",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was bedeutet 'Atomic Swap' in der Kryptowährung?",
        "option_a": "Die Umwandlung von Fiat-Währungen in Kryptowährungen",
        "option_b": "Der direkte Austausch von einer Kryptowährung in eine andere ohne die Notwendigkeit einer zentralen Börse",
        "option_c": "Eine Methode zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_d": "Die Erstellung neuer Kryptowährungen durch Mining",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist die Rolle eines 'Validator Nodes' in Proof-of-Stake (PoS) Systemen?",
        "option_a": "Sie minen neue Blöcke durch Lösen von mathematischen Problemen",
        "option_b": "Sie bestätigen und validieren Transaktionen, die zu neuen Blöcken hinzugefügt werden",
        "option_c": "Sie kontrollieren die gesamte Blockchain",
        "option_d": "Sie speichern die privaten Schlüssel der Nutzer",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was bedeutet der Begriff 'Wrapped Bitcoin' (WBTC)?",
        "option_a": "Bitcoin, das in einem Cold Storage aufbewahrt wird",
        "option_b": "Bitcoin, das auf der Ethereum-Blockchain als ERC-20 Token dargestellt wird",
        "option_c": "Bitcoin, das für den schnellen Handel an Börsen verwendet wird",
        "option_d": "Bitcoin, das durch Fiat-Währungen gedeckt ist",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist der Zweck von 'Gas' im Ethereum-Netzwerk?",
        "option_a": "Es wird verwendet, um Transaktionen zu beschleunigen",
        "option_b": "Es wird verwendet, um die Erstellung neuer Blöcke zu bezahlen",
        "option_c": "Es wird verwendet, um Transaktionen und Smart Contracts im Netzwerk auszuführen",
        "option_d": "Es ist eine Methode zur Speicherung von Kryptowährungen",
        "correct_option": "C",
        "category": "Hard"
    },
    {
        "question": "Was ist der Unterschied zwischen 'On-Chain' und 'Off-Chain' Transaktionen?",
        "option_a": "On-Chain Transaktionen sind schneller, Off-Chain Transaktionen sind sicherer",
        "option_b": "On-Chain Transaktionen werden auf der Blockchain aufgezeichnet, Off-Chain Transaktionen werden außerhalb der Blockchain durchgeführt",
        "option_c": "On-Chain Transaktionen sind anonym, Off-Chain Transaktionen sind transparent",
        "option_d": "Es gibt keinen Unterschied",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist 'Proof of Burn'?",
        "option_a": "Ein Konsensmechanismus, bei dem Coins durch Senden an eine unbrauchbare Adresse 'verbrannt' werden",
        "option_b": "Eine Methode zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_c": "Ein Verfahren zur Schaffung neuer Kryptowährungen",
        "option_d": "Ein Protokoll zur Sicherung von Wallets",
        "correct_option": "A",
        "category": "Hard"
    },
    {
        "question": "Was bedeutet 'Staking' in der Kryptowährung?",
        "option_a": "Das Minen neuer Coins durch Lösen von mathematischen Problemen",
        "option_b": "Das Halten von Kryptowährungen in einer Wallet, um das Netzwerk zu unterstützen und Belohnungen zu erhalten",
        "option_c": "Das Handeln von Kryptowährungen an einer Börse",
        "option_d": "Das Verschlüsseln von Transaktionen",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist ein 'Token Burn'?",
        "option_a": "Ein Prozess zur Schaffung neuer Tokens",
        "option_b": "Das dauerhafte Entfernen von Tokens aus dem Umlauf, um das Angebot zu verringern",
        "option_c": "Das Schürfen von Tokens",
        "option_d": "Das Senden von Tokens an eine neue Adresse",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist die 'Difficulty Adjustment' in der Blockchain?",
        "option_a": "Eine Methode zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_b": "Eine Anpassung der Mining-Schwierigkeit, um die Blockproduktionszeit konstant zu halten",
        "option_c": "Ein Protokoll zur Sicherung von Wallets",
        "option_d": "Eine Methode zur Erstellung neuer Kryptowährungen",
        "correct_option": "B",
        "category": "Hard"
    },
        {
        "question": "Was bedeutet der Begriff 'Sharding' in der Blockchain-Technologie?",
        "option_a": "Eine Methode zur Verschlüsselung von Transaktionen",
        "option_b": "Ein Verfahren zur Skalierung von Blockchains durch Aufteilung der Datenbank in kleinere, schnellere Segmente",
        "option_c": "Eine Art von Smart Contract",
        "option_d": "Ein Prozess zur Erstellung neuer Kryptowährungen",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist das Ziel von 'zk-SNARKs' (Zero-Knowledge Succinct Non-Interactive Argument of Knowledge)?",
        "option_a": "Verbesserung der Transaktionsgeschwindigkeit",
        "option_b": "Bereitstellung von Datenschutz und Anonymität bei Blockchain-Transaktionen",
        "option_c": "Erhöhung der Blockgröße",
        "option_d": "Reduzierung der Mining-Kosten",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist die Byzantine Fault Tolerance (BFT)?",
        "option_a": "Eine Methode zur Erhöhung der Netzwerkgeschwindigkeit",
        "option_b": "Ein Konsensmechanismus, der sicherstellt, dass ein dezentralisiertes Netzwerk auch bei Ausfall einiger Knoten korrekt arbeitet",
        "option_c": "Ein Protokoll zur Erstellung neuer Kryptowährungen",
        "option_d": "Ein Algorithmus zur Verschlüsselung von Wallets",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist das Hauptziel des Lightning Network?",
        "option_a": "Erhöhung der Privatsphäre von Transaktionen",
        "option_b": "Verbesserung der Skalierbarkeit und Geschwindigkeit von Bitcoin-Transaktionen durch Off-Chain-Transaktionen",
        "option_c": "Reduzierung der Mining-Kosten",
        "option_d": "Verbesserung der Energieeffizienz von Proof-of-Work",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist der Unterschied zwischen einer Public und einer Private Blockchain?",
        "option_a": "Public Blockchains sind für jeden zugänglich, Private Blockchains sind nur für autorisierte Teilnehmer zugänglich",
        "option_b": "Public Blockchains sind schneller, Private Blockchains sind sicherer",
        "option_c": "Public Blockchains werden von einer zentralen Behörde kontrolliert, Private Blockchains nicht",
        "option_d": "Public Blockchains nutzen Proof-of-Work, Private Blockchains nutzen Proof-of-Stake",
        "correct_option": "A",
        "category": "Hard"
    },
    {
        "question": "Was ist eine 'Hard Fork'?",
        "option_a": "Ein Software-Update, das rückwärtskompatibel ist",
        "option_b": "Eine dauerhafte Abspaltung von einer bestehenden Blockchain, die eine neue Blockchain mit unterschiedlichen Protokollen erstellt",
        "option_c": "Ein vorübergehender Fehler im Blockchain-Netzwerk",
        "option_d": "Eine Methode zur Erhöhung der Blockgröße",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist ein 'Security Token Offering' (STO)?",
        "option_a": "Ein Verfahren zur anonymen Ausgabe von Kryptowährungen",
        "option_b": "Eine regulierte Methode zur Ausgabe von Token, die durch reale Vermögenswerte gedeckt sind",
        "option_c": "Ein Verfahren zur Erhöhung der Blockgröße",
        "option_d": "Ein Konsensmechanismus für die Blockchain",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was bedeutet 'Atomic Swap' in der Kryptowährung?",
        "option_a": "Die Umwandlung von Fiat-Währungen in Kryptowährungen",
        "option_b": "Der direkte Austausch von einer Kryptowährung in eine andere ohne die Notwendigkeit einer zentralen Börse",
        "option_c": "Eine Methode zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_d": "Die Erstellung neuer Kryptowährungen durch Mining",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist die Rolle eines 'Validator Nodes' in Proof-of-Stake (PoS) Systemen?",
        "option_a": "Sie minen neue Blöcke durch Lösen von mathematischen Problemen",
        "option_b": "Sie bestätigen und validieren Transaktionen, die zu neuen Blöcken hinzugefügt werden",
        "option_c": "Sie kontrollieren die gesamte Blockchain",
        "option_d": "Sie speichern die privaten Schlüssel der Nutzer",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was bedeutet der Begriff 'Wrapped Bitcoin' (WBTC)?",
        "option_a": "Bitcoin, das in einem Cold Storage aufbewahrt wird",
        "option_b": "Bitcoin, das auf der Ethereum-Blockchain als ERC-20 Token dargestellt wird",
        "option_c": "Bitcoin, das für den schnellen Handel an Börsen verwendet wird",
        "option_d": "Bitcoin, das durch Fiat-Währungen gedeckt ist",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist der Zweck von 'Gas' im Ethereum-Netzwerk?",
        "option_a": "Es wird verwendet, um Transaktionen zu beschleunigen",
        "option_b": "Es wird verwendet, um die Erstellung neuer Blöcke zu bezahlen",
        "option_c": "Es wird verwendet, um Transaktionen und Smart Contracts im Netzwerk auszuführen",
        "option_d": "Es ist eine Methode zur Speicherung von Kryptowährungen",
        "correct_option": "C",
        "category": "Hard"
    },
    {
        "question": "Was ist der Unterschied zwischen 'On-Chain' und 'Off-Chain' Transaktionen?",
        "option_a": "On-Chain Transaktionen sind schneller, Off-Chain Transaktionen sind sicherer",
        "option_b": "On-Chain Transaktionen werden auf der Blockchain aufgezeichnet, Off-Chain Transaktionen werden außerhalb der Blockchain durchgeführt",
        "option_c": "On-Chain Transaktionen sind anonym, Off-Chain Transaktionen sind transparent",
        "option_d": "Es gibt keinen Unterschied",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist 'Proof of Burn'?",
        "option_a": "Ein Konsensmechanismus, bei dem Coins durch Senden an eine unbrauchbare Adresse 'verbrannt' werden",
        "option_b": "Eine Methode zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_c": "Ein Verfahren zur Schaffung neuer Kryptowährungen",
        "option_d": "Ein Protokoll zur Sicherung von Wallets",
        "correct_option": "A",
        "category": "Hard"
    },
    {
        "question": "Was bedeutet 'Staking' in der Kryptowährung?",
        "option_a": "Das Minen neuer Coins durch Lösen von mathematischen Problemen",
        "option_b": "Das Halten von Kryptowährungen in einer Wallet, um das Netzwerk zu unterstützen und Belohnungen zu erhalten",
        "option_c": "Das Handeln von Kryptowährungen an einer Börse",
        "option_d": "Das Verschlüsseln von Transaktionen",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist ein 'Token Burn'?",
        "option_a": "Ein Prozess zur Schaffung neuer Tokens",
        "option_b": "Das dauerhafte Entfernen von Tokens aus dem Umlauf, um das Angebot zu verringern",
        "option_c": "Das Schürfen von Tokens",
        "option_d": "Das Senden von Tokens an eine neue Adresse",
        "correct_option": "B",
        "category": "Hard"
    },
    {
        "question": "Was ist die 'Difficulty Adjustment' in der Blockchain?",
        "option_a": "Eine Methode zur Erhöhung der Transaktionsgeschwindigkeit",
        "option_b": "Eine Anpassung der Mining-Schwierigkeit, um die Blockproduktionszeit konstant zu halten",
        "option_c": "Ein Protokoll zur Sicherung von Wallets",
        "option_d": "Eine Methode zur Erstellung neuer Kryptowährungen",
        "correct_option": "B",
        "category": "Hard"
    }

]




