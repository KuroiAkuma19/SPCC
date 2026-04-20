#define FACTORIAL(n) \
({ \
    long long fact = 1; \
    for (int i = 1; i <= (n); i++) \
        fact *= i; \
    fact; \
})
