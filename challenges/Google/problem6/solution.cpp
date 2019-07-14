#include <iostream>
#include <assert.h>

template<typename T>
T* xor_t(T* node1, T* node2) {
    return (T*)((uintptr_t)node1 ^ (uintptr_t)node2);
}

class Node {
public:
    void* data; // any data
    Node* both; // ptr to XOR of prev/next

    Node(void* data=nullptr, Node* both=nullptr) {
        this->data = data;
        this->both = both;
    }
};

class LinkedList {
public:
    int length;
    Node* head;
    Node* tail;

    LinkedList() {
        this->head = nullptr;
        this->tail = nullptr;
        this->length = 0;
    }

    void add(void* data) {
        Node* node = new Node(data);

        if (this->length == 0) {
            this->head = node;
            this->tail = node;
        }
        else {
            this->tail->both = xor_t<Node>(this->tail->both, node);
            node->both = this->tail;
            this->tail = node;
        }
        this->length++;
    }

    Node* get(int index) {
        if (index < 0 || index >= this->length) {
            return nullptr;
        }

        Node* prev = nullptr;
        Node* current = this->head;
        int idx = 0;

        while (idx < index) {
            Node* temp = current;
            current = xor_t<Node>(prev, current->both);
            prev = temp;
            idx++;
        }

        return current;
    }
};

int main() {
    LinkedList* list = new LinkedList();

    int x = 3;
    char y = '5';
    double z = 0.5554;

    list->add(&x);
    list->add(&y);
    list->add(&z);

    assert(list->get(0)->data == &x);
    assert(list->get(1)->data == &y);
    assert(list->get(2)->data == &z);

    return 0;
}