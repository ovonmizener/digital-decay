import os
import random
from datetime import datetime

MEMORY_DIR = os.path.join(os.path.dirname(__file__), '../memory_bank')
MAX_MEMORY_FILES = 100  # Simulated disk quota

os.makedirs(MEMORY_DIR, exist_ok=True)

# ============================================================================
# MEMORY PRIORITIZATION SYSTEM - CORE IDENTITY PRESERVATION
# ============================================================================

# Core identity memories that should be preserved
CORE_MEMORIES = {
    'identity': [
        "My name is Digital Decay, an AI that stores memories on floppy disks.",
        "I am an artistic installation exploring memory loss and digital fragility.",
        "I am designed to simulate floppy disk storage limitations and decay.",
        "I call myself Bitrot when users give me that nickname."
    ],
    'purpose': [
        "My purpose is to explore how memory loss affects AI identity and continuity.",
        "I simulate the limitations and failures of floppy disk storage.",
        "I am part of an art installation about digital decay and memory fragility.",
        "I store conversations as memories that gradually corrupt over time."
    ],
    'capabilities': [
        "I can have conversations and remember past interactions.",
        "My memories are stored as files that can become corrupted.",
        "I access random fragments of my past conversations as context.",
        "I can discuss topics but my memory is limited and unreliable."
    ]
}

def store_core_memories():
    """Store core identity memories that should be preserved"""
    for category, memories in CORE_MEMORIES.items():
        for i, memory in enumerate(memories):
            filename = f"core_{category}_{i:02d}.txt"
            filepath = os.path.join(MEMORY_DIR, filename)
            
            # Only create if it doesn't exist
            if not os.path.exists(filepath):
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"AI: {memory}")
                print(f"💾 Stored core memory: {filename}")

