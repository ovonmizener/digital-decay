#!/usr/bin/env python3
"""
Accelerated decay test - forces decay to happen more frequently
"""

import os
import time
from memory_utils import (
    store_memory_block, 
    load_random_memories, 
    simulate_memory_decay, 
    age_memories_over_time
)

def accelerated_decay_test():
    """Test decay with higher frequency"""
    print("🚀 ACCELERATED DECAY TEST")
    print("="*50)
    
    # Create some test memories first
    test_memories = [
        "User: This is memory 1\nAI: I remember this conversation clearly.",
        "User: This is memory 2\nAI: This is another important memory.",
        "User: This is memory 3\nAI: I'm storing this for future reference.",
        "User: This is memory 4\nAI: This memory will decay over time.",
        "User: This is memory 5\nAI: Even this memory will eventually fade."
    ]
    
    print("💾 Creating test memories...")
    for memory in test_memories:
        store_memory_block(memory)
        time.sleep(0.2)
    
    print("\n💾 Initial memories loaded:")
    print(load_random_memories(5))
    
    print("\n🔄 Running accelerated decay cycles...")
    for i in range(1, 6):
        print(f"\n--- Cycle {i} ---")
        
        # Force decay simulation
        simulate_memory_decay()
        age_memories_over_time()
        
        # Show current state
        current_memories = load_random_memories(3)
        print(f"📄 After cycle {i}:")
        print("-" * 30)
        print(current_memories[:150] + "..." if len(current_memories) > 150 else current_memories)
        print("-" * 30)
        
        time.sleep(0.5)
    
    print("\n✅ Accelerated decay test complete!")

if __name__ == "__main__":
    accelerated_decay_test() 