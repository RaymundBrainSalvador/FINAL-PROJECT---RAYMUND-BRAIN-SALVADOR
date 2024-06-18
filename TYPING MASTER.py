import time

def typing_master():
    text = "The quick brown fox jumps over the lazy dog"
    print("Type this text:")
    print(text)
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    accuracy = sum(1 for a, b in zip(text, user_input) if a == b) / len(text) * 100
    elapsed_time = end_time - start_time

    print(f"Time: {elapsed_time:.2f} sec")
    print(f"Accuracy: {accuracy:.2f}%")

typing_master()