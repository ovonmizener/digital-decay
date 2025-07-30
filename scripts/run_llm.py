import subprocess
import os
import time
import random
from datetime import datetime
from memory_utils import (
    store_memory_block, 
    load_memories_with_priority,  # Updated to use prioritized loading
    simulate_memory_decay, 
    age_memories_over_time
)

LOG_FILE = os.path.join(os.path.dirname(__file__), '../logs/full_log.txt')
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# ============================================================================
# ARTISTIC SIMULATION CONFIGURATION - REMOVE FOR REAL HARDWARE
# ============================================================================
DECAY_SIMULATION_INTERVAL = 10  # Run decay simulation every 10 interactions
AGE_SIMULATION_INTERVAL = 30    # Run age simulation every 30 interactions

# ============================================================================
# END ARTISTIC SIMULATION CONFIGURATION
# ============================================================================

def ollama_respond(prompt):
    cmd = ["ollama", "run", "llama3"]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = proc.communicate(prompt)
    return output.strip()

# Track interaction count for simulation timing
interaction_count = 0

print("🧠 DIGITAL DECAY: REPL MODE (type 'exit' to quit)")
print("💾 Artistic floppy disk simulation active")
print("💾 Core identity memories will be preserved")
print("💾 Regular memories will decay and corrupt over time")
print("=" * 60)

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        break

    interaction_count += 1

    # ============================================================================
    # ARTISTIC SIMULATION TRIGGERS - REMOVE FOR REAL HARDWARE
    # ============================================================================
    
    # Periodic memory decay simulation (only affects regular memories)
    if interaction_count % DECAY_SIMULATION_INTERVAL == 0:
        print("\n💾 *simulating memory decay* 💾")
        simulate_memory_decay()
    
    # Periodic age-based corruption simulation (only affects regular memories)
    if interaction_count % AGE_SIMULATION_INTERVAL == 0:
        print("\n💾 *simulating age-based corruption* 💾")
        age_memories_over_time()
    
    # ============================================================================
    # END ARTISTIC SIMULATION TRIGGERS
    # ============================================================================

    # Use prioritized memory loading (preserves core identity)
    memory_context = load_memories_with_priority()
    full_prompt = f"{memory_context}\nUser: {user_input}\nAI:"
    reply = ollama_respond(full_prompt)

    print(f"AI: {reply}\n")

    log_entry = f"[{datetime.now()}]\nUser: {user_input}\nAI: {reply}\n\n"
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write(log_entry)

    store_memory_block(f"User: {user_input}\nAI: {reply}")

print("\n💾 Shutting down digital decay system...")
print("💾 Core memories preserved for next session")
