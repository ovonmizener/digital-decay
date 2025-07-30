#!/usr/bin/env python3
"""
Debug script to show exactly what happens when reading corrupted memories
"""

import os
import random
from memory_utils import (
    store_memory_block, 
    load_random_memories, 
    simulate_memory_decay, 
    age_memories_over_time
)

def debug_memory_reading():
    """Show exactly what happens when reading memories"""
    print("🔍 DEBUGGING MEMORY READING")
    print("="*50)
    
    memory_dir = os.path.join(os.path.dirname(__file__), '../memory_bank')
    files = [f for f in os.listdir(memory_dir) if f.endswith('.txt')]
    
    print(f"💾 Found {len(files)} memory files")
    print("-" * 50)
    
    for i, filename in enumerate(files[:5]):  # Check first 5 files
        filepath = os.path.join(memory_dir, filename)
        size = os.path.getsize(filepath)
        
        print(f"\n📄 File {i+1}: {filename}")
        print(f"   Size: {size} bytes")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"   Status: ✅ READABLE")
                print(f"   Content: {content[:100]}...")
                
                # Check corruption level
                readable_chars = len([c for c in content if c.isprintable()])
                total_chars = len(content)
                corruption_level = (total_chars - readable_chars) / total_chars if total_chars > 0 else 0
                print(f"   Corruption: {corruption_level:.1%}")
                
        except UnicodeDecodeError as e:
            print(f"   Status: ❌ ENCODING ERROR")
            print(f"   Error: {e}")
        except FileNotFoundError as e:
            print(f"   Status: ❌ FILE NOT FOUND")
            print(f"   Error: {e}")
        except Exception as e:
            print(f"   Status: ❌ OTHER ERROR")
            print(f"   Error: {e}")
    
    print("\n" + "="*50)
    print("🧠 TESTING MEMORY LOADING")
    print("="*50)
    
    # Test the actual memory loading function
    memories = load_random_memories(3)
    print(f"\n📄 Loaded memories:")
    print("-" * 30)
    print(memories)
    print("-" * 30)
    
    # Count error messages
    error_count = memories.count("[CORRUPTED MEMORY BLOCK")
    error_count += memories.count("[MISSING MEMORY BLOCK")
    
    print(f"\n📊 Analysis:")
    print(f"   Total characters loaded: {len(memories)}")
    print(f"   Error messages found: {error_count}")
    print(f"   Readable content: {len(memories) - (error_count * 30)} chars")

def test_corruption_threshold():
    """Test if there's a corruption threshold"""
    print("\n" + "="*50)
    print("🧪 TESTING CORRUPTION THRESHOLD")
    print("="*50)
    
    # Create a test file with known corruption
    test_content = "This is a test memory that will be corrupted."
    store_memory_block(test_content)
    
    # Corrupt it multiple times
    for i in range(1, 6):
        print(f"\n--- Corruption Cycle {i} ---")
        simulate_memory_decay()
        
        # Try to read it
        memories = load_random_memories(1)
        print(f"📄 After {i} corruption cycles:")
        print(f"   Content: {memories}")
        print(f"   Length: {len(memories)} characters")

if __name__ == "__main__":
    debug_memory_reading()
    test_corruption_threshold() 