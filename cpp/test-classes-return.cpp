#include<iostream>

class A;
class A {
public:
    // A() = default;
    A* f1(int n) {
        x1 = n;
        return this;
    }
    A* f2(int n) {
        x1 = n;
        return this;
    }

    A f3(int n) {
        x1 = n;
        return *this;
    }
    A f4(int n) {
        x1 = n;
        return *this;
    }

    A& f5(int n) {
        x1 = n;
        return *this;
    }
    A& f6(int n) {
        x1 = n;
        return *this;
    }
private:
    int x1{0};

    friend std::ostream& operator<<(std::ostream& stream, A& a);
};

std::ostream& operator<<(std::ostream &stream, A& a) {
    stream << "X1: " << a.x1;
    return stream;
}

int main() {
    A a1, a2, a3;

    a1.f1(10)->f2(20);
    std::cout << a1 << "\n";

    a2.f3(30).f4(40);
    std::cout << a2 << "\n";

    a3.f5(50).f6(60);
    std::cout << a3 << "\n";
    return 0;
}
