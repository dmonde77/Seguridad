#include <gmp.h>

void fermat_factor(mpz_t p, mpz_t q, mpz_t N);

int main()
{
    mpz_t N;
    mpz_t p, q;

    mpz_init(N);
    mpz_init(p);
    mpz_init(q);

    mpz_set_str(N, "be0d02633305f3d5c3c6044d17149baf", 16);
    fermat_factor(p, q, N);

    gmp_printf("p = %Zd\n", p);
    gmp_printf("q = %Zd\n", q);

    mpz_clear(p);
    mpz_clear(q);
    mpz_clear(N);

    return 0;
}

void fermat_factor(mpz_t p, mpz_t q, mpz_t N)
{
    mpz_t a, b;

    mpz_init(a);
    mpz_init(b);

    mpz_sub_ui(a, N, 1);
    mpz_sqrt(a, a);
    mpz_add_ui(a, a, 1);

    while (1)
    {
        mpz_mul(b, a, a);
        mpz_sub(b, b, N);

        if (mpz_perfect_square_p(b))
            break;

        mpz_add_ui(a, a, 1);
    }

    mpz_sqrt(p, b);
    mpz_sqrt(q, b);
    mpz_add(p, a, p);
    mpz_sub(q, a, q);

    mpz_clear(a);
    mpz_clear(b);
}

