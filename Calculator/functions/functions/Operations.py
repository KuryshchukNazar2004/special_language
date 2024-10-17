def SaveToMemory(mem, result):
    save = input("Do you want to save the result to memory? (y/n): ").lower()
    if save == 'y':
        mem.Add(result)
        print(f"Result {result} saved to memory.")
    else:
        print("Result not saved to memory.")
