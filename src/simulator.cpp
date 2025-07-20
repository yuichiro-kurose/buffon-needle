#include <iostream>
#include <random>
#include <cmath>
#include <iomanip>

int main() {
  int needleCount;
  std::cout << "Enter number of needles to throw: ";
  std::cin >> needleCount;

  if (needleCount <= 0) {
    std::cerr << "Number of needles must be positive." << std::endl;
    return 1;
  }

  const double lineDistance = 2.0;
  const double needleLength = 1.0;

  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_real_distribution<double> distX(0.0, lineDistance / 2.0);
  std::uniform_real_distribution<double> distTheta(0.0, M_PI / 2.0);

  int intersectCount = 0;

  for (int i = 0; i < needleCount; ++i) {
    double d = distX(gen);       // Distance from center to nearest line
    double theta = distTheta(gen); // Angle from vertical

    if (d <= (needleLength / 2.0) * std::sin(theta)) {
      ++intersectCount;
    }
  }

  int nonIntersectCount = needleCount - intersectCount;
  double probability = static_cast<double>(intersectCount) / needleCount;
  double inverseProbability = (intersectCount > 0) ? 1.0 / probability : 0.0;

  std::cout << std::fixed << std::setprecision(6);
  std::cout << "Total needles thrown   : " << needleCount << std::endl;
  std::cout << "Needles intersected    : " << intersectCount << std::endl;
  std::cout << "Needles not intersected: " << nonIntersectCount << std::endl;
  std::cout << "Intersection probability: " << probability << std::endl;
  std::cout << "Inverse of probability : " << inverseProbability << std::endl;

  return 0;
}
