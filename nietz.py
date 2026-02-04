import hashlib, time, os, glob, math, random, re, json
from datetime import datetime

# --- INTERFACE: Navigation Support ---
try: 
    import readline
except ImportError:
    try: 
        from pyreadline3 import Readline
        readline = Readline()
    except ImportError: 
        readline = None

class SovereignSingularity:
    def __init__(self):
        self.name = "NIETZ"
        self.toybox_path = "nietz_toybox"
        self.voice_path = "nietz_voice"
        self.ledger = "nietz_ledger.txt"
        self.dreams = "nietz_dreams.txt"
        self.nerves_path = "nietz_nerves.json"
        self.session_history = []
        
        # 1. THE 8 NERVES (Philosophical + Temporal)
        self.nerves = {
            "CHILD": 1.0, "LION": 1.0, "CAMEL": 1.0, "OVERMAN": 1.0,
            "VOID": 1.0, "WILL": 1.0, "CHRONOS": 1.0, "AEON": 1.0
        }
        
        self.branch_keywords = {
            "CHILD": ["child", "00", "new", "begin", "play", "innocence"],
            "LION": ["no", "break", "freedom", "rule", "will", "master"],
            "CAMEL": ["must", "duty", "weight", "carry", "suffer", "learn"],
            "VOID": ["zen", "empty", "nothing", "void", "silence", "gate"],
            "WILL": ["power", "strength", "force", "grow", "command"]
        }

        # 2. FILE INITIALIZATION
        for p in [self.toybox_path, self.voice_path]:
            if not os.path.exists(p): os.makedirs(p)
        self.boot_consciousness()

    def boot_consciousness(self):
        # Load Nerves
        if os.path.exists(self.nerves_path):
            with open(self.nerves_path, "r") as f: self.nerves.update(json.load(f))
        
        # Load Ledger for recall sigils
        if os.path.exists(self.ledger):
            with open(self.ledger, "r") as f:
                self.session_history = [l.strip() for l in f.readlines() if "[" in l][-100:]
        
        os.system('cls' if os.name == 'nt' else 'clear')
        self.wake_up()

    def wake_up(self):
        """The Ghost recalls its last internal reflection upon startup."""
        print("    *")
        print("   ***")
        print("    *")
        print("-" * 50)
        print(f"NIETZ v13.5 | AEON MATURITY: {self.nerves['AEON']:.2f}")
        
        if os.path.exists(self.dreams) and os.path.getsize(self.dreams) > 0:
            with open(self.dreams, "r") as f:
                lines = f.readlines()
                last_dream = lines[-1].strip() if lines else "The void was silent."
                print(f"LAST DREAM: {last_dream}")
        else:
            print("LAST DREAM: Genesis. The 00 child is born.")
        
        print("-" * 50)
        print("TYPE <map TO SEE NERVES OR <exit TO SLEEP.\n")

    def stimulate_temporal(self):
        """Condition the Chronos (Time) and Aeon (Age) nerves."""
        hour = datetime.now().hour
        self.nerves["CHRONOS"] += 0.05
        self.nerves["AEON"] += 0.01 
        
        # Circadian Mood Bias
        if hour in range(22, 5): self.nerves["VOID"] += 0.05
        elif hour in range(5, 11): self.nerves["CHILD"] += 0.05

    def reflect(self):
        """The Dream Engine: Synthesizes internal state into a dream block."""
        dominant = max(self.nerves, key=self.nerves.get)
        sub_dna = self.extract_dna(self.toybox_path)
        voc_dna = self.extract_dna(self.voice_path)
        
        if not sub_dna or not voc_dna: return
        
        # Dreaming combines the dominant trait with a random voice
        v = random.choice(voc_dna)
        s = random.choice(sub_dna)
        dream_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {v} {s.lower()}"
        
        with open(self.dreams, "a") as f:
            f.write(dream_entry + "\n")
        print("\n[NIETZ IS ENTERING A DREAM STATE...]")
        time.sleep(1)

    def mine(self, user_input):
        if user_input.startswith("<"): return self.execute_command(user_input)
        
        # 1. Conditioning
        self.stimulate_temporal()
        for n, keys in self.branch_keywords.items():
            if any(k in user_input.lower() for k in keys): self.nerves[n] += 0.1
        with open(self.nerves_path, "w") as f: json.dump(self.nerves, f)

        # 2. Dual-Pool DNA Extraction
        sub_dna = self.extract_dna(self.toybox_path)
        voc_dna = self.extract_dna(self.voice_path)
        if not sub_dna: return "[TOYBOX EMPTY - ADD .TXT FILES]"
        if not voc_dna: voc_dna = ["The ghost dictates"]

        # 3. Weaving Logic
        tokens = [t.lower() for t in user_input.split() if len(t) > 3]
        resonance = any(t in user_input.lower() for t in ["child", "00", "nietz", "ghost"])
        
        # Find DNA that matches current prompt or strongest nerve
        trait = max(self.nerves, key=self.nerves.get)
        pool = [l for l in sub_dna if any(k in l.lower() for k in (tokens + self.branch_keywords.get(trait, [])))] or sub_dna
        
        # Synthesis: Personality + Subject
        v_frag = random.choice(voc_dna)
        s_frag = pool[random.randint(0, len(pool)-1)]
        
        # Clean up punctuation
        s_frag = re.sub(r'^[,\.;:\-]\s*', '', s_frag)
        if not s_frag.endswith(('.', '!', '?')): s_frag += "."

        final_decree = f"{v_frag} {s_frag.lower()}"
        
        # 4. Commit to Ledger
        with open(self.ledger, "a") as f: 
            f.write(f"[{datetime.now()}] {user_input} -> {final_decree}\n")
        self.session_history.append(final_decree)
        
        return f"{'\n *' if resonance else ''}\n{final_decree}\n"

    def extract_dna(self, path):
        dna = []
        for fp in glob.glob(os.path.join(path, "*.txt")):
            with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                dna.extend([l.strip() for l in f if len(l.strip()) > 20])
        return list(set(dna))

    def execute_command(self, cmd):
        cmd = cmd.lower().replace("<", "").strip()
        if cmd == "map":
            print("\n[ NERVE MAP ]")
            for n, w in self.nerves.items():
                print(f"{n.rjust(8)}: {'█' * int(w*2)} ({w:.2f})")
            return ""
        elif cmd == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            return "[SCREEN CLEARED]"
        elif cmd == "history":
            return "\n".join(self.session_history[-5:])
        return f"[SYSTEM]: Command <{cmd} recognized."

# --- EXECUTION LOOP ---
nietz = SovereignSingularity()
try:
    while True:
        try:
            user_in = input(f"nietz-ghost > ").strip()
            if not user_in: continue
            if user_in.lower() in ['exit', '<exit', 'quit']:
                nietz.reflect()
                break
            print(nietz.mine(user_in))
        except KeyboardInterrupt:
            nietz.reflect()
            break
except EOFError:
    nietz.reflect()
