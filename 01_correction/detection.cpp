#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> a = {"01010100", "01001011", "10110111", "10101000"};
    std::vector<size_t> result;
    for (size_t i = 0; i < a.size(); i++) {
        for (size_t j = i + 1; j < a.size(); j++) {
            size_t temp = 0;
            for (size_t k = 0; k < a[i].size(); k++) {
                if (a[i][k] != a[j][k])
                    temp++;
            }
            result.push_back(temp);
        }
    }
    size_t min = a[0].size();
    for (const auto& x : result) {
        if (x < min)
            min = x;
    }

    std::cout << "d(V) = " << min << std::endl;
}
