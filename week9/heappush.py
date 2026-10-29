def heappush(heap, n):
    heap.append(n)              # Insert at the last node
    i = len(heap) - 1            # Position of node n

    while i != 1:                # Perform up-heap if n is not the root
        pi = i // 2               # Position of parent node

        if n <= heap[pi]:         # Stop if n is smaller than or equal to parent
            break

        heap[i] = heap[pi]        # Move parent down
        i = pi                    # i becomes the parent's index

    heap[i] = n                   # Insert n at the final position


def heappop(heap):
    size = len(heap) - 1          # Number of nodes

    if size == 0:                 # Empty heap
        return None

    root = heap[1]                # Root node to remove
    last = heap[size]             # Last node (leaf)
    pi = 1                        # Parent node index
    i = 2                         # Child node index

    while i <= size:              # Until the last node
        if i < size and heap[i] < heap[i + 1]:
            i += 1                # Choose the right child if it is larger

        if last >= heap[i]:       # Stop if the child is smaller than or equal to last
            break

        heap[pi] = heap[i]        # Move child up
        pi = i                    # Update parent index
        i *= 2                    # Move to the left child

    heap[pi] = last                # Place last node at the parent position
    heap.pop()                     # Remove the last node
    return root                    # Return the original root

heap = [None]

heappush(heap, 30)
heappush(heap, 10)
heappush(heap, 50)
heappush(heap, 20)

print("Heap:", heap)

print("Removed:", heappop(heap))
print("Removed:", heappop(heap))

print("Heap after removal:", heap)