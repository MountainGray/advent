from advent import get_input, solution_timer
from functools import lru_cache

def process_input(inp):
    blueprint = {}
    for idx, line in enumerate(inp):
        _, line = line.split(": ")
        ore, clay, obsidian, geode = line.split(". ")
        ore = int(ore.split(" ")[-2])
        clay = int(clay.split(" ")[-2])
        obsidian = (int(obsidian.split(" ")[-5]), int(obsidian.split(" ")[-2]))
        geode = (int(geode.split(" ")[-5]), int(geode.split(" ")[-2]))
        blueprint[idx + 1] = (ore, clay, obsidian, geode)
    return blueprint


def pre_recurse(blueprint, time):
    max_ores = max([blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]])
    max_clay = blueprint[2][1]
    max_obsidian = blueprint[3][1]
    start_robots = (1, 0, 0)  # ore, clay, obsidian
    resources = (0, 0, 0)  # ore, clay, obsidian

    @lru_cache(maxsize=None)
    def recurse(time, blueprint, robots, resources, geos):
        if time == 0:
            return geos
        m_score = geos

        if robots[2] > 0:
            if (
                resources[0] >= blueprint[3][0] and resources[2] >= blueprint[3][1]
            ):  # can buy geode
                score = recurse(
                    time - 1,
                    blueprint,
                    (robots[0], robots[1], robots[2]),
                    (
                        resources[0] - blueprint[3][0] + robots[0],
                        resources[1] + robots[1],
                        resources[2] - blueprint[3][1] + robots[2],
                    ),
                    geos + time - 1,
                )
                if score > m_score:
                    m_score = score

            else:  # can't yet buy geode

                # can gather
                p1, p2 = blueprint[3]
                req1, req2 = p1 - resources[0], p2 - resources[2]
                half1, half2 = (
                    1 if req1 % robots[0] > 0 else 0,
                    1 if req2 % robots[2] > 0 else 0,
                )
                ttw1, ttw2 = (
                    time - (req1 // robots[0]) - half1 - 1,
                    time - (req2 // robots[2]) - half2 - 1,
                )
                if ttw1 < ttw2 and ttw1 >= 0:
                    delta = time - ttw1

                    score = recurse(
                        ttw1,
                        blueprint,
                        (robots[0], robots[1], robots[2]),
                        (
                            resources[0] - p1 + robots[0] * delta,
                            resources[1] + robots[1] * delta,
                            resources[2] - p2 + robots[2] * delta,
                        ),
                        geos + ttw1,
                    )
                    if score > m_score:
                        m_score = score

                elif ttw2 <= ttw1 and ttw2 >= 0:
                    delta = time - ttw2
                    score = recurse(
                        ttw2,
                        blueprint,
                        (robots[0], robots[1], robots[2]),
                        (
                            resources[0] - p1 + robots[0] * delta,
                            resources[1] + robots[1] * delta,
                            resources[2] - p2 + robots[2] * delta,
                        ),
                        geos + ttw2,
                    )
                    if score > m_score:
                        m_score = score

        if robots[1] > 0:  # have clay robot
            # go to obsidian (ore & clay)
            if (
                robots[2] < max_obsidian
                and robots[2] * time + resources[2] < max_obsidian * time
            ):
                p1, p2 = blueprint[2]
                if resources[0] >= p1 and resources[1] >= p2:  # can buy obsidian
                    score = recurse(
                        time - 1,
                        blueprint,
                        (robots[0], robots[1], robots[2] + 1),
                        (
                            resources[0] - p1 + robots[0],
                            resources[1] - p2 + robots[1],
                            resources[2] + robots[2],
                        ),
                        geos,
                    )
                    if score > m_score:
                        m_score = score
                else:
                    req1, req2 = p1 - resources[0], p2 - resources[1]
                    half1, half2 = (
                        1 if req1 % robots[0] > 0 else 0,
                        1 if req2 % robots[1] > 0 else 0,
                    )
                    ttw1, ttw2 = (
                        time - (req1 // robots[0]) - half1 - 1,
                        time - (req2 // robots[1]) - half2 - 1,
                    )
                    if ttw1 < ttw2 and ttw1 >= 0:
                        delta = time - ttw1
                        score = recurse(
                            ttw1,
                            blueprint,
                            (robots[0], robots[1], robots[2] + 1),
                            (
                                resources[0] - p1 + robots[0] * delta,
                                resources[1] - p2 + robots[1] * delta,
                                resources[2] + robots[2] * delta,
                            ),
                            geos,
                        )
                        if score > m_score:
                            m_score = score

                    elif ttw2 <= ttw1 and ttw2 >= 0:
                        delta = time - ttw2
                        score = recurse(
                            ttw2,
                            blueprint,
                            (robots[0], robots[1], robots[2] + 1),
                            (
                                resources[0] - p1 + robots[0] * delta,
                                resources[1] - p2 + robots[1] * delta,
                                resources[2] + robots[2] * delta,
                            ),
                            geos,
                        )
                        if score > m_score:
                            m_score = score

        # go to buy clay
        if robots[1] < max_clay and robots[1] * time + resources[1] < max_clay * time:
            requried_time = blueprint[1] - resources[0]
            if requried_time > 0:
                half = 1 if requried_time % robots[0] > 0 else 0
                time_to_wait = time - (requried_time // robots[0]) - half - 1
                delta = time - time_to_wait
                if time_to_wait >= 0:
                    score = recurse(
                        time_to_wait,
                        blueprint,
                        (robots[0], robots[1] + 1, robots[2]),
                        (
                            resources[0] - blueprint[1] + robots[0] * delta,
                            resources[1] + delta * robots[1],
                            resources[2] + delta * robots[2],
                        ),
                        geos,
                    )
                    if score > m_score:
                        m_score = score

            else:
                score = recurse(
                    time - 1,
                    blueprint,
                    (robots[0], robots[1] + 1, robots[2]),
                    (
                        resources[0] - blueprint[1] + robots[0],
                        resources[1] + robots[1],
                        resources[2] + robots[2],
                    ),
                    geos,
                )
                if score > m_score:
                    m_score = score

        # go to buy ore
        if robots[0] < max_ores and robots[0] * time + resources[0] < max_ores * time:
            requried_time = blueprint[0] - resources[0]
            if requried_time > 0 and time - requried_time >= 0:
                half = 1 if requried_time % robots[0] > 0 else 0
                time_to_wait = time - (requried_time // robots[0]) - half - 1
                delta = time - time_to_wait
                if time_to_wait >= 0:
                    score = recurse(
                        time_to_wait,
                        blueprint,
                        (robots[0] + 1, robots[1], robots[2]),
                        (
                            resources[0] - blueprint[0] + robots[0] * delta,
                            resources[1] + robots[1] * delta,
                            resources[2] + robots[2] * delta,
                        ),
                        geos,
                    )
                    if score > m_score:
                        m_score = score

            elif resources[0] >= blueprint[0]:
                score = recurse(
                    time - 1,
                    blueprint,
                    (robots[0] + 1, robots[1], robots[2]),
                    (
                        resources[0] - blueprint[0] + robots[0],
                        resources[1] + robots[1],
                        resources[2] + robots[2],
                    ),
                    geos,
                )
                if score > m_score:
                    m_score = score

        return m_score

    return recurse(time, blueprint, start_robots, resources, 0)


@solution_timer(2022, 19, 1)
def part_one(inp):
    blueprints = process_input(inp)
    return sum(
        [pre_recurse(blueprints[i], 24) * (i) for i in range(1, len(blueprints) + 1)]
    )


@solution_timer(2022, 19, 2)
def part_two(inp):
    blueprints = process_input(inp)
    s = 1
    for i in range(1, 4):
        s *= pre_recurse(blueprints[i], 32)
    return s


if __name__ == "__main__":
    input = get_input(2022, 19)
    part_one(input)
    part_two(input)
