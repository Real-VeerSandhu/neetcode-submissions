class Node {
    public:

    int key;
    int value;
    Node* next;
    Node* prev;

    Node(int k, int v) : key(k), value(v), next(nullptr), prev(nullptr) {}
};


class LRUCache {
private:

    int cap;
    Node* left;
    Node* right;
    unordered_map<int, Node*> cache;

    void insert(Node* node) {
        Node* oldEnd = right->prev;
        oldEnd->next = node;
        node->prev = oldEnd;
        node->next = right;
        right->prev = node;
    }

    void remove(Node* node) {
        Node* behind = node->prev;
        Node* ahead = node->next;
        behind->next = ahead;
        ahead->prev = behind;
    }


public:
    LRUCache(int capacity) {
        cap = capacity;
        left = new Node(0, 0);
        right = new Node(0, 0);
        left->next = right;
        right->prev = left;
        cache.clear();
    }
    
    int get(int key) {
        if (!cache.count(key)) return -1;

        Node* node = cache[key];
        int returnValue = node->value;

        remove(node);
        insert(node);

        return returnValue;


    }
    
    void put(int key, int value) {
        if (cache.count(key)) {
            Node* oldNode = cache[key];
            remove(oldNode);
            delete oldNode;
        }

        Node* newNode = new Node(key, value);
        insert(newNode);
        cache[key] = newNode;

        if (cache.size() > cap) {
            Node* toDelete = left->next;
            remove(toDelete);
            cache.erase(toDelete->key);
            delete toDelete;
        }
    }
};
