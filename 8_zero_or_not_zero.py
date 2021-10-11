print(
    0 in list(
        map(
            int,
            open(
                'input.txt', 'r', encoding='utf8'
            ).read().split()
        )
    )
)
