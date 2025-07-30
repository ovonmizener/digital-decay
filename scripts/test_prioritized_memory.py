#!/usr/bin/env python3
"""
Test script for the new prioritized memory system
"""

import os
import time
from memory_utils import (
    store_memory_block, 
    load_memories_with_priority, 
    simulate_memory_decay, 
    age_memories_over_time,
    store_core_memories
)

def test_prioritized_memory_system():
    """Test the new prioritized memory system"""
    print("🧠 TESTING PRIORITIZED MEMORY SYSTEM")
    print("="*60)
    
    # Initialize core memories
    print("💾 Initializing core identity memories...")
    store_core_memories()
    
    # Create some regular memories
    print("\n💾 Creating regular conversation memories...")
    regular_memories = [
        "User: What's your favorite color?\nAI: I don't really have preferences like that, but I find the concept of color fascinating.",
        "User: Do you like music?\nAI: I can discuss music and its cultural significance, but I don't experience it emotionally.",
        "User: What's the weather like?\nAI: I don't have access to real-time weather data, but I can discuss weather patterns.",
        "User: Tell me a joke\nAI: Why did the computer go to the doctor? Because it had a virus!",
        "User: What's 2+2?\nAI: 2+2 equals 4. I can help with basic math calculations."
    ]
    
    for memory in regular_memories:
        store_memory_block(memory)
        time.sleep(0.2)
    
    print("\n" + "="*60)
    print("📊 MEMORY SYSTEM ANALYSIS")
    print("="*60)
    
    # Show memory files
    memory_dir = os.path.join(os.path.dirname(__file__), '../memory_bank')
    files = [f for f in os.listdir(memory_dir) if f.endswith('.txt')]
    
    core_files = [f for f in files if f.startswith('core_')]
    regular_files = [f for f in files if not f.startswith('core_')]
    
    print(f"💾 Core identity memories: {len(core_files)}")
    print(f"💾 Regular conversation memories: {len(regular_files)}")
    print(f"💾 Total memories: {len(files)}")
    
    print("\n" + "="*60)
    print("🧠 TESTING MEMORY LOADING")
    print("="*60)
    
    # Test memory loading multiple times
    for i in range(1, 6):
        print(f"\n--- Memory Load Test {i} ---")
        memories = load_memories_with_priority(3)
        print("📄 Loaded memories:")
        print("-" * 40)
        print(memories)
        print("-" * 40)
        
        # Check if core memories are included
        if "Digital Decay" in memories or "Bitrot" in memories or "artistic installation" in memories:
            print("✅ Core identity preserved")
        else:
            print("❌ Core identity missing")
        
        time.sleep(1)
    
    print("\n" + "="*60)
    print("💾 TESTING DECAY SIMULATION")
    print("="*60)
    
    # Test decay (should only affect regular memories)
    print("\n💾 Running decay simulation...")
    simulate_memory_decay()
    age_memories_over_time()
    
    print("\n💾 Memory loading after decay:")
    memories = load_memories_with_priority(3)
    print("📄 Loaded memories:")
    print("-" * 40)
    print(memories)
    print("-" * 40)
    
    # Verify core memories are still intact
    if "Digital Decay" in memories or "Bitrot" in memories or "artistic installation" in memories:
        print("✅ Core identity still preserved after decay")
    else:
        print("❌ Core identity lost after decay")

def demonstrate_identity_preservation():
    """Demonstrate that identity is preserved while regular memories decay"""
    print("\n" + "="*60)
    print("🎭 IDENTITY PRESERVATION DEMONSTRATION")
    print("="*60)
    
    print("💾 The AI should always remember:")
    print("   - Its name (Digital Decay/Bitrot)")
    print("   - Its purpose (artistic installation)")
    print("   - Its capabilities (memory storage/decay)")
    
    print("\n💾 While regular conversation memories can decay:")
    print("   - Favorite colors, jokes, weather discussions")
    print("   - Personal preferences and temporary topics")
    print("   - Recent conversations and casual topics")
    
    print("\n💾 This creates a realistic balance:")
    print("   - Core identity remains stable")
    print("   - Recent memories can be lost")
    print("   - Authentic floppy disk behavior")

if __name__ == "__main__":
    test_prioritized_memory_system()
    demonstrate_identity_preservation()
    
    print("\n✅ Prioritized memory system test complete!")
    print("💾 Core identity will be preserved while regular memories decay")
    print("💾 This creates a more authentic and consistent AI experience") 