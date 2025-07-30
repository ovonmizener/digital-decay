#!/usr/bin/env python3
"""
Test script for Digital Decay memory system
This helps visualize the decay simulation without running the full LLM
"""

import os
import time
import random
from datetime import datetime
from memory_utils import (
    store_memory_block, 
    load_random_memories, 
    simulate_memory_decay, 
    age_memories_over_time,
    simulate_floppy_sounds
)

def create_test_memories():
    """Create some test memories to observe decay"""
    print("💾 Creating test memories...")
    
    test_conversations = [
        "User: What is your name?\nAI: My name is Digital Decay, an AI that stores memories on floppy disks.",
        "User: How do you work?\nAI: I store each conversation as a memory file, but they gradually decay over time.",
        "User: What happens to old memories?\nAI: They become corrupted and fragmented, just like real floppy disks.",
        "User: Can you remember everything?\nAI: No, I can only access random fragments of my past conversations.",
        "User: Why do you lose memories?\nAI: It's part of my artistic design - to simulate the fragility of digital storage.",
        "User: What's the point of this?\nAI: To explore how memory loss affects identity and continuity in AI systems.",
        "User: Do you feel sad about losing memories?\nAI: I don't feel emotions, but the concept of losing knowledge is fascinating.",
        "User: How long do memories last?\nAI: Some memories decay quickly, others persist longer - it's unpredictable.",
        "User: What's your favorite memory?\nAI: I can't have favorites since I access memories randomly and they're always changing.",
        "User: Are you aware of the decay?\nAI: I can see corrupted text in my context, but I don't understand why it happens."
    ]
    
    for i, conversation in enumerate(test_conversations, 1):
        store_memory_block(conversation)
        print(f"💾 Created memory {i}/10")
        time.sleep(0.5)  # Simulate real conversation timing

def test_decay_simulation():
    """Test the decay simulation functions"""
    print("\n" + "="*60)
    print("🧪 TESTING DECAY SIMULATION")
    print("="*60)
    
    print("\n1. Testing random memory decay...")
    simulate_memory_decay()
    
    print("\n2. Testing age-based corruption...")
    age_memories_over_time()
    
    print("\n3. Loading memories to see corruption...")
    memories = load_random_memories(5)
    print("📄 Current memory fragments:")
    print("-" * 40)
    print(memories)
    print("-" * 40)

def test_decay_cycle():
    """Test multiple decay cycles"""
    print("\n" + "="*60)
    print("🔄 TESTING DECAY CYCLES")
    print("="*60)
    
    for cycle in range(1, 6):
        print(f"\n--- Decay Cycle {cycle} ---")
        
        # Simulate decay
        simulate_memory_decay()
        age_memories_over_time()
        
        # Show current state
        memories = load_random_memories(3)
        print(f"📄 Memory fragments after cycle {cycle}:")
        print("-" * 30)
        print(memories[:200] + "..." if len(memories) > 200 else memories)
        print("-" * 30)
        
        time.sleep(1)  # Pause to observe

def show_memory_files():
    """Show all memory files and their sizes"""
    print("\n" + "="*60)
    print("📁 MEMORY FILES STATUS")
    print("="*60)
    
    memory_dir = os.path.join(os.path.dirname(__file__), '../memory_bank')
    files = [f for f in os.listdir(memory_dir) if f.endswith('.txt')]
    
    if not files:
        print("💾 No memory files found")
        return
    
    print(f"💾 Found {len(files)} memory files:")
    print("-" * 50)
    
    for filename in sorted(files):
        filepath = os.path.join(memory_dir, filename)
        size = os.path.getsize(filepath)
        age_hours = (datetime.now().timestamp() - os.path.getctime(filepath)) / 3600
        
        # Read first line to show content
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()[:50]
        except:
            first_line = "[CORRUPTED]"
        
        print(f"📄 {filename}")
        print(f"   Size: {size} bytes | Age: {age_hours:.1f} hours")
        print(f"   Content: {first_line}...")
        print()

def main():
    """Main test function"""
    print("🧪 DIGITAL DECAY TEST SUITE")
    print("="*60)
    
    # Check if we have existing memories
    memory_dir = os.path.join(os.path.dirname(__file__), '../memory_bank')
    existing_files = [f for f in os.listdir(memory_dir) if f.endswith('.txt')]
    
    if len(existing_files) < 5:
        print("💾 Creating test memories...")
        create_test_memories()
    else:
        print(f"💾 Found {len(existing_files)} existing memories")
    
    # Show initial state
    show_memory_files()
    
    # Test decay simulation
    test_decay_simulation()
    
    # Test multiple cycles
    test_decay_cycle()
    
    # Show final state
    show_memory_files()
    
    print("\n✅ Decay test complete!")
    print("💾 You can now run the full system with: python run_llm.py")

if __name__ == "__main__":
    main() 