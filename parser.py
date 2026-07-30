def parse_file(filename: str) -> tuple[list[list[int]], list[list[int]]]:
    with open(filename) as f:
        sections = f.read().strip().split("\n\n")

    if len(sections) != 2:
        raise ValueError("The file must contain two sections separated by an empty line.")

    def parse_section(section: str) -> list[list[int]]:
        return [
            list(map(int, line.split()))
            for line in section.splitlines()
        ]

    return parse_section(sections[0]), parse_section(sections[1])