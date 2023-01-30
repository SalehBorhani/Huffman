# HuffmanCoding
With Huffman algorithm we can decrease the size of the text files.

## How does exactly Huffman algorithm work?
Suppose the string below is to be sent over a network.

![Screenshot from 2023-01-27 22-42-07](https://user-images.githubusercontent.com/95637102/215175446-ad028505-a762-4926-bf6c-eb687291fd4a.png)

Each character occupies 8 bits. There are a total of 15 characters in the above string. Thus, a total of 8 * 15 = 120 bits are required to send this string.

Using the Huffman Coding technique, we can compress the string to a smaller size.
Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.

Once the data is encoded, it has to be decoded. Decoding is done using the same tree.

Huffman Coding prevents any ambiguity in the decoding process using the concept of prefix code ie. a code associated with a character should not be present in the prefix of any other code. The tree created above helps in maintaining the property.

Huffman coding is done with the help of the following steps:
1. Calculate the frequency of each character in the string.

![Screenshot from 2023-01-27 22-41-45](https://user-images.githubusercontent.com/95637102/215176922-8e5cd82f-78bf-46eb-82ee-bcf045b2fda4.png)

2. Sort the characters in increasing order of the frequency. These are stored in a priority queue.

![image](https://user-images.githubusercontent.com/95637102/215177621-10a54de7-8247-4b18-b824-c951a371b10d.png)

3. Make each unique character as a leaf node.

4. Create an empty node. Assign the minimum frequency to the left child of node and assign the second minimum frequency to the right child of node. Set the value of the node as the sum of the above two minimum frequencies.

![image](https://user-images.githubusercontent.com/95637102/215178683-01247852-a89c-4b1d-afd7-04e26e7d99fb.png)

5. Remove these two minimum frequencies from queue and add the sum into the list of frequencies.

6. Insert that node which we created in step 4 into the tree.

7. Repeat steps 3 to 5 for all the characters.

![image](https://user-images.githubusercontent.com/95637102/215179427-9dff8cd4-9d0f-4a1d-a049-12eb3c74a384.png)

![image](https://user-images.githubusercontent.com/95637102/215474460-cc9c2b82-8b6b-4bdf-a829-9d74de06c9e1.png)

8. For each non-leaf node, assign 0 to the left edge and 1 to the right edge.

![image](https://user-images.githubusercontent.com/95637102/215474679-fce89144-7614-4781-86f5-7bdccde73091.png)

And at the end the codes of the characters will be like below:

![image](https://user-images.githubusercontent.com/95637102/215475197-8c44d40f-c1ed-4e87-80e9-632988784eb9.png)

