#include <vector>
using namespace std;

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int val) : val{val}, next{nullptr} {}

    ListNode(int val, ListNode* next) : val{val}, next{next} {}
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;

public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    int get(int index) {
        int i = 0;
        ListNode* cur = head;

        while (cur) {
            if (i == index) {
                return cur->val;
            }

            cur = cur->next;
            i++;
        }

        return -1;
    }

    void insertHead(int val) {
        ListNode* newNode = new ListNode(val, head);
        head = newNode;

        if (tail == nullptr) {
            tail = newNode;
        }
    }
    
    void insertTail(int val) {
        ListNode* newNode = new ListNode(val);

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
            return;
        }

        tail->next = newNode;
        tail = newNode;
    }

    bool remove(int index) {
        if (head == nullptr) {
            return false;
        }

        if (index == 0) {
            ListNode* toDelete = head;
            head = head->next;

            if (head == nullptr) {
                tail = nullptr;
            }

            delete toDelete;
            return true;
        }

        int i = 0;
        ListNode* cur = head;

        while (cur && cur->next) {
            if (i + 1 == index) {
                ListNode* toDelete = cur->next;
                cur->next = toDelete->next;

                if (toDelete == tail) {
                    tail = cur;
                }

                delete toDelete;
                return true;
            }

            cur = cur->next;
            i++;
        }

        return false;
    }

    vector<int> getValues() {
        vector<int> values;

        ListNode* cur = head;

        while (cur) {
            values.push_back(cur->val);
            cur = cur->next;
        }

        return values;
    }
};