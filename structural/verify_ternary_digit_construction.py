#!/usr/bin/env python3
"""Finite replay for the classical ternary 0/1 3-AP-free construction.

This script is regression evidence only; the general theorem has an elementary
carry-free proof in TERNARY-DIGIT-CLASSICAL-CONSTRUCTION.md.
"""

from itertools import product


def construction(d: int) -> list[int]:
    return sorted(
        1 + sum(bit * (3 ** i) for i, bit in enumerate(bits))
        for bits in product((0, 1), repeat=d)
    )


def first_nontrivial_ap(values: list[int]):
    S = set(values)
    for i, a in enumerate(values):
        for c in values[i + 1 :]:
            total = a + c
            if total % 2 == 0:
                b = total // 2
                if b in S and a != b != c:
                    return (a, b, c)
    return None


def main() -> None:
    for d in range(1, 10):
        values = construction(d)
        expected_size = 2 ** d
        expected_max = (3 ** d + 1) // 2
        assert len(values) == expected_size, (d, len(values), expected_size)
        assert values[0] == 1
        assert values[-1] == expected_max, (d, values[-1], expected_max)
        witness = first_nontrivial_ap(values)
        assert witness is None, (d, witness)
        print(
            f"d={d}: size={len(values):4d}, max={values[-1]:5d}, "
            "3AP-free=PASS"
        )

    # Previously isolated release-day fragments.
    assert len(construction(5)) == 32 and max(construction(5)) <= 243
    assert len(construction(6)) == 64 and max(construction(6)) <= 729
    assert len(construction(7)) == 128 and max(construction(7)) <= 2187
    print("isolated r3(243/729/2187) lower bounds: PASS")


if __name__ == "__main__":
    main()
