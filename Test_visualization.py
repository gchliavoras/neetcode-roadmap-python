import matplotlib.pyplot as plt
import time

def visualize_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Visualization
        plt.figure(figsize=(10, 2))
        plt.bar(range(len(arr)), arr, color="grey", alpha=0.7)
        plt.bar(mid, arr[mid], color="blue", label="Mid Pointer")
        plt.bar(left, arr[left], color="green", label="Left Pointer")
        plt.bar(right, arr[right], color="red", label="Right Pointer")
        plt.legend()
        plt.title(f"Target: {target}, Left: {left}, Right: {right}, Mid: {mid}")
        plt.xticks(range(len(arr)))
        plt.show()
        time.sleep(1)  # Pause to visualize changes
        
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"{target} not found in the array.")
    return -1

# Test the visualization
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
visualize_binary_search(arr, target)