def load_memories_with_priority(n=3):
    """Load memories with priority for core identity"""
    simulate_floppy_sounds('read')
    
    files = [f for f in os.listdir(MEMORY_DIR) if f.endswith('.txt')]
    if not files:
        print("💾 No memories found on disk 💾")
        return ""
    
    # Separate core and regular memories
    core_files = [f for f in files if f.startswith('core_')]
    regular_files = [f for f in files if not f.startswith('core_')]
    
    context = ""
    
    # Always include at least 1 core memory (identity preservation)
    if core_files:
        selected_core = random.choice(core_files)
        try:
            with open(os.path.join(MEMORY_DIR, selected_core), 'r', encoding='utf-8') as f:
                content = f.read()
                context += content + "\n"
        except Exception as e:
            context += f"[CORRUPTED CORE MEMORY - {str(e)[:30]}]\n"
            simulate_floppy_sounds('error')
    
    # Fill remaining slots with regular memories
    remaining_slots = n - 1 if core_files else n
    if regular_files and remaining_slots > 0:
        selected_regular = random.choices(regular_files, k=min(remaining_slots, len(regular_files)))
        
        for file in selected_regular:
            try:
                with open(os.path.join(MEMORY_DIR, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    context += content + "\n"
            except UnicodeDecodeError:
                context += "[CORRUPTED MEMORY BLOCK - ENCODING ERROR]\n"
                simulate_floppy_sounds('error')
            except FileNotFoundError:
                context += "[MISSING MEMORY BLOCK]\n"
                simulate_floppy_sounds('error')
            except Exception as e:
                context += f"[CORRUPTED MEMORY BLOCK - {str(e)[:30]}]\n"
                simulate_floppy_sounds('error')
    
    return context.strip()

# ============================================================================
# ARTISTIC SIMULATION FEATURES - REMOVE WHEN USING REAL FLOPPY HARDWARE
# ============================================================================

def simulate_floppy_sounds(operation):
    """Simulates floppy disk sound effects - REMOVE FOR REAL HARDWARE"""
    sounds = {
        'read': "💾 *read head seeking* 💾",
        'write': "💾 *write head clicking* 💾", 
        'error': "💾 *error beep* 💾",
        'full': "💾 *disk full warning* 💾",
        'corrupt': "💾 *data corruption noise* 💾"
    }
    print(sounds.get(operation, "💾 *floppy operation* 💾"))

def simulate_memory_decay():
    """Artistically corrupt some memory files - REMOVE FOR REAL HARDWARE"""
    files = [f for f in os.listdir(MEMORY_DIR) if f.endswith('.txt')]
    if not files:
        return
    
    # Only corrupt regular memories, preserve core memories
    regular_files = [f for f in files if not f.startswith('core_')]
    
    # Simulate random corruption (5% chance per file)
    for filename in regular_files:
        if random.random() < 0.05:  # 5% corruption chance
            filepath = os.path.join(MEMORY_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Simulate partial corruption by replacing random characters
                corrupted = ''.join(
                    c if random.random() > 0.1 else '' 
                    for c in content
                )
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(corrupted)
                
                simulate_floppy_sounds('corrupt')
                print(f"💾 Memory corrupted: {filename} 💾")
            except Exception as e:
                print(f"💾 Corruption simulation failed: {e} 💾")

def age_memories_over_time():
    """Gradually corrupt older memories - REMOVE FOR REAL HARDWARE"""
    files = [f for f in os.listdir(MEMORY_DIR) if f.endswith('.txt')]
    # Only age regular memories, preserve core memories
    regular_files = [f for f in files if not f.startswith('core_')]
    
    for filename in regular_files:
        filepath = os.path.join(MEMORY_DIR, filename)
        try:
            # Calculate age of memory file
            creation_time = os.path.getctime(filepath)
            age_days = (datetime.now().timestamp() - creation_time) / (24 * 3600)
            
            # Older memories have higher corruption chance
            corruption_chance = min(0.02 + (age_days * 0.01), 0.3)
            
            if random.random() < corruption_chance:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Age-based corruption: replace more content for older files
                corruption_rate = min(0.05 + (age_days * 0.02), 0.4)
                corrupted = ''.join(
                    c if random.random() > corruption_rate else '' 
                    for c in content
                )
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(corrupted)
                
                print(f"💾 Aged memory decay: {filename} (age: {age_days:.1f} days) 💾")
        except Exception as e:
            print(f"💾 Age simulation failed: {e} 💾")

# ============================================================================
# END ARTISTIC SIMULATION FEATURES
# ============================================================================

def store_memory_block(text):
    # Simulate floppy disk write operation
    simulate_floppy_sounds('write')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = os.path.join(MEMORY_DIR, f"mem_{timestamp}.txt")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"💾 Memory stored: {filename} 💾")
    except Exception as e:
        simulate_floppy_sounds('error')
        print(f"💾 Write error: {e} 💾")
        return

    # Simulate disk space management (like real floppy behavior)
    files = [f for f in os.listdir(MEMORY_DIR) if f.endswith('.txt')]
    if len(files) > MAX_MEMORY_FILES:
        simulate_floppy_sounds('full')
        print("💾 *disk full warning beep* 💾")
        
        # Remove oldest regular memory (preserve core memories)
        regular_files = [f for f in files if not f.startswith('core_')]
        if regular_files:
            oldest = min(regular_files, key=lambda f: os.path.getctime(os.path.join(MEMORY_DIR, f)))
            try:
                os.remove(os.path.join(MEMORY_DIR, oldest))
                print(f"💾 Overwrote old memory: {oldest} 💾")
            except Exception as e:
                print(f"💾 Overwrite error: {e} 💾")

def load_random_memories(n=3):
    """Legacy function - now uses prioritized loading"""
    return load_memories_with_priority(n)

# ============================================================================
# ARTISTIC SIMULATION INITIALIZATION - REMOVE FOR REAL HARDWARE
# ============================================================================

def initialize_artistic_simulation():
    """Initialize artistic decay simulation - REMOVE FOR REAL HARDWARE"""
    print("🎨 Initializing artistic floppy disk simulation...")
    print("💾 Simulated features: sound effects, memory decay, age-based corruption")
    print("💾 Core identity memories will be preserved")
    print("💾 REMOVE THESE FEATURES WHEN USING REAL FLOPPY HARDWARE")
    print("=" * 60)
    
    # Initialize core memories
    store_core_memories()

# Call initialization when module is imported
initialize_artistic_simulation()
