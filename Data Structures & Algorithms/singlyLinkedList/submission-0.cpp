class ListNode {
    public:

        int val;
        ListNode* next;

        ListNode(int val) : val(val), next(nullptr) {}
        ListNode(int val, ListNode* next) : val(val), next(next) {}
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;
public:
    LinkedList() {
        head = new ListNode(-1);
        tail = head;
    }

    int get(int index) {
        ListNode* cur = head->next;
        int count = 0;
        while(cur != nullptr) {
            if (count == index) {
                return cur->val;
            }
            count++;
            cur = cur->next;
        }
        return -1;
    }

    void insertHead(int val) {
        ListNode* newNode = new ListNode(val);
        newNode->next = head->next;
        head->next = newNode;
        if (newNode->next == nullptr) {
            tail = newNode;
        }
    }
    
    void insertTail(int val) {
        tail->next = new ListNode(val);
        tail = tail->next;
    }

    bool remove(int index) {
        int count = 0;
        ListNode* cur = head;
        while (cur != nullptr && count < index) {
            count++;
            cur = cur->next;
        }
        if (cur != nullptr && cur->next != nullptr) {
            if (cur->next == tail) {
                tail = cur;
            }
            ListNode* toDelete = cur->next;
            cur->next = cur->next->next;
            delete toDelete;
            return true;
        }
        return false;
    }

    vector<int> getValues() {
        vector<int> values;
        ListNode* cur = head->next;
        while (cur != nullptr) {
            values.push_back(cur->val);
            cur = cur->next;
        }
        return values;
    }
};
